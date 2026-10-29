import pymysql

connection=pymysql.connect(host="localhost",port=3306,user="root",password='9098',database="advance_python")
cursor=connection.cursor()

sql="update emp set name='abc' where id=16"

cursor.execute(sql)
print("update row")
connection.commit()
connection.close()