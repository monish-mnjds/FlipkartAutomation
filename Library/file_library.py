"""Module to drive data from json file"""
import json


class ReadJson:
    """class to read locators from json"""
    @staticmethod
    def read_locators(filelocation):
        """loading the data from json file"""
        with open(filelocation) as file:
            json_obj = json.load(file)
            dict_ = {}
            for key, value in json_obj.items():
                dict_[key] = (value['locatorType'], value['locatorValue'])
        return dict_

    @staticmethod
    def read_test_data(file):
        """loading the test data from test_data.json"""
        with open(file) as fileobj:
            j_obj = json.load(fileobj)
            list_ = [(value['Series'], value['Game']) for key, value in j_obj.items()]
        return list_
