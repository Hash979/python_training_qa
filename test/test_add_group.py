# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
    app.group.Create(Group(name="sss", header="sss", footer="sss"))

def test_add_empty_group(app):
    app.group.Create(Group(name="", header="", footer=""))





