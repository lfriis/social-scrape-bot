# #

# Get instagram followers for both platforms
#     Get likes and comments on a monthly basis
# Get facebok followers and page likes and check-ins for both
# Get youtube subscribers
# Get tiktok followers and likes for both

# Run everyday before 9AM

# #

import requests
from bs4 import BeautifulSoup

apiKey = 'AIzaSyDvLJgqSzJuLHwrT0uyAsDUbvrFxIGSd3I'

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

    print(user)
    print('Instagram Followers: \n', followers)

def getFacebookData(url):
    soup  = BeautifulSoup(url.text, 'lxml')

    data  = soup.find('div', attrs={'class': '_4-u3 _5sqi _5sqk'})
    likes = data.find('span', attrs={'class':'_52id _50f5 _50f7'}) #finding span tag inside class
    
    print('Facebook Likes: \n', likes.text)

# Pull subscribers from youtube
def getYoutubeData(url):
    soup = BeautifulSoup(url.text, 'lxml')

    data = soup.find('div', attrs={'class': '"style-scope ytd-c4-tabbed-header-renderer', "id": "subscriber-count"})
    
    print(data)
    # subs = data.find('div#description', attrs={'class': 'yt-formatted-string'}) "class": "style-scope ytd-c4-tabbed-header-renderer"

    # print('Youtube Subsribers: ', subs)


# getInstagramData(clinicaInstagram)
# getFacebookData(clinicaFacebook)
getYoutubeData(clinicaYoutube)

# getInstagramData(voirInstagram)
# getFacebookData(voirFacebook)
