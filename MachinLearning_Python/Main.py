# Créé par thomi, le 20/02/2023 en Python 3.7
import get_image
import model_predict
import classtomovement
import connectionJetsonArduino
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import sys
import datetime
from tensorflow import keras
from tensorflow.keras.models import Model
import tensorflow as tf
import pathlib
import os
from tensorflow.keras import layers
from pickle import *
import time

dataset_model = bool(input("Pressez 1 pour récupérer les données du modèle"))
if dataset_model:
    save = open('/home/thomas/projet_robot/dataset_model',"rb")
    model = load(save)
    img_height = load(save)
    img_width = load(save)
    save.close()

initialisation_cam = bool(input("Pressez 1 pour initialiser la caméra"))
if initialisation_cam:
  cam = cv2.VideoCapture(0) #Activation de la caméra, CAP_DSHOW pour que ca prenne moins de temps

connectionJetsonArduino.ArduinoJetson()

while j:

    img = get_image.get_img(cam)
    classe = model_predict.predict_model(img,model,img_height,img_width)

    if classe == 0:
         serial.Serial().write("Avancer|")
    elif classe == 1:
        serial.Serial().write("Tourner_a_droite|")
    elif classe == 2:
        serial.Serial().write("Tourner_a_gauche|")






