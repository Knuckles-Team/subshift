# Subshift
*Version: 0.1.9*

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
```
