if __name__ == "__main__":
    import time
    import twitterService as twitterService
    cKey=""
    cSecret=""
    atKey=""
    atSecret=""
    splitter=""#string to check if someone wants me to answer him
    botName=""#what's the name of your bot
    answerTweet=""#what to answer
    twitterInstance=twitterService.TwitterService(cKey,cSecret,atKey,atSecret)
    numberofTweets=0
    numberofTweetsperHour=0
    lastID=None# Change this if you wish
    while(True):
		if(numberofTweets>998):#daily limits :(
			print("See you tomorrow fellah, almost reached my limit")
			numberofTweets=0
			time.sleep(24*60*60)#(hours*minutes*seconds thus sleep for 24 hours)
		if(numberofTweetsperHour>18):#half hour limits :(
			print("Refilling")
			numberofTweetsperHour=0
			time.sleep(60*60)#(minutes*seconds thus sleep for 1 hour)
		time.sleep(60)#sleep 60 seconds between requests
		mentions=twitterInstance.getMentions(lastid=lastID)
		for mention in mentions:
			status=mention.text.lower()
			if status.find(splitter)!=-1:
				reply=mention.id
				status=status.split("@")
				status.remove(splitter)
				status.remove("botName")
				author=mention.user.screen_name #who wrote the tweet
				message=""
				for user in status:
					message=message+"@"+user+" "#mention all users mentioned
					message=message+answerTweet+"@"+author
					if lastID!=reply:
						twitterInstance.post(message,reply)#post tweet
						lastID=reply
						numberofTweets+=1
						numberofTweetsperHour+=1
    
        
