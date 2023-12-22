# flake8: noqa
from setuptools import find_packages, setup

setup(
    name="data-traps-core",
    version="0.1.0",
    description="",
    long_description="",
    url="https://github.com/mmazurekgda/data-traps-core",
    author="Michał Mazurek",
    license="GPLv3+",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.12",
    packages=find_packages(exclude=["*.test"]),
    install_requires=[
        "pydantic>=2.5.2",
        "pydantic-yaml",
    ],
)
