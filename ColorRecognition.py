import cv2
import numpy as np
import pandas as pd

# Global variables
index = ['color', 'color_name', 'hex', 'R', 'G', 'B']
csv = pd.read_csv('colors.csv', names=index, header=None)

clicked = False
r = g = b = xpos = ypos = 0

def recognize_color(R, G, B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R - int(csv.loc[i,'R'])) + abs(G - int(csv.loc[i,'G'])) + abs(B - int(csv.loc[i,'B']))
        if d <= minimum:
            minimum = d
            cname = csv.loc[i,'color_name']
    return cname

def mouse_click(event, x, y, flags, param):
    # if event == cv2.EVENT_LBUTTONDBLCLK:
    if event == cv2.EVENT_LBUTTONUP:
        global b, g, r, xpos, ypos, clicked

        clicked = True
        xpos = x
        ypos = y

        b, g, r = img[y,x]

        b = int(b)
        g = int(g)
        r = int(r)

# Startup
cv2.namedWindow('Color Recognition')
cv2.setMouseCallback('Color Recognition', mouse_click)

image_path = 'test1.jpg'
# image_path = 'test2.jpg'

img = cv2.imread(image_path)

while 1:
    cv2.imshow('Color Recognition', img)
    if clicked:
        cv2.rectangle(img,(20,20), (750,60), (b,g,r), -1)

        text = recognize_color(r,g,b) + ' R='+ str(r) +  ' G='+ str(g) +  ' B='+ str(b)
        cv2.putText(img, text, (50,50), 2, 0.8, (255,255,255), 2, cv2.LINE_AA)

        if r + g + b >= 600:
            cv2.putText(img, text, (50,50), 2, 0.8, (0,0,0), 2, cv2.LINE_AA)
            
        clicked = False

    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
