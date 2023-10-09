# Créé par thomi, le 18/02/2023 en Python 3.7
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import sys
import datetime
from tensorflow import keras
from tensorflow.keras.models import Model
import tensorflow as tf
from pickle import *
import pathlib
import os
from tensorflow.keras import layers

def train_model(data_path,batch_size,img_height,img_width,num_classes,iter):

    data_dir = pathlib.Path(data_path) #chemin ou sont rangées les images


    train_data = tf.keras.preprocessing.image_dataset_from_directory(  # prérequis pour entrainer le réseau
    data_dir, #endroit pour aller chercher les images
    validation_split=0.2, #?
    subset="training",
    seed=42,
    image_size=(img_height, img_width), #taille image
    batch_size=batch_size,  # taille lot données
        )

    val_data = tf.keras.preprocessing.image_dataset_from_directory(    # prérequis pour valider le réseau
       data_dir,
       validation_split=0.2,
       subset="validation",
       seed=42,
       image_size=(img_height, img_width),
       batch_size=batch_size   )


    model =     tf.keras.Sequential([  #création du model de réseau de neurones

      layers.experimental.preprocessing.Rescaling(1./255), # Couche de rescaling pour mettre les pixels entre 0 et 1 ( 1ère couche)
      layers.Conv2D(128,4, activation = 'relu'), #(128 neurones, taille de la matrice de kernel, ?) dimension du filtre
      layers.MaxPooling2D(),                   # méthode du maximum
      layers.Conv2D(64,4, activation='relu'),
      layers.MaxPooling2D(),
      layers.Conv2D(32,4, activation='relu'),
      layers.MaxPooling2D(),
      layers.Conv2D(16,4, activation='relu'),
      layers.MaxPooling2D(),
      layers.Flatten(), # vecteur à partir d'une matrice
      layers.Dense(64, activation = 'relu'), # 64 neurones, on peut jouer avec l'activation
      layers.Dense(num_classes, activation = 'softmax') # softmax pour avoir la probabilité entre les différentes classes, nombre de neurones fin = nombre de classes

        ])

    model.compile(optimizer='adam',  #configuration du model avec losses and metrics
              loss=tf.losses.SparseCategoricalCrossentropy(from_logits=True), #adam le plus utilisé, choix de la loss
              metrics=['accuracy'],)

    logdir="logs"

    tensorboard_callback = keras.callbacks.TensorBoard(log_dir=logdir,histogram_freq=1, write_images=logdir,embeddings_data=train_data)
                                                     # fonction de retour Réseau de neurones

    model.fit(  #entrainement du model
     train_data,    # données d'entrainement
     validation_data=val_data,  #données de validation
     epochs = iter,                       #nombre d'itération
     callbacks=[tensorboard_callback])

    save = open ('C:/Users/thomi/OneDrive/Bureau/projet_robot_Nvidia/dataset_model',"wb")
    dump (model,save)
    dump (img_height,save)
    dump(img_width,save)
    save.close()

train_model('C:/Users/thomi/OneDrive/Bureau/projet_robot_Nvidia/dataset_train',3,200,200,3,1)

