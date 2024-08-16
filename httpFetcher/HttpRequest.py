import requests
from bs4 import BeautifulSoup
import csv

from requests import Response

from httpFetcher.HttpFetcherInterface import HttpFetcherInterface

class HttpRequest(HttpFetcherInterface):
    """ A simplistic implementation of HttpFetcherInterface that leverages the Python Request module.

    # TODO Set the user agent dynamically.
    # TODO Try with resources.
    # TODO Add in error handling logic
    # TODO raise an error / Exception in some cases.
    # TODO manage redirects, if the host is redirected, pass that info up and don't call that redirected host again.
    # TODO change to a logger of some sort.

    ...

    Attributes
    ----------
     httpEnabled : Boolean
        A flag to enable real HTTP calls.

    Methods
    -------
    get(Uri)
        Gets the content from a given URI
    """

    # Class variables
    httpEnabled : bool = False

    def __init__(self, http_enabled : bool):
        self.httpEnabled = http_enabled

    def get(self, uri: str) -> str :
        r"""Sends a GET request.

        :param uri: URI for the new :class:`Request` object.
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
                response = requests.get(uri)

                if response.status_code > 299:
                    print( "URL: {}\nResponse\n{}", uri, response) # info
                    raise RuntimeError( response.status_code )

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

            print (response.text) # Trace
            return response.text
        else:
            print("******** HTTP calls are disabled in the application.yml. ********") # WARN
            return ""
