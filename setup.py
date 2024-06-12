from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='xagpy',
    version='0.5',
    packages=find_packages(),
    install_requires=['requests'],
    description='Api wrapper for the Xag(Xbox account generator) api',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/dropalways/xagpy',
    license='MIT',
)
