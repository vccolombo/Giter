from setuptools import setup, find_packages
import os

with open('README.md', "r") as file:
    long_description = file.read()

setup(
    name='giter',
    version='1.0.2',
    packages=find_packages(),
    author='David Voigt',
    author_email='David.Voigt1998@gmail.com',
    description='Command line application to quickly set up new repositories on Github and add it as origin to your local repo.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Xcal1bur/Giter',
    license='GNU General Public License v3.0',
    install_requires=['requests', 'pygithub'],
    entry_points={'console_scripts': ['giter = giter.giter:main']},
)
