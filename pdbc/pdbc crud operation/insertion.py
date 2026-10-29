import pymysql

connection=pymysql.connect(host="localhost",port=3306,user="root",password='9098',database="advance_python")
cursor=connection.cursor()

sql="insert into emp values(16,'xyz',50000, 2)"

cursor.execute(sql)
print("inserted row")
connection.commit()
connection.close()