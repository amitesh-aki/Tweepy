from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import twitter_credentials
import json
import MySQLdb

db = MySQLdb.connect(host = "localhost",
					 user = "root",
					 passwd = "Rootno3333",
					 db = "twitter_api"
					 )

class StdOutListener(StreamListener):

	def on_data(self,data):
		cur = db.cursor()
		print(data)
		sql = "INSERT INTO tweepy(data) VALUES(%s)"
		cur.execute(sql,[data])
		db.commit()
		return True

	def on_error(self,status):
		print(status)

if __name__ == "__main__":

	lisener = StdOutListener()
	auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
	auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)

	stream = Stream(auth,lisener)

	stream.filter(track=['Donald Trump', 'Hillary Clinton', 'BBC', 'CNN', 'Al Jazeera'])

db.close()