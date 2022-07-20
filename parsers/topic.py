import logging
from bs4 import BeautifulSoup

from locators.topic_locators import TopicPageLocator

    
def TopicParser(topic):
    
    soup = BeautifulSoup(topic, 'html.parser')

    locator = TopicPageLocator.TOPIC_LOCATOR
    logging.debug(f"Topics html: {(soup.select(locator)).string.strip()}")
    return (soup.select(locator)).string.strip()
