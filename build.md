> python 3.10

## macos

python3 -m venv .venv

source .venv/bin/activate


pip install -r requirements.txt

python setup.py bdist_dmg




## windows


python -m venv .venv

source .venv/Scripts/activate


pip install -r requirements.txt

python setup.py bdist_msi


rm -rf build dist




how to sign code for mac dmg

https://developer.apple.com/forums/thread/678816