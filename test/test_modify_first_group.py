from model.group import Group


def test_modify_group_name(app):
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(name="New group111"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)


def test_modify_group_header(app):
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(header="New header111"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)


__author__ = 'GiSDeCain'
