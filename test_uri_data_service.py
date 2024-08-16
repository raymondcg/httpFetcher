import unittest
from httpFetcher.UriDataService import UriDataService
from unittest.mock import MagicMock

from httpFetcher.HttpFetcherInterface import HttpFetcherInterface
from httpFetcher.HttpRequest import HttpRequest


class TestUriDataService(unittest.TestCase):
    """ Class is used to test that the URI Data Service respects the robot.txt file.

    This class isn't intended to test the actual http fetcher logic, and as such will mock the http fetcher.

    """
    __uri_data_service : UriDataService

    def setUp(self):
        # Setup mock for httpFetcher, don't actually call http.
        # MockitoAnnotations.openMocks( this );
        # Setup uri_data_service to use in other tests in this file.
        self.__uri_data_service = UriDataService( False )

    def test_allowedMusicalTest(self) :
        # Arrange
        robot_url : str = "http://www.musi-cal.com/robots.txt"
        url_to_test : str = "http://www.musi-cal.com/"
        #robot : str = fileHelper.readFile( this.getClass().getResource( "/robots/musi-cal.txt" ).getFile() )
        #when( __uri_data_service.getSite( robot_url ) ).thenReturn( robot )
        #when( __uri_data_service.get( url_to_test ) ).thenReturn( "Winner" )

        # Act
        result : str = self.__uri_data_service.get( url_to_test )

        # Assert
        #verify( __uri_data_service, times( 2 ) ).get( anyString() )
        self.assertTrue( result == "Winner" )

    def test_notAllowedMusicalTest(self):
        # Arrange
        #String robotUrl = "http://www.musi-cal.com/robots.txt"
        #String urlToTest = "http://www.musi-cal.com/wp-admin/"
        #String robot = fileHelper.readFile( this.getClass().getResource( "/robots/musi-cal.txt" ).getFile() )
        #when( lookupDao.getSite( robotUrl ) ).thenReturn( robot )
        #when( lookupDao.getSite( urlToTest ) ).thenReturn( "" )

        # Act
        #String result = dataRetrievalService.getData( urlToTest )

        # Assert
        #verify( lookupDao, times( 1 ) ).getSite( anyString() )
        #self.assertTrue( result.equals( "" ) )
        pass # Just used to No-op the test, remove line when test is usable.

   # // No robots.txt means allowed.
    def test_noRobotsTxt(self) :
        # Arrange
        #String robotUrl = "http://www.musi-cal.com/robots.txt"
        #String urlToTest = "http://www.musi-cal.com/wp-admin/"
        #when( lookupDao.getSite( robotUrl ) ).thenThrow( new RuntimeException( "404" ) )
        #when( lookupDao.getSite( urlToTest ) ).thenReturn( "Winner" )

        # Act
        #String result = dataRetrievalService.getData( urlToTest )

        # Assert
        #verify( lookupDao, times( 2 ) ).getSite( anyString() )
        #self.assertTrue( result.equals( "Winner" ) )
        pass # Just used to No-op the test, remove line when test is usable.

    #// Temporarily Denied, too many redirects
    def test_endlessRedirectsRobotsTxt(self) :
        # Arrange
        #String robotUrl = "http://www.musi-cal.com/robots.txt"
        #String urlToTest = "http://www.musi-cal.com/wp-admin/"
        #when( lookupDao.getSite( robotUrl ) ).thenThrow( new RuntimeException( "301" ) )
        #when( lookupDao.getSite( urlToTest ) ).thenReturn( "Winner" )

        # Act
        #String result = dataRetrievalService.getData( urlToTest )

        # Assert
        #verify( lookupDao, times( 1 ) ).getSite( anyString() )
        #self.assertTrue( result.equals( "" ) )
        pass # Just used to No-op the test, remove line when test is usable.

    #// Temporarily Denied, not able to parse runtime exception
    def test_unparsableRobotsTxt(self) :
        # Arrange
        #String robotUrl = "http://www.musi-cal.com/robots.txt"
        #String urlToTest = "http://www.musi-cal.com/wp-admin/"
        #when( lookupDao.getSite( robotUrl ) ).thenThrow( new RuntimeException( "Gonna Fail" ) )
        #when( lookupDao.getSite( urlToTest ) ).thenReturn( "Winner" )

        # Act
        #String result = dataRetrievalService.getData( urlToTest )

        # Assert
        #verify( lookupDao, times( 1 ) ).getSite( anyString() )
        #self.assertTrue( result.equals( "" ) )
        pass # Just used to No-op the test, remove line when test is usable.

    def test_agentNotAllowed(self) :
        # Arrange
        #String robotUrl = "http://www.google.com/robots.txt"
        #String urlToTest = "http://www.google.com/search/"
        #String robot = fileHelper.readFile( this.getClass().getResource( "/robots/denyWebnerdbot.txt" ).getFile() )
        #when( lookupDao.getSite( robotUrl ) ).thenReturn( robot )
        #when( lookupDao.getSite( urlToTest ) ).thenReturn( "" )

        # Act
        #String result = dataRetrievalService.getData( urlToTest )

        # Assert
        #verify( lookupDao, times( 1 ) ).getSite( anyString() )
        #self.assertTrue( result.equals( "" ) )
        pass # Just used to No-op the test, remove line when test is usable.

    def test_agentAllowed(self) :
        # Arrange
        #String robotUrl = "http://www.google.com/robots.txt"
        #String urlToTest = "http://www.google.com/search/"
        #String robot = fileHelper.readFile( this.getClass().getResource( "/robots/allowWebnerdbot.txt" ).getFile() )
        #when( lookupDao.getSite( robotUrl ) ).thenReturn( robot )
        #when( lookupDao.getSite( urlToTest ) ).thenReturn( "winner" )

        # Act
        #String result = dataRetrievalService.getData( urlToTest )

        # Assert
        #verify( lookupDao, times( 2 ) ).getSite( anyString() )
        #self.assertTrue( result.equals( "winner" ) )
        pass # Just used to No-op the test, remove line when test is usable.

if __name__ == '__main__':
    unittest.main()
