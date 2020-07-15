# :space_invader: Social-Scrape-Bot

> This python application is used to collect social media data and append daily results to sheets file on Google Drive. </br>
> Scrape is running on a NodeJS server with a daily cron job. </br>
> This data is collected from Instagram, Facebook, and YouTube to automate how a marketing department can track and collect data.

> Server is being hosted on <img src="https://www.raspberrypi.org/app/uploads/2011/10/Raspi-PGB001.png" height="25">Raspberry Pi
 ---
![Recordit GIF](http://g.recordit.co/j0OjNJ6QD9.gif)
![Recordit GIF](http://g.recordit.co/0nCCA7NR6o.gif)

### Framework, Packages, & APIs
For this application to successfully compile by default, the following packages below are required:
- <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1024px-Python-logo-notext.svg.png" height="20"> Python v3.8

```shell
// Scraping
$ pip install requests bs4

// Pathing
$ pip install dotenv pathlib

// Google Drive Authentication
$ pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

- <img src="https://nodejs.org/static/images/logo-hexagon-card.png" height="25"> Node v12
```shell
// Server
$ npm install express

// Cron and Email Notification
$ npm install node-cron shelljs nodemailer
```
- <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Cloud-API-Logo.svg/1200px-Cloud-API-Logo.svg.png" height="20"> Google API </br>
The following APIs are used to retrieve and insert scrape data:
  - <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/Logo_of_Google_Drive.svg/1024px-Logo_of_Google_Drive.svg.png" height="20"><a href="https://console.developers.google.com/apis/library/drive.googleapis.com"> Drive API</a>
  - <img src="https://seeklogo.com/images/G/google-sheets-logo-70C2B2CA6A-seeklogo.com.png" height="20"><a href="https://console.developers.google.com/apis/library/sheets.googleapis.com">   Sheets API</a> 
  - <img src="https://cdn4.iconfinder.com/data/icons/logos-and-brands/512/395_Youtube_logo-512.png" height="20"><a href="https://console.developers.google.com/apis/library/youtube.googleapis.com"> YouTube Data API</a>
---
### _.env_ File Structure
File that holds confidential keys:
```shell
USERNAME=****
PASSWORD=****

CLINICA_API_KEY=****
CLINICA_CHANNEL_ID=****

VOIR_API_KEY=****
VOIR_CHANNEL_ID=****
```
---
### _google_drive_secret.json_ File Structure
After creating credentials to Google Drive API, a JSON file will be downloaded to your machine:
```shell
{
  "type": "service_account",
  "project_id": ****,
  "private_key_id": ****,
  "private_key": ****,
  "client_email": ****,
  "client_id": ****,
  "auth_uri": ****,
  "token_uri": ****,
  "auth_provider_x509_cert_url": ****,
  "client_x509_cert_url": ****
}
```
