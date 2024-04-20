from setuptools import setup, find_packages

setup(
    name='xagpy',
    version='0.2',
    packages=find_packages(),
    install_requires=['requests'],
    description='Api wrapper for the Xag(Xbox account generator) api',
    url='https://github.com/dropalways/xagpy',
    license='MIT',
)
