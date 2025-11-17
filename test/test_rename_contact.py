from model.Contact import Contact

def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.clear_contact()
    app.contact.edit_first_contact(Contact(
        firstname="Den",
        middlename="Brig",
        lastname="Hellen",
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
    app.session.logout()