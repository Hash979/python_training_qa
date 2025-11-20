from model.group import Group

def test_edit_group_header(app):
    if app.group.count() == 0:
        app.group.Create(Group(name="test"))
    app.group.edit_group(Group(name="TESTNAME"))

def test_edit_group_footer(app):
    if app.group.count() == 0:
        app.group.Create(Group(name="test"))
    app.group.edit_group(Group(footer="DDDD"))