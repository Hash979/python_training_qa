from model.Contact import Contact
import random

def test_edit_contact(app, orm, json_contacts, check_ui):
    if len(orm.get_contact_list()) == 0:
        app.contact.create_contact(Contact(firstname="test"))
    old_contacts = orm.get_contact_list()
    contact_to_edit = random.choice(old_contacts)
    new_contact_data = json_contacts
    new_contact_data.id = contact_to_edit.id
    app.contact.edit_contact_by_id(contact_to_edit.id, new_contact_data)
    new_contacts = orm.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts = [new_contact_data if c.id == contact_to_edit.id else c for c in old_contacts]
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(app.contact.get_contact_list(), key=Contact.id_or_max) == sorted(new_contacts,
                                                                                       key=Contact.id_or_max)

#def test_edit_firstname_contact(app):
#    if app.contact.count() == 0:
#        app.contact.create_contact(Contact(firstname="test"))
#    app.contact.edit_first_contact(Contact(
#        firstname="Grib"
#    ))