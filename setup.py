from setuptools import find_packages, setup

setup(
    name="github-sentinel",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "PyGithub>=2.1.1",
        "schedule>=1.2.0",
        "python-dotenv>=1.0.0",
        "requests>=2.31.0",
        "pydantic>=2.5.2",
        "rich>=13.7.0",
        "click>=8.1.7",
        "aiohttp>=3.9.1",
        "jinja2>=3.1.2",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.3",
            "black>=23.11.0",
            "isort>=5.12.0",
            "mypy>=1.7.1",
        ]
    },
    entry_points={
        "console_scripts": [
            "github-sentinel=github_sentinel.__main__:cli",
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="GitHub 仓库监控工具",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/github-sentinel",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
)
