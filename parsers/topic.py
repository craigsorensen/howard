import logging
from bs4 import BeautifulSoup

from locators.topic_locators import TopicPageLocator

    
def TopicParser(topic):
    
    soup = BeautifulSoup(topic, 'html.parser')

    locator = TopicPageLocator.TOPIC_LOCATOR2
    logging.debug(f"Topics html: {(soup.select_one(locator).attrs['alt'])}")
    return (soup.select_one(locator).attrs['alt'])
