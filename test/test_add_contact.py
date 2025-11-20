# -*- coding: utf-8 -*-
from model.Contact import Contact


def test_add_contact(app):
    app.contact.create_contact(Contact(
        firstname="Anton",
        middlename="Velikoborets",
        lastname="Anton",
        nickname="Hash",
        photo_path=u"C:\\test.png",
        company="SecCode",
        title="sss",
        address="Groove street",
        home="8992",
        mobile="+79211908672",
        work="1232",
        fax="1233",
        email="hshus087@gmail.com",
        email2="hshus087@gmail.com",
        email3="hshus087@gmail.com",
        homepage="hshus087@gmail.com",
        bday="22",
        bmonth="November",
        byear="2001",
        aday="22",
        amonth="December",
        ayear="2002"
    ))


