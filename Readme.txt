# Exercise_2 instructions
### How to run this Twitter wordcount application

#### Set up the machine
1. Create an Amazon EC2 instance and install streamparse and lein on it. 
2. Make sure that python 2.7 is the default Python version
3. Install psycopg2 by running: pip install psycopg2
4. Install tweepy by running: pip install tweepy
5. Import all files in exercise_2 folder from github:
    git clone https://github.com/mpera/exercise_2

#### Set up postgres database
1. Make sure that port 5432 is open on the instance
2. Make sure that postgres is running: ps auxwww | grep postgres
    If not, run: /data/start_postgres.sh
3. Create Tcount database and Tweetwordcount table by running db_setup.py

#### Run the stream
1. Change directory to streaming app: cd tweetwordcount
2. Run streamparse: sparse run
3. Run for as long as you want (I did 10 minutes at the start of the Olympic games)

#### Get results from the database
1. To see all words and counts, run: python finalresults.py
2. To see the total count of a specific word, run: python finalresults.py <word>
3. To see all the words within a count range (eg, 2,5), run: python histogram.py <x,y>

#### Notes
To learn about the full architecture, see Architecture.pdf.  To see the app in action, see the Screenshots folder.  To see a histogram of the top 20 words during the first 10 minutes of the 2016 Olympic games, see Plot.png

