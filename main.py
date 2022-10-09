import tweepy
import config
from sympy import *

PRIME_FILE = "prime.txt"

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


def main():
    get_next_prime()

if __name__ == '__main__':
    main()