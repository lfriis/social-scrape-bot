# #

# Get instagram followers for both platforms
#     Get likes and comments on a monthly basis
# Get facebok followers and page likes and check-ins for both
# Get youtube subscribers
# Get tiktok followers and likes for both

# Run everyday before 9AM

# #

import re
import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
api_key = os.getenv('API_KEY')
channel_id = os.getenv('CHANNEL_ID')

# print(api_key)
# print(channel_id)

clinicaInstagram = requests.get('https://www.instagram.com/theclinica/')
clinicaFacebook  = requests.get('https://www.facebook.com/THECLINICA.CA/')
clinicaYoutube   = requests.get('https://www.youtube.com/channel/UC4XA4xDLyFRWQSJUs2E7EKw')

voirInstagram    = requests.get('https://www.instagram.com/voirhaircare/')
voirFacebook     = requests.get('https://www.facebook.com/voirhaircare/')
voirYoutube      = requests.get('https://www.youtube.com/channel/UCdYK8aiJppxvhsdbcdISvEg')

def getInstagramData(url):
    soup = BeautifulSoup(url.text, 'lxml')

    data = soup.find_all('meta', attrs={'property':'og:description'})
    text = data[0].get('content').split()

    user = '%s %s %s' % (text[-3], text[-2], text[-1])
    followers = text[0]

    print('\n' + user)
    print('Instagram Followers: ', followers)

def getFacebookData(url):
    soup  = BeautifulSoup(url.text, 'lxml')

    likes   = soup.find("div",text=re.compile('people like this')).text
    follows = soup.find("div",text=re.compile('people follow this')).text

    print('Facebook Likes: '     + likes.split()[0])
    print('Facebook Followers: ' + follows.split()[0])

# Pull subscribers from youtube
def getYoutubeData(url):
    soup = BeautifulSoup(url.text, 'lxml')

    data = soup.find('div', attrs={'class': '"style-scope ytd-c4-tabbed-header-renderer', "id": "subscriber-count"})
    
    print(data)


getInstagramData(clinicaInstagram)
getFacebookData(clinicaFacebook)
# getYoutubeData(clinicaYoutube)

getInstagramData(voirInstagram)
getFacebookData(voirFacebook)