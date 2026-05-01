import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root' ,
    password='Himanshu4444@',
    database='form'
)
my_cursor = conn.cursor()

conn.commit()
conn.close()

print("connection succesfull created !")