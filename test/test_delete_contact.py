import random
from model.Contact import Contact

def test_delete_some_contact(app, orm, check_ui):
    if len(orm.get_contact_list()) == 0:
        app.contact.create_contact(Contact(firstname="test"))
    old_contacts = orm.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = orm.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(app.contact.get_contact_list(), key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
