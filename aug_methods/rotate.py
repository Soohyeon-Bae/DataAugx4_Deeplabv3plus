import os
import cv2

file_path = 'only_crack_img_053-055'
file_names = os.listdir(file_path)

for filename in file_names:
    print(filename)
    img = cv2.imread('only_crack_img_053-055/' + filename, cv2.IMREAD_COLOR)

    img90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)  # 시계방향으로 90도 회전
    img180 = cv2.rotate(img, cv2.ROTATE_180)  # 180도 회전
    img270 = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)  # 반시계방향으로 90도 회전
    # = 시계방향으로 270도 회전

    cv2.imwrite('bigeye2_rot/img/original/'+filename, img)
    cv2.imwrite('bigeye2_rot/img/rotate90/'+filename, img90)
    cv2.imwrite('bigeye2_rot/img/rotate180/'+filename, img180)
    cv2.imwrite('bigeye2_rot/img/rotate270/'+filename, img270)


