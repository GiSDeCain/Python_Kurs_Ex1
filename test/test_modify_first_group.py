from model.group import Group


def test_modify_group_name(app):
    app.group.modify_first_group(Group(name="New group111"))


def test_modify_group_header(app):
    app.group.modify_first_group(Group(header="New header111"))


__author__ = 'GiSDeCain'
