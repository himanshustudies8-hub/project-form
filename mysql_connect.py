import mysql.connector

conn = mysql.connector.connect(
    host='sql12.freesqldatabase.com',
    user='sql12825012',
    password='b6wdUwJViL',
    database='sql12825012'
)
my_cursor = conn.cursor()

conn.commit()
conn.close()

print("connection succesfull created !")