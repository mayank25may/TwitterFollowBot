#liketweetfollowuserwithphrase
#python run_bot2.py count phrase1 #hashtag1
import sys
from TwitterFollowBot import TwitterBot

my_bot = TwitterBot()

count = sys.argv[1:][0]
phrases = sys.argv[2:]

for num in range(0,int(count)):
	for phrase in phrases:
		print "Following the user and liking the tweet with phrase " + phrase
		my_bot.auto_fav_and_follow(phrase, count=1)