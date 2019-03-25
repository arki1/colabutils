import setuptools
import colabutils

with open("README.md", "r") as fh:
    long_description = fh.read()

install_requires = [
    'google-api-python-client>=1.6.7',
    'ipython>=5.5.0',
]

setuptools.setup(
    name="colabutils",
    version=colabutils.__version__,
    author="ARKi1",
    author_email="fabricio@arki1.com",
    description="Utilities to use with Google Colaboratory",
    install_requires=install_requires,
    long_description=long_description,
    long_description_content_type="text/markdown",
    license=open('LICENSE').read(),
    url="https://github.com/arki1/colabutils",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "LICENSE :: OSI APPROVED :: GNU GENERAL PUBLIC LICENSE V3 (GPLV3)",
        "Operating System :: OS Independent",
    ],
)
