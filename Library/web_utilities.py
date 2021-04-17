"""Module for click, send_keys and window handles"""


class CommonUtility:
    """for reusing mouse and keyboard actions"""
    @staticmethod
    def click_on(driver, element):
        """to click on the webpage"""
        loc_type, loc_value = element
        driver.find_element(loc_type, loc_value).click()

    @staticmethod
    def switch_2(driver):
        """to switch between the tabs"""
        handles = driver.window_handles
        driver.switch_to.window(handles[1])

    @staticmethod
    def send_to(driver, element, string):
        """to enter the value in the prompt"""
        loc_type, loc_value = element
        driver.find_element(loc_type, loc_value).send_keys(string)

    @staticmethod
    def close_the_tab(driver):
        """for closing the child browser"""
        driver.close()
