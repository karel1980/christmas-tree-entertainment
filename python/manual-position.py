import cv2
import sys
import json

def load_image(lights, num):
  if num < 0:
    return cv2.imread('reference.png')

  led_img = cv2.imread('led-%02d.png'%num)
  if lights[num]['x'] == None:
      return cv2.rectangle(led_img, (0,0),(20,20), (255,255,255), 3)

  x,y = lights[num]['x'], lights[num]['y']
  return cv2.rectangle(led_img, (x-10,y-10),(x+10,y+10), (255,255,255), 3)


def main():
  filename = sys.argv[1]
  lights = json.load(open(filename))

  num = -1

  cv2.namedWindow("current")

  def on_click(event, x, y, flags, params):
    if num < 0:
      return
    if event == cv2.EVENT_LBUTTONDOWN:
      lights[num]['x'] = x
      lights[num]['y'] = y
      current = None

  cv2.setMouseCallback("current", on_click)

  current = None
      
  while True:
    if current is None:
        current = load_image(lights, num)

    cv2.imshow("current", current)
    key = cv2.waitKey(30)

    if key == ord('q'): #quit (carefully, not saving here)
      cv2.destroyAllWindows()
      break
    if key == ord('n'): #next image
      if num < len(lights)-1:
        num += 1
        current = None
    if key == ord('p'): #previous image
      if num >= 0:
        num -= 1
        current = None
    if key == ord('s'): #save
      json.dump(lights, open(filename,'w'))
    if key == ord(' '): #Clear current image
      lights[num]['x'] = None
      lights[num]['y'] = None
      current = None
      
if __name__=="__main__":
    main()
