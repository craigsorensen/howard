
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

    def __repr__(self):
        return f'<Show {self.date}, Topics: {self.topics}>'   

    @property
    def date(self):
        locator = ShowLocators.DATE_LOCATOR
        return (self.parent.select_one(locator).string).strip()

    @property
    def topics(self):
        locator = TopicPageLocator.TOPIC_LOCATOR
        topic_list = self.parent.select(locator)
        topics = []
        # topic HTML array (<A> tag)

        for t in topic_list:
            topics.append(TopicParser(str(t)))
            logging.debug(f'Topic: {t}')
        return topics
    
