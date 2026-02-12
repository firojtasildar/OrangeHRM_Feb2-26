from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




class  LoginPage:
    text_username_xpath="//input[@name='username']"
    text_password_xpath="//input[@name='password']"
    btn_login_xpath="//button[@type='submit']"
    btn_menu_xpath="//p[@class='oxd-userdropdown-name']"
    btn_logout_xpath="//a[text()='Logout']"

    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(self.driver,20)

    #enter username
    def enter_username(self,username):
        self.wait.until(EC.presence_of_element_located((By.XPATH,self.text_username_xpath))).send_keys(username)

    #enter password
    def enter_password(self,password):
        self.wait.until(EC.presence_of_element_located((By.XPATH,self.text_password_xpath))).send_keys(password)

    #click login button
    def click_login_button(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH,self.btn_login_xpath))).click()

    def click_menu_button(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH,self.btn_menu_xpath))).click()

    def verify_login_success(self):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH,self.btn_menu_xpath)))
            return "login_pass"
        except:
            return "login_fail"

    def click_logout_button(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH,self.btn_logout_xpath))).click()





