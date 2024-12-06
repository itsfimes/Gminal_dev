# Stock package manager for Gminal
# It does your usual package manager stuff

import os
import tarfile
import json
import shutil
import tempfile
import requests
import colorama
from colorama import Fore
from utils.print_utils import write_progress, tqdm_bar
import subprocess

colorama.init(autoreset=True)


def sudo_exec(command, core=None):
    if isinstance(command, str):
        command = command.split(" ")


    if core is not None and core.debug_mode:
        print(command, type(command))
    try:
        # Run the sudo command securely
        result = subprocess.run(
            command,
            check=False,  # Don't raise an exception immediately
            capture_output=True,  # Capture stdout and stderr
        )

        if result.returncode != 0:  # Non-zero return code indicates failure
            # Check if the error was due to permission denial
            if b"password" in result.stderr.lower():
                raise PermissionError("Sudo prompt was cancelled or failed due to incorrect credentials.")
            else:
                raise PermissionError(f"Failed to sudo for {command}: {result.stderr.decode().strip()}")

    except PermissionError as e:
        raise Exception(f"Error: {e}")


class PackageNotFoundError(Exception):
    def __init__(self, message="package gone :c"):
        super(PackageNotFoundError, self).__init__(message)


class GminalPackageManager:
    def __init__(self, core, packagelist_path="packagelist.gres", installlistpath="installed_packages.gres"):
        self.packagelist_path = packagelist_path
        self.installed_packages_list_path = installlistpath
        self.packages = self._load_package_list()
        self.installed_packages = self._load_installed_packages_list()
        self.core = core

    def _load_package_list(self):
        packages = []
        with open(self.packagelist_path, 'r') as f:
            for line in f:
                if line.strip() and '*' in line:
                    name, url, version = line.split('*')
                    # packages[name.strip()] = url_template.strip(), version.strip()
                    packages.append({
                        "name": name,
                        "url": url,
                        "version": version
                    })
        return packages

    def _load_installed_packages_list(self):
        packages = []
        with open(self.installed_packages_list_path, 'r') as file:
            for line in file:
                line = line.strip()  # Remove trailing whitespace/newlines
                if not line:
                    continue  # Skip empty lines

                # Split the line into parts
                parts = line.split('*')
                if len(parts) < 4:
                    raise ValueError(f"Invalid format: {line}")

                name = parts[0]
                version = parts[1]
                description = parts[2]
                paths = parts[3].split('|')  # Get every path

                # Store in a dictionary or any desired structure
                packages.append({
                    'name': name,
                    'version': version,
                    'description': description,
                    'paths': paths
                })

        return packages

    def get_package_by_name(self, name, list):
        for package in list:
            if package['name'] == name:
                return package
        return None

    def install_package(self, package_name):
        package = self.get_package_by_name(package_name, self.packages)
        if package is None:
            print(f"Package '{package_name}' not found!")
            raise PackageNotFoundError("Package not found in package list :c")

        print("Requesting root")
        sudo_exec(["sudo", "echo", '"root"'])  # Request root at the start, so we don't have to annoy the user later
        # if os.geteuid() != 0:
        #     raise PermissionError("Root privileges are required.")

        url = package["url"].replace('%p', package_name)
        print(f"Downloading {package_name} from {url}...")

        with tempfile.TemporaryDirectory() as tmp_dir:
            tarball_path = os.path.join(tmp_dir, f"{package_name}.tar.gz")
            response = requests.get(url, stream=True)  # Stream the response for chunked downloading
            chunk_size = 512  # Define chunk size

            with open(tarball_path, 'wb') as f:
                with tqdm_bar(total=int(response.headers.get('content-length', 0)), unit='B', unit_scale=True,
                              desc="Downloading") as pbar:
                    for chunk in response.iter_content(chunk_size=chunk_size):
                        if chunk:  # Write the chunk if it's not empty
                            f.write(chunk)
                            # Update the tqdm progress bar
                            pbar.update(len(chunk))

            # Extract the tarball
            with tarfile.open(tarball_path, 'r:gz') as tar:
                print("Extracting")
                tar.extractall(path=tmp_dir)
            os.remove(tarball_path)
            # print(len(os.listdir(tmp_dir)))
            # print(os.listdir(tmp_dir))
            if package_name not in os.listdir(tmp_dir) and len(os.listdir(tmp_dir)) == 1:
                package_dir = os.path.join(tmp_dir, "".join(os.listdir(tmp_dir)))
                # print(package_dir)
            else:
                package_dir = os.path.join(tmp_dir, package_name)

            package_json_path = os.path.join(package_dir, 'package.json')

            if not os.path.exists(package_json_path):
                print(f"Error: 'package.json' not found in {package_name} package!")
                raise Exception(f"No package.json file was found at {package_json_path}")

            with open(package_json_path, 'r') as f:
                package_info = json.load(f)

            package_files = []
            # Move files based on what is in "package.json"
            with tqdm_bar(package_info.get('files', []), desc="Processing files", unit="file") as pbar:
                for file_entry in pbar:
                    # if os.geteuid() != 0:  # Check root permissions for every file
                    #     print(f"{Fore.RED}Lost root access, will ask again.")
                    # Update tqdm description for the current file
                    pbar.set_postfix(current_file=file_entry['source'])
                    # Construct source and destination paths
                    src = os.path.join(package_dir, file_entry['source'])
                    dest = str(os.path.join(self.core.startingdir, file_entry['destination']))
                    # Track the processed files
                    package_files.append(dest)
                    # Ensure the destination directory exists
                    os.makedirs(os.path.dirname(dest), exist_ok=True)
                    # Move the file to the destination
                    shutil.move(src, dest)
                    # Set permissions for the file
                    sudo_exec(["sudo", "chmod", "600", dest])
            with open(f"{self.core.startingdir}/utils/package_manager/installed_packages.gres", "a+") as f:
                f.write(f"{package_name}*{package_info.get("version")}*"
                        f"{package_info.get("description").replace("*", "").replace("\n", " - ")}*"
                        f"{'|'.join(package_files)}\n")

            print(f"Done!")
            print("Reloading commands")
            self.core.load_commands(silent=True)

    def uninstall_package(self, package_name):
        package = self.get_package_by_name(package_name, self.installed_packages)
        if package is None:
            print(f'Package "{package_name}" not found in installed packages')
            if package_name in self.packages:
                print(f"But it has been found in the package list. Did you mean to {Fore.GREEN}install it{Fore.RESET}?")
                print(f"If yes, just copy-paste this command :3 {Fore.MAGENTA}gpm -i {package_name}")
            raise PackageNotFoundError("Package not found in installed packages list :c")

        print(f"{Fore.RED}Uninstalling{Fore.RESET} {package['name']} version {package['version']}")
        print(f"Removing {len(package['paths'])} files..." if len(
            package["paths"]) > 1 else f"Removing {len(package['paths'])} file...")

        for idx, path in enumerate(package["paths"]):
            sudo_exec(f"sudo chmod 777 {path}")
            if os.path.isfile(path) or os.path.islink(path):
                os.remove(path)
            elif os.path.isdir(path):
                shutil.rmtree(path)
            else:
                raise Exception(f"Invalid filetype for {path}. It is not a file or a directory.")
            progress = ((idx + 1) / len(package["paths"])) * 100  # Calculate progress
            write_progress("Uninstalling", int(progress))
        print()
        print("Updating package list")
        updated_lines = []
        with open(self.installed_packages_list_path, 'w+') as file:
            for line in file:
                if line.strip().split('*', 1)[0] != package_name:
                    updated_lines.append(line)
            file.writelines(updated_lines)

        print("Done!")

    def list_packages(self, type="installed"):
        if type == "installed":
            print(f"{Fore.MAGENTA}Installed{Fore.RESET} packages: ")
            total = 0
            for package in self.installed_packages:
                total += 1  # ik this is not efficient
                print(
                    f"{Fore.LIGHTCYAN_EX}{package["name"]}{Fore.RESET} | version: {Fore.LIGHTMAGENTA_EX}{package["version"]}")
            print(f"Total of {total} packages")

        if type == "available":
            print(f"{Fore.MAGENTA}Available{Fore.RESET} packages: ")
            total = 0
            for package in self.packages:
                # print(package["name"])
                total += 1
                print(
                    f"{Fore.LIGHTCYAN_EX}{package["name"]}{Fore.RESET} | version: {Fore.LIGHTMAGENTA_EX}{package["version"]}")

            print(f"Total of {total} packages")

    def update_package_lists(self,
                             package_list="https://raw.githubusercontent.com/ItzFimes/Gminal_dev/refs/heads/main/utils/package_manager/packagelist.gres"):
        print("Updating package list!")
        print(f"Using update link: {Fore.LIGHTCYAN_EX}{package_list}")
        print("Downloading...")
        response = requests.get(package_list, stream=True)
        chunk_size = 512

        with open(self.packagelist_path, "wb") as f:
            with tqdm_bar(total=int(response.headers.get('content-length', 0)), unit='B', unit_scale=True,
                              desc="Downloading") as pbar:
                for chunk in response.iter_content(chunk_size=chunk_size):
                    if chunk:  # Write the chunk if it's not empty
                        f.write(chunk)
                        # Update the tqdm progress bar
                        pbar.update(len(chunk))


# Example usage:
# manager = GminalPackageManager()
# manager.install_package('sample_package')
