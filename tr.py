import cv2
import argparse
import pandas as pd
from sklearn.processing import StandardScaler
import seaborn
import pysimplegui

parser = argparse.ArgumentParser()
parser.add_argument("0", help="index of the camera to read from", type=int)
args = parser.parse_args()

capture = cv2.VideoCapture(0)
if capture.isOpened()is False:
    print("Error opening the camera")
while capture.isOpened():
    ret, frame = capture.read()

    if ret is True:
        cv2.imshow('Input frame from the camera', frame)
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Grayscale input camera', gray_frame)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
    else:
        break
capture.release()
cv2.destroyAllWindows()

