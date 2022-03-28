# Subshift

A handy Python library to shift your subtitles +/- seconds so they align with your video

### Usage:
| Short Flag | Long Flag | Description              |
| --- | ------|--------------------------|
| -f | --file | Subtitle File            |
| -m | --mode | + / -                    |
| -t | --time | Time in seconds to shift |

### Example:
```bash
python3 subshift.py --file English.srt --mode + --time 5
```