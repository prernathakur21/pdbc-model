import  pymysql
def testInsert4(data={}):
    id = data['id']
    name = data['name']
    address = data['address']
    state = data['state']
    city = data['city']
    phone_number=data['phone_number']
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='9098', db='advanced_project')
    cursor = connection.cursor()
    sql = "insert into college values(%s, %s, %s, %s, %s, %s)"
    data = (id, name, address, state, city,phone_number)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print('data inserted successfully')

params = {}
params['id'] = 6
params['name'] ='MIT'
params['address'] ='nipaniya road bypass'
params['state'] ='Madhya Pradesh'
params['city'] ='indore'
params['phone_number']='9098220949'


print(params)
testInsert4(params)