from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json 
from pprint import pprint

data_file = open('twitter.json')  
data = json.load(data_file)
##Json file with all the ckey, csecret, atoken, and asecret
pprint(data)


common_names_for_marijuana = ["Marijuana", "Marihuana", "pot", "weed"]
#consumer key, consumer secret, access token, access secret.
ckey = data['twitter']["consumer_key"]
csecret = data['twitter']["consumer_secret"]
atoken = data['twitter']["access_token"]
asecret = data['twitter']["access_token_secret"]

class listener(StreamListener):
    def on_data(self, data):
        print(data)
        return(True)

    def on_error(self, status):
        print status
'''
    #def __init__(self, api=None, path=None):
        #I don't remember exactly why I defined this.
        #self.api = api
        #We'll need this later.
        #self.path = path
        #self.x_count = 1
    
    #def on_data(self, data):
        #       
        #tweet = all_data["text"]        
        #username = all_data["user"]["screen_name"]
        #print((username,tweet))
        #with open("marjiuana based tweets.txt" ,"a") as fid:
            fid.write(tweet+"\n")
        self.x_count += 1 
        print (self.x_count)
        return True

    #def on_error(self, status):
        print (status)
'''

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())


try:
    print(twitterStream.filter(track=common_names_for_marijuana))
except (RuntimeError):
    pass
