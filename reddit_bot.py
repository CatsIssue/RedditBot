import praw
import config 
import time

def bot_login():
	print("Loggin in ...")
	r =	praw.Reddit(
			username = config.username,
			password = config.password,
			client_secret = config.client_secret,
			user_agent = "busterronitest's dog comment responder v0.1",
			client_id = config.client_id)
	print ("Logged in...")

	return r


# core of the loop 
def run_bot(r): 
	print("Obtaining 100 comments")

	comment_replied_to = []

	for comment in r.subreddit('test').comments(limit = 30):
	  if "dog" in comment.body:
	  	print("String with  \"dog\" found in comment" + comment.id)
	  	comment.reply("I find you")
	  	print("Replied done on comment at " + comment.id)
	  	comment_replied_to.append(comment.id)

	#Sleep during 10 seconds 
	print("Sleeping during 10 seconds")
	time.sleep(10)	  	

r = bot_login()	
while(True):
	run_bot(r)	  	
