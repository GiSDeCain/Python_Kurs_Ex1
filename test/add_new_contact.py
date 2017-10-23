# -*- coding: utf-8 -*-
from selenium.webdriver.chrome.webdriver import WebDriver
from model.contact import Contact


success = True
wd = WebDriver()
wd.implicitly_wait(60)


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


def login():
    wd.get("http://localhost/addressbook/index.php")
    wd.find_element_by_name("user").clear()
    wd.find_element_by_name("user").send_keys("admin")
    wd.find_element_by_id("LoginForm").click()
    wd.find_element_by_name("pass").clear()
    wd.find_element_by_name("pass").send_keys("secret")
    wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()


def add_new_contact(Contact(firstName="gfhfghh", middleName="xgnhghhc", lastName="xgnhcgh", nickName="cxgbncgb",
                    title="xgbxgb", company="xgnxcfgnn", address="cghnhmnmvghn", homeNumber="465567546", mobileNumber="64745467",
                    workNumber="64745746", faxNumber="467467456", email="fgvbxfgb@dfgdf.po", byear="1999",
                    address2="xgfbfcgbh", phoneNumber2="45765677", notes="dghdfghdfgh")):
    # go to add new contact page
    wd.find_element_by_link_text("add new").click()
    # name section
    wd.find_element_by_name("firstname").clear()
    wd.find_element_by_name("firstname").send_keys(firstName)
    wd.find_element_by_name("middlename").clear()
    wd.find_element_by_name("middlename").send_keys(middleName)
    wd.find_element_by_name("lastname").clear()
    wd.find_element_by_name("lastname").send_keys(lastName)
    wd.find_element_by_name("nickname").clear()
    wd.find_element_by_name("nickname").send_keys(nickName)
    # address section
    wd.find_element_by_name("title").clear()
    wd.find_element_by_name("title").send_keys(title)
    wd.find_element_by_name("company").clear()
    wd.find_element_by_name("company").send_keys(company)
    wd.find_element_by_name("address").clear()
    wd.find_element_by_name("address").send_keys(address)
    # home phone
    wd.find_element_by_name("home").clear()
    wd.find_element_by_name("home").send_keys(homeNumber)
    # mobile phone
    wd.find_element_by_name("mobile").clear()
    wd.find_element_by_name("mobile").send_keys(mobileNumber)
    # work phone
    wd.find_element_by_name("work").clear()
    wd.find_element_by_name("work").send_keys(workNumber)
    # fax
    wd.find_element_by_name("fax").clear()
    wd.find_element_by_name("fax").send_keys(faxNumber)
    # email
    wd.find_element_by_name("email").clear()
    wd.find_element_by_name("email").send_keys(email)
    # day from dropdown list (1-31)
    if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[3]").is_selected():
        wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[3]").click()
    # month from drop down list (1-12)
    if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[2]").is_selected():
        wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[2]").click()
    # year
    wd.find_element_by_name("byear").clear()
    wd.find_element_by_name("byear").send_keys(byear)
    # add second address
    wd.find_element_by_name("address2").clear()
    wd.find_element_by_name("address2").send_keys(address2)
    # add second phone
    wd.find_element_by_name("phone2").clear()
    wd.find_element_by_name("phone2").send_keys(phoneNumber2)
    # add some notes
    wd.find_element_by_name("notes").clear()
    wd.find_element_by_name("notes").send_keys(notes)
    # submit new contact
    bug_element = wd.find_element_by_name('submit')
    wd.execute_script("arguments[0].click();", bug_element)
    # back to home page


def logout():
    wd.find_element_by_link_text("Logout").click()


try:
    login()
    add_new_contact()
    logout()
finally:
    wd.quit()
    if not success:
        raise Exception("Test failed.")


__author__ = 'GiSDeCain'
