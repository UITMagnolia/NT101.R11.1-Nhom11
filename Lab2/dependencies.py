import sys
import subprocess
import importlib.util

def ensure_package(package_name, import_name=None):
    import_name = import_name or package_name

    if importlib.util.find_spec(import_name) is None:
        print(f"[INSTALL] Installing {package_name}...")

        subprocess.check_call([
            sys.executable,
            "-m",
            "pip",
            "install",
            package_name
        ])

        print(f"[SUCCESS] {package_name} installed!")
    else:
        print(f"[OK] {package_name} already installed.")


PACKAGES = {
    "pycryptodome": "Crypto",       # For task 2.2, 2.3, 2.4
    "numpy": "numpy",               # For task 2.6
    "matplotlib": "matplotlib",     # Optional
    "sympy": "sympy"                # Optional 
}

# If you want to install specific packages in a task
# Use the following function
# Then you can import them in your code
# Example: (paste the following code in your task file, uncommend it))
# install_dependencies(["pycryptodome", "numpy"])
# from Crypto.Cipher import DES
# from numpy import array

def install_dependencies(packages=None):
    if packages is None:
        packages = PACKAGES.keys()

    for package in packages:
        ensure_package(package, PACKAGES.get(package))