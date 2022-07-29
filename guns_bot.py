import requests                                             #Used for doing actual http requests
from dotenv import load_dotenv                              #That's for maintaing my bot credentials hidden
import schedule                                             #Used for maintaining the tweet interval
from keep_alive import keep_alive

import os                                                   #For retrieving the credentials and acessing songs
from urllib.parse import quote as percentage_encode         #Used to generate an OAuth valid string for Twitter authenticating
import base64                                               #Same purpose as above
from hashlib import sha1                                    #Same purpose as above
import hmac                                                 #Same purpose as above
import time                                                 #Same Purpose as above and to sleep until next tweet time
import random                                               #Used for choosing wich verse will be posted
import json                                                 #Used for oppening song information

#These lines loads all the credentials and keep them stored for the running time
load_dotenv()
consumer_key = os.getenv("twitter_consumer_key")
consumer_secret = os.getenv("twitter_consumer_secret")
acess_token = os.getenv("twitter_acess_token")
acess_secret = os.getenv("twitter_acess_secret")

#This loads the possible songs (I fucking hate this file opening thing please god free me from needing to edit it for the rest of my life)
songs = []
for directory in os.walk("./"):
    for file in directory[2]:
        directory[2][directory[2].index(file)] = directory[0] + "/" + file
    songs = [*songs, *directory[2]]
songs = list(filter(lambda f: f.endswith(".json"), songs))

MULTIPLE_VERSES_PROB = 25

def build_oauth_header(base_url, method, request_parameters):
    """It's been some months since I did this thing. I don't fucking know if there's a lib
       that does this dirty job, but if it does then I didn't fucking managed to find it when
       I needed. Anyways, this works fine lol."""
    auth_parameters = {
        "oauth_consumer_key": consumer_key,
        "oauth_nonce": base64.b64encode(bytearray([random.randint(0,255) for i in range(32)])).decode("ascii"),
        "oauth_signature_method": "HMAC-SHA1",
        "oauth_timestamp": str(time.time()),
        "oauth_token": acess_token,
        "oauth_version": "1.0"
    }
    parameters = {**request_parameters, **auth_parameters}
    for key in parameters:
        parameters[key] = percentage_encode(parameters[key], safe = "")
    parameters = dict(sorted(parameters.items()))
    parameter_string = ""
    for key in parameters:
        parameter_string += key + "=" + parameters[key] + "&"
    parameter_string = parameter_string[:-1]
    signature = method + "&" + percentage_encode(base_url, safe = "") + "&" + percentage_encode(parameter_string, safe = "")
    signature = bytearray(signature.encode())
    signing_key = percentage_encode(consumer_secret, safe = "") + "&" + percentage_encode(acess_secret, safe = "")
    signing_key = bytearray(signing_key.encode())
    auth_parameters['oauth_signature'] = base64.urlsafe_b64encode(hmac.new(signing_key, signature, sha1).digest())
    DST = "OAuth "
    for key in auth_parameters:
        DST += percentage_encode(key, safe = "") + "=\"" + percentage_encode(auth_parameters[key], safe = "") + "\", "
    DST = DST[:-2]
    return {"Authorization": DST}

def post_tweet(verses):
    """This function simply posts a tweet."""
    base_url = f"https://api.twitter.com/1.1/statuses/update.json"
    request_parameters = {
        "status": verses
    }
    headers = build_oauth_header(base_url, "POST", request_parameters)
    response = requests.post(base_url, headers = headers, data = request_parameters)
    return response.json()

def answer_tweet(text, tweet_id):
    """This function replies to a existing tweet, and needs its ID of course."""
    base_url = f"https://api.twitter.com/1.1/statuses/update.json"
    request_parameters = {
        "status": text,
        "in_reply_to_status_id": str(tweet_id)
    }
    headers = build_oauth_header(base_url, "POST", request_parameters)
    response = requests.post(base_url, headers = headers, data = request_parameters)
    return response.json()

def return_random_line():
    """This method gets a random verse (or a combination of verses) from a random music.
       It also returns info like song name and so.""" 
    chosen_music = random.choice(songs)
    with open(chosen_music, "r") as file:
        song_info = json.load(file)
        payload = { 
            "name": song_info['name'],
            "artist": song_info['artist'],
            "album": song_info['album'],
            "cover": song_info['cover'],
            "links": song_info['links']
        }
        if payload['cover']:
            payload['cover_info'] = song_info['cover_info']
        n = random.randint(1, 100)
        if n < MULTIPLE_VERSES_PROB:
            payload['verse'] = random.choice(song_info['combinations'])
        else:
            payload['verse'] = random.choice(song_info['lyrics'].split("\n"))
        return payload

def tweet_a_verse():
    verse = return_random_line()
    tweet = post_tweet(verse['verse'])
    text_info = f"{verse['name']} from {verse['album']} - {verse['artist']}\n"\
    f"Listen to it here: {' '.join(verse['links'])}"
    answer_tweet(text_info, tweet['id'])
    print("I've made a post.")

if __name__ == "__main__":
    schedule.every().hour.at(":00").do(tweet_a_verse)
    keep_alive() #This stuff is because of my host,aand isn't needed for running the bot itself
    print("The script is running. Posts will be done at every hour.")
    while True:
        schedule.run_pending()
        time.sleep(1)
