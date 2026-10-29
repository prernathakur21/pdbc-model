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


# test_add()

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
    param['page_size'] = 0

    marksheet = MarksheetModel()
    marksheet.search(param)


test_search()
# test_delete()
# test_update()
