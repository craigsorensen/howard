from bs4 import BeautifulSoup

from locators.show_locators import ShowLocators

element = '''<div role="listitem" class="w-dyn-item">
               <div class="event-wrapper">
                 <div class="div-block-2">
                   <div class="event-date-wrapper">
                      <div class="event-month">Jul</div>
                      <div class="event-date">16</div>
                   </div>
                   <div class="event-body-wrapper">
                     <div class="event-prehead w-condition-invisible w-dyn-bind-empty"></div>
                   <div class="event-name">Pure Fun Comedy</div>
                   <div class="event-details">
                     <div class="event-day">Sat</div>
                     <div class="event-time">7:30 pm</div>
                    </div>
                  </div>
                </div>
                <div class="event-ctas">
                  <a href="#" class="button secondary w-condition-invisible w-button">RSVP</a>
                  <a href="https://www.blcomedy.com/events/pure-fun-comedy-2022-07-03233620246" class="button primary w-button">Get Tickets</a>
                </div>
              </div></div>'''

soup = BeautifulSoup(element, 'html.parser')

month_locator = ShowLocators.MONTH_LOCATOR
day_locator = ShowLocators.DAY_LOCATOR
date_locator = ShowLocators.DWEEK_LOCATOR
print(month_locator)
print(day_locator)
month = (soup.select_one(month_locator).string).strip()
date = (soup.select_one(date_locator).string).strip()
day = (soup.select_one(day_locator).string).strip()
print(f'{date} {month} {day}')