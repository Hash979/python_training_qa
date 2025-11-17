from model.group import Group

def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_group(Group(name="DDDD", header="DDDD", footer="DDDD"))
    app.session.logout()
