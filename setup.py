from setuptools import setup

setup(
    name='vpn-switchboard',
    version='0.0.1',
    scripts=['main.py'],
    install_requires=[
        'appdirs',
    ],
    entry_points={
        'console_scripts': [
            'vpn-switchboard = main:main',
        ],
    },
)