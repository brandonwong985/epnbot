import tweepy
import config
from sympy import *
import random
from apscheduler.schedulers.blocking import BlockingScheduler
import datetime

PRIME_FILE = "prime.txt"
DEBUG_FILE = "debug.txt"
TWEET_TIMESTAMP = '0'
MY_TIMEZONE = "America/Los_Angeles"
punct = ["...", "?", "?!", "!", "~", "?..", "!!"]


auth = tweepy.OAuthHandler(config.api_key, config.api_key_secret)
auth.set_access_token(config.access_token, config.access_token_secret)

api = tweepy.API(auth)
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

def read_last_prime(FILE_NAME):
    file = open(FILE_NAME, 'r')
    last_prime = int(file.read().strip())
    file.close()
    return last_prime

def write_last_prime(FILE_NAME, last_prime):
    file = open(FILE_NAME, 'w')
    file.write(str(last_prime))
    file.close()
    return

def get_next_prime():
    last_prime = read_last_prime(PRIME_FILE)
    next_prime = nextprime(int(last_prime))
    return next_prime

def tweet_prime_number():
    prime = get_next_prime()
    tweet = str(prime) + random.choice(punct)   
    t = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    try:
        api.update_status(tweet)
        print("tweeted " + tweet + " at " + t)  
        write_last_prime(PRIME_FILE, prime)  
    except:
        tweet_failed(DEBUG_FILE, prime, t)

def tweet_failed(FILE_NAME, failed_prime, t):
    file = open(FILE_NAME, 'a')
    file.write("tweet " + str(failed_prime) + " failed at " + str(t))
    file.close()
    return


def main():
    sched = BlockingScheduler(timezone=MY_TIMEZONE)
    sched.add_job(tweet_prime_number, 'cron', minute=TWEET_TIMESTAMP)
    sched.start()

if __name__ == '__main__':
    main()