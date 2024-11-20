#!/bin/bash
pip install -r requirements.txt --quiet

python ./main.py "$1" "$2"
