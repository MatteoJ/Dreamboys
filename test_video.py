import cv2
import torch

vc = cv2.VideoCapture(0)

while True:
    rval, frame = vc.read()
    cv2.imshow("preview", frame)
    key = cv2.waitKey(20)
    if key == 27:
        break

cv2.destroyWindow("preview")
vc.release()

