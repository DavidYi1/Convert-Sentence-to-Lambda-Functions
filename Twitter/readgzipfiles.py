import gzip
f = gzip.open('Tweets\case\opioid_2015-06-07-16-14', 'rb')
tweetsdata = open('Tweets\case\cases','w')
tweetsdata.writelines(f)
f.close()
tweetsdata.close