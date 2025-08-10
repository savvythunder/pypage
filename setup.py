#!/usr/bin/env python3
"""
Setup script for PyPage - Enhanced HTML Generator Library
"""

from setuptools import setup, find_packages
import os

# Read the README file for long description
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Read requirements from pyproject.toml or requirements file
def read_requirements():
    requirements = []
    if os.path.exists("requirements.txt"):
        with open("requirements.txt", "r") as f:
            requirements = [line.strip() for line in f if line.strip() and not line.startswith("#")]
    return requirements

setup(
    name="pypage",
    version="3.0.0",
    author="PyPage Development Team",
    author_email="dev@pypage.org",
    description="Enhanced HTML Generator Library with advanced features",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/pypage/pypage",
    project_urls={
        "Bug Tracker": "https://github.com/pypage/pypage/issues",
        "Documentation": "https://docs.pypage.org",
        "Source Code": "https://github.com/pypage/pypage",
    },
    packages=find_packages(exclude=["tests*", "testing*", "docs*", "examples*"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Markup :: HTML",
        "Topic :: Software Development :: Code Generators",
        "Framework :: Flask",
    ],
    python_requires=">=3.8",
    install_requires=[
        "flask>=2.0.0",
        "flask-sqlalchemy>=3.0.0",
        "sqlalchemy>=2.0.0",
        "jinja2>=3.0.0",
        "markupsafe>=2.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=22.0.0",
            "flake8>=5.0.0",
            "mypy>=1.0.0",
            "pre-commit>=3.0.0",
        ],
        "pdf": [
            "weasyprint>=60.0",
            "reportlab>=4.0.0",
        ],
        "charts": [
            "plotly>=5.0.0",
            "matplotlib>=3.5.0",
        ],
        "full": [
            "weasyprint>=60.0",
            "reportlab>=4.0.0",
            "plotly>=5.0.0",
            "matplotlib>=3.5.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "pypage=pypage.cli:main",
        ],
    },
    include_package_data=True,
    package_data={
        "pypage": [
            "templates/*.html",
            "static/css/*.css",
            "static/js/*.js",
        ],
    },
    keywords=[
        "html",
        "generator",
        "web",
        "framework",
        "bootstrap",
        "css",
        "javascript",
        "components",
        "ui",
        "responsive",
        "dark-mode",
        "animations",
        "charts",
        "forms",
    ],
    zip_safe=False,
)