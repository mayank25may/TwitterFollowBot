#retweetfollowuserwithphrase
#python run_bot5.py file_with_tweet_in_each_row
#file_with_tweet_in_each_row shuld be present in ./data folder
import sys
import os
import argparse
from TwitterFollowBot import TwitterBot

my_bot = TwitterBot()

file_name = sys.argv[1:][0]

dir_path = os.path.dirname(os.path.realpath(__file__)) 

file_path = dir_path + "/data/" + file_name

print "Reading tweets from file " + file_path

with open(file_path) as f:
	for tweet in f:
		print len(tweet)
		if len(tweet) <= 140 and len(tweet) > 1:
			print tweet
			my_bot.send_tweet(tweet)
		else:
			print "Coud not tweet since the length is more than 140 characters or is nil"