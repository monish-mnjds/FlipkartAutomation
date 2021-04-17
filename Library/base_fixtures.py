"""File for using fixture in POM approach"""
import pytest
from selenium import webdriver
from Library.config import Config


class DriverInit:  #pylint: disable=too-few-public-methods
    """fixture used for providing a fixed base line"""

    @classmethod
    @pytest.fixture(autouse=True, scope='class')
    def driver_init(cls, request):
        """Browser Options"""
        if Config.BROWSER.upper() == 'CHROME':
            driver = webdriver.Chrome(Config.EXECUTABLE_PATH)
        elif Config.BROWSER.upper() == 'FIREFOX':
            driver = webdriver.Firefox()

        request.cls.driver = driver
        driver.get(Config.URL)
        driver.implicitly_wait(30)
        driver.maximize_window()
        yield
        driver.quit()
