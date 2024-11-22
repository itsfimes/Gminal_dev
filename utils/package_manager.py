import os
import tarfile
import json
import shutil
import tempfile
import requests
from utils.print_utils import write_progress

class PackageNotFoundError(Exception):
    def __init__(self, message="Redraw event"):
        super(PackageNotFoundError, self).__init__(message)


class GminalPackageManager:
    def __init__(self, core, packagelist_path='packagelist.gres'):
        self.packagelist_path = packagelist_path
        self.packages = self._load_package_list()
        self.core = core

    def _load_package_list(self):
        packages = {}
        with open(self.packagelist_path, 'r') as f:
            for line in f:
                if line.strip() and '*' in line:
                    name, url_template = line.split('*')
                    packages[name.strip()] = url_template.strip()
        return packages

    def install_package(self, package_name):
        if package_name not in self.packages:
            print(f"Package '{package_name}' not found!")
            raise PackageNotFoundError("Package not found in package list :c")

        url = self.packages[package_name].replace('%p', package_name)
        print(f"Downloading {package_name} from {url}...")

        with tempfile.TemporaryDirectory() as tmp_dir:
            tarball_path = os.path.join(tmp_dir, f"{package_name}.tar.gz")

            response = requests.get(url, stream=True)  # Stream the response for chunked downloading
            total_size = int(response.headers.get('content-length', 0))  # Get total size from headers
            chunk_size = 1024  # Define chunk size
            task_name = "Downloading"

            with open(tarball_path, 'wb') as f:
                downloaded_size = 0
                for chunk in response.iter_content(chunk_size=chunk_size):
                    if chunk:  # Write the chunk if it's not empty
                        f.write(chunk)
                        downloaded_size += len(chunk)

                        # Calculate progress percentage
                        progress = (downloaded_size / total_size) * 100 if total_size else 100

                        # Update the progress bar
                        write_progress(task_name, int(progress))
            print()  # Move to the next line after the progress bar

            # Extract the tarball
            with tarfile.open(tarball_path, 'r:gz') as tar:
                print("Extracting")
                tar.extractall(path=tmp_dir)

            if package_name not in os.listdir(tmp_dir):
                package_dir = os.path.join(tmp_dir, package_name)
            else:
                package_dir = os.path.join(f"{tmp_dir}/{package_name}")

            print(package_dir)
            package_json_path = os.path.join(package_dir, 'package.json')
            print(package_json_path)

            if not os.path.exists(package_json_path):
                print(f"Error: 'package.json' not found in {package_name} package!")
                return

            with open(package_json_path, 'r') as f:
                package_info = json.load(f)

            # Move files based on 'package.json'
            for file_entry in package_info.get('files', []):
                src = os.path.join(package_dir, file_entry['source'])
                dest = os.path.join(self.core.startingdir, file_entry['destination'])
                os.makedirs(os.path.dirname(dest), exist_ok=True)
                shutil.move(src, dest)
                os.system(f"chmod 600 {dest}")

            print(f"Done!")
            print("Reloading commands")
            self.core.load_commands(silent=True)

# Example usage:
# manager = GminalPackageManager()
# manager.install_package('sample_package')
