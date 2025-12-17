import random
from model.group import Group

def test_deleete_some_group(app, orm, check_ui):
    if len(orm.get_group_list()) == 0:
        app.group.Create(Group(name="test"))
    old_groups = orm.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    new_groups = orm.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(app.group.get_group_list(), key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)