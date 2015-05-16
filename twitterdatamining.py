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
ckey = data["ckey"]
csecret = data["csecret"]
atoken = data["atoken"]
asecret = data["asecret"]

class listener(StreamListener):
    
    def __init__(self, api=None, path=None):
        #I don't remember exactly why I defined this.
        self.api = api
        #We'll need this later.
        self.path = path
        self.x_count = 1
    
    def on_data(self, data):
        all_data = json.loads(data)       
        tweet = all_data["text"]        
        username = all_data["user"]["screen_name"]
        print((username,tweet))
        with open("marjiuana based tweets.txt" ,"a") as fid:
            fid.write(tweet+"\n")
        self.x_count += 1 
        print (self.x_count)
        return True

    def on_error(self, status):
        print (status)


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())


try:
    print(twitterStream.filter(track=common_names_for_marijuana))
except (RuntimeError):
    pass
