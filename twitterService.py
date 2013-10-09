#!/var/lib/openshift/5255b3144382eccf93000296/python/virtenv/bin/python
import twitter
class TwitterService:
	'Base class handling all twitter requests based on python-twitter api.'
	api=None;
        lastid=None;
	def __init__(self,cKey,cSecret,atKey,atSecret):
		self.api=twitter.Api(consumer_key=cKey,
consumer_secret=cSecret, access_token_key=atKey, access_token_secret=atSecret)
		
        def getMentions(self,lastid=None):
		''' Get mentions of user '''
            self.lastID=self.getLastFetchedTweetID()
            #pretty much rubbish but anyway...
            if(self.lastID is not None):
                mentionsList=self.api.GetMentions(count=200,since_id=lastid,max_id=None,trim_user=False,contributor_details=False,include_entities=True)
            else:
                mentionsList=self.api.GetMentions(count=20,since_id=None,max_id=None,trim_user=False,contributor_details=False,include_entities=True)
                self.lastID=self.setLastFetchedTweetID(mentionsList)
            return mentionsList
    
        def post(self,message,reply):
		''' Post Tweet '''
			status=message
			try:
				self.api.PostUpdate(status, in_reply_to_status_id=reply, latitude=None, longitude=None, place_id=None, display_coordinates=False, trim_user=False)
			except twitter.TwitterError as e:
				if e.code==185:
					print ("rate limited")
					time.sleep(60*60)#sleeping for an hour
        
        def setLastFetchedTweetID(self,tweetsList):
		''' Set a tweetID to avoid cursoring'''
		higher=tweetsList.__len__()
		if higher-1>=0:
			self.lastid=tweetsList[higher-1].id
            
        def getLastFetchedTweetID(self):
		''' Get a tweetID to avoid cursoring'''
		return self.lastid
