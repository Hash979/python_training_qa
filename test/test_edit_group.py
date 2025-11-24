from model.group import Group

#def test_edit_group_header(app):
#    old_groups = app.group.get_group_list()
#    if app.group.count() == 0:
#        app.group.Create(Group(name="test"))
#    app.group.edit_group(Group(name="TESTNAME"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)

def test_edit_group_footer(app):
    group = Group(name="test")
    group.id = old_groups[0].id
    if app.group.count() == 0:
        app.group.Create(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.edit_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
