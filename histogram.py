# This script gets two integers k1,k2 and returns all the words that their total number of occurrences in the stream is more or equal than k1 and less or equal than k2. For example:
#$ python histogram.py 3,8
#$ <word2>: 8
#<word3>: 6
#<word1>: 3

import sys
import psycopg2

# Storing histogram integers 
num1 = int(sys.argv[1][0])
num2 = int(sys.argv[1][2]) + 1

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()

# Gets all records in number range and stores output in rec
histlist = range(num1, num2)
cur.execute('SELECT word, count FROM Tweetwordcount WHERE count = ANY(%s)', (histlist,))
rec = cur.fetchall()

# Prints output in "<word2>: 8" fashion
numrec = range(0, len(rec))
for num in numrec:
	print "%s: %s" % (rec[num][0], rec[num][1])
