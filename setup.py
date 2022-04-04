from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in mobility_api/__init__.py
from mobility_api import __version__ as version

setup(
	name="mobility_api",
	version=version,
	description="APIs to connect ERPNext with Arabian tiers Front-End",
	author="Aerele Technologies Private Limited",
	author_email="vignesh@aerele.in",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
