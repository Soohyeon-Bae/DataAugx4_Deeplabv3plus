import os
import cv2

file_path = 'label_1_dilated_disk3'
file_names = os.listdir(file_path)

for filename in file_names:
    print(filename)
    img = cv2.imread('label_1_dilated_disk3/' + filename)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(filename, gray)