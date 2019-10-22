import os

import tensorflow as tf
from tensorflow import keras

class train:
    def __init__(self):
        self.__train_dir = './data/train'
        self.__validation_dir= './data/validation'
        self.__image_size = 150
        self.__batch_size = 32
        # datos de los filtros
        self.__filtros_conv1 = 16
        self.__filtros_conv2 = 32
        self.__filtros_conv3 = 64
        self.__filtro_size1 = (4, 4)
        self.__filtro_size2 = (3, 3)
        self.__filtro_size3 = (2, 2)
        self.__pool_size = (2, 2)
        #datos del modelo
        self.__epoch = 50
        self.__class = 27
        # Cierra cualquier sesión de keras que se encuentre activa en la PC
        keras.backend.clear_session()

    #Preprocesamiento de las imagenes
    def image_reescale(self):
        self.__train_datagen = keras.preprocessing.image.ImageDataGenerator(rescale=1. / 255)
        self.__validation_datagen = keras.preprocessing.image.ImageDataGenerator(rescale=1. / 255)

    #Generador de entrenamiento y validación
    def generator(self):
        self.__train_generator = self.__train_datagen.flow_from_directory(
            self.__train_dir,
            target_size=(self.__image_size, self.__image_size),
            batch_size=self.__batch_size,
            class_mode='categorical'
        )
        self.__validation_generator = self.__validation_datagen.flow_from_directory(
            self.__validation_dir,
            target_size=(self.__image_size, self.__image_size),
            batch_size=self.__batch_size,
            class_mode='categorical'
        )

    def model_creation(self):
        self.__cnn = tf.keras.Sequential()

    def add_layer(self, layer):
        self.__cnn.add(layer)

    def train(self):
        self.__cnn.add(tf.python.keras.layers.Flatten)
        self.__cnn.add(tf.python.keras.layers.Dense(256, activation='relu'))
        self.__cnn.add(tf.python.keras.layers.Dropout(0.5))

    def save_model(self):
        if not os.path.exists('./model/'):
            os.mkdir(dir)
        self.__cnn.save('./model/model.h5')
        self.__cnn.save_weights('./model/weights.h5')

    def train(self):
        self.image_reescale()
        self.generator()
        self.model_creation()
        self.train()
        self.save_model()