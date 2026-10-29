import pymysql

connection=pymysql.connect(host="localhost",port=3306,user="root",password='9098',database="advance_python")
cursor=connection.cursor()

sql="select * from emp"

cursor.execute(sql)
result=cursor.fetchall()

for data in result:
    print(data[0],data[1],data[2],data[3])
connection.close()