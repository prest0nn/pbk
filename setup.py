from setuptools import setup

setup(
    name='pbk',
    version='2.0',
    py_modules=['preston'],
    install_requires=[
        'requests',
        'colorama',
    ],
    entry_points={
        'console_scripts': [
            'pbk=preston:main',
        ],
    },
)