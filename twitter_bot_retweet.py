import tweepy
from textblob import TextBlob
import time

CONSUMER_KEY='kfxKzlDoxbxxkxApgCNzPmK0S'
CONSUMER_SECRET='Jr0NwOsvmPvFKrLtRBoSM1kqt7VdlhTwxklbBsqpKC95iG8vc5'
ACCESS_TOKEN_KEY='1431851105370005504-nHyCabVTlypmd1iH5YEzpnjWdqPbkd'
ACCESS_TOKEN_SECRET='XWk9JdsthTM4YRsvGDoD0XLcZMoLkrrWVNNmZ6YlOf6CS'

KEY='スノーボード'
authenticator=tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
authenticator.set_access_token(ACCESS_TOKEN_KEY,ACCESS_TOKEN_SECRET)

api=tweepy.API(authenticator,wait_on_rate_limit=True)

bot_id=int(api.me().id_str)

class MyStreamListener(tweepy.StreamListener):
    def on_status(self,tweet):

        print(f'{tweet.author.screen_name}-{tweet.text}')
        print("Tweet Found!")
        if tweet.in_reply_to_status_id is None and tweet.author.id!=bot_id:
            if not tweet.retweeted:
                try:
                    print("retweet attempting...")
                    api.retweet(tweet.id)
                    print("retweet completed")
                except Exception as err:
                    print(err)

stream_listener=MyStreamListener()
stream=tweepy.Stream(auth=api.auth,listener=stream_listener)
stream.filter(track=[KEY],languages="ja")