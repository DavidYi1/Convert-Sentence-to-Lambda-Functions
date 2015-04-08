from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json 


#consumer key, consumer secret, access token, access secret.
ckey="XbVzBf820RxReoxMtpe39FpuZ"
csecret="7G5jeyow2znuBvH3PDY2GnInjMl1T3z5uymCrOSxmDygDqnPdD"
atoken="378750618-gAnqXjTEfn5kPYyHMDSQxHE2apd1O8pR8qlbe5Yu"
asecret="gE12ID1pHOemqtONwNj5Dho6V9tDongeFW1GEZ2aDVmyT"

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
print(twitterStream.filter(track=["weed"]))
