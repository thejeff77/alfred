#!/bin/bash
brew install sox
brew install mpg321
brew install portaudio
virtualenv venv -p /usr/local/bin/python3.6
source venv/bin/activate
pip3 install -r requirements.txt
deactivate
echo "activate with: source venv/bin/activate"
