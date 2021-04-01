"""Documentation Generator for wandb."""
from setuptools import setup, find_packages

project_name = 'docugen'
version = '0.0.0'
REQUIRED_PKGS = [
    'astor',
    'absl-py',
    'protobuf>=3.14',
    'pyyaml',
]

setup(
    name=project_name,
    version=version,
    description="A documentation generator.",
    author="Artira Roy Gosthipaty",
    author_email="aritra.born2fly@gmail.com",
    url='http://github.com/ariG23498/docugen',
    download_url='https://github.com/ariG23498/docugen/tags',
    install_requires=REQUIRED_PKGS,
    packages=find_packages('.'),
)
