# Import the modules

import tweepy
from tweepy import OAuthHandler
import os
from PIL import Image
import requests
from io import BytesIO
import pandas as pd


def twitter_api():
    access_token = 'Access - Token'
    access_token_secret = 'Access - Token -Secret'
    consumer_key = 'Consumer -Key'
    consumer_secret = 'Consumer - Secret - Key'

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    return api


def merge_image(url_image, url_logo):
    response = requests.get(url_image)
    background = Image.open(BytesIO(response.content)).convert("RGBA")
    response2 = requests.get(url_logo)
    logo = Image.open(BytesIO(response2.content)).convert("RGBA")

    background.paste(logo, (0, 0, logo.size[0], logo.size[1]), logo)
    background.save("temp.png", format="png")


def tweet_woimage(message):
    api = twitter_api()
    api.update_status(message)


def tweet_image(url, message, pos):
    api = twitter_api()
    filename = 'temp.png'
    url_logo = 'http://cityread.london/wp-content/uploads/2016/02/HarperCollins-logo.png'

    request = requests.get(url, stream=True)
    request2 = requests.get(url_logo, stream=True)
    if request.status_code == 200 and request2.status_code == 200:
        merge_image(url, url_logo)
        api.update_with_media(filename, status=message)
        os.remove(filename)

    else:
        tweet_woimage(message)
        print("Warning!!! Tweet with ID." + str(pos + 1) + " Unable to download image")


def obtain_excel_data(path, sheet):
    df = pd.read_excel(path, sheet_name=sheet)
    return df
