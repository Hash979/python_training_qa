import random

from model.group import Group
from random import randrange
def test_deleete_some_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.Create(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups.remove(group)
    assert old_groups == new_groups