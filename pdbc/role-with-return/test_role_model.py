from role_model import RoleModel

def test_add():
    data = {}
    # data['id'] = 22
    data['name'] = 'megha'
    data['description'] = 'hello megha'

    role = RoleModel()
    role.add(data)

def test_update():
    data = {}
    data['id'] = 2
    data['name'] = 'megha'
    data['description'] = 'mmmjjhhg'

    role = RoleModel()
    role.update(data)

def test_delete():
    test = RoleModel()
    test.delete(1)

def test_search():
    params = {}
    # params['name'] = 'abc'
    # params['rollNo'] = 101
    params['pageNo'] = 1
    params['pageSize'] = 0
    model = RoleModel()
    list = model.search(params)
    for data in list:
        print(data['id'], '\t', data['name'], '\t', data['description'] )


def test_get():
    model = RoleModel()
    list = model.get(5)
    for data in list:
        print(data['id'], '\t', data['name'], '\t', data['description'] )

# test_add()
# test_update()
# test_delete()
# test_get()
test_search()
