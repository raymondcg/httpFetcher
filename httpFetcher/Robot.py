from urllib.robotparser import RobotFileParser
from xmlrpc.client import DateTime


class Robot:
    """

    ...

    Attributes
    ----------
     __crawl_delay : int
     __base_robot_rules : BaseRobotRules
     __last_updated : DateTime
        When was this Robot.txt file last updated.
     __last_accessed : DateTime
        When was this Robot.txt file last accessed.

    Methods
    -------
    get(Uri)
        Gets the content from a given URI
    """

    # Instance variables
    __crawl_delay : int
    __base_robot_rules : RobotFileParser
    __last_updated : DateTime
    __last_accessed : DateTime

    def __init__(self,  crawl_delay, last_updated, last_accessed):
        self.__crawl_delay = crawl_delay
        self.__last_updated= last_updated
        self.__last_accessed = last_accessed

    @property
    def crawl_delay(self):
        return self.__crawl_delay

    @crawl_delay.setter
    def crawl_delay(self, value):
        print("Called")
        if value >= 0:
            self.__crawl_delay = value
        else:
            raise ValueError("crawl_delay can't be negative")

    @property
    def base_robot_rules(self):
        return self.__base_robot_rules

    @base_robot_rules.setter
    def base_robot_rules(self, value):
        print("Called")
        if value >= 0:
            self.__base_robot_rules = value
        else:
            raise ValueError("base_robot_rules can't be negative")

    @property
    def last_updated(self):
        return self.__last_updated

    @last_updated.setter
    def last_updated(self, value):
        print("Called")
        if value >= 0:
            self.__last_updated = value
        else:
            raise ValueError("last_updated can't be negative")

    @property
    def last_accessed(self):
        return self.__last_accessed

    @last_accessed.setter
    def last_accessed(self, value):
        print("Called")
        if value >= 0:
            self.__last_accessed = value
        else:
            raise ValueError("last_accessed can't be negative")
