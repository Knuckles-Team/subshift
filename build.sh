#!/bin/bash

python3 -m pip install -r ./requirements.txt
sudo chmod +x ./*.py
docker run -v "$(pwd):/src/" cdrx/pyinstaller-windows
python3 setup.py bdist_wheel --universal
