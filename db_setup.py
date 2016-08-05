# Script to set up tcount and Tweetwordcount in postgres using psycopg2

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

conn = psycopg2.connect(database="postgres", user="postgres", password="pass", host="localhost", port="5432")
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cur = conn.cursor()

# creating data base
try:
    cur.execute("CREATE DATABASE tcount")
	conn.commit()
except:
    print "Could not create Tcount"​

conn.close()

# creating table
conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()

try:
	cur.execute('''CREATE TABLE Tweetwordcount
		(word TEXT PRIMARY KEY     NOT NULL,
       	count INT     NOT NULL);''')
	conn.commit()
except:
	print "Could not create Tweetwordcount"​

conn.close()