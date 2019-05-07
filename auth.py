#!/usr/bin/env python

import tweepy
import os

auth = tweepy.OAuthHandler("YOUR_TOKEN", "YOUR_SECRET")

try:
    redirect_url = auth.get_authorization_url()
except tweepy.TweepError:
    print('Failed to get Twitter request token!')

print('Attempting to open ' + redirect_url)
os.system('xdg-open "' + redirect_url + '"')

verifier = raw_input('Verifier:')

try:
    auth.get_access_token(verifier)
except tweepy.TweepError:
    print('Failed to get Twitter access token!')

print('Access token: ' + auth.access_token)
print('Access secret: ' + auth.access_token_secret)
