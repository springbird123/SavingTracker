#!/bin/bash
sleep 1
if ! [[ -x "$(command -v python3)" ]]
then
  echo 'Error: 
    Python 3 is not installed.
    To install Python 3, please visit https://www.python.org/downloads/' >&2
  exit 1
pip install pandas
pip install art