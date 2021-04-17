"""Module for creating test data and we need to use it with parameterize marker"""
from pprint import pprint
import json
from Library.config import Config

data = {
       'TD1': {'Series': 'PlayStation 5 Games',
               'Game': 'selectSpiderMan'}
}

fileobj = open(Config.TEST_JSON, "w+")
json.dump(data, fileobj, indent=4)

fileobj = open(Config.TEST_JSON, "r")
info = json.load(fileobj)
pprint(info)

fileobj.close()
