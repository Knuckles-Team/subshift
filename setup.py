#!/usr/bin/env python
# coding: utf-8

from setuptools import setup

setup(
    name='subshift',
    version="0.1.4",
    description='Synchronize your subtitle files by shifting the subtitle time (+/-)',
    url='https://github.com/Knucklessg1/subsync',
    author='Audel Rouhi',
    author_email='knucklessg1@gmail.com',
    license='Unlicense',
    packages=[],
    install_requires=['chardet'],
    scripts=['subshift.py', 'subshift'],
    package_data={'subshift': ['subshift']},
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: Public Domain',
        'Environment :: Console',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)