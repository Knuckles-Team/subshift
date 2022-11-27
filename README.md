# Subshift
*Version: 0.5.1*

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

#### Install Instructions
Install Python Package

```bash
python -m pip install subshift
```

#### Build Instructions
Build Python Package

```bash
sudo chmod +x ./*.py
sudo pip install .
python3 setup.py bdist_wheel --universal
# Test Pypi
twine upload --repository-url https://test.pypi.org/legacy/ dist/* --verbose -u "Username" -p "Password"
# Prod Pypi
twine upload dist/* --verbose -u "Username" -p "Password"
```
