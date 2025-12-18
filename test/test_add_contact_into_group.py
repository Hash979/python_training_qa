# -*- coding: utf-8 -*-
from model.Contact import Contact
from model.group import Group
import random

def test_delete_some_contact(app, orm):
    if len(orm.get_contact_list()) == 0:
        app.contact.create_contact(Contact(firstname="test"))
    if len(orm.get_group_list()) == 0:
        app.group.Create(Group(name="test"))
    old_contacts = orm.get_contact_list()
    contact = random.choice(old_contacts)
    old_groups = orm.get_group_list()
    group = random.choice(old_groups)
    app.contact.add_contact_into_group(contact.id, group.id)
    assert any(c.id == contact.id for c in orm.get_contacts_in_group(group))
    app.contact.remove_contact_from_group(contact.id, group.id)
    assert all(c.id != contact.id for c in orm.get_contacts_in_group(group))
