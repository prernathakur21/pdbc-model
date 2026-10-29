import  pymysql
def testRead6(param={}):
    id = param.get('id', 0)
    name = param.get('name', '')
    address = param.get('address', '')
    # city = param.get('city', '')
    # phone_number = param.get('phone_number', 0)
    pageNo = param.get('pageNo', 1)
    pageSize = param.get('pageSize', 0)

    connection = pymysql.connect(host='localhost', port=3306, user='root', password='9098', db='advanced_project')
    cursor = connection.cursor()
    sql = "select * from college where 1=1"
    if id != 0:
        sql += " and id = " + str(id)
    if name != '':
        sql += " and name like '" + name + "%'"
    if address != '':
        sql += " and address = '" + address + "'"
    # if city != 0:
    #     sql += " and city = " + str(city)
    # if phone_number != 0:
    #     sql += " and phone_number = " + str(phone_number)

    if pageSize > 0:
        pageNo = (pageNo - 1) * pageSize
        sql += " limit " + str(pageNo) + ", " + str(pageSize)

    print('sql => ', sql)
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        print(data[0], '\t', data[1])
    connection.commit()
    connection.close()


param = {}
param['id'] = 2
param['name'] = 'N'
param['pageNo'] = 1
param['pageSize'] = 10

testRead6(param)