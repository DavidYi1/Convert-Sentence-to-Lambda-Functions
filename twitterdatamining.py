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

    def on_data(self, data):
        all_data = json.loads(data)       
        tweet = all_data["text"]        
        username = all_data["user"]["screen_name"]
        print((username,tweet))
        return True

    def on_error(self, status):
        print (status)


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())

drugstream = twitterStream.filter(track=common_names_for_marijuana)
##drugtweets = open("drugtweets.txt","w")
##for tweet in drugstream:
##    drugtweets.write(tweet)
