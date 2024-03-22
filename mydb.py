import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'nmor55209354'
)

cusorObject = dataBase.cursor()

cusorObject.execute('CREATE DATABASE rocky')

print('All Done!')