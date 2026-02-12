import allure
import pytest

from Utilities.logger import Logger_class
from Utilities.readConfig import ReadConfig
from pageObjects.Login_Page import LoginPage


@pytest.mark.usefixtures("driver_setup")
class Test_OrangeHRM_Login_001:
    driver=None
    username= ReadConfig.get_username()
    password= ReadConfig.get_password()
    login_url=ReadConfig.get_login_url()

    log=Logger_class.get_logger()


    @allure.title("Verify OrangeHRM Login Page URL")
    @allure.description("This test verifies the URL of the OrangeHRM login page")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.step("Navigate to OrangeHRM Login Page")
    @allure.link("https://opensource-demo.orangehrmlive.com/")
    @allure.issue("https://github.com/allure-framework/allure-python/issues/123")
    @allure.testcase("https://github.com/allure-framework/allure-python/issues/123")
    @allure.feature("OrangeHRM Login")
    @allure.story("Verify Login Page URL")
    #@allure.testcase("Verify OrangeHRM Login Page URL")
    @allure.tag("Regression")
    @allure.label("Priority", "High")
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.flaky(reruns=1,reruns_delay=1)
    def test_verify_url(self):
        self.log.info("Starting test_verify_url")
        self.log.info("Verify OrangeHRM Login Page URL")
        self.driver.get(self.login_url)
        self.log.info("Login Page URL: "+self.driver.current_url)
        self.log.info("Login Page Title: "+self.driver.title)
        self.log.info("OrangeHRM page loaded successfully")
        #assert driver.current_url=="https://opensource-demo.orangehrmlive.com/"
        if self.driver.title=="OrangeHRM":
            self.log.info("OrangeHRM Login Page url verified")
            self.driver.save_screenshot("screenshots\\test_verify_url_pass.png")
            self.log.info("Screenshot saved for passed test cases")
            allure.attach.file("screenshots\\test_verify_url_pass.png",name="test_verify_url_pass",attachment_type=allure.attachment_type.PNG)
            assert True
        else:
            self.driver.save_screenshot("screenshots\\test_verify_url_fail.png")
            allure.attach.file("screenshots\\test_verify_url_fail.png",name="test_verify_url_fail",attachment_type=allure.attachment_type.PNG)
            assert False
        self.log.info("Test case completed")
        self.log.info("======================================================")
#pytest -v -s --browser=chrome --html=HTML_Reports\OrangeHRM_Login_001.html --alluredir=Allure_Reports

    @allure.title("Verify OrangeHRM Login")
    @allure.description("This test verifies the login functionality of the OrangeHRM application")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.step("Enter Username and Password and Click Login Button")
    @allure.link("https://opensource-demo.orangehrmlive.com/")
    @allure.issue("https://github.com/allure-framework/allure-python/issues/123")
    @allure.testcase("https://github.com/allure-framework/allure-python/issues/123")
    @allure.feature("OrangeHRM Login")
    @allure.story("Verify Login Functionality")
    #@allure.tag("Regression")
    @allure.label("Priority", "High")
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.flaky(reruns=1,reruns_delay=1)
    def test_verify_orangehrm_login_002(self):
        self.log.info("Starting test_verify_orangehrm_login_002")
        self.log.info("Verify OrangeHRM Login Functionality")
        self.driver.get(self.login_url)
        login_page=LoginPage(self.driver) #Object created
        login_page.enter_username(self.username)
        login_page.enter_password(self.password)
        login_page.click_login_button()
        result=login_page.verify_login_success()
        if result=="Login Successful":
            self.log.info("OrangeHRM Login Successful")
            self.driver.save_screenshot("screenshots\\test_verify_orangehrm_login_002_pass.png")
            self.log.info("Screenshot saved for passed test cases")
            allure.attach.file("screenshots\\test_verify_orangehrm_login_002_pass.png",name="test_verify_orangehrm_login_002_pass",attachment_type=allure.attachment_type.PNG)
            login_page.click_menu_button()
            login_page.click_logout_button()
            assert True
        else:
            self.log.info("OrangeHRM Login Failed")
            self.driver.save_screenshot("screenshots\\test_verify_orangehrm_login_002_fail.png")
            self.log.info("Screenshot saved for failed test cases")
            allure.attach.file("screenshots\\test_verify_orangehrm_login_002_fail.png",name="test_verify_orangehrm_login_002_fail",attachment_type=allure.attachment_type.PNG)
            assert False
        self.log.info("Test case completed")
        self.log.info("======================================================")