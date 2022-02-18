import setuptools
from setuptools.command.install import install
from conda.cli import main as conda_run


pkgs = ['core', 'matching', 'io']


class CondaInstallCommand(install):
    def run(self):
        install.run(self)
        conda_run('conda', 'install', '-c', 'conda-forge', '-y', 'openjdk', 'maven', 'jpype1')
        for pkg in pkgs:
            path = f'src/ontobuilder/jars/{pkg}'
            conda_run('cd', path)
            conda_run('mvn', 'install', 'dependency:copy-dependencies')
        

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
        'install': CondaInstallCommand,
    }
)
