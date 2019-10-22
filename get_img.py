import os
import sys
import cnn
import mysql.connector
from mysql.connector import Error

class get_img:
    def cnn_img(self, id, dir):
        cnn.cnn.get_img(id, dir)

    def get_dir_img(self, id):
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='####',
                                                 user='####',
                                                 password='####')
            cursor = connection.cursor()
            cursor.execute("SELECT t.* from transcripcion t INNER JOIN usuario u INNER JOIN usuario_transcripcion ut ON u.id = ut.fkIdUsuario AND t.id = fkIdTranscripcion WHERE u.id = '"+id+"'")
            records = cursor.fetchall()
            for row in records:
                if row[1] == 'NULL':
                    self.cnn_img(row[0], row[5])
                    exit()
            cursor.close()
        except Error as e:
            print("Error reading data from server", e)
        finally:
            if connection.is_connected():
                connection.close()

img = get_img()
img.get_dir_img(sys.argv[1])
