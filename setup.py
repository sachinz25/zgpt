
from setuptools import setup, find_packages

# Read the contents of your README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="zgpt",
    version="0.2.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A versatile CLI assistant powered by the Gemini API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/zgpt",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.0",
    ],
    entry_points={
        "console_scripts": [
            "zgpt=zgpt.cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
