
import mysql.connector

class CConexion:

    def ConexionBaseDeDatos():
        try:
            conexion = mysql.connector.connect(user="root",password="root",
                                               host="127.0.0.1",
                                               database="clientesdb",
                                               port="3306")
            print("conexion correcta")

            return conexion
        
        except mysql.connector.Error as error:
            print("Error al conectarte a la BD {}".format(error))

            return conexion

    ConexionBaseDeDatos()