import mysql.connector
from conexion_bd import conectar_bd

def importar_sql(archivo_sql):
    conexion = conectar_bd()
    if conexion:
        cursor = conexion.cursor()
        with open(archivo_sql, 'r') as file:
            sql_script = file.read()
        for statement in sql_script.split(';'):
            if statement.strip():
                cursor.execute(statement)
        conexion.commit()
        print("Archivo SQL importado exitosamente")
        conexion.close()

if __name__ == '__main__':
    importar_sql('alquileresBD.sql')