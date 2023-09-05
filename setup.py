from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="generator_gitignore_file",  
    version="0.1.0",  
    description="Create a .gitignore file for a given type from toptal.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="vitorio",
    packages=find_packages(),
    install_requires=["click", "requests"],
    entry_points={
        'console_scripts': [
            'gitignore_creator=generator.main:create_gitignore'
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha", 
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords="gitignore, toptal, development",
    python_requires=">=3.7, <4",
)
