import os
import cv2

file_path = 'bigeye1_rot/mask/mask'
file_names = os.listdir(file_path)

for filename in file_names:
    print(filename)
    img = cv2.imread('bigeye1_rot/mask/mask/' + filename)
    flip = cv2.flip(img, 1)
    cv2.imwrite('bigeye1_rot_flip/mask/'+filename, flip)
