import numpy as np
from tensorflow.python.keras.preprocessing.image import load_img, img_to_array
from tensorflow.python.keras.models import load_model

class predict:

    def __init__(self):
        self.__image_size = 150
        self.__cnn = load_model('./model/model.h5')
        self.__cnn.load_weights('./model/mweight.h5')

    def predict(self, file):
        x = load_img(file, target_size=(self.__image_size, self.__image_size))
        x = img_to_array(x)
        x = np.expand_dims(x, axis=0)
        array = self.__cnn.predict(x)
        result = array[0]
        answer = np.argmax(result)
        return answer