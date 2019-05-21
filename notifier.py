

import time
from notify import *
from topnews import topStories

# path to notification window icon
ICON_PATH = "/home/piyush/Desktop/Python_projects/Desktop_Notifier/1040216.svg"

# fetch news items
newsitems = topStories()

# initialise the d-bus connection
init("News Notifier")

# create Notification object
n = Notification(None, icon=ICON_PATH)

# set urgency level
n.set_urgency(URGENCY_NORMAL)

# set timeout for a notification
n.set_timeout(10000)

for newsitem in newsitems:

    # update notification data for Notification object
    n.update(newsitem['title'], newsitem['description'])

    # show notification on screen
    n.show()

    # short delay between notifications
    time.sleep(4)
