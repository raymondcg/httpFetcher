import unittest


class TestUriDataServiceInt(unittest.TestCase):
    """Class is used to test that the Uri Data Service respects robot.txt files from Google.

    """

    def test_allowedTest(self):
        # Arrange
        url_to_test : str = "http://google.com/search/about"

        # Act
        result = dataRetrievalService.getData( urlToTest )

        # Assert, if allowed then will return a nonempty string.
        self.assertTrue(len(result.text) > 0)


    def test_notAllowedTest(self):
        # Arrange
        url_to_test : str = "http://google.com/search"

        # Act
        result = dataRetrievalService.getData( urlToTest )

        # Assert, if not allowed then will return an empty string.
        self.assertTrue(len(result.text) == 0)

if __name__ == '__main__':
    unittest.main()
