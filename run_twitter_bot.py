import sys
import os
import argparse

from TwitterFollowBot import TwitterBot

my_bot = TwitterBot("config-sendx.txt")

ap = argparse.ArgumentParser(description='Twitter growth strategies')

dir_path = os.path.dirname(os.path.realpath(__file__)) 


def follow_follower_of_account(account, _count):
	print "About to start following followers of " + account
	my_bot.auto_follow_followers_of_user(account, count=_count)

def follow_user_like_tweet(file_name, count):
	file_path = dir_path + "/data/" + file_name
	print "Reading phrases from file " + file_path

	with open(file_path) as f:
		for num in range(0,int(count)):
			for phrase in f:
				print "Following the user and liking the tweet with phrase " + phrase
				my_bot.auto_fav_and_follow(phrase, count)

def follow_user_retweet(file_name, count):
	file_path = dir_path + "/data/" + file_name
	print "Reading phrases from file " + file_path

	with open(file_path) as f:
		for num in range(0,int(count)):
			for phrase in f:
				print "RTing the tweet with phrase " + phrase + " and following the user"
				my_bot.auto_rt_and_follow(phrase, count)

def follow_user_retweet_add_to_list(file_name, count, list_name):
	file_path = dir_path + "/data/" + file_name
	print "Reading phrases from file " + file_path

	with open(file_path) as f:
		for num in range(0,int(count)):
			for phrase in f:
				print "RTing the tweet with phrase " + phrase + " following the user and adding him to list " + list_name
				my_bot.auto_rt_and_follow_and_add_to_list(phrase, list_name, count=1)

def tweet(file_name):
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

def add_arguments(ap):
	#followfolloersof
	ap.add_argument('-s1', help='Follow followers of an account. Example Usage: -s1 sendxio 100', nargs=2)
	#liketweetfollowuserwithphrase
	ap.add_argument('-s2', help='Like tweet and follow users with phrase. Usage: -s2 phrases.txt 10', nargs=2)
	#retweetfollowuserwithphrase
	ap.add_argument('-s3', help='Retweet and follow user with phrase. Usage: -s3  phrases.txt 10', nargs=2)
	#retweetfollowaddtolistuserwithphrase
	ap.add_argument('-s4', help='Retweet, follow and add to list a user with phrase. Usage: -s4 phrases.txt 10 marketing', nargs=3)
	#tweet
	ap.add_argument('-s5', help='Tweet tweets in a file inside /data directory. Usage: -s5 tweet.txt', nargs=1)



add_arguments(ap)
opts = ap.parse_args()

if not any([opts.s1, opts.s2, opts.s3, opts.s4, opts.s5]):
    ap.print_usage()
    quit()

my_bot.sync_follows()

if (opts.s1):
	account = opts.s1[0]
	count = int(opts.s1[1])
	print account, count
	follow_follower_of_account(account, count)
elif opts.s2:
	file_name = opts.s2[0]
	count = int(opts.s2[1])
	follow_user_like_tweet(file_name, count)
elif opts.s3:
	file_name = opts.s3[0]
	count = int(opts.s3[1])
	follow_user_retweet(file_name, count)
elif opts.s4:
	file_name = opts.s4[0]
	count = int(opts.s4[1])
	list_name = opts.s4[2]
	follow_user_retweet_add_to_list(file_name, count, list_name)
elif opts.s5:
	file_name = opts.s5[0]
	tweet(file_name)
