# video filename
# loading screen filename
# threshold (default 0.25)

import cv2
import sys
import numpy as np
from matplotlib import pyplot as plt

args = sys.argv

cap = cv2.VideoCapture(args[1]) # video

template = cv2.imread(args[2],0) # loading screen
w, h = template.shape[::-1]

# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video stream or file")

totalframes = 0
loadingframes = 0

threshold = 0.25

if (len(args) >= 4):
    threshold = float(args[3])
    

# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:

    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)

    totalframes += 1

    results = np.where( res >= threshold)

    if results[0].size > 0:
        loadingframes += 1

    print(f"Running, Total frames {totalframes}, loading frames {loadingframes}")

  # Break the loop
  else: 
    break

# When everything done, release the video capture object
cap.release()

print(f"Total frames {totalframes}, loading frames {loadingframes}")
