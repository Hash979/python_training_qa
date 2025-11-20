from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create_contact(self, contact, new_contact=True):
        wd = self.app.wd
        if new_contact:
            self.open_add_new_contact_page()
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
        if new_contact:
            wd.find_element(By.XPATH, "//div[@id='content']/form/input[20]").click()
        else:
            wd.find_element(By.NAME, "update").click()
            self.app.open_home_page()


    def open_add_new_contact_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "add new").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element(By.NAME, "selected[]").click()
        wd.find_element(By.NAME, "delete").click()
        self.app.open_home_page()


    def clear_contact(self):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element(By.CSS_SELECTOR, 'img[alt="Edit"]').click()
        wd.find_element(By.NAME, "firstname").clear()
        wd.find_element(By.NAME, "middlename").clear()
        wd.find_element(By.NAME, "lastname").clear()
        wd.find_element(By.NAME, "nickname").clear()
        wd.find_element(By.NAME, "photo").clear()
        wd.find_element(By.NAME, "company").clear()
        wd.find_element(By.NAME, "title").clear()
        wd.find_element(By.NAME, "address").clear()
        wd.find_element(By.NAME, "home").clear()
        wd.find_element(By.NAME, "mobile").clear()
        wd.find_element(By.NAME, "work").clear()
        wd.find_element(By.NAME, "fax").clear()
        wd.find_element(By.NAME, "email").clear()
        wd.find_element(By.NAME, "email2").clear()
        wd.find_element(By.NAME, "email3").clear()
        wd.find_element(By.NAME, "homepage").clear()
