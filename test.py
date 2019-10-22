import numpy as np
from tensorflow.python.keras.preprocessing.image import load_img, img_to_array
from tensorflow.python.keras.models import load_model
from os import listdir
longitud, altura = 150, 150
modelo = './model/model2v(1)y2.h5'
pesos = './model/weights2v(1)y2.h5'

cnn = load_model(modelo)
cnn.load_weights(pesos)

def predict(file):
    x = load_img(file, target_size=(longitud, altura))
    x = img_to_array(x)
    x = np.expand_dims(x, axis=0)
    arreglo = cnn.predict(x)  # Retorna un arreglo de dos dimenciones [[1,0,0]] con la clase
    resultado = arreglo[0]  # Resultado es igual a los resultados almacenados en el arreglo de dos dimenciones
    respuesta = np.argmax(resultado)
    #    print(resultado)
    #    print(respuesta)
    return respuesta


# print('/content/drive/My Drive/Trabajo Terminal/Transcript/Transcript/data/train/A/a_('+repr(i+1)+').jpg')
# aux = predict('/content/drive/My Drive/Trabajo Terminal/Transcript/Transcript/data/train/A/a_ (3).jpg')

total = 1
contador = 0
list = listdir('/home/yohovani/Documents/opencv-text-detection/recortes/')
list.sort()
print(list)
for i in list:
#for i in range(total):
#    aux = predict('./pruebas/Z/z_ ('+repr(i+1)+').jpg')
    aux = predict('/home/yohovani/Documents/opencv-text-detection/recortes/'+i)
    if aux == 0:
        print("a")
    elif aux == 1:
        print("b")
    elif aux == 2:
        print("c")
    elif aux == 3:
        print("d")
    elif aux == 4:
        print("de")
    elif aux == 5:
        print("e")
    elif aux == 6:
        print("en")
    elif aux == 7:
        print("f")
    elif aux == 8:
        print("g")
    elif aux == 9:
        print("h")
    elif aux == 10:
        print("i")
    elif aux == 11:
        print("j")
    elif aux == 12:
        print("l")
    elif aux == 13:
        print("m")
    elif aux == 14:
        print("n")
    elif aux == 15:
        print("ñ")
    elif aux == 16:
        print("o")
    elif aux == 17:
        print("p")
    elif aux == 18:
        print("q")
    elif aux == 19:
        print("que")
    elif aux == 20:
        print("r")
    elif aux == 21:
        print("s")
    elif aux == 22:
        print("t")
    elif aux == 23:
        print("u")
    elif aux == 24:
        print("v")
    elif aux == 25:
        print("y")
    elif aux == 26:
        print("z")
        contador += 1

print(repr(contador / total))
print(repr(contador))