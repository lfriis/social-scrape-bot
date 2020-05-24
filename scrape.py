# #

# SOCIAL SCRAPE

# Get instagram followers for both platforms
#     Get likes and comments on a monthly basis
# Get facebok followers and page likes and check-ins for both
# Get youtube subscribers
# Get tiktok followers and likes for both

# Run everyday before 9AM

# #

import json
import urllib.request
import re
import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
from pathlib import Path

# Pulling sensitive keys from .env file
load_dotenv()
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

api_key = os.getenv('API_KEY')
channel_id = os.getenv('CHANNEL_ID')

clinicaInstagram = 'https://www.instagram.com/theclinica/?__a=1'
clinicaFacebook  = requests.get('https://www.facebook.com/THECLINICA.CA/')
clinicaAPIKey    = os.getenv('CLINICA_API_KEY')
clinicaChannelID = os.getenv('CLINICA_CHANNEL_ID')

voirInstagram    = 'https://www.instagram.com/voirhaircare/?__a=1'
voirFacebook     = requests.get('https://www.facebook.com/voirhaircare/')
voirAPIKey       = os.getenv('VOIR_API_KEY')
voirChannelID    = os.getenv('VOIR_CHANNEL_ID')

def getInstagramData(url):

    json_url = urllib.request.urlopen(url)
    data     = json.loads(json_url.read())

    followerCount  = data['graphql']['user']['edge_followed_by']['count']
    followingCount = data['graphql']['user']['edge_follow']['count']
    postCount      = data['graphql']['user']['edge_owner_to_timeline_media']['count']
    
    print('\nINSTAGRAM DATA')
    print('Total Following: '     + str(followingCount))
    print('Total followerCount: ' + str(followerCount))
    print('Total Posts: '         + str(postCount))

def getFacebookData(url):
    soup  = BeautifulSoup(url.text, 'lxml')

    likeCount   = soup.find("div", text = re.compile('people like this')).text
    followCount = soup.find("div", text = re.compile('people follow this')).text

    print('\nFACEBOOK DATA')
    print('Facebook Likes: '     + likeCount.split()[0])
    print('Facebook Followers: ' + followCount.split()[0])

# Pull reporting data from youtube
def getYoutubeData(channel_id, api_key):
    request = "https://www.googleapis.com/youtube/v3/channels?part=statistics&id=" + channel_id + "&key=" + api_key

    json_url = urllib.request.urlopen(request)
    data     = json.loads(json_url.read())

    viewCount        = data['items'][0]['statistics']['viewCount']
    commentCount     = data['items'][0]['statistics']['commentCount']
    subscriberCount  = data['items'][0]['statistics']['subscriberCount']
    videoCount       = data['items'][0]['statistics']['videoCount']

    print('\nYOUTUBE DATA ')
    print('Total Views:        ' + viewCount)
    print('Total Comments:     ' + commentCount)
    print('Total Subscribers:  ' + subscriberCount)
    print('Total Videos:       ' + videoCount)

getInstagramData(clinicaInstagram)
getFacebookData(clinicaFacebook)

getInstagramData(voirInstagram)
getFacebookData(voirFacebook)

getYoutubeData(channel_id, api_key)
# getYoutubeData(clinicaChannelID, clinicaAPIKey)
# getYoutubeData(voirChannelID, voirAPIKey)