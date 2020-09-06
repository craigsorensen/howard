import re
from bs4 import BeautifulSoup

from locators.show_page_locator import ShowPageLocator
from parsers.show import ShowParser

class ShowPage:
    '''
    Takes the page and parses out the show elements
    '''
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def shows(self):
        locator = ShowPageLocator.SHOW_LOCATOR
        show_list = self.soup.select(locator)

        #print(show_list)
        return [ShowParser(e) for e in show_list]
    


       
        
