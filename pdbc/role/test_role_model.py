from role_model import RoleModel


def test_add():
    data = {}
    # data['id'] = 22
    data['name'] = 'megha'
    data['description'] = 'hello megha'

    role = RoleModel()
    role.add(data)
# test_add()

def test_update():
    data = {}
    data['id'] = 2
    data['name'] = 'megha'
    data['description'] = 'mmmjjhhg'

    role = RoleModel()
    role.update(data)

# test_update()
def test_delete():
    role = RoleModel()
    role.delete()
#
# test_delete()

def test_search():
   param={}

   # param['name']=''
   param['page_no'] = 1
   param['page_size'] = 10

   role = RoleModel()
   role.search(param)

test_search()




