# from datetime import date, datetime, timedelta
# import json
from bs4 import BeautifulSoup

import codecs
import logging
import re
import requests
import sys

def extract_emails(request_text):
    # text = request_text.text
    soup = BeautifulSoup(request_text, 'html.parser')
    pattern = re.compile("swrot13\('.*'\)")
    scripts = (soup.find_all("script", text=pattern))
    for script in scripts:
        matches = re.search(r'\w*@\w*\.\w*', script.text)
        #print(matches.group(0))
        print(codecs.decode(matches.group(0),'rot_13'))


# create logger with name
logger = logging.getLogger('teacher_emails')
logger.setLevel(logging.DEBUG)

# # create file handler logger
# fh = logging.FileHandler('logger = logging.getLogger('teacher_emails')
# .log')
# fh.setLevel(logging.DEBUG)

# create console handler logger 
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

# create formatter and add to handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# fh.setFormatter(formatter)
ch.setFormatter(formatter)

# add handlers to logger
# logger.addHandler(fh)
logger.addHandler(ch)

#DIRECTORY_URL =sys.argv[1]
#logger.info(DIRECTORY_URL)

directory_url=r'https://go.lindberghschools.ws/Page/14990'
secondary_url = r'https://go.lindberghschools.ws//cms/UserControls/ModuleView/ModuleViewRendererWrapper.aspx?DomainID=1849&PageID=14990&ModuleInstanceID=21174&PageModuleInstanceID=20912&Tag=&PageNumber=3&RenderLoc=0&FromRenderLoc=0&IsMoreExpandedView=false&EnableQuirksMode=0&Filter=&ScreenWidth=1021&ViewID=00000000-0000-0000-0000-000000000000&_=1591826707309'

# r = requests.get(secondary_url)
r = requests.get(directory_url)
logger.info(r.status_code)

extract_emails(r.text)


# <li class="staffemail">
# href="mailto:xxx"

