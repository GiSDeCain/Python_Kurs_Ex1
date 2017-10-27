

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def add_new_contact(self, contact):
        self.open_add_contact_page()
        self.fill_new_contact_form(contact)
        self.submit_new_contact()

    def modify_first_contact(self, contact):
        wd = self.app.wd
        # start modify contact
        wd.find_element_by_xpath("//*[@title='Edit'][1]").click()
        self.fill_new_contact_form(contact)
        bug_element = wd.find_element_by_name('update')
        wd.execute_script("arguments[0].click();", bug_element)

    def del_first_contact(self):
        # delete first contact from list
        wd = self.app.wd
        # select first element from list
        wd.find_element_by_xpath("//table[@id='maintable']//input[@type='checkbox']").click()
        # scroll down page
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # submit deletion
        wd.find_element_by_xpath("//div[@class='left']/*[@value='Delete']").click()
        # confirm alert
        wd.switch_to_alert().accept()

    def open_add_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def fill_new_contact_form(self, contact):
        wd = self.app.wd
        # name section
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstName)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middleName)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastName)
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickName)
        # address section
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        # home phone
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.homeNumber)
        # mobile phone
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobileNumber)
        # work phone
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.workNumber)
        # fax
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.faxNumber)
        # email
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        # day from dropdown list (1-31)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[3]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[3]").click()
        # month from drop down list (1-12)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[2]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[2]").click()
        # year
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.byear)
        # add second address
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.address2)
        # add second phone
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.phoneNumber2)
        # add some notes
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.notes)

    def submit_new_contact(self):
        wd = self.app.wd
        bug_element = wd.find_element_by_name('submit')
        wd.execute_script("arguments[0].click();", bug_element)


__author__ = 'GiSDeCain'
