# SOCIAL SCRAPE

# Install google drive requirements: pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

import json
import urllib.request
import re
import requests
from bs4 import BeautifulSoup
import os
import datetime
import time
from dotenv import load_dotenv
from pathlib import Path
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Pulling sensitive keys from .env file
load_dotenv()
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
api_key = os.getenv('API_KEY')
channel_id = os.getenv('CHANNEL_ID')

# Setting up auth for google sheets 
scope  = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds  = ServiceAccountCredentials.from_json_keyfile_name("google_drive_secret.json")
client = gspread.authorize(creds)

newDate  = datetime.datetime.now()
date  = datetime.date.today()
start = time.time()

clinica_google_sheet = client.open('SOCIAL MEDIA TRACKING').get_worksheet(0)
voir_google_sheet    = client.open('SOCIAL MEDIA TRACKING').get_worksheet(1)

# Setting up Social Media URLs
clinica          = "THE CLINICA"
clinicaInstagram = 'https://www.instagram.com/theclinica/?__a=1'
clinicaFacebook  = requests.get('https://www.facebook.com/THECLINICA.CA/')
clinicaTikTok    = requests.get('https://www.tiktok.com/@theclinica?_d=dae6af52k35ahb&language=en&sec_uid=MS4wLjABAAAAuxNZMcep3-Ntdi2v8Hkx37mSbsI4Q4IYsg_uKsojpaHXeFoVD84W4TfqP-6VktOV&share_author_id=6771453030593577986&u_code=d9mimk6b31e4je&utm_campaign=client_share&app=musically&utm_medium=ios&user_id=6771453030593577986&tt_from=sms&utm_source=sms&source=h5_m')
clinicaAPIKey    = os.getenv('CLINICA_API_KEY')
clinicaChannelID = os.getenv('CLINICA_CHANNEL_ID')

voir             = "VOIR HAIRCARE"
voirInstagram    = 'https://www.instagram.com/voirhaircare/?__a=1'
voirFacebook     = requests.get('https://www.facebook.com/voirhaircare/')
voirAPIKey       = os.getenv('VOIR_API_KEY')
voirChannelID    = os.getenv('VOIR_CHANNEL_ID')

# Scraping Instagram JSON result for data
def getInstagramData(account, url):

    json_url = urllib.request.urlopen(url)
    data     = json.loads(json_url.read())

    followerCount  = data['graphql']['user']['edge_followed_by']['count']
    postCount      = data['graphql']['user']['edge_owner_to_timeline_media']['count']
    
    instagramData = [followerCount, postCount]

    return instagramData

# Scraping Facebook page
def getFacebookData(account, url):
    soup  = BeautifulSoup(url.text, 'lxml')

    likeCount    = soup.find("div", text = re.compile('people like this')).text.split()[0]
    followCount  = soup.find("div", text = re.compile('people follow this')).text.split()[0]

    facebookData = [followCount, likeCount]

    return facebookData

# Pull reporting data from YouTube API
def getYoutubeData(account, channel_id, api_key):
    request = "https://www.googleapis.com/youtube/v3/channels?part=statistics&id=" + channel_id + "&key=" + api_key

    json_url = urllib.request.urlopen(request)
    data     = json.loads(json_url.read())

    viewCount        = data['items'][0]['statistics']['viewCount']
    subscriberCount  = data['items'][0]['statistics']['subscriberCount']
    videoCount       = data['items'][0]['statistics']['videoCount']

    youtubeData = [subscriberCount, viewCount, videoCount]

    return youtubeData

# Building list to append to existing spreadsheet
clinicaRow = [str(date), 
                getInstagramData (clinica, clinicaInstagram)[0], " ", getInstagramData(clinica, clinicaInstagram)[1],
                getFacebookData  (clinica, clinicaFacebook)[0],  getFacebookData (clinica, clinicaFacebook)[1],
                getYoutubeData   (clinica, clinicaChannelID, clinicaAPIKey)[0], getYoutubeData(clinica, clinicaChannelID, clinicaAPIKey)[1],
                getYoutubeData   (clinica, clinicaChannelID, clinicaAPIKey)[2]
             ]

voirRow    = [str(date), 
                getInstagramData (voir, voirInstagram)[0], " ", getInstagramData(voir, voirInstagram)[1],
                getFacebookData  (voir, voirFacebook)[0],  getFacebookData (voir, voirFacebook)[1],
                getYoutubeData   (voir, voirChannelID, voirAPIKey)[0], getYoutubeData(voir, voirChannelID, voirAPIKey)[1],
                getYoutubeData   (voir, voirChannelID, voirAPIKey)[2]
             ]

# Appending new data to each googlesheet
clinica_google_sheet.append_row(clinicaRow)
voir_google_sheet.append_row(voirRow)

print("\n[{}] records inserted into {} on {}...".format(len(clinicaRow), clinica, newDate))
print("\n[{}] records inserted into {} on {}...\n".format(len(voirRow), voir, newDate))

print("It took [{}] seconds to execute...\n".format(round(time.time() - start, 2)))