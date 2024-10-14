# Install and Manage Linux Packages
# Problem: Write a script to install, update, and remove Linux packages using a package manager (e.g., apt or yum).
# Objective: Automate software management.

import subprocess
import sys

def install_package(package_name):
    """Install a package using apt or yum."""
    try:
        if is_debian_based():
            subprocess.run(['sudo', 'apt', 'install', '-y', package_name], check=True)
        elif is_redhat_based():
            subprocess.run(['sudo', 'yum', 'install', '-y', package_name], check=True)
        print(f"Successfully installed {package_name}.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install {package_name}. Error: {e}")

def update_package(package_name):
    """Update a specific package using apt or yum."""
    try:
        if is_debian_based():
            subprocess.run(['sudo', 'apt', 'update'], check=True)  # Update package list
            subprocess.run(['sudo', 'apt', 'upgrade', package_name, '-y'], check=True)
        elif is_redhat_based():
            subprocess.run(['sudo', 'yum', 'update', package_name, '-y'], check=True)
        print(f"Successfully updated {package_name}.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to update {package_name}. Error: {e}")

def remove_package(package_name):
    """Remove a package using apt or yum."""
    try:
        if is_debian_based():
            subprocess.run(['sudo', 'apt', 'remove', '-y', package_name], check=True)
        elif is_redhat_based():
            subprocess.run(['sudo', 'yum', 'remove', '-y', package_name], check=True)
        print(f"Successfully removed {package_name}.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to remove {package_name}. Error: {e}")

def is_debian_based():
    """Check if the system is Debian-based."""
    return subprocess.call(['lsb_release', '-is'], stdout=subprocess.PIPE).decode().strip() in ['Ubuntu', 'Debian']

def is_redhat_based():
    """Check if the system is Red Hat-based."""
    return subprocess.call(['lsb_release', '-is'], stdout=subprocess.PIPE).decode().strip() in ['Fedora', 'RedHat']

def main():
    """Main function to handle package management commands."""
    if len(sys.argv) < 3:
        print("Usage: python3 package_manager.py <install|update|remove> <package_name>")
        sys.exit(1)

    command = sys.argv[1].lower()
    package_name = sys.argv[2]

    if command == "install":
        install_package(package_name)
    elif command == "update":
        update_package(package_name)
    elif command == "remove":
        remove_package(package_name)
    else:
        print("Invalid command. Use install, update, or remove.")
        sys.exit(1)

if __name__ == "__main__":
    main()
