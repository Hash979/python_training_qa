from model.Contact import Contact

def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    contacts = Contact(
        firstname="firstname",
        middlename="don",
        lastname="lastname",
        nickname="ssd",
        photo_path=u"C:\\test.png",
        company="dd",
        title="dd",
        address="dd",
        home="dd",
        mobile="+11112",
        work="dd",
        fax="dd",
        email="dd@gmail.com",
        email2="dd@gmail.com",
        email3="dd@gmail.com",
        homepage="dd@gmail.com",
        bday="12",
        bmonth="November",
        byear="2020",
        aday="21",
        amonth="December",
        ayear="2022"
    )
    contacts.id = old_contacts[0].id
    app.contact.edit_first_contact(contacts)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts)  == len(new_contacts)
    old_contacts[0] = contacts
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

#def test_edit_firstname_contact(app):
#    if app.contact.count() == 0:
#        app.contact.create_contact(Contact(firstname="test"))
#    app.contact.edit_first_contact(Contact(
#        firstname="Grib"
#    ))