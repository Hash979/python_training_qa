import jsonpickle
from model.Contact import Contact
import random
import string
import os
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["numbers of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o,a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_day():
    return str(random.randint(1, 28))


def random_year(start=1970, end=2025):
    return str(random.randint(start, end))


def random_month():
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    return random.choice(months)

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*5
    return prefix + "".join(random.choice(symbols) for i in range(random.randrange(maxlen)))


def random_phone(maxlen=10):
    return "".join(random.choice(string.digits) for i in range(random.randrange(5, maxlen)))


def random_email(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join(random.choice(symbols) for i in range(random.randrange(maxlen))) + "@mail.com"

testdata = [
    Contact(firstname="", lastname=""),
    Contact(firstname=random_string("fn_", 10), lastname=""),
    Contact(firstname="", lastname=random_string("ln_", 10))
] + [
    Contact(
        firstname=random_string("fn_", 10),
        lastname=random_string("ln_", 10),
        email=random_email("email_", 10)
    )
] + [
    Contact(
        firstname=random_string("fn_", 10),
        middlename=random_string("mn_", 10),
        lastname=random_string("ln_", 10),
        nickname=random_string("nick_", 10),
        company=random_string("comp_", 10),
        title=random_string("title_", 10),
        address=random_string("addr_", 20),
        home=random_phone(),
        mobile=random_phone(),
        work=random_phone(),
        fax=random_phone(),
        email=random_email("email_", 10),
        email2=random_email("email2_", 10),
        email3=random_email("email3_", 10),
        homepage=random_string("site_", 10),
        bday=random_day(),
        bmonth=random_month(),
        byear=random_year(),
        aday=random_day(),
        amonth=random_month(),
        ayear=random_year()
    )
    for i in range(n)
]


file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), f)


with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
