import time
from TwitterFollowBot import TwitterBot
import datetime

my_bot = TwitterBot("config.txt")
my_bot.bot_setup("config.txt")
my_bot.bot_setup("config.txt")

timer = datetime.datetime.now()

try:
	my_bot.sync_follows()
except Exception: 
	pass

while True:	
	
	try:
		my_bot.auto_follow_followers()
	except Exception: 
			pass
	

	hashtags = ["#data", "#machinelearning", "#datascience", "#computervision", "#bigdata"]
	for hashtag in hashtags:
		try:
			my_bot.auto_follow(hashtag, count=1000)
		except Exception: 
			pass		
		
	keywords = ["born2data", "dataradar.io", "dataradar"]
	for keyword in keywords:
		try:
			my_bot.auto_fav(keyword, count=1000)
		except Exception: 
			pass
		try:
			my_bot.auto_rt(keyword, count=1000)
		except Exception: 
			pass
		
	actual_time = datetime.datetime.now()
	elapsed = actual_time - timer
	
	if elapsed > datetime.timedelta(hours=72):
		timer = actual_time
		try:
			my_bot.sync_follows()
		except Exception: 
			pass

		my_bot.bot_setup("config.txt")
		
		try:
			my_bot.auto_unfollow_all_followers()
		except Exception: 
			pass