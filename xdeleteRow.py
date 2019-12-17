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
sql="delete from student where id = %s"
values = (1,)

cursor.execute(sql, values)
db.commit()

print("delete done")