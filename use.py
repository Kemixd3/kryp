import os

#os.system("pyarmor obfuscate --restrict=0 use.py")
os.system("pyarmor obfuscate --recursive --output dist.2 dist/__init__.py")

