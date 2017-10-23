# -*- coding: utf-8 -*-
from selenium.webdriver.chrome.webdriver import WebDriver


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
    wd.find_element_by_name("user").click()
    wd.find_element_by_name("user").clear()
    wd.find_element_by_name("user").send_keys("admin")
    wd.find_element_by_id("LoginForm").click()
    wd.find_element_by_name("pass").click()
    wd.find_element_by_name("pass").clear()
    wd.find_element_by_name("pass").send_keys("secret")
    wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()


def add_name():
    # name section
    wd.find_element_by_name("firstname").click()
    wd.find_element_by_name("firstname").clear()
    wd.find_element_by_name("firstname").send_keys("gfhfghh")
    wd.find_element_by_name("middlename").click()
    wd.find_element_by_name("middlename").clear()
    wd.find_element_by_name("middlename").send_keys("xgnhghhc")
    wd.find_element_by_name("lastname").click()
    wd.find_element_by_name("lastname").clear()
    wd.find_element_by_name("lastname").send_keys("xgnhcgh")
    wd.find_element_by_name("nickname").click()
    wd.find_element_by_name("nickname").clear()
    wd.find_element_by_name("nickname").send_keys("cxgbncgb")


def add_address():
    # address section
    wd.find_element_by_name("title").click()
    wd.find_element_by_name("title").clear()
    wd.find_element_by_name("title").send_keys("xgbxgb")
    wd.find_element_by_name("company").click()
    wd.find_element_by_name("company").clear()
    wd.find_element_by_name("company").send_keys("xgnxcfgnn")
    wd.find_element_by_name("address").click()
    wd.find_element_by_name("address").clear()
    wd.find_element_by_name("address").send_keys("cghnhmnmvghn")


def add_numbers():
    # home phone
    wd.find_element_by_name("home").click()
    wd.find_element_by_name("home").clear()
    wd.find_element_by_name("home").send_keys("465567546")
    # mobile phone
    wd.find_element_by_name("mobile").click()
    wd.find_element_by_name("mobile").clear()
    wd.find_element_by_name("mobile").send_keys("64745467")
    # work phone
    wd.find_element_by_name("work").click()
    wd.find_element_by_name("work").clear()
    wd.find_element_by_name("work").send_keys("64745746")
    # fax
    wd.find_element_by_name("fax").click()
    wd.find_element_by_name("fax").clear()
    wd.find_element_by_name("fax").send_keys("467467456")
    # email
    wd.find_element_by_name("email").click()
    wd.find_element_by_name("email").clear()
    wd.find_element_by_name("email").send_keys("fgvbxfgb@dfgdf.po")


def add_birthday():
    # day from dropdown list (1-31)
    if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[3]").is_selected():
        wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[3]").click()
    # month from drop down list (1-12)
    if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[2]").is_selected():
        wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[2]").click()
    # year
    wd.find_element_by_name("byear").click()
    wd.find_element_by_name("byear").clear()
    wd.find_element_by_name("byear").send_keys("1999")


def add_second_address():
    # add second address
    wd.find_element_by_name("address2").click()
    wd.find_element_by_name("address2").clear()
    wd.find_element_by_name("address2").send_keys("xgfbfcgbh")
    # add second phone
    wd.find_element_by_name("phone2").click()
    wd.find_element_by_name("phone2").clear()
    wd.find_element_by_name("phone2").send_keys("45765677")
    # add some notes
    wd.find_element_by_name("notes").click()
    wd.find_element_by_name("notes").clear()
    wd.find_element_by_name("notes").send_keys("dghdfghdfgh")


def add_new_contact_page():
    # go to add new contact page
    wd.find_element_by_link_text("add new").click()


def submit_new_contact():
    wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()


def back_home_page():
    wd.find_element_by_link_text("home page").click()


def logout():
    wd.find_element_by_link_text("Logout").click()


try:
    login()
    add_new_contact_page()
    add_name()
    add_address()
    add_numbers()
    add_birthday()
    add_second_address()
    submit_new_contact()
    back_home_page()
    logout()
finally:
    wd.quit()
    if not success:
        raise Exception("Test failed.")


__author__ = 'GiSDeCain'
