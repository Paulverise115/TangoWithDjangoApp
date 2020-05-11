import unittest

from abc import ABC, abstractmethod
from unittest.mock import MagicMock


class ConfigureCategories(ABC):
    @abstractmethod
    def getConfig(self):
        pass


class ConfigFromStub(ConfigureCategories):

    def getConfig():
        return {'title': 'Official Python Tutorial',
                'url': 'http://docs.python.org/3/tutorial/',
                'views': '10'}


class indexTest(unittest.TestCase):
    database = ConfigFromStub.getConfig()


    def test_DatabaseFromStub(self):
        result = self.database
        self.assertEqual({'title': 'Official Python Tutorial',
                          'url': 'http://docs.python.org/3/tutorial/',
                          'views': '10'}, result)


    def test_DatabaseFromMock(self):
        propertyData = {'title': 'Official Python Tutorial',
                'url': 'http://docs.python.org/3/tutorial/',
                'views': '10'}

        ConfigFromStub.getConfig = MagicMock(return_value=propertyData)
        result = self.database
        print(result)
        self.assertEqual({'title': 'Official Python Tutorial',
                'url': 'http://docs.python.org/3/tutorial/',
                'views': '10'}, result)

    def test_databaseFromFake(self):
        localCopyPropertyData = {'title': 'Official Python Tutorial',
                'url': 'http://docs.python.org/3/tutorial/',
                'views': '10'}

        configFromFake = localCopyPropertyData

        self.assertEqual(configFromFake['title'], 'Official Python Tutorial')


