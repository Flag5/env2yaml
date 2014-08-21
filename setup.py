from setuptools import setup

setup(
    name="env2yaml",
    version = '1.0',
    maintainer='Luminoso Technologies, Inc.',
    maintainer_email='dev@luminoso.com',
    license = "MIT",
    url = 'http://github.com/LuminosoInsight/env2yaml',
    platforms = ["any"],
    description = ("A library for exporting the current environment into YAML "
                   "with anchors"),
    py_modules=['env2yaml'],
    install_requires=['pyyaml'],
    entry_points={
        'console_scripts': [
            'env2yaml = env2yaml:main',
            ]},
)
