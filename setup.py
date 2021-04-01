"""Documentation Generator for wandb."""
from setuptools import setup

PROJECT_NAME = 'docugen'
VERSION = '0.0.0'
REQUIRED_PKGS = [
    'astor',
]

setup(
    name=PROJECT_NAME,
    version=VERSION,
    description="A documentation generator.",
    author="Artira Roy Gosthipaty",
    author_email="aritra.born2fly@gmail.com",
    install_requires=REQUIRED_PKGS,
    packages=['docugen'],
)
