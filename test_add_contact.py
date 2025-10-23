# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
from Contact import Contact


class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_add_new_contact_page(wd)
        self.create_new_contact(wd, Contact(
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
        self.logout(wd)

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def login(self, wd, username, password):
        wd.find_element(By.NAME, "user").clear()
        wd.find_element(By.NAME, "user").send_keys(username)
        wd.find_element(By.NAME, "pass").clear()
        wd.find_element(By.NAME, "pass").send_keys(password)
        wd.find_element(By.XPATH, "//input[@value='Login']").click()

    def open_add_new_contact_page(self, wd):
        wd.find_element(By.LINK_TEXT, "add new").click()

    def create_new_contact(self, wd, contact):
        wd.find_element(By.NAME, "firstname").send_keys(contact.firstname)
        wd.find_element(By.NAME, "middlename").send_keys(contact.middlename)
        wd.find_element(By.NAME, "lastname").send_keys(contact.lastname)
        wd.find_element(By.NAME, "nickname").send_keys(contact.nickname)
        wd.find_element(By.NAME, "photo").send_keys(contact.photo_path)
        wd.find_element(By.NAME, "company").send_keys(contact.company)
        wd.find_element(By.NAME, "title").send_keys(contact.title)
        wd.find_element(By.NAME, "address").send_keys(contact.address)
        wd.find_element(By.NAME, "home").send_keys(contact.home)
        wd.find_element(By.NAME, "mobile").send_keys(contact.mobile)
        wd.find_element(By.NAME, "work").send_keys(contact.work)
        wd.find_element(By.NAME, "fax").send_keys(contact.fax)
        wd.find_element(By.NAME, "email").send_keys(contact.email)
        wd.find_element(By.NAME, "email2").send_keys(contact.email2)
        wd.find_element(By.NAME, "email3").send_keys(contact.email3)
        wd.find_element(By.NAME, "homepage").send_keys(contact.homepage)

        # date
        Select(wd.find_element(By.NAME, "bday")).select_by_visible_text(contact.bday)
        Select(wd.find_element(By.NAME, "bmonth")).select_by_visible_text(contact.bmonth)
        wd.find_element(By.NAME, "byear").send_keys(contact.byear)
        Select(wd.find_element(By.NAME, "aday")).select_by_visible_text(contact.aday)
        Select(wd.find_element(By.NAME, "amonth")).select_by_visible_text(contact.amonth)
        wd.find_element(By.NAME, "ayear").send_keys(contact.ayear)

        # Sace contact
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[20]").click()

    def logout(self, wd):
        wd.find_element(By.LINK_TEXT, "Logout").click()

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
            return True
        except NoSuchElementException:
            return False

    def is_alert_present(self):
        try:
            self.wd.switch_to.alert
            return True
        except NoAlertPresentException:
            return False

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
