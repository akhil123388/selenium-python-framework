
from selenium import webdriver
from page.home.login_page import LoginPage
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):
    # baseURL = "https://letskodeit.teachable.com/"
    # driver = webdriver.Chrome()
    # driver.maximize_window()
    # driver.implicitly_wait(3)
    # driver.get(baseURL)

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.clearTextField()
        self.lp.login("test@email.com", "abcabc")
        loginResult = self.lp.verifyLoginSuccessful()
        assert loginResult == True

    @pytest.mark.run(order=1)
    def test_InvalidLogin(self):
        self.lp.login("test@email.com", "abcabcabc")
        loginResult = self.lp.verifyLoginFailure()
        assert loginResult == True