# This script gets a word as an argument and returns the total number of word occurrences in the stream. For example:
# $ python finalresults.py hello
# $ Total number of occurences of “hello”: 10

# Running finalresults.py without an argument returns all the words in the stream and their total count of occurrences, sorted alphabetically in an ascending order, one word per line. For example:
# $ python finalresults.py
# $ (<word1>, 2), (<word2>, 8), (<word3>, 6), (<word4>, 1), 

# Connect to postgres on the instance first 

import psycopg2
import sys # for argv; sys.argv[1] is the word passed to the script

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()

try:
	word = str(sys.argv[1]).lower()  # pulls word if given as an argument
	cur.execute("SELECT word, count from Tweetwordcount WHERE word=%s;", (word,))
	rec = cur.fetchone()
	print "Total number of occurences of '%s': %s" % (word, rec[1])
		
except:	
	cur.execute("SELECT word, count from Tweetwordcount;")
	rec = cur.fetchall()
	# Sorting numerically
	rec_numeric = sorted(rec, key=lambda x:(x[1]))
	# Sorting alphabetically
	final = sorted(rec_numeric, key=lambda x:(x[0][0]))
	
	# Printing one word per line
	numfinal = range(0, len(final))
	for num in numfinal:
		print "%s: %s" % (final[num][0], final[num][1])

conn.close()
		
