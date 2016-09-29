from TwitterFollowBot import TwitterBot

my_bot = TwitterBot("config-sendx.txt")

my_bot.send_tweet("Hello @mayank25may #hello")

#my_bot.sync_follows()

#my_bot.auto_follow("#marketing")

#my_bot.auto_follow_followers()

#my_bot.auto_fav("#marketing", count=1000)

#my_bot.auto_rt("#marketing", count=1000)

#my_bot.auto_add_to_list("#marketing", "marketing", count=10)




#Strategy 1
#Follow all followers of a follower and send them a DM on follow.
#inputs required - list of targeted 'followers'

#Strategy 2
#Liking a tweet containg a specific pahrase and/or hashtag
#Follow the respective user
#inputs required - list of phrase and/or hastag

#Strategy 3
#Retweeting a tweet containg a specific phrase and/or hashtag
#Follow the respective user

#Strategy 4
#Retweeting a tweet containg a specific phrase and/or hashtag
#Follow the respective user
#Adding him to a respective list
#DM should be tailored in such cases
#inputs required - list of phrase and/or hashtag

#Strategy 5
#Post a tweet
#inputs required - list of tweet texts

#Strategy 6
#Post a targeted tweet with @user
#inputs required - list of tweet texts

