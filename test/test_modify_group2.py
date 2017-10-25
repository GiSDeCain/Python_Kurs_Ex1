from model.group import Group


def test_modify_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify(Group(name="SDFsdf1", header="DFsdfd1", footer="zdfgdfgzf1"))
    app.session.logout()


__author__ = 'GiSDeCain'
