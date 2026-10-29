import pymysql

def testUpdate4(data):
    id = data['id']
    name = data['name']
    # address = data['address']
    state = data['state']
    # city= data['city']
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='9098', db='advanced_project')
    cursor = connection.cursor()
    sql = "update college set state = %s, name = %s  where id = %s"
    data = (state, name, id)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print('data updated successfully')


params = {}
params['id'] = 4
params['name'] = 'indore college'
params['state'] = 'mumbai'


testUpdate4(params)