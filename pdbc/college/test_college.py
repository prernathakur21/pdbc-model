from college_model import CollegeModel

def test_add():
    data = {}
    # data['id']=1
    data['name']='seoni'
    data['address']=' bypass'
    data['state']='UP'
    data['city']='bhopal'
    data['phone_number']='000000000'

    model=CollegeModel()
    model.add(data)

# test_add()

def test_update():
    data={}
    data['id']=9
    data['name']=' kolkatta college '
    data['address']='madhumilan square'
    data['state']='rayghad'
    data['city']='seoni'
    data['phone_number']=7806073435

    model=CollegeModel()
    model.update(data)

# test_update()

def test_delete():

    model=CollegeModel()
    model.delete(0)

# test_delete()

def test_search():
    param={}
    param['pageNo']=1
    param['pageSize']=8

    model = CollegeModel()
    model.search(param)

test_search()


