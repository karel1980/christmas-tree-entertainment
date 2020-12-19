import pygame
import json
import sys
from pygame.locals import *

import serial
import os
import glob
import time


WIDTH,HEIGHT = 400, 400

def get_extents(lights):
    minx = min([l['x']for l in lights])
    maxx = max([l['x']for l in lights])
    miny = min([l['y']for l in lights])
    maxy = max([l['y']for l in lights])
    return minx, maxx,miny,maxy
  
def find_nearest(lights, pos):
    nearest = 0
    best = 9999999999
    for light in lights:
        dist = (light['x']-pos[0])**2 + (light['y']-pos[1])**2
        if dist < best:
            best = dist
            nearest = light['num']

    return nearest

def load_lights(filename, include_disabled = False):
    lights = json.load(open(sys.argv[1]))

    if include_disabled:
      return lights

    return [ l for l in lights if l['x'] is not None ]

def main():
    lights = load_lights(sys.argv[1])

    dev = glob.glob('/dev/cu.usbmodem*')[0]
    print("using device:", dev)
    arduino = serial.Serial(dev, 9600, timeout=.1)

    pygame.init()

    window = pygame.display.set_mode((WIDTH, HEIGHT))

    #extents = get_extents(lights)
    extents = 0,800,0,800

    minx,maxx,miny,maxy=extents

    running = True
    while running:

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the background with white
        window.fill((255, 255, 255))

        pos = pygame.mouse.get_pos()

        sx = int(pos[0]*(maxx-minx)/WIDTH + minx)
        sy = int(pos[1]*(maxy-miny)/HEIGHT + miny)
        scaled_pos = sx,sy
        
        n = find_nearest(lights, scaled_pos)
        arduino.write([n])
        # Draw a solid blue circle in the center
        #pygame.draw.circle(window, (0, 0, 255), (250, 250), 75)


        # Flip the display
        pygame.display.flip()

    # Done! Time to quit.
    pygame.quit()

if __name__ == "__main__":
  main()

if __name__=="__main__":
  main()
