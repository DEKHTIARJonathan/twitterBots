import twitter
import time
import sys

# ==========================================================================================================

DM_text = """Hey my friend, at DataRadar.IO we love sharing knowledge : freely and ads free. We think that knowledge is the most valuable thing and therefore we offer a free and unlimited access to our platform https://www (dot) dataradar.io over an API. If you have any project aiming to create a social media bot or a tech blog we would love to hear about it.
If you have any specific needs, don't hesitate to tell us. I'm always trying to improve the platform.

You'll find hundreds of high value ressources about data science, machine learning, deep learning, computer vision and so on!
Let's freely share knowledge !

If needed, you can contact me at : contact@dataradar.io

See you at dataradar.io

Regards,
Jonathan Dekhtiar"""

# ===========================================================================================================


# Make constants to hold values of our keys
consumer_key_var = "#############################"
consumer_secret_var = "#############################"
access_token_var = "#############################"
access_token_secret_var = "#############################"

api = twitter.Api(consumer_key=consumer_key_var,
                      consumer_secret=consumer_secret_var,
                      access_token_key=access_token_var,
                      access_token_secret=access_token_secret_var)

followers = []

cursor_var = -1

while cursor_var != 0 :
	try:
		users = api.GetFollowersPaged(screen_name="born2data", cursor=cursor_var, count=200)
		cursor_var = users[0]
	except Exception:
		time.sleep(60*5)
		pass

	for user in users[2]["users"]:
		followers.append(user[u'screen_name'])
		
time.sleep(60*15)

while 1:

	temp_list = []
	
	cursor_var = -1

	while cursor_var != 0 :
		try:
			users = api.GetFollowersPaged(screen_name="born2data", cursor=cursor_var, count=200)
			cursor_var = users[0]
		except Exception:
			time.sleep(60*5)
			pass

		for user in users[2]["users"]:
			temp_list.append(user[u'screen_name'])
		
	for user_tmp in temp_list:
	
		if user_tmp not in followers:
			try:
				api.PostDirectMessage(DM_text, screen_name=user_tmp)
				time.sleep(60)
			except Exception: 
				pass
			followers.append(user_tmp)
	
	time.sleep(60*15)