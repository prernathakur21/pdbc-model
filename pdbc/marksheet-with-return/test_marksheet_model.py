from marksheet_model import MarksheetModel

def test_add():
    data = {}
    # data['id']=8
    data['roll_no'] = 109
    data['name'] = 'harsh'
    data['physics'] = 81
    data['chemistry'] = 70
    data['maths'] = 79

    marksheet = MarksheetModel()
    marksheet.add(data)

def test_update():
    data = {}
    data['id'] = 2
    data['roll_no'] = 102
    data['name'] = 'minakshi'
    data['physics'] = 70
    data['chemistry'] = 85
    data['maths'] = 78

    marksheet = MarksheetModel()
    marksheet.update(data)


def test_delete():
    marksheet = MarksheetModel()
    marksheet.delete()


def test_search():
    param = {}
    param['page_no'] = 1
    param['page_size'] = 10

    marksheet = MarksheetModel()
    # marksheet.search(param)
    list = marksheet.search(param)

    for obj in list:
        print(obj['id'], '\t', obj['roll_no'], '\t', obj['name'], '\t', obj['physics'], '\t', obj['chemistry'], '\t',
              obj['maths'])


test_search()
# test_add()
# test_update()
# test_delete()
