import mysql.connector

conn=mysql.connector.connect(host='localhost',username='root',password='6618',database='school')
my_cursor=conn.cursor()

conn.commit()
conn.close()
print("connect")