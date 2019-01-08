# use tweepy module to fetch some tweets and print them out
# Challange steps:
# Your challenge for this week is: Write code that will:

# 1 Search Twitter for a term, say Python.

# 2 Find the top trends on Twitter.

# 3 Print 100 tweets from the Twitter streaming trends1.

import tweepy

#$# Boilerplate
# Account creds here:
consumer_key = 'INSERT CONSUMER KEY HERE'
consumer_secret = 'INSERT CONSUMER SECRET HERE'
access_token = 'INSERT ACCESS TOKEN HERE'
access_token_secret = 'INSERT ACCESS TOKEN SECRET HERE'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


# Code tests V
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

# 1 & 3 Finds and prints tweets matching q={query}
for tweet in tweepy.Cursor(api.search, q='python', lang='en').items(100):
    print(tweet.text.lower())

# Find top trends on Twitter and print them
trends1 = api.trends_place(1)
trends = list(set([trend['name'] for trend in trends1[0]['trends']]))
print(trendsName)
