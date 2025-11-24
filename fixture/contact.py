from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from model.Contact import Contact
from sys import maxsize
class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_add_new_contact_page(self):
        wd = self.app.wd
        if not wd.current_url.startswith("http://localhost/addressbook/edit.php?id="):
            wd.find_element(By.LINK_TEXT, "add new").click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element(By.NAME, "selected[]").click()

    def create_contact(self, contact):
        wd = self.app.wd
        self.open_add_new_contact_page()
        self.fill_contact_form(contact)
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[20]").click()
        self.app.open_home_page()

    def edit_first_contact(self, contact):
        wd = self.app.wd
        self.app.open_home_page
        wd.find_element(By.CSS_SELECTOR, 'img[alt="Edit"]').click()
        self.fill_contact_form(contact)
        wd.find_element(By.NAME, "update").click()
        self.app.open_home_page()

    def delete_first_contact(self):
        wd = self.app.wd
        self.app.open_home_page
        self.select_first_contact()
        wd.find_element(By.NAME, "delete").click()
        self.app.open_home_page()

    def fill_contact_form(self, contact):
        wd = self.app.wd

        self.is_None("firstname", contact.firstname)
        self.is_None("middlename", contact.middlename)
        self.is_None("lastname", contact.lastname)
        self.is_None("nickname", contact.nickname)

        self.is_None("photo", contact.photo_path)

        self.is_None("company", contact.company)
        self.is_None("title", contact.title)
        self.is_None("address", contact.address)

        self.is_None("home", contact.home)
        self.is_None("mobile", contact.mobile)
        self.is_None("work", contact.work)
        self.is_None("fax", contact.fax)

        self.is_None("email", contact.email)
        self.is_None("email2", contact.email2)
        self.is_None("email3", contact.email3)
        self.is_None("homepage", contact.homepage)

        # Даты
        self.is_None("bday", contact.bday, is_select=True)
        self.is_None("bmonth", contact.bmonth, is_select=True)
        self.is_None("byear", contact.byear)

        self.is_None("aday", contact.aday, is_select=True)
        self.is_None("amonth", contact.amonth, is_select=True)
        self.is_None("ayear", contact.ayear)

    def is_None(self, field_name, value, is_select=False):
        wd = self.app.wd
        if value is not None:
            if is_select:
                Select(wd.find_element(By.NAME, field_name)).select_by_visible_text(value)
            else:
                wd.find_element(By.NAME, field_name).clear()
                wd.find_element(By.NAME, field_name).send_keys(value)

    def count(self):
        wd = self.app.wd
        self.app.open_home_page
        return len (wd.find_elements(By.NAME, "selected[]"))

    def get_contact_list(self):
        wd = self.app.wd
        self.app.open_home_page
        contacts = []
        for element in wd.find_elements(By.CSS_SELECTOR, "tr[name='entry']"):
            tds = element.find_elements(By.TAG_NAME, "td")
            lastname = tds[1].text
            firstname = tds[2].text
            id = element.find_element(By.NAME, "selected[]").get_attribute("value")
            contacts.append(Contact(firstname=firstname, lastname=lastname, id=id))
        return contacts