import re
from bs4 import BeautifulSoup

from locators.topic_locator import TopicPageLocator
from parsers.topic import TopicParser

class ShowPage:
    '''
    Takes the page and parses out the show elements
    '''
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def topics(self):
        locator = TopicPageLocator.TOPIC_LOCATOR
        show_list = self.soup.select(locator)
        # print(show_list)
        return [TopicParser(e) for e in show_list]
    


       
        
