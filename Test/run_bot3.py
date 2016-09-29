#retweetfollowuserwithphrase
#python run_bot3.py count phrase1 #hashtag1
import sys
from TwitterFollowBot import TwitterBot

my_bot = TwitterBot()

count = sys.argv[1:][0]
phrases = sys.argv[2:]

for num in range(0,int(count)):
	for phrase in phrases:
		print "RTing the tweet with phrase " + phrase + " and following the user"
		my_bot.auto_rt_and_follow(phrase, count=1)