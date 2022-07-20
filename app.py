import requests
import os
import logging
import json

from datetime import datetime
from pages.show_pages import ShowPage
from send_push import push

SHOW_URL = "https://www.vulcanatx.com/"
CRED_DIR = os.path.expanduser("~")
api_cred_file = "{0}/.killtony_push_api.txt".format(CRED_DIR)
SCRIPT_EXC_DIR = os.path.dirname(os.path.realpath(__file__))
database = "{0}/database.json".format(SCRIPT_EXC_DIR)
log_dir = f'{SCRIPT_EXC_DIR}/app.log'

logging.basicConfig(filename=log_dir, format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s', level=logging.DEBUG)

# Get page content
page_content = requests.get(SHOW_URL).content
#fakepage = "{0}\\fakepage\\fakepage.html".format(SCRIPT_EXC_DIR)
#with open(fakepage, 'r') as f:
#    print("reading fakepage from disk")
#    page_content = f.read()


# Get the show elements from the page
page = ShowPage(page_content)

shows = page.shows

# open show db file
with open(database, 'r') as f:
    print("reading show database from disk")
    db = f.read()

show_db = json.loads(db)

# Get push API credentials from disk
if os.path.isfile(api_cred_file):
    with open(api_cred_file, 'r') as f:
        creds = f.readlines()
    TOKEN = creds[0].strip().split(':')[1]
    USER = creds[1].strip().split(':')[1]
else:
    print(f"No API Credentials found in: {api_cred_file} - Check README file for setup instuctions")
    logging.info(f"No API Credentials found in: {api_cred_file} - Check README file for setup instuctions")


show_list = []
new_show = False
# Add filtered shows listed on webpage to list
for show in shows:
    if (show.date[1].lower()) == 'oct' and (show.topic).lower() == 'kill tony':
        print(f'{show.date} - {show.topic}')
        show_list.append(show.date)

for show in show_list:
    if show not in show_db['shows']:
        show_db['shows'].append(show)
        new_show = True

if new_show:
    print('sending notification')
    push.send(TOKEN, USER, f"New KILL TONY show added. DATE: {show_db['shows'][-1]}")
    with open(database, 'w+') as f:
        print("Writing DB")
        f.write(json.dumps(show_db))

if not new_show:
    print("No new show found")
    logging.info("No new show found}")





