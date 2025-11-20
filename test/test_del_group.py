from model.group import Group

def test_deleete_first_group(app):
    if app.group.count() == 0:
        app.group.Create(Group(name="test"))
    app.group.delete_first_group()
