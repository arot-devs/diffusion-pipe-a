#!/bin/bash

git clone https://github.com/arot-devs/procslib
git clone https://github.com/arot-devs/trainlib
git clone https://github.com/arot-devs/imagelib

cd procslib
pip install -e .
./pip_install.sh