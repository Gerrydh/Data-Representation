import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="kim123"
    #user="gerardh",
    #password="Nov2019123" 
)

cursor = db.cursor()

cursor.execute("CREATE DATABASE datarepresentation")