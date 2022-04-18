#!/usr/bin/env python
# coding: utf-8

from setuptools import setup

setup(
    name='subshift',
    version="0.1.6",
    description='Synchronize your subtitle files by shifting the subtitle time (+/-)',
    long_description='''# Subshift
*Version 0.1.5*

A handy Python library to shift your subtitles +/- seconds so they align with your video

### Usage:
| Short Flag | Long Flag | Description              |
| --- | ------|--------------------------|
| -h | --help | See Usage                |
| -f | --file | Subtitle File            |
| -m | --mode | + / -                    |
| -t | --time | Time in seconds to shift |

### Example:
```bash
python3 subshift.py --file English.srt --mode + --time 5
```


#### Build Instructions
Build Python Package

```bash
sudo chmod +x ./*.py
sudo pip install .
python3 setup.py bdist_wheel --universal
# Test Pypi
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
# Prod Pypi
twine upload dist/*
```''',
    long_description_content_type='text/markdown',
    url='https://github.com/Knucklessg1/subsync',
    author='Audel Rouhi',
    author_email='knucklessg1@gmail.com',
    license='Unlicense',
    packages=[],
    install_requires=['chardet'],
    scripts=['subshift.py', 'subshift', 'dist/subshift/*'],
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
