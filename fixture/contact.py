from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from model.Contact import Contact
import re
from sys import maxsize
class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_add_new_contact_page(self):
        wd = self.app.wd
        if not wd.current_url.startswith(edit_prefix=self.app.base_url + "edit.php?id="):
            wd.find_element(By.LINK_TEXT, "add new").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements(By.NAME, "selected[]")[index].click()
    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, "input[value='%s']" % id).click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element(By.NAME, "selected[]").click()

    def create_contact(self, contact):
        wd = self.app.wd
        self.open_add_new_contact_page()
        self.fill_contact_form(contact)
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[20]").click()
        self.app.open_home_page()
        self.contact_cache = None

    def edit_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        self.fill_contact_form(contact)
        wd.find_element(By.NAME, "update").click()
        self.app.open_home_page()
        self.contact_cache = None

    def edit_contact_by_id(self, id, contact):
        wd = self.app.wd
        self.open_contact_to_edit_by_id(id)
        self.fill_contact_form(contact)
        wd.find_element(By.NAME, "update").click()
        self.app.open_home_page()
        self.contact_cache = None

    def open_contact_to_edit_by_id(self, contact_id):
        wd = self.app.wd
        self.app.open_home_page()
        edit_link = wd.find_element(By.CSS_SELECTOR, f'a[href="edit.php?id={contact_id}"]')
        edit_link.click()
        return wd

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements(By.CSS_SELECTOR, 'img[alt="Edit"]')[index].click()
        return wd

    def edit_first_contact(self, contact):
        self.edit_contact_by_index(0, contact)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        wd.find_element(By.NAME, "delete").click()
        self.app.open_home_page()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(id)
        wd.find_element(By.NAME, "delete").click()
        self.app.open_home_page()
        self.group_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

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
        self.app.open_home_page()
        return len (wd.find_elements(By.NAME, "selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements(By.CSS_SELECTOR, "tr[name='entry']"):
                tds = element.find_elements(By.TAG_NAME, "td")
                lastname = tds[1].text
                firstname = tds[2].text
                id = element.find_element(By.NAME, "selected[]").get_attribute("value")
                address = tds[3].text
                all_emails = tds[4].text
                all_phones = tds[5].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id, all_phones=all_phones, all_emails=all_emails, address=address))
        return self.contact_cache

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element(By.NAME, "firstname").get_attribute("value")
        lastname = wd.find_element(By.NAME, "lastname").get_attribute("value")
        address = wd.find_element(By.NAME, "address").get_attribute("value")
        id = wd.find_element(By.NAME, "id").get_attribute("value")
        E_mail = wd.find_element(By.NAME, "email").get_attribute("value")
        E_mail2 = wd.find_element(By.NAME, "email2").get_attribute("value")
        E_mail3 = wd.find_element(By.NAME, "email3").get_attribute("value")
        homephone = wd.find_element(By.NAME, "home").get_attribute("value")
        workphone = wd.find_element(By.NAME, "work").get_attribute("value")
        mobilephone = wd.find_element(By.NAME, "mobile").get_attribute("value")
        fax = wd.find_element(By.NAME, "fax").get_attribute("value")
        return  Contact(firstname=firstname, lastname=lastname, id=id, address=address, home=homephone, work=workphone, mobile=mobilephone, fax=fax, email=E_mail, email2=E_mail2, email3=E_mail3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element(By.ID, "content").text
        home = re.search("H: (.*)", text).group(1)
        work = re.search("W: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        fax = re.search("F: (.*)", text).group(1)
        return Contact(home=home, work=work,
                       mobile=mobile, fax=fax)

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements(By.CSS_SELECTOR, 'img[alt="Details"]')[index].click()
        return wd

    def add_contact_into_group(self, id, group_id):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(id)
        wd.find_element(By.CSS_SELECTOR, "select[name='to_group'] option[value='%s']" % group_id).click()
        wd.find_element(By.NAME, "add").click()
        self.app.open_home_page()

    def remove_contact_from_group(self, id, id_group):
        wd = self.app.wd
        self.app.open_home_page()
        wd.get(self.app.base_url + "?group=%s" % id_group)
        self.delete_contact_by_id(id)




