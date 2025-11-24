from selenium.webdriver.common.by import By
from model.group import  Group
class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements(By.NAME, "name")) > 0):
            wd.find_element(By.LINK_TEXT, "groups").click()

    def Create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element(By.NAME, "new").click()
        self.fill_group_form(group)
        wd.find_element(By.NAME, "submit").click()
        self.return_to_groups_page()
        self.group_cache = None

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        self.select_fist_group()
        wd.find_element(By.NAME, "delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def edit_group(self, text):
        wd = self.app.wd
        self.open_groups_page()
        self.select_fist_group()
        wd.find_element(By.NAME, "edit").click()
        self.fill_group_form(text)
        wd.find_element(By.NAME, "update").click()
        self.return_to_groups_page()
        self.group_cache = None

    def fill_group_form(self, group):
        wd = self.app.wd
        self.is_None("group_name", group.name)
        self.is_None("group_header", group.header)
        self.is_None("group_footer", group.footer)

    def is_None(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)

    def select_fist_group(self):
        wd = self.app.wd
        wd.find_element(By.NAME, "selected[]").click()

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "group page").click()

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len (wd.find_elements(By.NAME, "selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements(By.CSS_SELECTOR, "span.group"):
                text = element.text
                id = element.find_element(By.NAME, "selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)