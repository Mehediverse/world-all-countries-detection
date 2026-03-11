from setuptools import setup, find_packages
import os

# Read README if it exists, otherwise use description
long_description = "Advanced phone number country detection with 100% coverage for shared country codes. Supports 250 countries with intelligent area code detection for 12 shared prefix groups."

if os.path.exists("README.md"):
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()

setup(
    name="world-all-countries-detection",
    version="1.0.0",
    author="Mehediverse",
    author_email="",
    description="Advanced phone number country detection with 100% coverage for shared country codes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Mehediverse/world-all-countries-detection",
    py_modules=[
        "countrydetect",
        "countrydetect_advanced",
        "process_phone_files",
        "bulk_country_detector"
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Communications :: Telephony",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.6",
    install_requires=[],
    extras_require={
        "files": ["pandas>=1.3.0", "openpyxl>=3.0.0", "PyPDF2>=2.0.0"],
    },
    entry_points={
        "console_scripts": [
            "detect-country=process_phone_files:main",
            "detect-bulk=bulk_country_detector:main",
        ],
    },
)
