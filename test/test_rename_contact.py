from model.Contact import Contact

def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="test"))
    app.contact.edit_first_contact(Contact(
        firstname="Don",
        middlename="don",
        lastname="don",
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
    ))

def test_edit_firstname_contact(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="test"))
    app.contact.edit_first_contact(Contact(
        firstname="Grib"
    ))