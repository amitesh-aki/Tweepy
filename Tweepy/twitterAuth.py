# twitterAuth.py

import twitter

"""This script is meant to connect to the Twitter API via the tokens below"""

api = twitter.Api(consumer_key='yourConsumerKeyGoesHere',
    consumer_secret='yourConsumerSecretGoesHere',
    access_token_key='your-AccessTokenGoesHere',
    access_token_secret='yourTokenSecretGoesHere')