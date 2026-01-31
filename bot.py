import tweepy
import time
import random
import json
from datetime import datetime, timedelta

# Load config
with open("config.json", "r") as f:
    config = json.load(f)

API_KEY = config["API_KEY"]
API_SECRET = config["API_SECRET"]
ACCESS_TOKEN = config["ACCESS_TOKEN"]
ACCESS_SECRET = config["ACCESS_SECRET"]
POST_MESSAGE = config["POST_MESSAGE"]

MODE = config.get("MODE", "random")
FIXED_HOUR = config.get("FIXED_HOUR", 12)
FIXED_MINUTE = config.get("FIXED_MINUTE", 0)

# Authenticate
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

def post_message():
    try:
        api.update_status(POST_MESSAGE)
        print(f"Posted '{POST_MESSAGE}' at {datetime.now()}")
    except Exception as e:
        print("Error posting:", e)

# Main loop
while True:
    if MODE == "random":
        hours = random.randint(0, 23)
        minutes = random.randint(0, 59)
        seconds = random.randint(0, 59)
    elif MODE == "fixed":
        hours = FIXED_HOUR
        minutes = FIXED_MINUTE
        seconds = 0
    else:
        print("Invalid MODE in config.json. Defaulting to random.")
        hours = random.randint(0, 23)
        minutes = random.randint(0, 59)
        seconds = random.randint(0, 59)

    next_post = datetime.now().replace(hour=hours, minute=minutes, second=seconds, microsecond=0)
    if next_post < datetime.now():
        next_post += timedelta(days=1)

    wait_seconds = (next_post - datetime.now()).total_seconds()
    print(f"Next post scheduled at {next_post}")
    
    time.sleep(wait_seconds)
    post_message()
