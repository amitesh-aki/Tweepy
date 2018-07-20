# -*- coding: utf-8 -*-
import unicodedata
import json
import MySQLdb

db = MySQLdb.connect(host = "localhost",
					 user = "root",
					 passwd = "Rootno3333",
					 db = "twitter_api",
					 use_unicode=True, charset="utf8"
					 )

def readOne():
	cur = db.cursor()
	sql = "SELECT * FROM tweepy WHERE retrieved = 0 ORDER BY id ASC LIMIT 1"
	cur.execute(sql)
	return cur.fetchone()

def insertTweet(id, text):
	cur = db.cursor()
	sql = "INSERT INTO tweet(`id`, `text`) value(%s,%s)"
	cur.execute(sql, [id, text]);
	return db.commit()	

def updateRetrieveStatus(id):
	cur = db.cursor()
	sql = "UPDATE tweepy SET retrieved = 1 WHERE id = %s"
	cur.execute(sql, [id])
	return db.commit()	

if __name__ == "__main__":
	row = readOne()
	id = row[0]
	json = json.loads(row[1]);
	tweet_id = int(json['id'])
	text = bytes(json['text'], 'utf-8').decode('utf-8', 'ignore')
	insertTweet(tweet_id, text)
	updateRetrieveStatus(id)

db.close()