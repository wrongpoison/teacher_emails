from bs4 import BeautifulSoup

import codecs
import logging
import re
import requests
import string
import sys

# def get_email(response_text):
#     soup = ''
#     soup = BeautifulSoup(response_text, 'html.parser')
    
#     email_links = (soup.find_all("a", href=re.compile(r"^mailto\:")))
#     for l in email_links:
#         email = l['href']
#         print(email.split(':')[1])

def extract_emails(request_text):
    soup = BeautifulSoup(request_text, 'html.parser')
    pattern = re.compile("swrot13\('.*'\)")
    scripts = (soup.find_all("script", text=pattern))
    for script in scripts:
        matches = re.search(r'[\w\.]*@\w*\.\w*', script.text)
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

for x in range(10000, 20000):
    url= r'https://www.slps.org/Domain/' + str(x)
    logger.info(url)
    r = requests.get(url)
    logger.info(r.status_code)

    extract_emails(r.text)

# url = r'https://www.slps.org/Domain/13252'
# logger.info(url)
# r = requests.get(url)
# logger.info(r.status_code)

# extract_emails(r.text)