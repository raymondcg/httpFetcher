import requests
from bs4 import BeautifulSoup
import csv

from requests import Response

from httpFetcher.HttpFetcherInterface import HttpFetcherInterface

class HttpRequest(HttpFetcherInterface):
    """ A simplistic implementation of HttpFetcherInterface that leverages the Python Request module.

    ...

    Attributes
    ----------
     httpEnabled : Boolean
        A flag to enable real HTTP calls.

    Methods
    -------
    says(sound=None)
        Prints the animals name and what sound it makes
    """

    # Class variables
    httpEnabled : bool = False
    # LOGGER

    def __init__(self, http_enabled : bool):
        self.httpEnabled = http_enabled

    def get( self, url: str ):
        r"""Sends a GET request.

        :param url: URL for the new :class:`Request` object.
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        """

        # Make sure all the forward slashes are correct.
        if self.httpEnabled:
            print( "******** Real Call to the internet ********" ) # Debug
            response : Response
            try  :
                #getRequest.addHeader( "User-Agent", env.getProperty( "useragent" ) )
                # Add header with associated user agent details.
                response = requests.get(url)

                if response.status_code > 299:
                    print( "URL: {}\nResponse\n{}", url, response ) # info
                    #throw new RuntimeException( String.format( "%s", response.getStatusLine().getStatusCode() ) )

            except requests.exceptions.Timeout as e:
                # Maybe set up for a retry, or continue in a retry loop
                print(e)
            except requests.exceptions.TooManyRedirects as e:
                # Tell the user their URL was bad and try a different one
                print(e)
            except requests.exceptions.RequestException as e:
                # catastrophic error. bail.
                print(e)
                raise SystemExit(e)

            print (response) # Trace
            return response
        else:
            print("******** HTTP calls are disabled in the application.yml. ********") # WARN
            return ""
