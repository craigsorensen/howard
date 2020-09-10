import requests
import os
import logging

from datetime import datetime
from pages.show_pages import ShowPage
from send_push import push

SHOW_URL = "https://www.howardstern.com/show/"
CRED_DIR = os.path.expanduser("~")
api_cred_file = "{0}/.pushover.txt".format(CRED_DIR)
SCRIPT_EXC_DIR = os.path.dirname(os.path.realpath(__file__))
lock_file = "{0}/push.lock".format(SCRIPT_EXC_DIR)
log_dir = f'{SCRIPT_EXC_DIR}/app.log'

logging.basicConfig(filename=log_dir, format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s', level=logging.INFO)



date = datetime.now()
formatted_date = date.strftime("%b %d, %Y")
f_date = datetime.strptime(formatted_date, "%b %d, %Y")

# f_date = "Jul 20, 2020"

# get the show elements from the page
page_content = requests.get(SHOW_URL).content
page = ShowPage(page_content)
shows = page.shows

# Check if lock exists and confirm validity
if os.path.isfile(lock_file):
    with open(lock_file, 'r') as f:
	    lock_date = f.readline().strip()
    if lock_date == date.strftime("%b %d, %Y"):
        print("Found lockfile. Has notification already been sent?")
        logging.info("Found lockfile. Has notification already been sent today?")
        logging.info(f"Lockfile Location: {lock_file}")
        logging.info(f"Lockdate: {lock_date}")
        quit("quitting")
    else:
        print("Old lockfile found, removing!")
        logging.info("Old lockfile found, removing!")
        os.remove(lock_file)

# Get push API credentials from disk
if os.path.isfile(api_cred_file):
    with open(api_cred_file, 'r') as f:
        creds = f.readlines()
    TOKEN = creds[0].strip().split(':')[1]
    USER = creds[1].strip().split(':')[1]
else:
    print(f"No API Credentials found in: {api_cred_file} - Check README file for setup instuctions")
    logging.info(f"No API Credentials found in: {api_cred_file} - Check README file for setup instuctions")

new_show = False
# Check shows, alert if new 
for show in shows:
    compare_show_date = datetime.strptime(show.date, "%b %d, %Y")
    if compare_show_date == f_date:
        print("Sending push notification...")
        logging.info("Sending push notification...")
        new_show = True
        push.send(TOKEN, USER, show.topics)
        
        with open(lock_file, 'w+') as f:
            # print("writing lock file")
            f.write(formatted_date)

if not new_show:
    print(f"No new show found for {f_date}")
    logging.info(f"No new show found for {str(f_date)}")
   






