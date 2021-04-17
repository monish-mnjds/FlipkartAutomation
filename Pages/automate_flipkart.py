"""Automation script for Flipkart"""
from Library.config import Config
from Library.web_utilities import CommonUtility
from Library.file_library import ReadJson

read_json = ReadJson()
com_util = CommonUtility()
element = read_json.read_locators(Config.OBJECT_JSON)


class Flipkart:
    """Flipkart class containing test cases to add a game to the cart and
    to place the order"""
    def __init__(self, driver, series, game):
        self.driver = driver
        self.series = series
        self.game = game

    def handle_popup(self):
        """to handle the popup which appears at the first place"""
        com_util.click_on(self.driver, element['clickOnPopup'])

    def search_item(self):
        """entering the desired text into the search box"""
        com_util.send_to(self.driver, element['clickOnSearch'], self.series)

    def click_on_magnify(self):
        """after entering the text, we need to click on magnify icon"""
        com_util.click_on(self.driver, element['clickOnMagnify'])

    def click_on_fassured(self):
        """only to purchase the product which is flipkart assured"""
        com_util.click_on(self.driver, element['clickOnfAssured'])

    def select_a_game(self):
        """selecting a fAssured game"""
        com_util.click_on(self.driver, element[self.game])

    def switch_tab(self):
        """to pass the control to the new tab"""
        com_util.switch_2(self.driver)

    def add_to_cart(self):
        """we are adding the game to our cart"""
        com_util.click_on(self.driver, element['clickOnAddToCart'])

    def close_current_tab(self):
        """we are closing the child tab"""
        com_util.close_the_tab(self.driver)

    def click_on_place_order(self):
        """clicking the place order icon"""
        com_util.click_on(self.driver, element['clickOnPlaceOrder'])
