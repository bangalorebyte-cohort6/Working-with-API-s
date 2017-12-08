import json 
import twitter
# Keys and token from Twitter Dev
consumer_key = 'V7NMDq4w2jqY3XfuhVMQIus6U'
consumer_secret = 'Fh91YD6XAui8Cv37bwDVJa1IwdFUAtavIUpzLHHLiz7OE1SY84'
oauth_token = '886811149156491265-MiLUyDvaI2tdsRjhk0s1X8bVTnChTSQ'
oauth_token_secret = 'KfuBI33I2pPxez2llydllT8qSZJPLBHbW485hNAYz3VOg'


# authentication
auth = twitter.oauth.OAuth(oauth_token,oauth_token_secret,
    consumer_key,consumer_secret)

twitter_api = twitter.Twitter(auth=auth)

#function to search for tweets, parameters to be taken from 
# https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets
def just_twitter_search(twitter_api, q,lang, max_results=1, **kw):
    search_results = twitter_api.search.tweets(q=q, count=1, **kw)
    statuses = search_results['statuses']
    return statuses

# this variable executes the function
# q is the query parameter 
results = just_twitter_search(twitter_api,q="Iphone X",max_results=1,lang="en")
print(results)