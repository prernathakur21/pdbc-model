from college_model import CollegeModel

def test_add():
    data = {}
    # data['id']=8
    data['name']='seoni'
    data['address']=' bypass'
    data['state']='UP'
    data['city']='bhopal'
    data['phone_number']='000000000'

    test=CollegeModel()
    test.add(data)

def test_update():
    data={}
    data['id']=2
    data['name']='rjpv bhopal'
    data['state']='MP'

    test1=CollegeModel()
    test1.update(data)

def test_delete():
    test2=CollegeModel()
    test2.delete(11)

def test_get():
    model = CollegeModel()
    list = model.get(5)
    for data in list:
        print(data['id'], '\t', data['name'], '\t', data['address'], '\t', data['state'], '\t', data['city'], '\t', data['phone_number'], )

def test_name():
    model = CollegeModel()
    list = model.find_by_name('MIT')
    for data in list:
        print(data['id'], '\t', data['name'], '\t', data['address'], '\t', data['state'], '\t', data['city'], '\t',data['phone_number'], )

def test_search():
    params = {}
    # params['name'] = 'abc'
    # params['roll_no'] = 101
    params['page_no'] = 1
    params['page_size'] = 0
    model = CollegeModel()
    list = model.search(params)
    for data in list:
        print(data['id'], '\t', data['name'], '\t', data['address'], '\t', data['state'], '\t', data['city'], '\t',data['phone_number'], )


# test_add()
# test_update()
# test_delete()
# test_get()
# test_name()
test_search()