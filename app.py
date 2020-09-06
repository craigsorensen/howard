import requests
import os

from datetime import datetime
from pages.show_pages import ShowPage
from send_push import push

SHOW_URL = "https://www.howardstern.com/show/"
CRED_DIR = os.path.expanduser("~")
api_cred_file = "{0}/.pushover.txt".format(CRED_DIR)
SCRIPT_EXC_DIR = os.path.dirname(os.path.realpath(__file__))
lock_file = "{0}/push.lock".format(SCRIPT_EXC_DIR)


date = datetime.now()
f_date = date.strftime("%b %d, %Y")
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
        quit("quitting")
    else:
        print("Old lockfile found, removing!")
        os.remove(lock_file)

# Get push API credentials from disk
if os.path.isfile(api_cred_file):
    with open(api_cred_file, 'r') as f:
        creds = f.readlines()
    TOKEN = creds[0].strip().split(':')[1]
    USER = creds[1].strip().split(':')[1]
else:
    print(f"No API Credentials found in: {api_cred_file}")

new_show = False
# Check shows, alert if new 
for show in shows:
    if show.date == f_date:
        print("Sending push notification...")
        new_show = True
        push.send(TOKEN, USER, show.topics)
        
        with open(lock_file, 'w+') as f:
            # print("writing lock file")
            f.write(f_date)

if not new_show:
    print(f"No new show found for {f_date}")
   






