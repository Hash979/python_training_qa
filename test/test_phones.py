import re
from random import randrange
def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[1]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(1)
    assert contact_from_home_page.all_phones == merge_phones_on_home_page(contact_from_edit_page)


def test_phone_on_contact_view_page(app):
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    assert contact_from_view_page.home == contact_from_edit_page.home
    assert contact_from_view_page.work == contact_from_edit_page.work
    assert contact_from_view_page.mobile == contact_from_edit_page.mobile
    assert contact_from_view_page.fax == contact_from_edit_page.fax

def test_contact_on_home_page(app):
    index = randrange(app.contact.count() + 1)
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_emails == merge_emails_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_phones == merge_phones_on_home_page(contact_from_edit_page)

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home, contact.mobile, contact.work,]))))

def merge_emails_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                    map(lambda x: re.sub(" ", "", x),
                        filter(lambda x: x is not None,
                             [contact.email, contact.email2, contact.email3]))))