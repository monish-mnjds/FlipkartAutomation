"""Module for test scripts of flipkart"""
from time import sleep
import pytest
from Pages.automate_flipkart import Flipkart
from Library.config import Config
from Library.base_fixtures import DriverInit
from Library.file_library import ReadJson

ReadTestData = ReadJson()
test_data = ReadTestData.read_test_data(Config.TEST_JSON)


# @pytest.mark.parametrize("series, game",
#                          [
#                              ("Playstation 5 Games", "selectSpiderMan")
#                          ]
#                          )
@pytest.mark.parametrize("series, game",
                         test_data
                         )
class TestFlipkart(DriverInit):
    """class has test_flipkart method for testing..."""
    def test_flipkart(self, series, game):
        """we are running all the tests from automate_flipkart"""
        flip = Flipkart(self.driver, series, game)  #pylint: disable=no-member
        flip.handle_popup()
        flip.search_item()
        flip.click_on_magnify()
        flip.click_on_fassured()
        flip.select_a_game()
        flip.switch_tab()
        flip.add_to_cart()
        flip.click_on_place_order()
        flip.close_current_tab()
