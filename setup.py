from setuptools import setup, find_packages

setup(
    name="Sistema Gem",
    version="1.0",
    description='Software de gestion ERP para emprendimientos y pymes',
    author='Ramiro Tules',
    password='mdi25g.c',
    packages=find_packages(),
    requires=[
        "openpyxl",
        "pickle",
    ],
)
