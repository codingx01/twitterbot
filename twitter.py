import tweepy
import time

def main(event, context):
    auth = tweepy.OAuthHandler('API-KEY', 'API-SECRET-TOKEN')
    auth.set_access_token('ACCESS-TOKEN','ACCESS-SECRET')

    api= tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    user = api.me()

    search = ('#100DaysOfCode OR #Javascript OR #Python OR #aws OR @TechParida OR #php OR #bookingjini')
    nmTweets = 100

    for tweet in tweepy.Cursor(api.search, search, lang='en').items(nmTweets):
        if not tweet.favorited:
            try:
                tweet.favorite()
                #tweet.retweet()
                time.sleep(5)

            except Exception as e:
                print(e.reason)

            except StopIteration:
                break
                
