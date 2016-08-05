from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt
import psycopg2


class TweetCounter(Bolt):

	def initialize(self, conf, ctx):
		self.counts = Counter()
		self.redis = StrictRedis()

	def process(self, tup):
		word = tup.values[0]
		word = word.lower()
	    
	    # Increment the local count
		self.counts[word] += 1
		self.emit([word, str(self.counts[word])])
        
		# Connect to tcount database
		conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
		cur = conn.cursor()
		
		# Inserts the word if its the first time the word has appeared
		try:			
			cur.execute("INSERT INTO Tweetwordcount (word,count) VALUES (%s, 1);", (word,))
			conn.commit()
			
		# Updates the word with a new count if the word has appeared before	
		except:
			conn.commit()
			cur.execute("UPDATE Tweetwordcount SET count=%s WHERE word=%s;", (self.counts[word], word))
			conn.commit()				


        # Log the count - just to see the topology running
		self.log('%s: %d' % (word, self.counts[word]))
