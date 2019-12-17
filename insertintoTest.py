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
sql="insert into student (name, age) values (%s, %s)"
values = ("Kim", 38)

cursor.execute(sql, values)

db.commit()
print("1 record inserted, ID", cursor.lastrowid)