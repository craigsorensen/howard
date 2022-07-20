
import logging

from parsers.topic import TopicParser
from locators.show_locators import ShowLocators
from locators.topic_locators import TopicPageLocator



class ShowParser:
    '''
    Given one of the specific show div's, find out the data about the show
    '''

    def __init__(self, parent):
        self.parent = parent
        #print each show
        #print(self.parent)

    def __repr__(self):
        return f'<Show {self.date}, Topic: {self.topic}>'   

    @property
    def date(self):
        month_locator = ShowLocators.MONTH_LOCATOR
        day_locator = ShowLocators.DAY_LOCATOR
        dweek_locator = ShowLocators.DWEEK_LOCATOR
        month = (self.parent.select_one(month_locator).string).strip()
        dweek = (self.parent.select_one(dweek_locator).string).strip()
        day = (self.parent.select_one(day_locator).string).strip()
        #print(f'{dweek} {month} {day}')
        return [dweek, month, day]

    @property
    def topic(self):
        locator = TopicPageLocator.TOPIC_LOCATOR
        return (self.parent.select_one(locator).string).strip()
    
