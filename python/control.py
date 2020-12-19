
import serial
import sys
import os
import glob
import time

def main():
  dev = glob.glob('/dev/cu.usbmodem*')[0]
  print("using device:", dev)
  arduino = serial.Serial(dev, 9600, timeout=.1)
  while True:
    for i in range(15,100):
      print("writing", i) 
      arduino.write([i])
      time.sleep(1)

if __name__=="__main__":
  main()
