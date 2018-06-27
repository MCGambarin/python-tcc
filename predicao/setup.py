import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="predicao",
    version="0.0.1",
    author="Matheus Augusto Gambarin",
    author_email="matheusgambarin@gmail.com",
    description="Pacote para predição de dados",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MCGambarin/python-tcc",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
