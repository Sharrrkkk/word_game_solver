from setuptools import setup, find_packages


setup(
    name="anagram_generator",
    version="1.0",
    description="Generate valid English word sets based on a specified word " \
        "length and a set of input characters using anagrams and a file with English words.",
    author="Sharrrkkk",
    url="https://github.com/Sharrrkkk/anagram_generator",
    project_urls={
        "Documentation": "https://github.com/Sharrrkkk/anagram_generator#README.md",
        "Source": "https://github.com/Sharrrkkk/anagram_generator"
    },
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "anagrams = project.cli:run_cli"
        ],
    },
    python_requires=">=3.10",
)