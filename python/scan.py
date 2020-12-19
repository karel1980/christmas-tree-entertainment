import pygame
import json
import sys
from pygame.locals import *

import serial
import os
import glob
import time

import cv2

NUM_LEDS = 100

def main():
    print("Press space when the camera is properly positioned")

    cap = cv2.VideoCapture(0)
  
    ready = False
    while not ready:
        ret, frame = cap.read()
        cv2.imshow("imshow", frame) 
        key = cv2.waitKey(30)
        if key==ord(' '):
            ready = True

    # y u no work? main thread?
    cv2.destroyAllWindows()
    cv2.imshow("other", frame)

    for i in range(3):
        print("%d ..."%(i))
        time.sleep(1)

    cv2.imwrite('reference.png', frame)

    dev = glob.glob('/dev/cu.usbmodem*')[0]
    arduino = serial.Serial(dev, 9600, timeout=.1)

    for i in range(NUM_LEDS):
      arduino.write([i])
      time.sleep(0.05)
      ret, frame = cap.read()

      filename = 'led-%02d.png'%(i)
      print("Writing", filename)
      cv2.imwrite(filename, frame)

if __name__=="__main__":
  main()
