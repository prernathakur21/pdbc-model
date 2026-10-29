import pymysql


class CollegeModel:

    def next_pk(self):
        pk = 0
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='9098', db='advanced_project')
        cursor = connection.cursor()
        sql = "select max(id) from college"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
        for data in result:
            if data[0] is not None:
                pk = data[0]
        connection.commit()
        connection.close()

        return pk + 1

    def add(self, data):
        id = CollegeModel.next_pk(self)
        name = data['name']
        address = data['address']
        state = data['state']
        city = data['city']
        phone_number = data['phone_number']
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='9098', db='advanced_project')
        cursor = connection.cursor()
        sql = "insert into college values(%s, %s, %s, %s, %s, %s)"
        data = (id, name, address, state, city, phone_number)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print('data inserted successfully')

    def update(self, data):
        id = data['id']
        name = data['name']
        address = data['address']
        state = data['state']
        city = data['city']
        phone_number = data['phone_number']

        connection = pymysql.connect(host='localhost', port=3306, user='root', password='9098', db='advanced_project')
        cursor = connection.cursor()
        sql = "update college set name = %s,address = %s,state = %s,city = %s,phone_number = %s  where id = %s"
        data = (name, address, state, city, phone_number, id)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print('data updated successfully')


    def delete(self, id):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='9098', db='advanced_project')
        cursor = connection.cursor()
        sql = "delete from college where id = %s"
        data = (id)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print('data deleted successfully')

    def get(self, id):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='9098', db='advanced_project')
        cursor = connection.cursor()
        sql = "select * from college where id = %s"
        data = (id,)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        for data in result:
            print(data[0], '\t', data[1], '\t', data[2], '\t', data[3], '\t', data[4], '\t', data[5])
        connection.commit()
        connection.close()

    def find_by_name(self, name):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='9098', db='advanced_project')
        cursor = connection.cursor()
        sql = "select * from college where name = %s"
        data = (id,)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        for data in result:
            print(data[0], '\t', data[1], '\t', data[2], '\t', data[3], '\t', data[4], '\t', data[5])
        connection.commit()
        connection.close()

    def search(self, param):
        id = param.get('id', 0)
        name = param.get('name', '')
        address = param.get('address', '')
        city = param.get('city', '')
        phone_number = param.get('phone_number', 0)
        page_no = param.get('page_no', 0)
        page_size = param.get('page_size', 0)

        connection = pymysql.connect(host='localhost', port=3306, user='root', password='9098', db='advanced_project')
        cursor = connection.cursor()
        sql = "select * from college where 1=1"
        if id != 0:
            sql += " and id = " + str(id)
        if name != '':
            sql += " and name like '" + name + "%'"
        if address != '':
            sql += " and address like '" + address + "%'"
        if city != '':
            sql += " and city like '" + city + "%'"
        if phone_number != 0:
            sql += " and phone_number = " + str(phone_number)

        if page_size > 0:
            page_no = (page_no - 1) * page_size
            sql += " limit " + str(page_no) + ", " + str(page_size)

        print('sql => ', sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        for data in result:
            print(data[0], '\t', data[1], '\t', data[2], '\t', data[3], '\t', data[4], '\t', data[5])
        connection.commit()
        connection.close()


