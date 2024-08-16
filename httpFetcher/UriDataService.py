import threading
import time
import urllib.robotparser

from urllib.parse import urlparse
from random import randint

from httpFetcher.HttpFetcherInterface import HttpFetcherInterface
from httpFetcher.HttpRequest import HttpRequest
from httpFetcher.Robot import Robot


class UriDataService:
    """ A URI Data service that will fetch the content from a given URI while respecting the robots.txt file

    # TODO Set the user agent dynamically.
    # TODO Try with resources.
    # TODO Add in error handling logic
    # TODO raise an error / Exception in some cases.
    # TODO manage redirects, if the host is redirected, pass that info up and don't call that redirected host again.
    # TODO change to a logger of some sort.

    ...

    Attributes
    ----------
     __httpFetcherInterface : HttpFetcherInterface
        A mechanism to get a response from a URI.
     __robot_dict : {} # Map<String, Robot>
     __locks : {} # Map<String, ReentrantReadWriteLock>
     __min_crawl_delay : int
        The minimum amount of time to wait between requests to a given host. The hosts Robot.txt can extend this time.
     __useragent : str

    Methods
    -------
    get(Uri)
        Gets the content from a given URI, assuming that the root level robot.txt file allows this to occur.
    """

    # Instance variables
    __httpFetcherInterface : HttpFetcherInterface
    __robot_dict : {} # Map<String, Robot>
    __locks : {} # Map<String, ReentrantReadWriteLock>
    __min_crawl_delay : int
    __useragent : str

    def __init__(self, http_enabled : bool):
        """ Basic constructor
        TODO put in a mechanism to have multiple options as to how to get uri content. Example Zenrows or ScrubberWeb.
        TODO set reasonable defaults for User Agent and min crawl delay. As well as allow consumers to override those values.

        :param http_enabled: Enable live calls to the internet.
        """
        self.httpFetcherInterface  = HttpRequest(True)

    def get( self, uri: str ) :
        # Clean up URI to have the right number of slashes.
        cleaned_up_uri = uri.replace("//","/").replace(":/","://",1)
        if self.__can_access( cleaned_up_uri ):
            return self.httpFetcherInterface.get( cleaned_up_uri )
        else :
            print( "Not allowed to get data from URL: {}", cleaned_up_uri )
            return ""

    def __can_access(self,uri : str) -> bool :
        """ Private method to determine if the established user agent is allowed access the given uri.

        :param uri: uri is the full uri to validate.
        :rtype bool Return value is if the user agent is allowed to get the uri or not.

        """

        url_object = urlparse(uri) #"scheme://netloc/path;parameters?query#fragment"

        host_id : str = url_object.scheme + "://" + url_object.netloc

        robot : Robot = self.__get_robot( host_id )
        results : bool = robot.base_robot_rules().can_fetch( self.__useragent, uri )
        print( "Allowed: {}, to URL: {}, for Host: {}", results, uri, host_id ) #debug

        now = time.time()
        time_since_last_update : int  = ( now - robot.last_accessed().getTime() )
        if results & time_since_last_update < robot.crawl_delay() :
            # waits time between requests seconds before performing the fetch
            random_time : int = randint(1,  1 + 2 * robot.crawl_delay() )
            time_to_wait : int = ( robot.crawl_delay() + random_time ) - time_since_last_update
            print( "{} s since last call, {} s until next call to host {}", time_since_last_update, time_to_wait, host_id ) #debug

            if  time_to_wait > 0  :
                time.sleep( time_to_wait )

        else :
            # No wait required, carry on.
            print( "{} s since last call, crawl delay {}, call host {}", time_since_last_update, robot.crawl_delay(), host_id ) #debug

        robot.last_accessed( time.time() )
        return results

    def __get_robot(self, host_id: str):
        """Private method to get the Robot.txt file for the given host.

        This method will retrieve the robot.txt file for the given host, parse it into the Robot object and
        store it in the robot dictionary for future utilization.

        :param host_id: host_id is the host portion of the given URI example: https://www.google.com/

        """
        robot : Robot

        try :
            # Gets write lock, since only a single call to a host is allowed within a large time window, locking isn't
            # dreadful. Additionally, this ensures that no race conditions occur.
            self.__get_lock( host_id ).acquire()
            print( "Got write lock for: {}", host_id ) #Debug

            robot = self.__robot_dict.get( host_id )

            now = time.time()
            if robot is None :
                robot = Robot(self.__min_crawl_delay, now, now)

            time_since_last_updated_seconds : int =  now - robot.last_updated().getTime()
            time_since_last_update_min : int = round( time_since_last_updated_seconds / 60 )
            if time_since_last_update_min > 30 :
                print( "Updating Robot rules due to age. Last updated {} minutes ago", time_since_last_update_min ) #info
                robot.last_updated( now )
                robot.base_robot_rules( None ) # Clears out any saved rules, to force the next step to get the rules again.

            if robot.base_robot_rules() is None :
                robot_parser = urllib.robotparser.RobotFileParser()

                try :
                    robot_uri = (host_id + "/robots.txt" ).replace("//", "/").replace(":/", "://", 1)
                    robot_parser.set_url( robot_uri )
                    robot_parser.read() # Ideally this would leverage the http fetcher interface for consistency of access to host.
                    print( "Host: {}, Agent: {}", host_id, self.__useragent ) # debug

                except  RuntimeError as e  :
                    print( "RuntimeError for Host {}", host_id, e ) # Trace
                    response_code : int
                    try :
                        response_code = int( repr(e) )
                        print("response_code is: {}", response_code )
                    except  ValueError as ex  :
                        print( "Couldn't process runtime exception message. Treating as temporarily denied.", ex ) #Error
                        response_code = 300
                    # TODO if it fails to get a robot.txt file then what? How will future can access work.

                self.__robot_dict.put( host_id, robot )

        finally :
            print( "Write lock released: {}", host_id ) #Debug
            self.__get_lock( host_id ).release()

        robot_delay : int = int(robot.base_robot_rules().getCrawlDelay() * 1000)
        if  robot_delay > self.__min_crawl_delay  :
            robot.crawl_delay( robot_delay )
        else :
            robot.crawl_delay( self.__min_crawl_delay )

        return robot

    def __get_lock(self, lock_id : str) -> threading.RLock:
        """Private method to control access to the robot dictionary to ensure that multiple threads do not attempt to
        modify the dictionary value at the same time for a given key.

        :param lock_id: lock_id is the host id that is being modified.

        """
        if not self.__locks.has_key( lock_id ) :
            self.__locks.put( lock_id, threading.RLock() )
        return self.__locks.get( lock_id )
        pass