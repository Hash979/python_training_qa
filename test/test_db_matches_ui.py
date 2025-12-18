from model.group import Group
from model.Contact import Contact
import re

def test_group_list(app, db):
    ui_list = app.group.get_group_list()
    def clean (group):
        return Group(id=group.id, name=group.name.strip())
    db_list = map(clean, db.get_group_list())
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)


def clean_contact(contact):
    def clear(s):
        return re.sub("[() -]", "", s) if s else ""

    def merge_phones(contact):
        return "\n".join(filter(None, map(clear, [contact.home, contact.mobile, contact.work])))

    def merge_emails(contact):
        return "\n".join(filter(None, map(lambda x: x.replace(" ", "") if x else "",
                                          [contact.email, contact.email2, contact.email3])))

    return Contact(
        id=contact.id,
        firstname=contact.firstname.strip() if contact.firstname else "",
        lastname=contact.lastname.strip() if contact.lastname else "",
        address=contact.address.strip() if contact.address else "",
        all_phones=merge_phones(contact),
        all_emails=merge_emails(contact)
    )


def test_add_contact(app, orm):
    new_contact = Contact(firstname="Test", lastname="User", address="123 Main St",
                          home="111", mobile="222", work="333",
                          email="test@example.com", email2="t2@example.com", email3="t3@example.com")

    old_list = orm.get_contact_list_full()
    app.contact.add(new_contact)
    ui_list = app.contact.get_contact_list()
    orm_list = map(clean_contact, orm.get_contact_list_full())
    assert len(old_list) + 1 == len(ui_list)
    assert sorted(ui_list, key=Contact.id_or_max) == sorted(orm_list, key=Contact.id_or_max)


def test_delete_contact(app, orm):
    old_list = orm.get_contact_list_full()

    if not old_list:
        app.contact.add(Contact(firstname="Temp", lastname="User"))
        old_list = orm.get_contact_list_full()

    contact_to_delete = old_list[0]
    app.contact.delete_by_id(contact_to_delete.id)

    ui_list = app.contact.get_contact_list()
    orm_list = map(clean_contact, orm.get_contact_list_full())

    assert len(ui_list) == len(old_list) - 1
    assert sorted(ui_list, key=Contact.id_or_max) == sorted(orm_list, key=Contact.id_or_max)