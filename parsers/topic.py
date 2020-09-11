import logging
from bs4 import BeautifulSoup

from locators.topic_locators import TopicPageLocator

    
def TopicParser(topic):
    
    soup = BeautifulSoup(topic, 'html.parser')

    locator = TopicPageLocator.TOPIC_LOCATOR2
    logging.debug(f"Topics: {(soup.select_one(locator).text).strip()}")
    return (soup.select_one(locator).text).strip()
