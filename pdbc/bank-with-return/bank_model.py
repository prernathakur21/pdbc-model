import pymysql


class BankModel:

    def next_pk(self):
        pk = 0
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='9098', db='advance_python')
        cursor = connection.cursor()
        sql = "select max(id) from bank"
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
        id = BankModel.next_pk(self)
        name = data['name']
        account_number = data['account_number']
        bank_name = data['bank_name']
        balance=data['balance']

        connection = pymysql.connect(host='localhost', port=3306, user='root', password='9098', db='advance_python')
        cursor = connection.cursor()
        sql = "insert into bank values(%s, %s, %s, %s, %s)"
        data = (id, name, account_number, bank_name, balance)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print('data inserted successfully')

    def update(self, data):
        id = data['id']
        name = data['name']
        account_number = data['account_number']
        bank_name = data['bank_name']
        balance = data['balance']

        connection = pymysql.connect(host='localhost', port=3306, user='root', password='9098', db='advance_python')
        cursor = connection.cursor()
        sql = "update bank set name = %s, account_number = %s, bank_name = %s, balance = %s where id = %s"
        data = (name, account_number, bank_name, balance, id)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print('data updated successfully')

    def delete(self, id):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='9098', db='advance_python')
        cursor = connection.cursor()
        sql = "delete from bank where id = %s"
        data = (id)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print('data deleted successfully')

    def get(self, id):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='9098', db='advanced_project')
        cursor = connection.cursor()
        sql = "select * from bank where id = %s"
        data = (id,)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        column_name = ("id", "name", "account_number", "bank_name", "balance")
        list = []
        for x in result:
            # print({column_name[i]: x[i] for i, _ in enumerate(x)})
            list.append({column_name[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return list

    def find_by_name(self, name):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='9098', db='advanced_project')
        cursor = connection.cursor()
        sql = "select * from bank where name = %s"
        data = (name,)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        column_name = ("id", "name", "account_number", "bank_name", "balance")
        list = []
        for x in result:
            # print({column_name[i]: x[i] for i, _ in enumerate(x)})
            list.append({column_name[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return list

    def search(self, param):
        id = param.get('id', 0)
        name = param.get('name', '')
        account_number = param.get('account_number', 0)
        bank_name = param.get('bank_name', '')
        balance = param.get('balance', 0)
        page_no = param.get('page_no', 0)
        page_size = param.get('page_size', 0)

        connection = pymysql.connect(host='localhost', port=3306, user='root', password='9098', db='advance_python')
        cursor = connection.cursor()
        sql = "select * from bank where 1=1"
        if id != 0:
            sql += " and id = " + str(id)
        if name != '':
            sql += " and name like '" + name + "%'"
        if account_number != 0:
            sql += " and account_number = " + str(account_number)
        if bank_name != 0:
            sql += " and bank_name like '" + bank_name + "%'"
        if balance != 0:
            sql += " and balance = " + str(balance)

        if page_size > 0:
            page_no = (page_no - 1) * page_size
            sql += " limit " + str(page_no) + ", " + str(page_size)

        print('sql => ', sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        column_name = ("id", "name", "account_number", "bank_name", "balance")
        list = []
        for x in result:
            # print({column_name[i]: x[i] for i, _ in enumerate(x)})
            list.append({column_name[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return list
