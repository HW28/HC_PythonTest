import unittest
from functions import *
from os import path
import json
from pathlib import Path


class TestFunctions(unittest.TestCase):

    def test_credentials(self):
        self.assertEqual(str(type(twitter_api().verify_credentials())),  "<class 'tweepy.models.User'>")

    def test_mergeImage(self):
        url_image = 'https://upload.wikimedia.org/wikipedia/commons/5/55/Dalailama1_20121014_4639.jpg'
        url_logo = 'http://cityread.london/wp-content/uploads/2016/02/HarperCollins-logo.png'

        self.assertTrue(str(path.exists('temp.png')))

    def test_tweetwoimage(self):
        text = "Test without image tweet"

        tweet_woimage(text)
        tweet = twitter_api().user_timeline(screen_name='swh_28', count=1)[0]
        json_str = json.dumps(tweet._json)
        resp_dict = json.loads(json_str)
        last_tweet = (resp_dict['text'])

        self.assertEqual(last_tweet, text)

    def test_tweetimage_text(self):
        text = "Test with image tweet"
        url = 'https://upload.wikimedia.org/wikipedia/commons/5/55/Dalailama1_20121014_4639.jpg'
        media = 'photo'

        tweet_image(url, text, 0)
        tweet = twitter_api().user_timeline(screen_name='swh_28', count=1)[0]
        json_str = json.dumps(tweet._json)
        resp_dict = json.loads(json_str)
        last_tweet_image = (resp_dict['entities']['media'][0]['type'])

        self.assertEqual(last_tweet_image, media)

    def test_obtain_excel_data(self):
        text = "Test with image tweet"
        url = 'https://upload.wikimedia.org/wikipedia/commons/5/55/Dalailama1_20121014_4639.jpg'
        media = 'photo'

        tweet_image(url, text, 0)
        tweet = twitter_api().user_timeline(screen_name='swh_28', count=1)[0]
        json_str = json.dumps(tweet._json)
        resp_dict = json.loads(json_str)
        last_tweet_image = (resp_dict['entities']['media'][0]['type'])

        self.assertEqual(last_tweet_image, media)

    def test_obtain_excel_data(self):
        number_of_tweets = 14
        data_folder = Path("in/")
        file_to_open = data_folder / "Python_exercise1.xlsx"

        data = obtain_excel_data(file_to_open, "data_table")
        entries = len(data)

        self.assertEqual(entries, number_of_tweets)


if __name__ == '__main__':
    unittest.main()
