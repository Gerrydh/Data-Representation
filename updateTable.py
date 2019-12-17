import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="kim123",
    #user="gerardh",
    #password="Nov2019123" 
    database="datarepresentation"
)

cursor = db.cursor()
sql="update student set name= %s, age=%s where id = %s"
values = ("Jim", 33, 1)

cursor.execute(sql, values)
db.commit()

print("update done")