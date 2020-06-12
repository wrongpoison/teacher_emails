from bs4 import BeautifulSoup

import codecs
import logging
import re
import requests
import sys

def extract_emails(request_text):
    soup = BeautifulSoup(request_text, 'html.parser')
    pattern = re.compile("swrot13\('.*'\)")
    scripts = (soup.find_all("script", text=pattern))
    for script in scripts:
        matches = re.search(r'\w*@\w*\.\w*', script.text)
        print(codecs.decode(matches.group(0),'rot_13'))


# create logger with name
logger = logging.getLogger('teacher_emails')
logger.setLevel(logging.DEBUG)

# create console handler logger 
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

# create formatter and add to handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

directory_url=r'https://go.lindberghschools.ws/Page/14990'
secondary_url = r'https://go.lindberghschools.ws//cms/UserControls/ModuleView/ModuleViewRendererWrapper.aspx?DomainID=1849&PageID=14990&ModuleInstanceID=21174&PageModuleInstanceID=20912&Tag=&PageNumber=3&RenderLoc=0&FromRenderLoc=0&IsMoreExpandedView=false&EnableQuirksMode=0&Filter=&ScreenWidth=1021&ViewID=00000000-0000-0000-0000-000000000000&_=1591826707309'

for x in range(50):
    url=r'https://go.lindberghschools.ws//cms/UserControls/ModuleView/ModuleViewRendererWrapper.aspx?DomainID=1849&PageID=14990&ModuleInstanceID=21174&PageModuleInstanceID=20912&Tag=&PageNumber=' + str(x) + '&RenderLoc=0&FromRenderLoc=0&IsMoreExpandedView=false&EnableQuirksMode=0&Filter=&ScreenWidth=1021&ViewID=00000000-0000-0000-0000-000000000000&_=1591826707309'
    logger.info(url)
    r = requests.get(url)
    logger.info(r.status_code)
    extract_emails(r.text)