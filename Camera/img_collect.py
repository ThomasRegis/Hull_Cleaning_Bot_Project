 # Créé par thomi, le 30/04/2023 en Python 3.7

import get_image
import PIL
import cv2
import string
import time

initialisation_cam = bool(input("Pressez 1 pour initialiser la caméra"))
if initialisation_cam:
 cam = cv2.VideoCapture(0) #Activation de la caméra, CAP_DSHOW pour que ca prenne moins de temps

n =0
j = True
while j:
    img_to_save = get_image.get_img(cam)
    cv2.imwrite('/home/thomas/projet_robot/data_sort/bateau'+str(n)+'.jpg',img_to_save)
    n += 1
    time.sleep(0.5)