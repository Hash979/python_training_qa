from fixture.orm import ORMFixture
from model.group import Group


db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


try:
    le = db.get_contacts_not_in_group(Group(id=15))
    for item in le:
        print(item)
    print(len(le))
finally:
    pass #db.destroy()
