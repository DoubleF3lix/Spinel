from setuptools import find_packages
from setuptools import setup


with open("README.md", "r") as readme:
    long_desc = readme.read()

setup(
    name="spinel",
    version="1.1.3",
    url="https://github.com/ProfessorFelix/Spinel",
    license='GNU General Public License v3.0',

    author="ProfessorFelix",

    description="A minecraft server wrapper written in python",
    long_description=long_desc,
    long_description_content_type="text/markdown",

    packages=find_packages(),

    install_requires=[],

    classifiers=[
        "Operating System :: OS Independent",
        'License :: OSI Approved :: GNU General Public License v3.0',
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.7',
)
