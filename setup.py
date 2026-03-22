from setuptools import setup, find_packages

setup(
    name="dataguardian",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy",
        "matplotlib",
        "seaborn"
    ],
    author="Your Name",
    description="A dataset diagnostic library for detecting data issues",
)