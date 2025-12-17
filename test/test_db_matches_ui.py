from model.group import Group
from model.Contact import Contact
import re

def test_group_list(app, db):
    ui_list = app.group.get_group_list()
    def clean (group):
        return Group(id=group.id, name=group.name.strip())
    db_list = map(clean, db.get_group_list())
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)

def test_contact_list(app, orm):
    ui_list = app.contact.get_contact_list()
    def clean(contact):
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
    orm_list = map(clean, orm.get_contact_list())
    assert sorted(ui_list, key=Contact.id_or_max) == sorted(orm_list, key=Contact.id_or_max)