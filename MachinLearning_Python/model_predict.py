# Créé par thomi, le 20/02/2023 en Python 3.7
import cv2
import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras.models import Model
from pickle import *






def predict_model(image_to_predict,model,img_height,img_width) :
  plt.imshow(cv2.cvtColor(image_to_predict, cv2.COLOR_BGR2RGB)) # convertir l'image
  image_to_predict = np.expand_dims(cv2.resize(image_to_predict,(img_height,img_width)), axis=0) # redimensionner l'image pour qu'elle soit prise par le model
  predict_x=model.predict(image_to_predict) # fonction prédiction
  classes_x=np.argmax(predict_x,axis=1)     # fonction prédiction
  print(classes_x)
  return(classes_x) # retorune la classe de l'image ( entier )




