from bs4 import BeautifulSoup

from locators.topic_locators import TopicPageLocator


# class TopicParser:
#     '''
#     Given one of the specific show div's, find the topics
#     '''

#     def __init__(self, parent):
#         self.parent = parent
#         print(parent.attrs)
        
#     def __repr__(self):
#         return f'<{self.topics}>'   

#     @property
#     def topics(self):

#         locator = TopicPageLocator.TOPIC_LOCATOR
#         #print((soup.select_one(locator).text).strip())

#         # print(topic_list)
#         # return topic_list
#         # return [(self.parent.select_one('a').string).strip() for e in topic_list]
    
def TopicParser(topic):
    
    soup = BeautifulSoup(topic, 'html.parser')

    locator = TopicPageLocator.TOPIC_LOCATOR2
    return (soup.select_one(locator).text).strip()
