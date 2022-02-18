import setuptools
from setuptools.command.install import install
from setuptools.command.develop import develop

import subprocess


pkgs = ['core', 'matching', 'io']


def post_install():
    subprocess.run('conda install -c conda-forge -y openjdk maven jpype1',
                   shell=True,
                   stdout=subprocess.PIPE,
                   stderr=subprocess.STDOUT,
                   universal_newlines=True)
                   
    for pkg in pkgs:
        path = f'src/ontobuilder/jars/{pkg}'
        subprocess.run(f'cd {path}; mvn install dependency:copy-dependencies',
                       shell=True,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.STDOUT,
                       universal_newlines=True)


class InstallCommand(install):
    def run(self):
        install.run(self)
        post_install()
        

class DevelopCommand(develop):
    def run(self):
        develop.run(self)
        post_install()        


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ontobuilder",
    version="0.0.1",
    author="Guy Dar",
    author_email="guyd1995@gmail.com",
    description="Python port to Ontobuilder",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dar-tau/py_ontobuilder",
    project_urls={
        "Bug Tracker": "https://github.com/dar-tau/py_ontobuilder/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    cmdclass={
        'install': InstallCommand,
        'develop': DevelopCommand
    }
)
