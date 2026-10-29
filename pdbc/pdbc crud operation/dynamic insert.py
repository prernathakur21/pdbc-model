import pymysql
# def testInsert4(data={}):
#     id = data['id']
#
#     name = data['name']
#     description=data['description']
#
#     connection = pymysql.connect(host='localhost', port=3306, user='root', password='9098', db='advance_python')
#     cursor = connection.cursor()
#     sql = "insert into role values(%s, %s, %s)"
#     data = (id, name,description)
#     cursor.execute(sql, data)
#     connection.commit()
#     connection.close()
#     print('data inserted successfully')
#
#
# params = {}
# params['id'] =21
# params['name'] = 'prerna'
# params['description'] ='hr'
#
# testInsert4(params)


# def testUpdate4(data):
#     id = data['id']
#     name = data['name']
#     description=data['description']
#
#
#     connection = pymysql.connect(host='localhost', port=3306, user='root', password='9098', db='advance_python')
#     cursor = connection.cursor()
#     sql = "update role set name=%s, description=%s where id=%s"
#     data = ( name,description,id)
#     cursor.execute(sql, data)
#     connection.commit()
#     connection.close()
#     print('data updated successfully')
#
# params = {}
# params['id'] = 16
# params['name'] = 'Minakshi'
# params['description']='Banking'
# testUpdate4(params)

#
# def testDelete3(id):
#     connection = pymysql.connect(host='localhost', port=3306, user='root', password='9098', db='advance_python')
#     cursor = connection.cursor()
#     sql = "delete from role where id = %s"
#     data = (id)
#     cursor.execute(sql, data)
#     connection.commit()
#     connection.close()
#     print('data deleted successfully')
#
# testDelete3(20)






