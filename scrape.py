# SOCIAL SCRAPE

# Get instagram followers for both platforms
#     Get likes and comments on a daily basis
# Get facebook followers and page likes and check-ins for both
# Get youtube subscribers
# Get tiktok followers and likes for both

# Run everyday before 9AM

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

date  = datetime.date.today()
start = time.time()

google_sheet = client.open('Social Scrape Test').sheet1

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

# Scraping Instagram JSON result
def getInstagramData(account, url):

    json_url = urllib.request.urlopen(url)
    data     = json.loads(json_url.read())

    followerCount  = data['graphql']['user']['edge_followed_by']['count']
    postCount      = data['graphql']['user']['edge_owner_to_timeline_media']['count']
    
    print('\nINSTAGRAM DATA FOR ' + account)
    print('Total Following: '      + str(followingCount))
    print('Total followerCount: '  + str(followerCount))
    print('Total Posts: '          + str(postCount))

# Scraping Facebook page
def getFacebookData(account, url):
    soup  = BeautifulSoup(url.text, 'lxml')

    likeCount    = soup.find("div", text = re.compile('people like this')).text.split()[0]
    followCount  = soup.find("div", text = re.compile('people follow this')).text.split()[0]

    facebookData = [followCount, likeCount]

    return facebookData

    # print('\nFACEBOOK DATA FOR ' + account)
    # print('Likes: '              + likeCount)
    # print('Followers: '          + followCount)

# Pull reporting data from YouTube API
def getYoutubeData(account, channel_id, api_key):
    request = "https://www.googleapis.com/youtube/v3/channels?part=statistics&id=" + channel_id + "&key=" + api_key

    json_url = urllib.request.urlopen(request)
    data     = json.loads(json_url.read())

    viewCount        = data['items'][0]['statistics']['viewCount']
    commentCount     = data['items'][0]['statistics']['commentCount']
    subscriberCount  = data['items'][0]['statistics']['subscriberCount']
    videoCount       = data['items'][0]['statistics']['videoCount']

    youtubeData = [subscriberCount, viewCount, commentCount, videoCount]

    return youtubeData

    # print('\nYOUTUBE DATA FOR '  + account)
    # print('Total Views:        ' + dataArray[0])
    # print('Total Comments:     ' + dataArray[1])
    # print('Total Subscribers:  ' + dataArray[2])
    # print('Total Videos:       ' + dataArray[3])


# def getTikTok(account, url):
#     page = requests.get(url)
#     soup  = BeautifulSoup(url.text, 'lxml')

#     data = soup.find('meta', {'name':'description'}).get('content')
    
#     print('\nTIKTOK DATA FOR ' + account)
#     print(page)
#     print(soup)
#     print(data)

# Building list to append to existing spreadsheet
clinicaRow = [str(date), 
                getInstagramData (clinica, clinicaInstagram)[0], " ", getInstagramData(clinica, clinicaInstagram)[1],
                getFacebookData  (clinica, clinicaFacebook)[0],  getFacebookData (clinica, clinicaFacebook)[1],
                getYoutubeData   (clinica, clinicaChannelID, clinicaAPIKey)[0], getYoutubeData(clinica, clinicaChannelID, clinicaAPIKey)[1],
                getYoutubeData   (clinica, clinicaChannelID, clinicaAPIKey)[2], getYoutubeData(clinica, clinicaChannelID, clinicaAPIKey)[3]
             ]

# look into getting youtube comments

# google_sheet.append_row(clinicaRow)

# print("[{}] records inserted on {}...  \n".format(len(clinicaRow), date))
# print("It took [{}] seconds to execute...\n".format(round(time.time() - start, 2)))


# getInstagramData(clinica, clinicaInstagram)
# getFacebookData (clinica, clinicaFacebook)
# getYoutubeData  (clinica, clinicaChannelID, clinicaAPIKey)

# getInstagramData(voir, voirInstagram)
# getFacebookData (voir, voirFacebook)
# getYoutubeData(voir, voirChannelID, voirAPIKey)