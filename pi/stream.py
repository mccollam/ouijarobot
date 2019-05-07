#!/usr/bin/env python

import os
import tweepy
import Queue
import threading
import json
from sets import Set
from time import sleep

err = False
if not "TWITTER_CONSUMER_KEY" in os.environ:
    print("Environment variable TWITTER_CONSUMER_KEY not set!")
    err = True
else:
    consumer_key = os.environ.get("TWITTER_CONSUMER_KEY", "")

if not "TWITTER_CONSUMER_SECRET" in os.environ:
    print("Environment variable TWITTER_CONSUMER_SECRET not set!")
    err = True
else:
    consumer_secret = os.environ.get("TWITTER_CONSUMER_SECRET", "")

if not "TWITTER_OAUTH_TOKEN" in os.environ:
    print("Environment variable TWITTER_OAUTH_TOKEN not set!")
    err = True
else:
    oauth_token = os.environ.get("TWITTER_OAUTH_TOKEN", "")

if not "TWITTER_OAUTH_SECRET" in os.environ:
    print("Environment variable TWITTER_OAUTH_SECRET not set!")
    err = True
else:
    oauth_secret = os.environ.get("TWITTER_OAUTH_SECRET", "")

twitter_track = os.environ.get("TWITTER_TRACK")
if not "TWITTER_TRACK" in os.environ:
    print("WARNING: Environment variable TWITTER_TRACK not set; nothing will be streamed!")
else:
    print("Tracking", twitter_track)

if not err:
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(oauth_token, oauth_secret)
    except:
        print("Could not set API tokens")
        err = True

if not err:
    try:
        api = tweepy.API(auth)
    except:
        print("Could not authenticate with Twitter")
        err = True

if err:
    print("ERROR: Twitter API communication failed")
    while True:
        sleep(100)


class RobotListener(tweepy.StreamListener):
    def on_status(self, status):
        # Filter out retweets because we don't get the full text and there's no real
        # point in going and looking up the original just to print it again -- people
        # should say unique things! :)
        if (not status.retweeted) and ('RT @' not in status.text):
            #print("FROM: @" + status.user.screen_name + " (" + status.user.name + ")")
            #print("TEXT: " + status.text)
            q.put(status)
            #print(q.qsize())
    
    def on_error(self, status_code):
        print("ERROR!  Status code: ", status_code)
        return False

def robot(letter):
    print("ROBOT:", letter)
    os.system("screen -S robot -X stuff '" + letter + "^M'")

def display_letter(letter):
    #print("DISPLAY:", letter)
    if letter == "\n":
        letter = "<br>"
    message = { "newmessage": False, "letter": letter }
    json.dump(message, fifo)
    fifo.write("\n")
    fifo.flush()

def display_new(handle):
    print("New tweet from ", handle)
    message = { "newmessage": True, "name": handle }
    json.dump(message, fifo)
    fifo.write("\n")
    fifo.flush()

def twitter_thread():
    print("Starting twitter thread")
    robotListener = RobotListener()
    robot = tweepy.Stream(auth = api.auth, listener = robotListener)
    robot.filter(track=[twitter_track])


board_chars = Set('abcdefghijklmnopqrstuvwxyz0123456789(,@!?:.)')
q = Queue.Queue()
fifo = open('messages', 'w')

t = threading.Thread(target=twitter_thread)
t.daemon = True
t.start()

while True:
    if not q.empty():
        # Grab a tweet and show it
        tweet = q.get()
        display_new("@" + tweet.user.screen_name + " (" + tweet.user.name + ")")
        # We'll show it character by character to allow the robot to move
        for c in tweet.text:
            display_letter(c)
            if Set(c.lower()).issubset(board_chars):
                robot(c.lower())
                sleep(2)
    sleep(5)
