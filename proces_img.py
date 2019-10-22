import sys
import numpy as np
from PIL import Image
from PIL import ImageDraw

class img:

    def open_img(self, dir):
        self.__img = Image.open(dir)
        self.__pix = self.__img.load()

    def get_RGB(self, x, y):
        return self.__pix[x, y]

    def segmentation(self):
        x = self.__img.size[0]
        y = self.__img.size[1]
        array_rule_color = np.zeros((5, 3), dtype=int)
        array = np.array([np.array(Image.new())])
        array_images = np.array(Image.Image("RGB", (x/2, y), "black"), 2)
        array_images[0] = Image.new("RGB", (x/2, y), "black")
        array_images[1] = Image.new("RGB", (x / 2, y), "black")
        for i in range(x-5):
            for j in range(y-5):
                #Obtener los colores de las coordenadas de la imagen
                array_rule_color[0] = self.__get_RGB(i+1, j)
                array_rule_color[1] = self.__get_RGB(i+1, j+1)
                array_rule_color[2] = self.__get_RGB(i + 1, j-1)
                array_rule_color[3] = self.___get_RGB(i, j+1)
                array_rule_color[4] = self.__get_RGB(i, j-1)
                #Proedio de color
                rule1 = (array_rule_color[0][0] + array_rule_color[0][1] + array_rule_color[0][2]) / 3
                rule2 = (array_rule_color[1][0] + array_rule_color[1][1] + array_rule_color[1][2]) / 3
                rule3 = (array_rule_color[2][0] + array_rule_color[2][1] + array_rule_color[2][2]) / 3
                rule4 = (array_rule_color[3][0] + array_rule_color[3][1] + array_rule_color[3][2]) / 3
                rule5 = (array_rule_color[4][0] + array_rule_color[4][1] + array_rule_color[4][2]) / 3
                if rule1 == 0:
                    if i+1 < (x-5):
                        for k in range(i):
                            array_images[0][k] = rule1
                            exit()
                        i += 1
                elif rule2 == 0:
                    if [i + 1 < (x - 5)] and [j+1 < (y - 5)]:
                        for k in range(i):
                            array_images[0][k] = rule1
                        i += 1
                        j += 1
                elif rule3 == 0:
                    if [i + 1 < (x - 5)] and [j-1 < (y - 5)]:
                        i += 1
                        j -= 1
                elif rule4 == 0:
                    if [j + 1 < (x - 5)]:
                        j += 1
                elif rule5 == 0:
                    if [j + 1 < (j - 5)]:
                        j -= 1
                else:
                    if [i + 1 < (x - 5)]:
                        i += 1
        return array_images


aux = img()
aux.open_img(sys.argv[1])
array = aux.segmentation()
array[0].show()
array[1].show()