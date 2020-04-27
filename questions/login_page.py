
from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
import logging
import utilities.custom_logger as cl


class LoginPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _login_link = "Login"
    _email_field = "user_email"
    _password_field = "user_password"
    _login_button = "commit"
    _verify_icon = "user_icon"


    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="link")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="name")

    def login(self, email="", password=""): # email and password are optional args
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        loginResult = self.isElementPresent("//*[@id='navbar']//span[@class='navbar-current-user']", locatorType="xpath")
        return loginResult

    def verifyLoginFailure(self):
        loginResult = self.isElementPresent("//div[contains(text(), 'Invalid email or password.')]", locatorType="xpath")
        return loginResult

    def clearTextField(self):
        self.clearField(self._email_field)
