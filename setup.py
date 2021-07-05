import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="echemex",
    version="0.0.2",
    author="Evan Miu",
    author_email="evm24@pitt.edu",
    description="Scripts for experimental electrochemistry data analysis in digital lab notebooks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/miuev/echemex",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['numpy>=1.17.2']
)
