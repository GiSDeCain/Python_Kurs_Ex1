from model.contact import Contact

def test_modify_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstName="gfhfghh2", middleName="xgnhghhc2", lastName="xgnhcgh2", nickName="cxgbncgb2",
                                             title="xgbxgb2", company="xgnxcfgnn2", address="cghnhmnmvghn2",
                                             homeNumber="465567546", mobileNumber="64745467", workNumber="64745746", faxNumber="467467456",
                                             email="fgvbxfgb@dfgdf.po", byear="1999",
                                             address2="xgfbfcgbh", phoneNumber2="45765677", notes="dghdfghdfgh"))
    app.session.logout()


__author__ = 'GiSDeCain'
