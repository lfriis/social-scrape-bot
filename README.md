# Social Scrape Bot

> Python app to collect social media data and append daily results to sheets file on Google Drive
---
> Scrape is running on a NodeJS server with a daily cron job
---
> This data is collected from Instagram, Facebook, YouTube to help Marketing department track crucial data.

### Framework, Packages, & APIs
This is app is running on:

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
$ npm isntall node-cron shelljs nodemailer
```
- <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Cloud-API-Logo.svg/1200px-Cloud-API-Logo.svg.png" height="20"> Google API Keys
  - <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/Logo_of_Google_Drive.svg/1024px-Logo_of_Google_Drive.svg.png" height="25"><a href="https://console.developers.google.com/apis/library/drive.googleapis.com">Drive API</a>
  - <a href="https://console.developers.google.com/apis/library/sheets.googleapis.com">Sheets API</a> 
  - <a href="https://console.developers.google.com/apis/library/youtube.googleapis.com">YouTube Data API</a>
