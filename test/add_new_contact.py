# -*- coding: utf-8 -*-
from model.contact import Contact


def add_new_contact(app):
    app.session.login()
    app.contact.add_new_contact(Contact(firstName="gfhfghh", middleName="xgnhghhc", lastName="xgnhcgh", nickName="cxgbncgb",
                                        title="xgbxgb", company="xgnxcfgnn", address="cghnhmnmvghn",
                                        homeNumber="465567546", mobileNumber="64745467", workNumber="64745746", faxNumber="467467456",
                                        email="fgvbxfgb@dfgdf.po", byear="1999",
                                        address2="xgfbfcgbh", phoneNumber2="45765677", notes="dghdfghdfgh"))
    app.session.logout()


__author__ = 'GiSDeCain'
