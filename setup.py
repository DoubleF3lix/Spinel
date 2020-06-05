import setuptools

with open("README.md", "r") as readme:
    long_description = readme.read()

setuptools.setup(
    name="Spinel",
    version="1.1.3",
    description="A minecraft server wrapper written in python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ProfessorFelix/Spinel/",
    packages=setuptools.find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)