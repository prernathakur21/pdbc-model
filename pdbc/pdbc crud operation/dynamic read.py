import pymysql

#
# def testRead1():
#     connection = pymysql.connect(host='localhost', port=3306, user='root', password='9098', db='advance_python')
#     cursor = connection.cursor()
#     sql = "select * from emp"
#     cursor.execute(sql)
#     result = cursor.fetchall()
#     for data in result:
#         print(data[0], '\t', data[1], '\t', data[2], '\t', data[3], '\t', data[4], '\t', data[5])
#     connection.commit()
#     connection.close()


# def testRead2():
#     connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advance_python')
#     cursor = connection.cursor()
#     sql = "select * from college"
#     cursor.execute(sql)
#     result = cursor.fetchall()
#     columnName = ("id", "rollNo", "name", "physics", "chemistry", "maths")
#     for x in result:
#         print({columnName[i]: x[i] for i, _ in enumerate(x)})
#     connection.commit()
#     connection.close()
#
#
# def testRead3():
#     connection = pymysql.connect(host='localhost', port=3306, user='root', password='9098', db='advance_python')
#     cursor = connection.cursor()
#
#     # sql = "select * from college"
#     sql = "select * from emp where id = 1"
#     # sql = "select * from college where roll_no = 101"
#     # sql = "select * from college where name like 'a%'"
#     # sql = "select * from college where physics = 12"
#     # sql = "select * from college where chemistry = 34"
#     # sql = "select * from college where maths = 55"
#
#     print('sql => ', sql)
#     cursor.execute(sql)
#     result = cursor.fetchall()
#     for data in result:
#         print(data[0], '\t', data[1], '\t', data[2], '\t', data[3], '\t', data[4], '\t', data[5])
#     connection.commit()
#     connection.close()
#
#
# def testRead4(id,name, salary,dept_id):
#     connection = pymysql.connect(host='localhost', port=3306, user='root', password='9098', db='advance_python')
#     cursor = connection.cursor()
#
#     sql = 'select * from emp'
#     if id != 0:
#         sql += " where id = " + str(id)
#
#     if name != '':
#         sql += " where name like '" + name + "%'"
#     if salary != 0:
#         sql += " where salary = " + str(salary)
#     if dept_id != 0:
#         sql += " where dept_id = " + str(dept_id)
#     # if chemistry != 0:
#     #     sql += " where chemistry = " + str(chemistry)
#     # if maths != 0:
#     #     sql += " where maths = " + str(maths)
#     print('sql => ', sql)
#     cursor.execute(sql)
#     result = cursor.fetchall()
#     for data in result:
#         print(data[0], '\t', data[1], '\t', data[2], '\t', data[3])
#     connection.commit()
#     connection.close()
# testRead4(1,'',0,0)

#
# def testRead5(param={}):
#     id = param.get('id', 0)
#     name = param.get('name', '')
#     # name = param.get('name', '')
#     salary = param.get('salary', 0)
#     dept_id = param.get('dept_id', 0)
#     # maths = param.get('maths', 0)
#
#     connection = pymysql.connect(host='localhost', port=3306, user='root', password='9098', db='advance_python')
#     cursor = connection.cursor()
#     sql = "select * from emp where 1=1"
#     if id != 0:
#         sql += " and id = " + str(id)
#
#     if name != ' ':
#         sql += " and name like '" + name + "%'"
#     if salary != 0:
#         sql += " and salary=" + str(salary)
#     if dept_id != 0:
#         sql += " and dept_id =" + str(dept_id)
#     # if maths != 0:
#     #     sql += " and maths = " + str(maths)
#
#     print('sql => ', sql)
#     cursor.execute(sql)
#     result = cursor.fetchall()
#     for data in result:
#         print(data[0], '\t', data[1], '\t', data[2], '\t', data[3])
#     connection.commit()
#     connection.close()
#
# param = {}
# param['name'] = "r"
# #param['dept_id'] = 2
#
# testRead5(param)


#
#
# def testRead6(param={}):
#     id = param.get('id', 0)
#     name = param.get('name', '')
#     salary = param.get('salary', 0)
#     dept_id = param.get('dept_id', 0)
#     pageSize=param.get('pageSize',0)
#     pageNo=param.get('pageNo',0)
#
#
#
#     connection = pymysql.connect(host='localhost', port=3306, user='root', password='9098', db='advance_python')
#     cursor = connection.cursor()
#     sql = "select * from emp where 1=1"
#     if id != 0:
#         sql += " and id = " + str(id)
#
#     if name != ' ':
#         sql += " and name like '" + name + "%'"
#     if salary != 0:
#         sql += " and salary=" + str(salary)
#     if dept_id != 0:
#         sql += " and dept_id =" + str(dept_id)
#     # if maths != 0:
#     #     sql += " and maths = " + str(maths)
#
#     if pageSize > 0:
#         pageNo = (pageNo - 1) * pageSize
#         sql += " limit " + str(pageNo) + "," + str(pageSize)
#
#     print('sql => ', sql)
#     cursor.execute(sql)
#     result = cursor.fetchall()
#     for data in result:
#         print(data[0], '\t', data[1], '\t', data[2], '\t', data[3])
#     connection.commit()
#     connection.close()
#
#
# # testRead1()
# # testRead2()
# # testRead3()
# # testRead4(1, 101, '', 0, 0, 0)
#
# param = {}
# param['name'] = 'a'
# param['dept_id'] = 1
# param['pageNo'] = 1
# param['pageSize'] = 5
#
# # testRead5(param)
#
# testRead6(param)