#followfolloersof
#python run_bot.py twitter_handle 
import sys
from TwitterFollowBot import TwitterBot

my_bot = TwitterBot()

my_bot.sync_follows()

account = sys.argv[1:][0]

print "About to start following followers of " + account

my_bot.auto_follow_followers_of_user(account, count=1000)
