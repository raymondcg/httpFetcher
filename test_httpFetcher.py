import unittest

from httpFetcher.HttpFetcherInterface import HttpFetcherInterface
from httpFetcher.HttpRequest import HttpRequest


class TestHttpFetcherMethods(unittest.TestCase):
    def setUp(self):
        pass

    def test_base_case_http_request(self):
        request : HttpFetcherInterface
        request = HttpRequest(True)
        result = request.get('http://www.google.com/search?q=mkyong')
        self.assertTrue( len(result) >0 )

    if __name__ == '__main__':
        unittest.main()


