#!/usr/bin/python
# -*- coding: utf-8 -*-

# face_recognition 安装步骤
# brew install cmake
# brew install boost
# brew install boost-python
# pip install face_recognition
import face_recognition

# pip install -U Pillow
from PIL import Image, ImageDraw

# https://www.jianshu.com/p/d2eaa7bbc868
import cv2

image = face_recognition.load_image_file("./img/test01.jpg")
face_locations = face_recognition.face_locations(image,model="cnn")
faceNum = len(face_locations)
# print(faceNum)
pil_image = Image.fromarray(image)
for i in range(0, faceNum):
    top =  face_locations[i][0]
    right =  face_locations[i][1]
    bottom = face_locations[i][2]
    left = face_locations[i][3]
    # 显示脸部图片
    # face_image = image[top:bottom, left:right]
    # pil_image = Image.fromarray(face_image)
    # pil_image.show()

    # pil_image = Image.fromarray(image)
    d = ImageDraw.Draw(pil_image, 'RGBA')
    d.rectangle((left, top, right, bottom),outline = "#00FF00")

pil_image.show()



# print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))


# image = face_recognition.load_image_file("./img/test01.jpg")
# image = cv2.imread("./img/test03.jpg",cv2.IMREAD_COLOR)
# face_locations = face_recognition.face_locations(image)
# print(face_locations)


# faceNum = len(face_locations)
# for i in range(0, faceNum):
#     top =  face_locations[i][0]
#     right =  face_locations[i][1]
#     bottom = face_locations[i][2]
#     left = face_locations[i][3]

#     start = (left, top)
#     end = (right, bottom)

#     color = (55,255,155)
#     cv2.rectangle(image, start, end, color, 3)

# # 显示识别结果
# # cv2.namedWindow("识别")
# cv2.imshow("识别", image)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
    

# image = cv2.imread("./img/test03.jpg",cv2.IMREAD_COLOR)
# #查找图像中所有面部的所有面部特征
# face_landmarks_list = face_recognition.face_landmarks(image)

# print("I found {} face(s) in this photograph.".format(len(face_landmarks_list)))

# for face_landmarks in face_landmarks_list:

#    #打印此图像中每个面部特征的位置
#     facial_features = [
#         'chin',
#         'left_eyebrow',
#         'right_eyebrow',
#         'nose_bridge',
#         'nose_tip',
#         'left_eye',
#         'right_eye',
#         'top_lip',
#         'bottom_lip'
#     ]

#     for facial_feature in facial_features:
#         print("The {} in this face has the following points: {}".format(facial_feature, face_landmarks[facial_feature]))

#    #让我们在图像中描绘出每个人脸特征！
#     pil_image = Image.fromarray(image)
#     d = ImageDraw.Draw(pil_image)

#     for facial_feature in facial_features:
#         d.line(face_landmarks[facial_feature], width=5)

#     pil_image.show()