#retweetfollowaddtolistuserwithphrase
#python run_bot4.py count list_name phrase1 #hashtag1
import sys
from TwitterFollowBot import TwitterBot

my_bot = TwitterBot()

count = sys.argv[1:][0]
list_name = sys.argv[1:][1]
phrases = sys.argv[2:]

for num in range(0,int(count)):
	for phrase in phrases:
		print "RTing the tweet with phrase " + phrase + " following the user and adding him to list " + list_name
		my_bot.auto_rt_and_follow_and_add_to_list(phrase, list_name, count=1)