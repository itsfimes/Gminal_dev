from utils import package_manager


def execute(self, package_name):
    """Install a package, optionally from a custom repository URL."""
    try:
        gpm = package_manager.GminalPackageManager(
            packagelist_path=f"{self.startingdir}/utils/package_manager/packagelist.gres", core=self)
        gpm.install_package(package_name)
        print(f"Package '{package_name}' installed successfully :33")
    except Exception as e:
        print(f"Failed to install package '{package_name}': {e}")
