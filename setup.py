# -*- coding: utf-8
from setuptools import find_packages, setup

setup(
    name='cleanup',
    author='dbcli',
    author_email='pgcli-dev@googlegroups.com',
    version='0.1',
    url='https://github.com/dbcli/cleanup',
    packages=find_packages(),
    include_package_data=True,
    description='Cleanup all the things',
    long_description=open('README.md').read(),
    install_requires=[line.strip() for line in open('requirements.txt') if line],
    extras_require={},
    entry_points="""
            [console_scripts]
            cleanup=cleanup.main:main
        """,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
