from bank_model import BankModel

def test_add():
    data = {}
    # data['id']=8
    data['name'] ='minakshi'
    data['account_number'] =1234567890
    data['bank_name'] ='sbi'
    data['balance'] =2000

    model = BankModel()
    model.add(data)

def test_update():
    data = {}
    data['id'] = 2
    data['name'] = 'megha'
    data['account_number'] = 123456789
    data['bank_name'] ='hdfc'
    data['balance'] = 70000

    model = BankModel()
    model.update(data)


def test_delete():
    model = BankModel()
    model.delete(7)


def test_search():
    param = {}
    param['page_no'] = 1
    param['page_size'] = 5

    model = BankModel()
    list = model.search(param)

    for obj in list:
        print(obj['id'], '\t', obj['name'], '\t', obj['account_number'], '\t', obj['bank_name'], '\t', obj['balance'])

#
test_search()
# test_add()
# test_update()
# test_delete()

