# Python drivers

## scan.py

Example usage:

    scan.py /dev/cu.usbmodem1234567

This script will light up each LED one by one and take a picture.
A reference photo is also taken. This can be used to automaticallly map the 
LED positions to x/y coordinates.

## game.py

Example usage:

    game.py lights.json /dev/cu.usbmodem1234567

This will open a blank window. When you mouse the mouse over the window, the id of the nearest led is sent to the arduino

