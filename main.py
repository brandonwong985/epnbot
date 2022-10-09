import tweepy
import config
from sympy import *
import random

PRIME_FILE = "prime.txt"
punct = ["...", "?", "?!", "!", "~", "?..", "!!"]

auth = tweepy.OAuthHandler(config.api_key, config.api_key_secret)
auth.set_access_token(config.access_token, config.access_token_secret)

api = tweepy.API(auth)
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

#api.update_status("updating status using tweepy!")

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
    write_last_prime(PRIME_FILE, next_prime)
    return next_prime

def tweet_prime_number():
    prime = get_next_prime()
    api.update_status(str(prime) + random.choice(punct))

def main():
    tweet_prime_number()

if __name__ == '__main__':
    main()