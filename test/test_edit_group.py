from model.group import Group
from random import randrange
#def test_edit_group_header(app):
#    old_groups = app.group.get_group_list()
#    if app.group.count() == 0:
#        app.group.Create(Group(name="test"))
#    app.group.edit_group(Group(name="TESTNAME"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)

import random
from model.group import Group

def test_edit_group_footer(app, orm, check_ui):
    if len(orm.get_group_list()) == 0:
        app.group.Create(Group(name="test"))
    old_groups = orm.get_group_list()
    group = random.choice(old_groups)
    new_group_data = Group(name="test")
    new_group_data.id = group.id
    app.group.edit_group_by_id(group.id, new_group_data)
    new_groups = orm.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups = [new_group_data if g.id == group.id else g for g in old_groups]
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(app.group.get_group_list(), key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

