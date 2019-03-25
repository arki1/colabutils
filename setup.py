import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

install_requires = [
    'google-api-python-client>=1.7.8',
]

setuptools.setup(
    name="colabutils",
    version="0.0.1",
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
