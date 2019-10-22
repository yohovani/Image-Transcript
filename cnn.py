import os
import sys
import predict
import train
import mysql.connector
from mysql.connector import Error

class cnn:
    def __init__(self):
        self.__entrenamiento = train()
        self.__predecir = predict()
        self.__connection = mysql.connector.connect(host='localhost',
                                                 database='test',
                                                 user='root',
                                                 password='Recovery')

#falta el id de la tranascripcion
    def save_transcription(self, transcript, id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("UPDATE Transcripcion SET Transcripcion = '"+transcript+"' WHERE id = '"+id+"'")
            self.connection.commit()
            cursor.close()
        except Error as e:
            print("Error reading data from server", e)
        finally:
            if self.connection.is_connected():
                self.connection.close()


    def transcription(self, id, dir):
        if not os.path.isfile('./model/model.h5') or not os.path.isfile('./model/weights.h5'):
            self.entrenamiento.train()
        else:
            transcript = ''
            for i in range(len(sys.argv)-1):
                transcript += self.predecir.predict(dir)
            self.save_transcription(id, transcript)

    def get_img(self, id, dir):
        if os.path.isfile(dir):
           self.transcription(id, dir)
        else:
            #se guarda un mensaje de error en BD
            cursor = self.connection.cursor()
            cursor.execute("UPDATE transcripcion SET Transcripcion = 'Error al procesar la imagen'")
            self.connection.commit()
            cursor.close()



