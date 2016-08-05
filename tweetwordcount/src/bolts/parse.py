Last login: Fri Aug  5 14:09:37 on ttys002
~ > cd Downloads/
Downloads >ssh -i "Pera.pem" root@ec2-54-86-153-245.compute-1.amazonaws.com
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
Someone could be eavesdropping on you right now (man-in-the-middle attack)!
It is also possible that a host key has just been changed.
The fingerprint for the RSA key sent by the remote host is
SHA256:9AX4NGQ4aHmvxjZF6cXebmiLk43uL4pWLLWzckAG6Bs.
Please contact your system administrator.
Add correct host key in /Users/megan/.ssh/known_hosts to get rid of this message.
Offending RSA key in /Users/megan/.ssh/known_hosts:54
RSA host key for ec2-54-86-153-245.compute-1.amazonaws.com has changed and you have requested strict checking.
Host key verification failed.
Downloads > chmod 400 Pera.pem
Downloads > ssh -i "Pera.pem" root@ec2-54-86-153-245.compute-1.amazonaws.com
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
Someone could be eavesdropping on you right now (man-in-the-middle attack)!
It is also possible that a host key has just been changed.
The fingerprint for the RSA key sent by the remote host is
SHA256:9AX4NGQ4aHmvxjZF6cXebmiLk43uL4pWLLWzckAG6Bs.
Please contact your system administrator.
Add correct host key in /Users/megan/.ssh/known_hosts to get rid of this message.
Offending RSA key in /Users/megan/.ssh/known_hosts:54
RSA host key for ec2-54-86-153-245.compute-1.amazonaws.com has changed and you have requested strict checking.
Host key verification failed.
Downloads > chmod 400 Pera.pem
Downloads >ssh -i "Pera.pem" root@ec2-52-87-217-103.compute-1.amazonaws.com
The authenticity of host 'ec2-52-87-217-103.compute-1.amazonaws.com (52.87.217.103)' can't be established.
RSA key fingerprint is SHA256:35xjINeYN9dLD1VSJFvj6G3fHiaEoiIp3uouzLUl+KQ.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added 'ec2-52-87-217-103.compute-1.amazonaws.com,52.87.217.103' (RSA) to the list of known hosts.
Last login: Fri Aug  5 18:21:49 2016 from 207.118.223.198
     ___   _        __   __   ____            __    
    / _ \ (_)___ _ / /  / /_ / __/____ ___ _ / /___ 
   / , _// // _ `// _ \/ __/_\ \ / __// _ `// // -_)
  /_/|_|/_/ \_, //_//_/\__//___/ \__/ \_,_//_/ \__/ 
           /___/                                                 
                                              
Welcome to a virtual machine image brought to you by RightScale!


[root@ip-172-31-4-51 ~]# fdisk -l

Disk /dev/xvda1: 32.2 GB, 32212254720 bytes
255 heads, 63 sectors/track, 3916 cylinders
Units = cylinders of 16065 * 512 = 8225280 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk identifier: 0x00000000


Disk /dev/xvdb: 4289 MB, 4289200128 bytes
255 heads, 63 sectors/track, 521 cylinders
Units = cylinders of 16065 * 512 = 8225280 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk identifier: 0x00000000


Disk /dev/xvdf: 107.4 GB, 107374182400 bytes
255 heads, 63 sectors/track, 13054 cylinders
Units = cylinders of 16065 * 512 = 8225280 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk identifier: 0x00000000

[root@ip-172-31-4-51 ~]# mount -t ext4 /dev/xvdf /data
[root@ip-172-31-4-51 ~]# git clone https://github.com/mpera/exercise_2/tree/master
Initialized empty Git repository in /root/master/.git/
error: The requested URL returned error: 403 Forbidden while accessing https://github.com/mpera/exercise_2/tree/master/info/refs

fatal: HTTP request failed
[root@ip-172-31-4-51 ~]# git clone https://github.com/mpera/exercise_2
Initialized empty Git repository in /root/exercise_2/.git/
remote: Counting objects: 67, done.
remote: Compressing objects: 100% (51/51), done.
remote: Total 67 (delta 22), reused 49 (delta 9), pack-reused 0
Unpacking objects: 100% (67/67), done.
[root@ip-172-31-4-51 ~]# ls -l
total 720
-rw-------  1 root root    287 Sep 22  2015 dans_bash_history.txt
drwxr-xr-x  4 root root   4096 Aug  5 19:53 exercise_2
-rw-r--r--  1 root root  12402 Jul 11 18:07 ez_setup.py
-rw-r--r--  1 root root    763 Aug  5 17:04 finalresults.py
-rw-r--r--  1 root root    446 Aug  5 16:38 histogram.py
drwxr-xr-x 11 root root   4096 May  4  2015 ipython
drwxr-xr-x  5 root root   4096 May  4  2015 pgxl-deployment-tools
-rw-r--r--  1 root root 655364 Jul 11 18:07 setuptools-24.0.2.zip
-rwxr-xr-x  1 root root    221 Sep 22  2015 start-hadoop.sh
-rwxr-xr-x  1 root root    252 Sep 22  2015 start-hadoop.sh~
-rwxr-xr-x  1 root root    209 Sep 22  2015 stop-hadoop.sh
-rwxr-xr-x  1 root root    222 Sep 22  2015 stop-hadoop.sh~
drwxr-xr-x 11 root root   4096 May  4  2015 streamparse
drwxr-xr-x  8 root root   4096 Jul 11 19:33 tweetcount
drwxr-xr-x  8 root root   4096 Aug  5 18:44 tweetwordcount
-rw-r--r--  1 root root    765 Jul 29 01:42 Twittercredentials.py
[root@ip-172-31-4-51 ~]# cd exercise_2/
[root@ip-172-31-4-51 exercise_2]# ls -l
total 20
-rw-r--r-- 1 root root  817 Aug  5 19:53 db_setup.py
-rw-r--r-- 1 root root 1384 Aug  5 19:53 finalresults.py
-rw-r--r-- 1 root root  826 Aug  5 19:53 histogram.py
-rw-r--r-- 1 root root 1157 Aug  5 19:53 README.md
drwxr-xr-x 5 root root 4096 Aug  5 19:53 tweetwordcount
[root@ip-172-31-4-51 exercise_2]# cd ..
[root@ip-172-31-4-51 ~]# cd ..
[root@ip-172-31-4-51 /]# ls -l
total 104
dr-xr-xr-x   2 root root  4096 Sep 28  2015 bin
dr-xr-xr-x   4 root root  4096 Mar 17  2015 boot
drwxrwxrwx  10 root root  4096 Jul 28 00:02 data
drwxr-xr-x  15 root root  3200 Aug  5 19:51 dev
drwxr-xr-x  88 root root  4096 Aug  5 19:53 etc
drwxr-xr-x   7 root root  4096 Sep 22  2015 home
dr-xr-xr-x  11 root root  4096 May  4  2015 lib
dr-xr-xr-x   9 root root 12288 May  4  2015 lib64
drwx------   2 root root 16384 Mar 17  2015 lost+found
drwxr-xr-x   2 root root  4096 Sep 23  2011 media
drwxr-xr-x   2 root root  4096 Sep 23  2011 mnt
drwxr-xr-x   5 root root  4096 May  4  2015 opt
dr-xr-xr-x  76 root root     0 Aug  5 19:51 proc
dr-xr-x---  17 root root  4096 Aug  5 19:53 root
dr-xr-xr-x   2 root root 12288 Sep 28  2015 sbin
drwxr-xr-x   7 root root     0 Aug  5 19:51 selinux
-rw-r--r--   1 root root     0 Jul 11 19:05 sentences.py
drwxr-xr-x   2 root root  4096 Sep 23  2011 srv
drwxr-xr-x  13 root root     0 Aug  5 19:51 sys
drwxrwxrwt 176 root root 12288 Aug  5 19:52 tmp
drwxr-xr-x  15 root root  4096 May  4  2015 usr
drwxr-xr-x  19 root root  4096 Mar 17  2015 var
[root@ip-172-31-4-51 /]# cd /data
[root@ip-172-31-4-51 data]# ls -l
total 688
drwxr-xr-x 5 root     root     4096 Jul 27 23:51 api
-rw-r--r-- 1 root     root     1642 Dec 14  2015 api_building_app.py
drwxrwxr-x 3 w205     w205     4096 Jul 28 00:13 dvd_api
drwxr-xr-x 3 hadoop   hadoop   4096 Jun 11 04:02 hadoop
drwxr-xr-x 3 hdfs     hdfs     4096 Jun 11 03:55 hadoop-hdfs
drwxr-xr-x 4 yarn     yarn     4096 Jun 11 03:56 hadoop-yarn
drwx------ 2 root     root    16384 Jun 11 03:54 lost+found
drwxr-xr-x 2 root     root     4096 Mar 23  2008 pagila-0.10.1
-rw-r--r-- 1 root     root   633143 Jun 11 04:04 pagila.zip
drwxr-xr-x 4 postgres root     4096 Jun 11 04:01 pgsql
-rw-r--r-- 1 root     root       50 Jul 27 23:45 requirements.txt
-rw-r--r-- 1 root     root      535 Jun 11 04:02 setup_hive_for_postgres.sql
-rwxr-xr-x 1 root     root      732 Jun 11 04:02 setup_zeppelin.sh
-rwxr-xr-x 1 root     root       93 Jun 11 04:02 start_postgres.sh
-rwxr-xr-x 1 root     root       92 Jun 11 04:02 stop_postgres.sh
[root@ip-172-31-4-51 data]# cd ..
[root@ip-172-31-4-51 /]# cd /exercise_2
-bash: cd: /exercise_2: No such file or directory
[root@ip-172-31-4-51 /]# ls -l
total 104
dr-xr-xr-x   2 root root  4096 Sep 28  2015 bin
dr-xr-xr-x   4 root root  4096 Mar 17  2015 boot
drwxrwxrwx  10 root root  4096 Jul 28 00:02 data
drwxr-xr-x  15 root root  3200 Aug  5 19:51 dev
drwxr-xr-x  88 root root  4096 Aug  5 19:53 etc
drwxr-xr-x   7 root root  4096 Sep 22  2015 home
dr-xr-xr-x  11 root root  4096 May  4  2015 lib
dr-xr-xr-x   9 root root 12288 May  4  2015 lib64
drwx------   2 root root 16384 Mar 17  2015 lost+found
drwxr-xr-x   2 root root  4096 Sep 23  2011 media
drwxr-xr-x   2 root root  4096 Sep 23  2011 mnt
drwxr-xr-x   5 root root  4096 May  4  2015 opt
dr-xr-xr-x  76 root root     0 Aug  5 19:51 proc
dr-xr-x---  17 root root  4096 Aug  5 19:53 root
dr-xr-xr-x   2 root root 12288 Sep 28  2015 sbin
drwxr-xr-x   7 root root     0 Aug  5 19:51 selinux
-rw-r--r--   1 root root     0 Jul 11 19:05 sentences.py
drwxr-xr-x   2 root root  4096 Sep 23  2011 srv
drwxr-xr-x  13 root root     0 Aug  5 19:51 sys
drwxrwxrwt 176 root root 12288 Aug  5 19:52 tmp
drwxr-xr-x  15 root root  4096 May  4  2015 usr
drwxr-xr-x  19 root root  4096 Mar 17  2015 var
[root@ip-172-31-4-51 /]# cd too
-bash: cd: too: No such file or directory
[root@ip-172-31-4-51 /]# cd root
[root@ip-172-31-4-51 ~]# ls -l
total 720
-rw-------  1 root root    287 Sep 22  2015 dans_bash_history.txt
drwxr-xr-x  4 root root   4096 Aug  5 19:53 exercise_2
-rw-r--r--  1 root root  12402 Jul 11 18:07 ez_setup.py
-rw-r--r--  1 root root    763 Aug  5 17:04 finalresults.py
-rw-r--r--  1 root root    446 Aug  5 16:38 histogram.py
drwxr-xr-x 11 root root   4096 May  4  2015 ipython
drwxr-xr-x  5 root root   4096 May  4  2015 pgxl-deployment-tools
-rw-r--r--  1 root root 655364 Jul 11 18:07 setuptools-24.0.2.zip
-rwxr-xr-x  1 root root    221 Sep 22  2015 start-hadoop.sh
-rwxr-xr-x  1 root root    252 Sep 22  2015 start-hadoop.sh~
-rwxr-xr-x  1 root root    209 Sep 22  2015 stop-hadoop.sh
-rwxr-xr-x  1 root root    222 Sep 22  2015 stop-hadoop.sh~
drwxr-xr-x 11 root root   4096 May  4  2015 streamparse
drwxr-xr-x  8 root root   4096 Jul 11 19:33 tweetcount
drwxr-xr-x  8 root root   4096 Aug  5 18:44 tweetwordcount
-rw-r--r--  1 root root    765 Jul 29 01:42 Twittercredentials.py
[root@ip-172-31-4-51 ~]# cd exercise_2/
[root@ip-172-31-4-51 exercise_2]# cd tweetwordcount/
[root@ip-172-31-4-51 tweetwordcount]# sparse run
Running tweetwordcount topology...
Routing Python logging to /root/exercise_2/tweetwordcount/logs.
Running lein command to run local cluster:
lein run -m streamparse.commands.run/-main topologies/tweetwordcount.clj -t 0 --option 'topology.workers=2' --option 'topology.acker.executors=2' --option 'streamparse.log.path="/root/exercise_2/tweetwordcount/logs"' --option 'streamparse.log.level="debug"'
WARNING: You're currently running as root; probably by accident.
Press control-C to abort or Enter to continue as root.
Set LEIN_ROOT to disable this warning.
Traceback (most recent call last):
  File "/usr/bin/sparse", line 9, in <module>
    load_entry_point('streamparse==2.1.4', 'console_scripts', 'sparse')()
  File "/usr/lib/python2.7/site-packages/streamparse/cli/sparse.py", line 57, in main
    args.func(args)
  File "/usr/lib/python2.7/site-packages/streamparse/cli/run.py", line 81, in main
    debug=args.debug)
  File "/usr/lib/python2.7/site-packages/streamparse/cli/run.py", line 52, in run_local_topology
    run(full_cmd)
  File "/usr/lib/python2.7/site-packages/invoke/__init__.py", line 32, in run
    return Context().run(command, **kwargs)
  File "/usr/lib/python2.7/site-packages/invoke/context.py", line 53, in run
    return runner_class(context=self).run(command, **kwargs)
  File "/usr/lib/python2.7/site-packages/invoke/runners.py", line 335, in run
    raise exception
KeyboardInterrupt
[root@ip-172-31-4-51 tweetwordcount]# cd ..
[root@ip-172-31-4-51 exercise_2]# cd ..
[root@ip-172-31-4-51 ~]# ps auxwww | grep postgres
root      3061  0.0  0.0 103248   832 pts/1    S+   19:56   0:00 grep postgres
[root@ip-172-31-4-51 ~]# /data/start_postgres.sh
could not change directory to "/root"
server starting
[root@ip-172-31-4-51 ~]# cd exercise_2/
[root@ip-172-31-4-51 exercise_2]# vi db_setup.py 
[root@ip-172-31-4-51 exercise_2]# cd ..
[root@ip-172-31-4-51 ~]# rm -rf exercise_2/
[root@ip-172-31-4-51 ~]# ls -l
total 716
-rw-------  1 root root    287 Sep 22  2015 dans_bash_history.txt
-rw-r--r--  1 root root  12402 Jul 11 18:07 ez_setup.py
-rw-r--r--  1 root root    763 Aug  5 17:04 finalresults.py
-rw-r--r--  1 root root    446 Aug  5 16:38 histogram.py
drwxr-xr-x 11 root root   4096 May  4  2015 ipython
drwxr-xr-x  5 root root   4096 May  4  2015 pgxl-deployment-tools
-rw-r--r--  1 root root 655364 Jul 11 18:07 setuptools-24.0.2.zip
-rwxr-xr-x  1 root root    221 Sep 22  2015 start-hadoop.sh
-rwxr-xr-x  1 root root    252 Sep 22  2015 start-hadoop.sh~
-rwxr-xr-x  1 root root    209 Sep 22  2015 stop-hadoop.sh
-rwxr-xr-x  1 root root    222 Sep 22  2015 stop-hadoop.sh~
drwxr-xr-x 11 root root   4096 May  4  2015 streamparse
drwxr-xr-x  8 root root   4096 Jul 11 19:33 tweetcount
drwxr-xr-x  8 root root   4096 Aug  5 18:44 tweetwordcount
-rw-r--r--  1 root root    765 Jul 29 01:42 Twittercredentials.py
[root@ip-172-31-4-51 ~]# git clone https://github.com/mpera/exercise_2
Initialized empty Git repository in /root/exercise_2/.git/
remote: Counting objects: 73, done.
remote: Compressing objects: 100% (57/57), done.
remote: Total 73 (delta 25), reused 49 (delta 9), pack-reused 0
Unpacking objects: 100% (73/73), done.
[root@ip-172-31-4-51 ~]# ls -l
total 720
-rw-------  1 root root    287 Sep 22  2015 dans_bash_history.txt
drwxr-xr-x  4 root root   4096 Aug  5 20:01 exercise_2
-rw-r--r--  1 root root  12402 Jul 11 18:07 ez_setup.py
-rw-r--r--  1 root root    763 Aug  5 17:04 finalresults.py
-rw-r--r--  1 root root    446 Aug  5 16:38 histogram.py
drwxr-xr-x 11 root root   4096 May  4  2015 ipython
drwxr-xr-x  5 root root   4096 May  4  2015 pgxl-deployment-tools
-rw-r--r--  1 root root 655364 Jul 11 18:07 setuptools-24.0.2.zip
-rwxr-xr-x  1 root root    221 Sep 22  2015 start-hadoop.sh
-rwxr-xr-x  1 root root    252 Sep 22  2015 start-hadoop.sh~
-rwxr-xr-x  1 root root    209 Sep 22  2015 stop-hadoop.sh
-rwxr-xr-x  1 root root    222 Sep 22  2015 stop-hadoop.sh~
drwxr-xr-x 11 root root   4096 May  4  2015 streamparse
drwxr-xr-x  8 root root   4096 Jul 11 19:33 tweetcount
drwxr-xr-x  8 root root   4096 Aug  5 18:44 tweetwordcount
-rw-r--r--  1 root root    765 Jul 29 01:42 Twittercredentials.py
[root@ip-172-31-4-51 ~]# cd exercise_2/
[root@ip-172-31-4-51 exercise_2]# ls -l
total 20
-rw-r--r-- 1 root root  812 Aug  5 20:01 db_setup.py
-rw-r--r-- 1 root root 1384 Aug  5 20:01 finalresults.py
-rw-r--r-- 1 root root  826 Aug  5 20:01 histogram.py
-rw-r--r-- 1 root root 1145 Aug  5 20:01 README.md
drwxr-xr-x 5 root root 4096 Aug  5 20:01 tweetwordcount
[root@ip-172-31-4-51 exercise_2]# vi db_setup.py 
[root@ip-172-31-4-51 exercise_2]# python db_setup.py 
Could not create Tcount
Could not create Tweetwordcount
[root@ip-172-31-4-51 exercise_2]# cd tweetwordcount/
[root@ip-172-31-4-51 tweetwordcount]# sparse run
Running tweetwordcount topology...
Routing Python logging to /root/exercise_2/tweetwordcount/logs.
Running lein command to run local cluster:
lein run -m streamparse.commands.run/-main topologies/tweetwordcount.clj -t 0 --option 'topology.workers=2' --option 'topology.acker.executors=2' --option 'streamparse.log.path="/root/exercise_2/tweetwordcount/logs"' --option 'streamparse.log.level="debug"'
WARNING: You're currently running as root; probably by accident.
Press control-C to abort or Enter to continue as root.
Set LEIN_ROOT to disable this warning.

4039 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:zookeeper.version=3.4.6-1569965, built on 02/20/2014 09:09 GMT
4052 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:host.name=ip-172-31-4-51.ec2.internal
4052 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:java.version=1.7.0_79
4052 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:java.vendor=Oracle Corporation
4052 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:java.home=/opt/jdk1.7.0_79/jre
4052 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:java.class.path=/root/exercise_2/tweetwordcount/test:/root/exercise_2/tweetwordcount/topologies:/root/exercise_2/tweetwordcount/dev-resources:/root/exercise_2/tweetwordcount/_resources:/root/exercise_2/tweetwordcount/_build/classes:/root/.m2/repository/ch/qos/logback/logback-classic/1.0.13/logback-classic-1.0.13.jar:/root/.m2/repository/org/clojure/tools.macro/0.1.0/tools.macro-0.1.0.jar:/root/.m2/repository/ring/ring-core/1.1.5/ring-core-1.1.5.jar:/root/.m2/repository/hiccup/hiccup/0.3.6/hiccup-0.3.6.jar:/root/.m2/repository/ring/ring-servlet/0.3.11/ring-servlet-0.3.11.jar:/root/.m2/repository/com/googlecode/json-simple/json-simple/1.1/json-simple-1.1.jar:/root/.m2/repository/org/clojure/math.numeric-tower/0.0.1/math.numeric-tower-0.0.1.jar:/root/.m2/repository/clj-time/clj-time/0.4.1/clj-time-0.4.1.jar:/root/.m2/repository/org/objenesis/objenesis/1.2/objenesis-1.2.jar:/root/.m2/repository/com/twitter/chill-java/0.3.5/chill-java-0.3.5.jar:/root/.m2/repository/com/parsely/streamparse/0.0.4-SNAPSHOT/streamparse-0.0.4-SNAPSHOT.jar:/root/.m2/repository/ring/ring-jetty-adapter/0.3.11/ring-jetty-adapter-0.3.11.jar:/root/.m2/repository/jline/jline/2.11/jline-2.11.jar:/root/.m2/repository/clj-stacktrace/clj-stacktrace/0.2.2/clj-stacktrace-0.2.2.jar:/root/.m2/repository/org/clojure/tools.nrepl/0.2.12/tools.nrepl-0.2.12.jar:/root/.m2/repository/org/slf4j/slf4j-api/1.7.5/slf4j-api-1.7.5.jar:/root/.m2/repository/ring/ring-devel/0.3.11/ring-devel-0.3.11.jar:/root/.m2/repository/org/mortbay/jetty/jetty-util/6.1.26/jetty-util-6.1.26.jar:/root/.m2/repository/javax/servlet/servlet-api/2.5/servlet-api-2.5.jar:/root/.m2/repository/clojure-complete/clojure-complete/0.2.4/clojure-complete-0.2.4.jar:/root/.m2/repository/org/yaml/snakeyaml/1.11/snakeyaml-1.11.jar:/root/.m2/repository/ch/qos/logback/logback-core/1.0.13/logback-core-1.0.13.jar:/root/.m2/repository/commons-lang/commons-lang/2.5/commons-lang-2.5.jar:/root/.m2/repository/org/mortbay/jetty/jetty/6.1.26/jetty-6.1.26.jar:/root/.m2/repository/joda-time/joda-time/2.0/joda-time-2.0.jar:/root/.m2/repository/commons-io/commons-io/2.4/commons-io-2.4.jar:/root/.m2/repository/commons-logging/commons-logging/1.1.3/commons-logging-1.1.3.jar:/root/.m2/repository/com/esotericsoftware/kryo/kryo/2.21/kryo-2.21.jar:/root/.m2/repository/com/esotericsoftware/minlog/minlog/1.2/minlog-1.2.jar:/root/.m2/repository/org/apache/storm/storm-core/0.9.5/storm-core-0.9.5.jar:/root/.m2/repository/compojure/compojure/1.1.3/compojure-1.1.3.jar:/root/.m2/repository/com/esotericsoftware/reflectasm/reflectasm/1.07/reflectasm-1.07-shaded.jar:/root/.m2/repository/com/twitter/carbonite/1.4.0/carbonite-1.4.0.jar:/root/.m2/repository/commons-codec/commons-codec/1.6/commons-codec-1.6.jar:/root/.m2/repository/commons-fileupload/commons-fileupload/1.2.1/commons-fileupload-1.2.1.jar:/root/.m2/repository/org/clojure/data.json/0.2.6/data.json-0.2.6.jar:/root/.m2/repository/org/slf4j/log4j-over-slf4j/1.6.6/log4j-over-slf4j-1.6.6.jar:/root/.m2/repository/org/jgrapht/jgrapht-core/0.9.0/jgrapht-core-0.9.0.jar:/root/.m2/repository/org/clojure/clojure/1.5.1/clojure-1.5.1.jar:/root/.m2/repository/org/clojure/tools.logging/0.2.3/tools.logging-0.2.3.jar:/root/.m2/repository/org/ow2/asm/asm/4.0/asm-4.0.jar:/root/.m2/repository/clout/clout/1.0.1/clout-1.0.1.jar:/root/.m2/repository/org/apache/commons/commons-exec/1.1/commons-exec-1.1.jar:/root/.m2/repository/com/googlecode/disruptor/disruptor/2.10.1/disruptor-2.10.1.jar:/root/.m2/repository/org/clojure/core.incubator/0.1.0/core.incubator-0.1.0.jar:/root/.m2/repository/org/clojure/tools.cli/0.2.4/tools.cli-0.2.4.jar
4053 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:java.library.path=/usr/java/packages/lib/amd64:/usr/lib64:/lib64:/lib:/usr/lib
4053 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:java.io.tmpdir=/tmp
4053 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:java.compiler=<NA>
4053 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:os.name=Linux
4053 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:os.arch=amd64
4053 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:os.version=2.6.32-504.12.2.el6.centos.plus.x86_64
4054 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:user.name=root
4054 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:user.home=/root
4054 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:user.dir=/root/exercise_2/tweetwordcount
4082 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:zookeeper.version=3.4.6-1569965, built on 02/20/2014 09:09 GMT
4083 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:host.name=ip-172-31-4-51.ec2.internal
4083 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:java.version=1.7.0_79
4083 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:java.vendor=Oracle Corporation
4083 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:java.home=/opt/jdk1.7.0_79/jre
4083 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:java.class.path=/root/exercise_2/tweetwordcount/test:/root/exercise_2/tweetwordcount/topologies:/root/exercise_2/tweetwordcount/dev-resources:/root/exercise_2/tweetwordcount/_resources:/root/exercise_2/tweetwordcount/_build/classes:/root/.m2/repository/ch/qos/logback/logback-classic/1.0.13/logback-classic-1.0.13.jar:/root/.m2/repository/org/clojure/tools.macro/0.1.0/tools.macro-0.1.0.jar:/root/.m2/repository/ring/ring-core/1.1.5/ring-core-1.1.5.jar:/root/.m2/repository/hiccup/hiccup/0.3.6/hiccup-0.3.6.jar:/root/.m2/repository/ring/ring-servlet/0.3.11/ring-servlet-0.3.11.jar:/root/.m2/repository/com/googlecode/json-simple/json-simple/1.1/json-simple-1.1.jar:/root/.m2/repository/org/clojure/math.numeric-tower/0.0.1/math.numeric-tower-0.0.1.jar:/root/.m2/repository/clj-time/clj-time/0.4.1/clj-time-0.4.1.jar:/root/.m2/repository/org/objenesis/objenesis/1.2/objenesis-1.2.jar:/root/.m2/repository/com/twitter/chill-java/0.3.5/chill-java-0.3.5.jar:/root/.m2/repository/com/parsely/streamparse/0.0.4-SNAPSHOT/streamparse-0.0.4-SNAPSHOT.jar:/root/.m2/repository/ring/ring-jetty-adapter/0.3.11/ring-jetty-adapter-0.3.11.jar:/root/.m2/repository/jline/jline/2.11/jline-2.11.jar:/root/.m2/repository/clj-stacktrace/clj-stacktrace/0.2.2/clj-stacktrace-0.2.2.jar:/root/.m2/repository/org/clojure/tools.nrepl/0.2.12/tools.nrepl-0.2.12.jar:/root/.m2/repository/org/slf4j/slf4j-api/1.7.5/slf4j-api-1.7.5.jar:/root/.m2/repository/ring/ring-devel/0.3.11/ring-devel-0.3.11.jar:/root/.m2/repository/org/mortbay/jetty/jetty-util/6.1.26/jetty-util-6.1.26.jar:/root/.m2/repository/javax/servlet/servlet-api/2.5/servlet-api-2.5.jar:/root/.m2/repository/clojure-complete/clojure-complete/0.2.4/clojure-complete-0.2.4.jar:/root/.m2/repository/org/yaml/snakeyaml/1.11/snakeyaml-1.11.jar:/root/.m2/repository/ch/qos/logback/logback-core/1.0.13/logback-core-1.0.13.jar:/root/.m2/repository/commons-lang/commons-lang/2.5/commons-lang-2.5.jar:/root/.m2/repository/org/mortbay/jetty/jetty/6.1.26/jetty-6.1.26.jar:/root/.m2/repository/joda-time/joda-time/2.0/joda-time-2.0.jar:/root/.m2/repository/commons-io/commons-io/2.4/commons-io-2.4.jar:/root/.m2/repository/commons-logging/commons-logging/1.1.3/commons-logging-1.1.3.jar:/root/.m2/repository/com/esotericsoftware/kryo/kryo/2.21/kryo-2.21.jar:/root/.m2/repository/com/esotericsoftware/minlog/minlog/1.2/minlog-1.2.jar:/root/.m2/repository/org/apache/storm/storm-core/0.9.5/storm-core-0.9.5.jar:/root/.m2/repository/compojure/compojure/1.1.3/compojure-1.1.3.jar:/root/.m2/repository/com/esotericsoftware/reflectasm/reflectasm/1.07/reflectasm-1.07-shaded.jar:/root/.m2/repository/com/twitter/carbonite/1.4.0/carbonite-1.4.0.jar:/root/.m2/repository/commons-codec/commons-codec/1.6/commons-codec-1.6.jar:/root/.m2/repository/commons-fileupload/commons-fileupload/1.2.1/commons-fileupload-1.2.1.jar:/root/.m2/repository/org/clojure/data.json/0.2.6/data.json-0.2.6.jar:/root/.m2/repository/org/slf4j/log4j-over-slf4j/1.6.6/log4j-over-slf4j-1.6.6.jar:/root/.m2/repository/org/jgrapht/jgrapht-core/0.9.0/jgrapht-core-0.9.0.jar:/root/.m2/repository/org/clojure/clojure/1.5.1/clojure-1.5.1.jar:/root/.m2/repository/org/clojure/tools.logging/0.2.3/tools.logging-0.2.3.jar:/root/.m2/repository/org/ow2/asm/asm/4.0/asm-4.0.jar:/root/.m2/repository/clout/clout/1.0.1/clout-1.0.1.jar:/root/.m2/repository/org/apache/commons/commons-exec/1.1/commons-exec-1.1.jar:/root/.m2/repository/com/googlecode/disruptor/disruptor/2.10.1/disruptor-2.10.1.jar:/root/.m2/repository/org/clojure/core.incubator/0.1.0/core.incubator-0.1.0.jar:/root/.m2/repository/org/clojure/tools.cli/0.2.4/tools.cli-0.2.4.jar
4083 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:java.library.path=/usr/java/packages/lib/amd64:/usr/lib64:/lib64:/lib:/usr/lib
4084 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:java.io.tmpdir=/tmp
4084 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:java.compiler=<NA>
4084 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:os.name=Linux
4084 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:os.arch=amd64
4084 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:os.version=2.6.32-504.12.2.el6.centos.plus.x86_64
4084 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:user.name=root
4084 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:user.home=/root
4085 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:user.dir=/root/exercise_2/tweetwordcount
5906 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Created server with tickTime 2000 minSessionTimeout 4000 maxSessionTimeout 40000 datadir /tmp/8f48dc84-f64b-4977-82f3-e5985a4ca806/version-2 snapdir /tmp/8f48dc84-f64b-4977-82f3-e5985a4ca806/version-2
5957 [main] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - binding to port 0.0.0.0/0.0.0.0:2000
5971 [main] INFO  backtype.storm.zookeeper - Starting inprocess zookeeper at port 2000 and dir /tmp/8f48dc84-f64b-4977-82f3-e5985a4ca806
6506 [main] INFO  backtype.storm.daemon.nimbus - Starting Nimbus with conf {"dev.zookeeper.path" "/tmp/dev-storm-zookeeper", "topology.tick.tuple.freq.secs" nil, "topology.builtin.metrics.bucket.size.secs" 60, "topology.fall.back.on.java.serialization" true, "topology.max.error.report.per.interval" 5, "zmq.linger.millis" 0, "topology.skip.missing.kryo.registrations" true, "storm.messaging.netty.client_worker_threads" 1, "ui.childopts" "-Xmx768m", "storm.zookeeper.session.timeout" 20000, "nimbus.reassign" true, "topology.trident.batch.emit.interval.millis" 50, "storm.messaging.netty.flush.check.interval.ms" 10, "nimbus.monitor.freq.secs" 10, "logviewer.childopts" "-Xmx128m", "java.library.path" "/usr/local/lib:/opt/local/lib:/usr/lib", "topology.executor.send.buffer.size" 1024, "storm.local.dir" "/tmp/a07dc6dc-f814-4184-ad13-936ef7ca3b13", "storm.messaging.netty.buffer_size" 5242880, "supervisor.worker.start.timeout.secs" 120, "topology.enable.message.timeouts" true, "nimbus.cleanup.inbox.freq.secs" 600, "nimbus.inbox.jar.expiration.secs" 3600, "drpc.worker.threads" 64, "storm.meta.serialization.delegate" "backtype.storm.serialization.DefaultSerializationDelegate", "topology.worker.shared.thread.pool.size" 4, "nimbus.host" "localhost", "storm.messaging.netty.min_wait_ms" 100, "storm.zookeeper.port" 2000, "transactional.zookeeper.port" nil, "topology.executor.receive.buffer.size" 1024, "transactional.zookeeper.servers" nil, "storm.zookeeper.root" "/storm", "storm.zookeeper.retry.intervalceiling.millis" 30000, "supervisor.enable" true, "storm.messaging.netty.server_worker_threads" 1, "storm.zookeeper.servers" ["localhost"], "transactional.zookeeper.root" "/transactional", "topology.acker.executors" nil, "topology.transfer.buffer.size" 1024, "topology.worker.childopts" nil, "drpc.queue.size" 128, "worker.childopts" "-Xmx768m", "supervisor.heartbeat.frequency.secs" 5, "topology.error.throttle.interval.secs" 10, "zmq.hwm" 0, "drpc.port" 3772, "supervisor.monitor.frequency.secs" 3, "drpc.childopts" "-Xmx768m", "topology.receiver.buffer.size" 8, "task.heartbeat.frequency.secs" 3, "topology.tasks" nil, "storm.messaging.netty.max_retries" 300, "topology.spout.wait.strategy" "backtype.storm.spout.SleepSpoutWaitStrategy", "nimbus.thrift.max_buffer_size" 1048576, "topology.max.spout.pending" nil, "storm.zookeeper.retry.interval" 1000, "topology.sleep.spout.wait.strategy.time.ms" 1, "nimbus.topology.validator" "backtype.storm.nimbus.DefaultTopologyValidator", "supervisor.slots.ports" [6700 6701 6702 6703], "topology.environment" nil, "topology.debug" false, "nimbus.task.launch.secs" 120, "nimbus.supervisor.timeout.secs" 60, "topology.message.timeout.secs" 30, "task.refresh.poll.secs" 10, "topology.workers" 1, "supervisor.childopts" "-Xmx256m", "nimbus.thrift.port" 6627, "topology.stats.sample.rate" 0.05, "worker.heartbeat.frequency.secs" 1, "topology.tuple.serializer" "backtype.storm.serialization.types.ListDelegateSerializer", "topology.disruptor.wait.strategy" "com.lmax.disruptor.BlockingWaitStrategy", "topology.multilang.serializer" "backtype.storm.multilang.JsonSerializer", "nimbus.task.timeout.secs" 30, "storm.zookeeper.connection.timeout" 15000, "topology.kryo.factory" "backtype.storm.serialization.DefaultKryoFactory", "drpc.invocations.port" 3773, "logviewer.port" 8000, "zmq.threads" 1, "storm.zookeeper.retry.times" 5, "topology.worker.receiver.thread.count" 1, "storm.thrift.transport" "backtype.storm.security.auth.SimpleTransportPlugin", "topology.state.synchronization.timeout.secs" 60, "supervisor.worker.timeout.secs" 30, "nimbus.file.copy.expiration.secs" 600, "storm.messaging.transport" "backtype.storm.messaging.netty.Context", "logviewer.appender.name" "A1", "storm.messaging.netty.max_wait_ms" 1000, "drpc.request.timeout.secs" 600, "storm.local.mode.zmq" false, "ui.port" 8080, "nimbus.childopts" "-Xmx1024m", "storm.cluster.mode" "local", "topology.max.task.parallelism" nil, "storm.messaging.netty.transfer.batch.size" 262144, "topology.classpath" nil}
6512 [main] INFO  backtype.storm.daemon.nimbus - Using default scheduler
6534 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
6795 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
6799 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000 sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@2fdf0598
6840 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
6853 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55497
6856 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
6871 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55497
6874 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.persistence.FileTxnLog - Creating new log file: log.1
6888 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c4c812e0000, negotiated timeout = 20000
6903 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c4c812e0000 with negotiated timeout 20000 for client /127.0.0.1:55497
6904 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
6906 [main-EventThread] INFO  backtype.storm.zookeeper - Zookeeper state update: :connected:none
7965 [ProcessThread(sid:0 cport:-1):] INFO  org.apache.storm.zookeeper.server.PrepRequestProcessor - Processed session termination for sessionid: 0x1565c4c812e0000
7967 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxn - Closed socket connection for client /127.0.0.1:55497 which had sessionid 0x1565c4c812e0000
7968 [main-EventThread] INFO  org.apache.storm.zookeeper.ClientCnxn - EventThread shut down
7977 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Session: 0x1565c4c812e0000 closed
7978 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
7981 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
7981 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000/storm sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@1c8c37d0
8000 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
8000 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
8000 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55498
8009 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55498
8011 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c4c812e0001 with negotiated timeout 20000 for client /127.0.0.1:55498
8011 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c4c812e0001, negotiated timeout = 20000
8012 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
8082 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
8083 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
8083 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000 sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@2ca59fc
8084 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
8085 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55499
8085 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
8085 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55499
8087 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c4c812e0002 with negotiated timeout 20000 for client /127.0.0.1:55499
8087 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c4c812e0002, negotiated timeout = 20000
8088 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
8088 [main-EventThread] INFO  backtype.storm.zookeeper - Zookeeper state update: :connected:none
8099 [ProcessThread(sid:0 cport:-1):] INFO  org.apache.storm.zookeeper.server.PrepRequestProcessor - Processed session termination for sessionid: 0x1565c4c812e0002
8100 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxn - Closed socket connection for client /127.0.0.1:55499 which had sessionid 0x1565c4c812e0002
8100 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Session: 0x1565c4c812e0002 closed
8101 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
8101 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
8101 [main-EventThread] INFO  org.apache.storm.zookeeper.ClientCnxn - EventThread shut down
8101 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000/storm sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@5332efbc
8102 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
8103 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55500
8103 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
8103 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55500
8105 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
8105 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
8106 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000 sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@49250068
8116 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c4c812e0003 with negotiated timeout 20000 for client /127.0.0.1:55500
8116 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c4c812e0003, negotiated timeout = 20000
8117 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
8117 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
8118 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55501
8118 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
8118 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55501
8120 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c4c812e0004 with negotiated timeout 20000 for client /127.0.0.1:55501
8120 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c4c812e0004, negotiated timeout = 20000
8120 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
8121 [main-EventThread] INFO  backtype.storm.zookeeper - Zookeeper state update: :connected:none
9123 [ProcessThread(sid:0 cport:-1):] INFO  org.apache.storm.zookeeper.server.PrepRequestProcessor - Processed session termination for sessionid: 0x1565c4c812e0004
9125 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Session: 0x1565c4c812e0004 closed
9125 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
9126 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
9126 [main-EventThread] INFO  org.apache.storm.zookeeper.ClientCnxn - EventThread shut down
9126 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxn - Closed socket connection for client /127.0.0.1:55501 which had sessionid 0x1565c4c812e0004
9127 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000/storm sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@440dffe1
9128 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
9128 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55502
9128 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
9129 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55502
9132 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c4c812e0005 with negotiated timeout 20000 for client /127.0.0.1:55502
9132 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c4c812e0005, negotiated timeout = 20000
9132 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
10210 [main] INFO  backtype.storm.daemon.supervisor - Starting Supervisor with conf {"dev.zookeeper.path" "/tmp/dev-storm-zookeeper", "topology.tick.tuple.freq.secs" nil, "topology.builtin.metrics.bucket.size.secs" 60, "topology.fall.back.on.java.serialization" true, "topology.max.error.report.per.interval" 5, "zmq.linger.millis" 0, "topology.skip.missing.kryo.registrations" true, "storm.messaging.netty.client_worker_threads" 1, "ui.childopts" "-Xmx768m", "storm.zookeeper.session.timeout" 20000, "nimbus.reassign" true, "topology.trident.batch.emit.interval.millis" 50, "storm.messaging.netty.flush.check.interval.ms" 10, "nimbus.monitor.freq.secs" 10, "logviewer.childopts" "-Xmx128m", "java.library.path" "/usr/local/lib:/opt/local/lib:/usr/lib", "topology.executor.send.buffer.size" 1024, "storm.local.dir" "/tmp/f3ece70c-3400-4c5f-b8a6-963795e92ed3", "storm.messaging.netty.buffer_size" 5242880, "supervisor.worker.start.timeout.secs" 120, "topology.enable.message.timeouts" true, "nimbus.cleanup.inbox.freq.secs" 600, "nimbus.inbox.jar.expiration.secs" 3600, "drpc.worker.threads" 64, "storm.meta.serialization.delegate" "backtype.storm.serialization.DefaultSerializationDelegate", "topology.worker.shared.thread.pool.size" 4, "nimbus.host" "localhost", "storm.messaging.netty.min_wait_ms" 100, "storm.zookeeper.port" 2000, "transactional.zookeeper.port" nil, "topology.executor.receive.buffer.size" 1024, "transactional.zookeeper.servers" nil, "storm.zookeeper.root" "/storm", "storm.zookeeper.retry.intervalceiling.millis" 30000, "supervisor.enable" true, "storm.messaging.netty.server_worker_threads" 1, "storm.zookeeper.servers" ["localhost"], "transactional.zookeeper.root" "/transactional", "topology.acker.executors" nil, "topology.transfer.buffer.size" 1024, "topology.worker.childopts" nil, "drpc.queue.size" 128, "worker.childopts" "-Xmx768m", "supervisor.heartbeat.frequency.secs" 5, "topology.error.throttle.interval.secs" 10, "zmq.hwm" 0, "drpc.port" 3772, "supervisor.monitor.frequency.secs" 3, "drpc.childopts" "-Xmx768m", "topology.receiver.buffer.size" 8, "task.heartbeat.frequency.secs" 3, "topology.tasks" nil, "storm.messaging.netty.max_retries" 300, "topology.spout.wait.strategy" "backtype.storm.spout.SleepSpoutWaitStrategy", "nimbus.thrift.max_buffer_size" 1048576, "topology.max.spout.pending" nil, "storm.zookeeper.retry.interval" 1000, "topology.sleep.spout.wait.strategy.time.ms" 1, "nimbus.topology.validator" "backtype.storm.nimbus.DefaultTopologyValidator", "supervisor.slots.ports" (1024 1025 1026), "topology.environment" nil, "topology.debug" false, "nimbus.task.launch.secs" 120, "nimbus.supervisor.timeout.secs" 60, "topology.message.timeout.secs" 30, "task.refresh.poll.secs" 10, "topology.workers" 1, "supervisor.childopts" "-Xmx256m", "nimbus.thrift.port" 6627, "topology.stats.sample.rate" 0.05, "worker.heartbeat.frequency.secs" 1, "topology.tuple.serializer" "backtype.storm.serialization.types.ListDelegateSerializer", "topology.disruptor.wait.strategy" "com.lmax.disruptor.BlockingWaitStrategy", "topology.multilang.serializer" "backtype.storm.multilang.JsonSerializer", "nimbus.task.timeout.secs" 30, "storm.zookeeper.connection.timeout" 15000, "topology.kryo.factory" "backtype.storm.serialization.DefaultKryoFactory", "drpc.invocations.port" 3773, "logviewer.port" 8000, "zmq.threads" 1, "storm.zookeeper.retry.times" 5, "topology.worker.receiver.thread.count" 1, "storm.thrift.transport" "backtype.storm.security.auth.SimpleTransportPlugin", "topology.state.synchronization.timeout.secs" 60, "supervisor.worker.timeout.secs" 30, "nimbus.file.copy.expiration.secs" 600, "storm.messaging.transport" "backtype.storm.messaging.netty.Context", "logviewer.appender.name" "A1", "storm.messaging.netty.max_wait_ms" 1000, "drpc.request.timeout.secs" 600, "storm.local.mode.zmq" false, "ui.port" 8080, "nimbus.childopts" "-Xmx1024m", "storm.cluster.mode" "local", "topology.max.task.parallelism" nil, "storm.messaging.netty.transfer.batch.size" 262144, "topology.classpath" nil}
10234 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
10234 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
10235 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000 sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@6d4d9023
10235 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
10236 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55503
10236 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
10237 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55503
10242 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c4c812e0006 with negotiated timeout 20000 for client /127.0.0.1:55503
10242 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c4c812e0006, negotiated timeout = 20000
10243 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
10243 [main-EventThread] INFO  backtype.storm.zookeeper - Zookeeper state update: :connected:none
11258 [ProcessThread(sid:0 cport:-1):] INFO  org.apache.storm.zookeeper.server.PrepRequestProcessor - Processed session termination for sessionid: 0x1565c4c812e0006
11264 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxn - Closed socket connection for client /127.0.0.1:55503 which had sessionid 0x1565c4c812e0006
11265 [main-EventThread] INFO  org.apache.storm.zookeeper.ClientCnxn - EventThread shut down
11265 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Session: 0x1565c4c812e0006 closed
11266 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
11267 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
11277 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000/storm sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@541a7482
11278 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
11278 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55504
11279 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
11279 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55504
11280 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c4c812e0007 with negotiated timeout 20000 for client /127.0.0.1:55504
11281 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c4c812e0007, negotiated timeout = 20000
11281 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
11333 [main] INFO  backtype.storm.daemon.supervisor - Starting supervisor with id 7612bccb-1d1b-4ce6-9c86-30fff5283baa at host ip-172-31-4-51.ec2.internal
11351 [main] INFO  backtype.storm.daemon.supervisor - Starting Supervisor with conf {"dev.zookeeper.path" "/tmp/dev-storm-zookeeper", "topology.tick.tuple.freq.secs" nil, "topology.builtin.metrics.bucket.size.secs" 60, "topology.fall.back.on.java.serialization" true, "topology.max.error.report.per.interval" 5, "zmq.linger.millis" 0, "topology.skip.missing.kryo.registrations" true, "storm.messaging.netty.client_worker_threads" 1, "ui.childopts" "-Xmx768m", "storm.zookeeper.session.timeout" 20000, "nimbus.reassign" true, "topology.trident.batch.emit.interval.millis" 50, "storm.messaging.netty.flush.check.interval.ms" 10, "nimbus.monitor.freq.secs" 10, "logviewer.childopts" "-Xmx128m", "java.library.path" "/usr/local/lib:/opt/local/lib:/usr/lib", "topology.executor.send.buffer.size" 1024, "storm.local.dir" "/tmp/6d6d5176-6018-40bc-a6db-96eb5c1af730", "storm.messaging.netty.buffer_size" 5242880, "supervisor.worker.start.timeout.secs" 120, "topology.enable.message.timeouts" true, "nimbus.cleanup.inbox.freq.secs" 600, "nimbus.inbox.jar.expiration.secs" 3600, "drpc.worker.threads" 64, "storm.meta.serialization.delegate" "backtype.storm.serialization.DefaultSerializationDelegate", "topology.worker.shared.thread.pool.size" 4, "nimbus.host" "localhost", "storm.messaging.netty.min_wait_ms" 100, "storm.zookeeper.port" 2000, "transactional.zookeeper.port" nil, "topology.executor.receive.buffer.size" 1024, "transactional.zookeeper.servers" nil, "storm.zookeeper.root" "/storm", "storm.zookeeper.retry.intervalceiling.millis" 30000, "supervisor.enable" true, "storm.messaging.netty.server_worker_threads" 1, "storm.zookeeper.servers" ["localhost"], "transactional.zookeeper.root" "/transactional", "topology.acker.executors" nil, "topology.transfer.buffer.size" 1024, "topology.worker.childopts" nil, "drpc.queue.size" 128, "worker.childopts" "-Xmx768m", "supervisor.heartbeat.frequency.secs" 5, "topology.error.throttle.interval.secs" 10, "zmq.hwm" 0, "drpc.port" 3772, "supervisor.monitor.frequency.secs" 3, "drpc.childopts" "-Xmx768m", "topology.receiver.buffer.size" 8, "task.heartbeat.frequency.secs" 3, "topology.tasks" nil, "storm.messaging.netty.max_retries" 300, "topology.spout.wait.strategy" "backtype.storm.spout.SleepSpoutWaitStrategy", "nimbus.thrift.max_buffer_size" 1048576, "topology.max.spout.pending" nil, "storm.zookeeper.retry.interval" 1000, "topology.sleep.spout.wait.strategy.time.ms" 1, "nimbus.topology.validator" "backtype.storm.nimbus.DefaultTopologyValidator", "supervisor.slots.ports" (1027 1028 1029), "topology.environment" nil, "topology.debug" false, "nimbus.task.launch.secs" 120, "nimbus.supervisor.timeout.secs" 60, "topology.message.timeout.secs" 30, "task.refresh.poll.secs" 10, "topology.workers" 1, "supervisor.childopts" "-Xmx256m", "nimbus.thrift.port" 6627, "topology.stats.sample.rate" 0.05, "worker.heartbeat.frequency.secs" 1, "topology.tuple.serializer" "backtype.storm.serialization.types.ListDelegateSerializer", "topology.disruptor.wait.strategy" "com.lmax.disruptor.BlockingWaitStrategy", "topology.multilang.serializer" "backtype.storm.multilang.JsonSerializer", "nimbus.task.timeout.secs" 30, "storm.zookeeper.connection.timeout" 15000, "topology.kryo.factory" "backtype.storm.serialization.DefaultKryoFactory", "drpc.invocations.port" 3773, "logviewer.port" 8000, "zmq.threads" 1, "storm.zookeeper.retry.times" 5, "topology.worker.receiver.thread.count" 1, "storm.thrift.transport" "backtype.storm.security.auth.SimpleTransportPlugin", "topology.state.synchronization.timeout.secs" 60, "supervisor.worker.timeout.secs" 30, "nimbus.file.copy.expiration.secs" 600, "storm.messaging.transport" "backtype.storm.messaging.netty.Context", "logviewer.appender.name" "A1", "storm.messaging.netty.max_wait_ms" 1000, "drpc.request.timeout.secs" 600, "storm.local.mode.zmq" false, "ui.port" 8080, "nimbus.childopts" "-Xmx1024m", "storm.cluster.mode" "local", "topology.max.task.parallelism" nil, "storm.messaging.netty.transfer.batch.size" 262144, "topology.classpath" nil}
11353 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
11354 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
11354 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000 sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@496d5aa8
11355 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
11355 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55505
11356 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
11372 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55505
11383 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c4c812e0008 with negotiated timeout 20000 for client /127.0.0.1:55505
11383 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c4c812e0008, negotiated timeout = 20000
11384 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
11384 [main-EventThread] INFO  backtype.storm.zookeeper - Zookeeper state update: :connected:none
11385 [ProcessThread(sid:0 cport:-1):] INFO  org.apache.storm.zookeeper.server.PrepRequestProcessor - Processed session termination for sessionid: 0x1565c4c812e0008
11387 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxn - Closed socket connection for client /127.0.0.1:55505 which had sessionid 0x1565c4c812e0008
11387 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Session: 0x1565c4c812e0008 closed
11387 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
11388 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
11388 [main-EventThread] INFO  org.apache.storm.zookeeper.ClientCnxn - EventThread shut down
11388 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000/storm sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@639afee3
11389 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
11389 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55506
11390 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
11390 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55506
11393 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c4c812e0009 with negotiated timeout 20000 for client /127.0.0.1:55506
11394 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c4c812e0009, negotiated timeout = 20000
11394 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
12416 [main] INFO  backtype.storm.daemon.supervisor - Starting supervisor with id c23194e0-4c28-41b5-934c-4619ba1f5279 at host ip-172-31-4-51.ec2.internal
12558 [main] INFO  backtype.storm.daemon.nimbus - Received topology submission for tweetwordcount with conf {"storm.id" "tweetwordcount-1-1470427339", "topology.acker.executors" 2, "streamparse.log.path" "/root/exercise_2/tweetwordcount/logs", "topology.kryo.decorators" (), "topology.name" "tweetwordcount", "topology.max.spout.pending" 5000, "topology.debug" false, "topology.kryo.register" nil, "topology.message.timeout.secs" 60, "topology.workers" 2, "topology.max.task.parallelism" nil, "streamparse.log.level" "debug"}
12633 [main] INFO  backtype.storm.daemon.nimbus - Activating tweetwordcount: tweetwordcount-1-1470427339
12849 [main] INFO  backtype.storm.scheduler.EvenScheduler - Available slots: (["c23194e0-4c28-41b5-934c-4619ba1f5279" 1027] ["c23194e0-4c28-41b5-934c-4619ba1f5279" 1028] ["c23194e0-4c28-41b5-934c-4619ba1f5279" 1029] ["7612bccb-1d1b-4ce6-9c86-30fff5283baa" 1024] ["7612bccb-1d1b-4ce6-9c86-30fff5283baa" 1025] ["7612bccb-1d1b-4ce6-9c86-30fff5283baa" 1026])
13036 [main] INFO  backtype.storm.daemon.nimbus - Setting new assignment for topology id tweetwordcount-1-1470427339: #backtype.storm.daemon.common.Assignment{:master-code-dir "/tmp/a07dc6dc-f814-4184-ad13-936ef7ca3b13/nimbus/stormdist/tweetwordcount-1-1470427339", :node->host {"7612bccb-1d1b-4ce6-9c86-30fff5283baa" "ip-172-31-4-51.ec2.internal", "c23194e0-4c28-41b5-934c-4619ba1f5279" "ip-172-31-4-51.ec2.internal"}, :executor->node+port {[3 3] ["c23194e0-4c28-41b5-934c-4619ba1f5279" 1027], [6 6] ["7612bccb-1d1b-4ce6-9c86-30fff5283baa" 1024], [5 5] ["c23194e0-4c28-41b5-934c-4619ba1f5279" 1027], [4 4] ["7612bccb-1d1b-4ce6-9c86-30fff5283baa" 1024], [7 7] ["c23194e0-4c28-41b5-934c-4619ba1f5279" 1027], [2 2] ["7612bccb-1d1b-4ce6-9c86-30fff5283baa" 1024], [1 1] ["c23194e0-4c28-41b5-934c-4619ba1f5279" 1027]}, :executor->start-time-secs {[7 7] 1470427339, [5 5] 1470427339, [3 3] 1470427339, [1 1] 1470427339, [6 6] 1470427339, [4 4] 1470427339, [2 2] 1470427339}}
14789 [Thread-3] INFO  backtype.storm.daemon.supervisor - Copying resources at file:/root/exercise_2/tweetwordcount/_resources/resources to /tmp/f3ece70c-3400-4c5f-b8a6-963795e92ed3/supervisor/stormdist/tweetwordcount-1-1470427339/resources
14867 [Thread-5] INFO  backtype.storm.daemon.supervisor - Copying resources at file:/root/exercise_2/tweetwordcount/_resources/resources to /tmp/6d6d5176-6018-40bc-a6db-96eb5c1af730/supervisor/stormdist/tweetwordcount-1-1470427339/resources
14928 [Thread-4] INFO  backtype.storm.daemon.supervisor - Launching worker with assignment #backtype.storm.daemon.supervisor.LocalAssignment{:storm-id "tweetwordcount-1-1470427339", :executors ([6 6] [4 4] [2 2])} for this supervisor 7612bccb-1d1b-4ce6-9c86-30fff5283baa on port 1024 with id 0cb82627-9ec8-4a80-b0a2-3c88b291cdd2
14930 [Thread-4] INFO  backtype.storm.daemon.worker - Launching worker for tweetwordcount-1-1470427339 on 7612bccb-1d1b-4ce6-9c86-30fff5283baa:1024 with id 0cb82627-9ec8-4a80-b0a2-3c88b291cdd2 and conf {"dev.zookeeper.path" "/tmp/dev-storm-zookeeper", "topology.tick.tuple.freq.secs" nil, "topology.builtin.metrics.bucket.size.secs" 60, "topology.fall.back.on.java.serialization" true, "topology.max.error.report.per.interval" 5, "zmq.linger.millis" 0, "topology.skip.missing.kryo.registrations" true, "storm.messaging.netty.client_worker_threads" 1, "ui.childopts" "-Xmx768m", "storm.zookeeper.session.timeout" 20000, "nimbus.reassign" true, "topology.trident.batch.emit.interval.millis" 50, "storm.messaging.netty.flush.check.interval.ms" 10, "nimbus.monitor.freq.secs" 10, "logviewer.childopts" "-Xmx128m", "java.library.path" "/usr/local/lib:/opt/local/lib:/usr/lib", "topology.executor.send.buffer.size" 1024, "storm.local.dir" "/tmp/f3ece70c-3400-4c5f-b8a6-963795e92ed3", "storm.messaging.netty.buffer_size" 5242880, "supervisor.worker.start.timeout.secs" 120, "topology.enable.message.timeouts" true, "nimbus.cleanup.inbox.freq.secs" 600, "nimbus.inbox.jar.expiration.secs" 3600, "drpc.worker.threads" 64, "storm.meta.serialization.delegate" "backtype.storm.serialization.DefaultSerializationDelegate", "topology.worker.shared.thread.pool.size" 4, "nimbus.host" "localhost", "storm.messaging.netty.min_wait_ms" 100, "storm.zookeeper.port" 2000, "transactional.zookeeper.port" nil, "topology.executor.receive.buffer.size" 1024, "transactional.zookeeper.servers" nil, "storm.zookeeper.root" "/storm", "storm.zookeeper.retry.intervalceiling.millis" 30000, "supervisor.enable" true, "storm.messaging.netty.server_worker_threads" 1, "storm.zookeeper.servers" ["localhost"], "transactional.zookeeper.root" "/transactional", "topology.acker.executors" nil, "topology.transfer.buffer.size" 1024, "topology.worker.childopts" nil, "drpc.queue.size" 128, "worker.childopts" "-Xmx768m", "supervisor.heartbeat.frequency.secs" 5, "topology.error.throttle.interval.secs" 10, "zmq.hwm" 0, "drpc.port" 3772, "supervisor.monitor.frequency.secs" 3, "drpc.childopts" "-Xmx768m", "topology.receiver.buffer.size" 8, "task.heartbeat.frequency.secs" 3, "topology.tasks" nil, "storm.messaging.netty.max_retries" 300, "topology.spout.wait.strategy" "backtype.storm.spout.SleepSpoutWaitStrategy", "nimbus.thrift.max_buffer_size" 1048576, "topology.max.spout.pending" nil, "storm.zookeeper.retry.interval" 1000, "topology.sleep.spout.wait.strategy.time.ms" 1, "nimbus.topology.validator" "backtype.storm.nimbus.DefaultTopologyValidator", "supervisor.slots.ports" (1024 1025 1026), "topology.environment" nil, "topology.debug" false, "nimbus.task.launch.secs" 120, "nimbus.supervisor.timeout.secs" 60, "topology.message.timeout.secs" 30, "task.refresh.poll.secs" 10, "topology.workers" 1, "supervisor.childopts" "-Xmx256m", "nimbus.thrift.port" 6627, "topology.stats.sample.rate" 0.05, "worker.heartbeat.frequency.secs" 1, "topology.tuple.serializer" "backtype.storm.serialization.types.ListDelegateSerializer", "topology.disruptor.wait.strategy" "com.lmax.disruptor.BlockingWaitStrategy", "topology.multilang.serializer" "backtype.storm.multilang.JsonSerializer", "nimbus.task.timeout.secs" 30, "storm.zookeeper.connection.timeout" 15000, "topology.kryo.factory" "backtype.storm.serialization.DefaultKryoFactory", "drpc.invocations.port" 3773, "logviewer.port" 8000, "zmq.threads" 1, "storm.zookeeper.retry.times" 5, "topology.worker.receiver.thread.count" 1, "storm.thrift.transport" "backtype.storm.security.auth.SimpleTransportPlugin", "topology.state.synchronization.timeout.secs" 60, "supervisor.worker.timeout.secs" 30, "nimbus.file.copy.expiration.secs" 600, "storm.messaging.transport" "backtype.storm.messaging.netty.Context", "logviewer.appender.name" "A1", "storm.messaging.netty.max_wait_ms" 1000, "drpc.request.timeout.secs" 600, "storm.local.mode.zmq" false, "ui.port" 8080, "nimbus.childopts" "-Xmx1024m", "storm.cluster.mode" "local", "topology.max.task.parallelism" nil, "storm.messaging.netty.transfer.batch.size" 262144, "topology.classpath" nil}
14933 [Thread-4] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
14934 [Thread-4] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
14943 [Thread-4] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000 sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@28c540
14944 [Thread-4-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
14945 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55508
14945 [Thread-4-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
14946 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55508
14947 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c4c812e000a with negotiated timeout 20000 for client /127.0.0.1:55508
14948 [Thread-4-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c4c812e000a, negotiated timeout = 20000
14948 [Thread-4-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
14948 [Thread-4-EventThread] INFO  backtype.storm.zookeeper - Zookeeper state update: :connected:none
14971 [Thread-6] INFO  backtype.storm.daemon.supervisor - Launching worker with assignment #backtype.storm.daemon.supervisor.LocalAssignment{:storm-id "tweetwordcount-1-1470427339", :executors ([3 3] [5 5] [7 7] [1 1])} for this supervisor c23194e0-4c28-41b5-934c-4619ba1f5279 on port 1027 with id 9e878b75-4466-44fa-acc4-8c5b1f3e89b7
14982 [Thread-6] INFO  backtype.storm.daemon.worker - Launching worker for tweetwordcount-1-1470427339 on c23194e0-4c28-41b5-934c-4619ba1f5279:1027 with id 9e878b75-4466-44fa-acc4-8c5b1f3e89b7 and conf {"dev.zookeeper.path" "/tmp/dev-storm-zookeeper", "topology.tick.tuple.freq.secs" nil, "topology.builtin.metrics.bucket.size.secs" 60, "topology.fall.back.on.java.serialization" true, "topology.max.error.report.per.interval" 5, "zmq.linger.millis" 0, "topology.skip.missing.kryo.registrations" true, "storm.messaging.netty.client_worker_threads" 1, "ui.childopts" "-Xmx768m", "storm.zookeeper.session.timeout" 20000, "nimbus.reassign" true, "topology.trident.batch.emit.interval.millis" 50, "storm.messaging.netty.flush.check.interval.ms" 10, "nimbus.monitor.freq.secs" 10, "logviewer.childopts" "-Xmx128m", "java.library.path" "/usr/local/lib:/opt/local/lib:/usr/lib", "topology.executor.send.buffer.size" 1024, "storm.local.dir" "/tmp/6d6d5176-6018-40bc-a6db-96eb5c1af730", "storm.messaging.netty.buffer_size" 5242880, "supervisor.worker.start.timeout.secs" 120, "topology.enable.message.timeouts" true, "nimbus.cleanup.inbox.freq.secs" 600, "nimbus.inbox.jar.expiration.secs" 3600, "drpc.worker.threads" 64, "storm.meta.serialization.delegate" "backtype.storm.serialization.DefaultSerializationDelegate", "topology.worker.shared.thread.pool.size" 4, "nimbus.host" "localhost", "storm.messaging.netty.min_wait_ms" 100, "storm.zookeeper.port" 2000, "transactional.zookeeper.port" nil, "topology.executor.receive.buffer.size" 1024, "transactional.zookeeper.servers" nil, "storm.zookeeper.root" "/storm", "storm.zookeeper.retry.intervalceiling.millis" 30000, "supervisor.enable" true, "storm.messaging.netty.server_worker_threads" 1, "storm.zookeeper.servers" ["localhost"], "transactional.zookeeper.root" "/transactional", "topology.acker.executors" nil, "topology.transfer.buffer.size" 1024, "topology.worker.childopts" nil, "drpc.queue.size" 128, "worker.childopts" "-Xmx768m", "supervisor.heartbeat.frequency.secs" 5, "topology.error.throttle.interval.secs" 10, "zmq.hwm" 0, "drpc.port" 3772, "supervisor.monitor.frequency.secs" 3, "drpc.childopts" "-Xmx768m", "topology.receiver.buffer.size" 8, "task.heartbeat.frequency.secs" 3, "topology.tasks" nil, "storm.messaging.netty.max_retries" 300, "topology.spout.wait.strategy" "backtype.storm.spout.SleepSpoutWaitStrategy", "nimbus.thrift.max_buffer_size" 1048576, "topology.max.spout.pending" nil, "storm.zookeeper.retry.interval" 1000, "topology.sleep.spout.wait.strategy.time.ms" 1, "nimbus.topology.validator" "backtype.storm.nimbus.DefaultTopologyValidator", "supervisor.slots.ports" (1027 1028 1029), "topology.environment" nil, "topology.debug" false, "nimbus.task.launch.secs" 120, "nimbus.supervisor.timeout.secs" 60, "topology.message.timeout.secs" 30, "task.refresh.poll.secs" 10, "topology.workers" 1, "supervisor.childopts" "-Xmx256m", "nimbus.thrift.port" 6627, "topology.stats.sample.rate" 0.05, "worker.heartbeat.frequency.secs" 1, "topology.tuple.serializer" "backtype.storm.serialization.types.ListDelegateSerializer", "topology.disruptor.wait.strategy" "com.lmax.disruptor.BlockingWaitStrategy", "topology.multilang.serializer" "backtype.storm.multilang.JsonSerializer", "nimbus.task.timeout.secs" 30, "storm.zookeeper.connection.timeout" 15000, "topology.kryo.factory" "backtype.storm.serialization.DefaultKryoFactory", "drpc.invocations.port" 3773, "logviewer.port" 8000, "zmq.threads" 1, "storm.zookeeper.retry.times" 5, "topology.worker.receiver.thread.count" 1, "storm.thrift.transport" "backtype.storm.security.auth.SimpleTransportPlugin", "topology.state.synchronization.timeout.secs" 60, "supervisor.worker.timeout.secs" 30, "nimbus.file.copy.expiration.secs" 600, "storm.messaging.transport" "backtype.storm.messaging.netty.Context", "logviewer.appender.name" "A1", "storm.messaging.netty.max_wait_ms" 1000, "drpc.request.timeout.secs" 600, "storm.local.mode.zmq" false, "ui.port" 8080, "nimbus.childopts" "-Xmx1024m", "storm.cluster.mode" "local", "topology.max.task.parallelism" nil, "storm.messaging.netty.transfer.batch.size" 262144, "topology.classpath" nil}
14982 [Thread-6] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
14983 [Thread-6] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
14983 [Thread-6] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000 sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@ac5feeb
14984 [Thread-6-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
14985 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55509
14986 [Thread-6-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
14987 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55509
15012 [Thread-6-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c4c812e000b, negotiated timeout = 20000
15013 [Thread-6-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
15013 [Thread-6-EventThread] INFO  backtype.storm.zookeeper - Zookeeper state update: :connected:none
15013 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c4c812e000b with negotiated timeout 20000 for client /127.0.0.1:55509
15015 [ProcessThread(sid:0 cport:-1):] INFO  org.apache.storm.zookeeper.server.PrepRequestProcessor - Processed session termination for sessionid: 0x1565c4c812e000b
15016 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxn - Closed socket connection for client /127.0.0.1:55509 which had sessionid 0x1565c4c812e000b
15017 [Thread-6] INFO  org.apache.storm.zookeeper.ZooKeeper - Session: 0x1565c4c812e000b closed
15017 [Thread-6] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
15017 [Thread-6] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
15017 [Thread-6-EventThread] INFO  org.apache.storm.zookeeper.ClientCnxn - EventThread shut down
15020 [Thread-6] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000/storm sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@20bf4111
15054 [Thread-6-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
15055 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55510
15055 [Thread-6-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
15055 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55510
15057 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c4c812e000c with negotiated timeout 20000 for client /127.0.0.1:55510
15057 [Thread-6-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c4c812e000c, negotiated timeout = 20000
15058 [Thread-6-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
15950 [ProcessThread(sid:0 cport:-1):] INFO  org.apache.storm.zookeeper.server.PrepRequestProcessor - Processed session termination for sessionid: 0x1565c4c812e000a
15964 [Thread-4] INFO  org.apache.storm.zookeeper.ZooKeeper - Session: 0x1565c4c812e000a closed
15964 [Thread-4] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
15965 [Thread-4] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
15965 [Thread-4-EventThread] INFO  org.apache.storm.zookeeper.ClientCnxn - EventThread shut down
15965 [Thread-4] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000/storm sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@41efda6e
15966 [Thread-4-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
15967 [Thread-4-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
15990 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxn - Closed socket connection for client /127.0.0.1:55508 which had sessionid 0x1565c4c812e000a
15990 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55511
15990 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55511
15992 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c4c812e000d with negotiated timeout 20000 for client /127.0.0.1:55511
15993 [Thread-4-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c4c812e000d, negotiated timeout = 20000
15994 [Thread-4-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
16012 [Thread-4] INFO  backtype.storm.daemon.worker - Reading Assignments.
16072 [Thread-6] INFO  backtype.storm.daemon.worker - Reading Assignments.
16184 [Thread-4] INFO  backtype.storm.daemon.worker - Launching receive-thread for 7612bccb-1d1b-4ce6-9c86-30fff5283baa:1024
16190 [Thread-6] INFO  backtype.storm.daemon.worker - Launching receive-thread for c23194e0-4c28-41b5-934c-4619ba1f5279:1027
16200 [Thread-7-worker-receiver-thread-0] INFO  backtype.storm.messaging.loader - Starting receive-thread: [stormId: tweetwordcount-1-1470427339, port: 1024, thread-id: 0 ]
16202 [Thread-8-worker-receiver-thread-0] INFO  backtype.storm.messaging.loader - Starting receive-thread: [stormId: tweetwordcount-1-1470427339, port: 1027, thread-id: 0 ]
16907 [Thread-4] INFO  backtype.storm.daemon.executor - Loading executor __acker:[2 2]
16907 [Thread-6] INFO  backtype.storm.daemon.executor - Loading executor count-bolt:[3 3]
16925 [Thread-4] INFO  backtype.storm.daemon.executor - Loaded executor tasks __acker:[2 2]
16928 [Thread-6] INFO  backtype.storm.daemon.executor - Loaded executor tasks count-bolt:[3 3]
16959 [Thread-4] INFO  backtype.storm.daemon.executor - Timeouts disabled for executor __acker:[2 2]
16959 [Thread-4] INFO  backtype.storm.daemon.executor - Finished loading executor __acker:[2 2]
16973 [Thread-6] INFO  backtype.storm.daemon.executor - Finished loading executor count-bolt:[3 3]
16981 [Thread-6] INFO  backtype.storm.daemon.executor - Loading executor parse-tweet-bolt:[5 5]
16983 [Thread-6] INFO  backtype.storm.daemon.executor - Loaded executor tasks parse-tweet-bolt:[5 5]
17000 [Thread-4] INFO  backtype.storm.daemon.executor - Loading executor count-bolt:[4 4]
17002 [Thread-4] INFO  backtype.storm.daemon.executor - Loaded executor tasks count-bolt:[4 4]
17004 [Thread-6] INFO  backtype.storm.daemon.executor - Finished loading executor parse-tweet-bolt:[5 5]
17014 [Thread-4] INFO  backtype.storm.daemon.executor - Finished loading executor count-bolt:[4 4]
17036 [Thread-6] INFO  backtype.storm.daemon.executor - Loading executor tweet-spout:[7 7]
17037 [Thread-6] INFO  backtype.storm.daemon.executor - Loaded executor tasks tweet-spout:[7 7]
17039 [Thread-4] INFO  backtype.storm.daemon.executor - Loading executor parse-tweet-bolt:[6 6]
17042 [Thread-4] INFO  backtype.storm.daemon.executor - Loaded executor tasks parse-tweet-bolt:[6 6]
17059 [Thread-6] INFO  backtype.storm.daemon.executor - Finished loading executor tweet-spout:[7 7]
17077 [Thread-4] INFO  backtype.storm.daemon.executor - Finished loading executor parse-tweet-bolt:[6 6]
17088 [refresh-active-timer] INFO  backtype.storm.daemon.worker - All connections are ready for worker 7612bccb-1d1b-4ce6-9c86-30fff5283baa:1024 with id 0cb82627-9ec8-4a80-b0a2-3c88b291cdd2
17107 [Thread-6] INFO  backtype.storm.daemon.executor - Loading executor __system:[-1 -1]
17107 [Thread-6] INFO  backtype.storm.daemon.executor - Loaded executor tasks __system:[-1 -1]
17137 [Thread-6] INFO  backtype.storm.daemon.executor - Finished loading executor __system:[-1 -1]
17151 [refresh-active-timer] INFO  backtype.storm.daemon.worker - All connections are ready for worker c23194e0-4c28-41b5-934c-4619ba1f5279:1027 with id 9e878b75-4466-44fa-acc4-8c5b1f3e89b7
17158 [Thread-4] INFO  backtype.storm.daemon.executor - Loading executor __system:[-1 -1]
17159 [Thread-4] INFO  backtype.storm.daemon.executor - Loaded executor tasks __system:[-1 -1]
17185 [Thread-4] INFO  backtype.storm.daemon.executor - Finished loading executor __system:[-1 -1]
17201 [Thread-4] INFO  backtype.storm.daemon.worker - Worker has topology config {"storm.id" "tweetwordcount-1-1470427339", "dev.zookeeper.path" "/tmp/dev-storm-zookeeper", "topology.tick.tuple.freq.secs" nil, "topology.builtin.metrics.bucket.size.secs" 60, "topology.fall.back.on.java.serialization" true, "topology.max.error.report.per.interval" 5, "zmq.linger.millis" 0, "topology.skip.missing.kryo.registrations" true, "storm.messaging.netty.client_worker_threads" 1, "ui.childopts" "-Xmx768m", "storm.zookeeper.session.timeout" 20000, "nimbus.reassign" true, "topology.trident.batch.emit.interval.millis" 50, "storm.messaging.netty.flush.check.interval.ms" 10, "nimbus.monitor.freq.secs" 10, "logviewer.childopts" "-Xmx128m", "java.library.path" "/usr/local/lib:/opt/local/lib:/usr/lib", "topology.executor.send.buffer.size" 1024, "storm.local.dir" "/tmp/f3ece70c-3400-4c5f-b8a6-963795e92ed3", "storm.messaging.netty.buffer_size" 5242880, "supervisor.worker.start.timeout.secs" 120, "topology.enable.message.timeouts" true, "nimbus.cleanup.inbox.freq.secs" 600, "nimbus.inbox.jar.expiration.secs" 3600, "drpc.worker.threads" 64, "storm.meta.serialization.delegate" "backtype.storm.serialization.DefaultSerializationDelegate", "topology.worker.shared.thread.pool.size" 4, "nimbus.host" "localhost", "storm.messaging.netty.min_wait_ms" 100, "storm.zookeeper.port" 2000, "transactional.zookeeper.port" nil, "topology.executor.receive.buffer.size" 1024, "transactional.zookeeper.servers" nil, "storm.zookeeper.root" "/storm", "storm.zookeeper.retry.intervalceiling.millis" 30000, "supervisor.enable" true, "storm.messaging.netty.server_worker_threads" 1, "storm.zookeeper.servers" ["localhost"], "transactional.zookeeper.root" "/transactional", "topology.acker.executors" 2, "streamparse.log.path" "/root/exercise_2/tweetwordcount/logs", "topology.kryo.decorators" (), "topology.name" "tweetwordcount", "topology.transfer.buffer.size" 1024, "topology.worker.childopts" nil, "drpc.queue.size" 128, "worker.childopts" "-Xmx768m", "supervisor.heartbeat.frequency.secs" 5, "topology.error.throttle.interval.secs" 10, "zmq.hwm" 0, "drpc.port" 3772, "supervisor.monitor.frequency.secs" 3, "drpc.childopts" "-Xmx768m", "topology.receiver.buffer.size" 8, "task.heartbeat.frequency.secs" 3, "topology.tasks" nil, "storm.messaging.netty.max_retries" 300, "topology.spout.wait.strategy" "backtype.storm.spout.SleepSpoutWaitStrategy", "nimbus.thrift.max_buffer_size" 1048576, "topology.max.spout.pending" 5000, "storm.zookeeper.retry.interval" 1000, "topology.sleep.spout.wait.strategy.time.ms" 1, "nimbus.topology.validator" "backtype.storm.nimbus.DefaultTopologyValidator", "supervisor.slots.ports" (1024 1025 1026), "topology.environment" nil, "topology.debug" false, "nimbus.task.launch.secs" 120, "nimbus.supervisor.timeout.secs" 60, "topology.kryo.register" nil, "topology.message.timeout.secs" 60, "task.refresh.poll.secs" 10, "topology.workers" 2, "supervisor.childopts" "-Xmx256m", "nimbus.thrift.port" 6627, "topology.stats.sample.rate" 0.05, "worker.heartbeat.frequency.secs" 1, "topology.tuple.serializer" "backtype.storm.serialization.types.ListDelegateSerializer", "topology.disruptor.wait.strategy" "com.lmax.disruptor.BlockingWaitStrategy", "topology.multilang.serializer" "backtype.storm.multilang.JsonSerializer", "nimbus.task.timeout.secs" 30, "storm.zookeeper.connection.timeout" 15000, "topology.kryo.factory" "backtype.storm.serialization.DefaultKryoFactory", "drpc.invocations.port" 3773, "logviewer.port" 8000, "zmq.threads" 1, "storm.zookeeper.retry.times" 5, "topology.worker.receiver.thread.count" 1, "storm.thrift.transport" "backtype.storm.security.auth.SimpleTransportPlugin", "topology.state.synchronization.timeout.secs" 60, "supervisor.worker.timeout.secs" 30, "nimbus.file.copy.expiration.secs" 600, "storm.messaging.transport" "backtype.storm.messaging.netty.Context", "logviewer.appender.name" "A1", "storm.messaging.netty.max_wait_ms" 1000, "drpc.request.timeout.secs" 600, "storm.local.mode.zmq" false, "ui.port" 8080, "nimbus.childopts" "-Xmx1024m", "storm.cluster.mode" "local", "topology.max.task.parallelism" nil, "storm.messaging.netty.transfer.batch.size" 262144, "topology.classpath" nil, "streamparse.log.level" "debug"}
17201 [Thread-4] INFO  backtype.storm.daemon.worker - Worker 0cb82627-9ec8-4a80-b0a2-3c88b291cdd2 for storm tweetwordcount-1-1470427339 on 7612bccb-1d1b-4ce6-9c86-30fff5283baa:1024 has finished loading
17218 [Thread-6] INFO  backtype.storm.daemon.executor - Loading executor __acker:[1 1]
17219 [Thread-6] INFO  backtype.storm.daemon.executor - Loaded executor tasks __acker:[1 1]
17222 [Thread-6] INFO  backtype.storm.daemon.executor - Timeouts disabled for executor __acker:[1 1]
17222 [Thread-6] INFO  backtype.storm.daemon.executor - Finished loading executor __acker:[1 1]
17239 [Thread-6] INFO  backtype.storm.daemon.worker - Worker has topology config {"storm.id" "tweetwordcount-1-1470427339", "dev.zookeeper.path" "/tmp/dev-storm-zookeeper", "topology.tick.tuple.freq.secs" nil, "topology.builtin.metrics.bucket.size.secs" 60, "topology.fall.back.on.java.serialization" true, "topology.max.error.report.per.interval" 5, "zmq.linger.millis" 0, "topology.skip.missing.kryo.registrations" true, "storm.messaging.netty.client_worker_threads" 1, "ui.childopts" "-Xmx768m", "storm.zookeeper.session.timeout" 20000, "nimbus.reassign" true, "topology.trident.batch.emit.interval.millis" 50, "storm.messaging.netty.flush.check.interval.ms" 10, "nimbus.monitor.freq.secs" 10, "logviewer.childopts" "-Xmx128m", "java.library.path" "/usr/local/lib:/opt/local/lib:/usr/lib", "topology.executor.send.buffer.size" 1024, "storm.local.dir" "/tmp/6d6d5176-6018-40bc-a6db-96eb5c1af730", "storm.messaging.netty.buffer_size" 5242880, "supervisor.worker.start.timeout.secs" 120, "topology.enable.message.timeouts" true, "nimbus.cleanup.inbox.freq.secs" 600, "nimbus.inbox.jar.expiration.secs" 3600, "drpc.worker.threads" 64, "storm.meta.serialization.delegate" "backtype.storm.serialization.DefaultSerializationDelegate", "topology.worker.shared.thread.pool.size" 4, "nimbus.host" "localhost", "storm.messaging.netty.min_wait_ms" 100, "storm.zookeeper.port" 2000, "transactional.zookeeper.port" nil, "topology.executor.receive.buffer.size" 1024, "transactional.zookeeper.servers" nil, "storm.zookeeper.root" "/storm", "storm.zookeeper.retry.intervalceiling.millis" 30000, "supervisor.enable" true, "storm.messaging.netty.server_worker_threads" 1, "storm.zookeeper.servers" ["localhost"], "transactional.zookeeper.root" "/transactional", "topology.acker.executors" 2, "streamparse.log.path" "/root/exercise_2/tweetwordcount/logs", "topology.kryo.decorators" (), "topology.name" "tweetwordcount", "topology.transfer.buffer.size" 1024, "topology.worker.childopts" nil, "drpc.queue.size" 128, "worker.childopts" "-Xmx768m", "supervisor.heartbeat.frequency.secs" 5, "topology.error.throttle.interval.secs" 10, "zmq.hwm" 0, "drpc.port" 3772, "supervisor.monitor.frequency.secs" 3, "drpc.childopts" "-Xmx768m", "topology.receiver.buffer.size" 8, "task.heartbeat.frequency.secs" 3, "topology.tasks" nil, "storm.messaging.netty.max_retries" 300, "topology.spout.wait.strategy" "backtype.storm.spout.SleepSpoutWaitStrategy", "nimbus.thrift.max_buffer_size" 1048576, "topology.max.spout.pending" 5000, "storm.zookeeper.retry.interval" 1000, "topology.sleep.spout.wait.strategy.time.ms" 1, "nimbus.topology.validator" "backtype.storm.nimbus.DefaultTopologyValidator", "supervisor.slots.ports" (1027 1028 1029), "topology.environment" nil, "topology.debug" false, "nimbus.task.launch.secs" 120, "nimbus.supervisor.timeout.secs" 60, "topology.kryo.register" nil, "topology.message.timeout.secs" 60, "task.refresh.poll.secs" 10, "topology.workers" 2, "supervisor.childopts" "-Xmx256m", "nimbus.thrift.port" 6627, "topology.stats.sample.rate" 0.05, "worker.heartbeat.frequency.secs" 1, "topology.tuple.serializer" "backtype.storm.serialization.types.ListDelegateSerializer", "topology.disruptor.wait.strategy" "com.lmax.disruptor.BlockingWaitStrategy", "topology.multilang.serializer" "backtype.storm.multilang.JsonSerializer", "nimbus.task.timeout.secs" 30, "storm.zookeeper.connection.timeout" 15000, "topology.kryo.factory" "backtype.storm.serialization.DefaultKryoFactory", "drpc.invocations.port" 3773, "logviewer.port" 8000, "zmq.threads" 1, "storm.zookeeper.retry.times" 5, "topology.worker.receiver.thread.count" 1, "storm.thrift.transport" "backtype.storm.security.auth.SimpleTransportPlugin", "topology.state.synchronization.timeout.secs" 60, "supervisor.worker.timeout.secs" 30, "nimbus.file.copy.expiration.secs" 600, "storm.messaging.transport" "backtype.storm.messaging.netty.Context", "logviewer.appender.name" "A1", "storm.messaging.netty.max_wait_ms" 1000, "drpc.request.timeout.secs" 600, "storm.local.mode.zmq" false, "ui.port" 8080, "nimbus.childopts" "-Xmx1024m", "storm.cluster.mode" "local", "topology.max.task.parallelism" nil, "storm.messaging.netty.transfer.batch.size" 262144, "topology.classpath" nil, "streamparse.log.level" "debug"}
17254 [Thread-6] INFO  backtype.storm.daemon.worker - Worker 9e878b75-4466-44fa-acc4-8c5b1f3e89b7 for storm tweetwordcount-1-1470427339 on c23194e0-4c28-41b5-934c-4619ba1f5279:1027 has finished loading
18125 [Thread-20-parse-tweet-bolt] INFO  backtype.storm.daemon.executor - Preparing bolt parse-tweet-bolt:(6)
18143 [Thread-16-count-bolt] INFO  backtype.storm.daemon.executor - Preparing bolt count-bolt:(4)
18145 [Thread-16-count-bolt] INFO  backtype.storm.utils.ShellProcess - Storm multilang serializer: backtype.storm.multilang.JsonSerializer
18147 [Thread-20-parse-tweet-bolt] INFO  backtype.storm.utils.ShellProcess - Storm multilang serializer: backtype.storm.multilang.JsonSerializer
18173 [Thread-11-__acker] INFO  backtype.storm.daemon.executor - Preparing bolt __acker:(2)
18175 [Thread-11-__acker] INFO  backtype.storm.daemon.executor - Prepared bolt __acker:(2)
18188 [Thread-24-__system] INFO  backtype.storm.daemon.executor - Preparing bolt __system:(-1)
18192 [Thread-24-__system] INFO  backtype.storm.daemon.executor - Prepared bolt __system:(-1)
18233 [Thread-15-parse-tweet-bolt] INFO  backtype.storm.daemon.executor - Preparing bolt parse-tweet-bolt:(5)
18233 [Thread-15-parse-tweet-bolt] INFO  backtype.storm.utils.ShellProcess - Storm multilang serializer: backtype.storm.multilang.JsonSerializer
18233 [Thread-27-__acker] INFO  backtype.storm.daemon.executor - Preparing bolt __acker:(1)
18234 [Thread-27-__acker] INFO  backtype.storm.daemon.executor - Prepared bolt __acker:(1)
18325 [Thread-12-count-bolt] INFO  backtype.storm.daemon.executor - Preparing bolt count-bolt:(3)
18326 [Thread-12-count-bolt] INFO  backtype.storm.utils.ShellProcess - Storm multilang serializer: backtype.storm.multilang.JsonSerializer
18327 [Thread-18-tweet-spout] INFO  backtype.storm.daemon.executor - Opening spout tweet-spout:(7)
18338 [Thread-22-__system] INFO  backtype.storm.daemon.executor - Preparing bolt __system:(-1)
18341 [Thread-18-tweet-spout] INFO  backtype.storm.utils.ShellProcess - Storm multilang serializer: backtype.storm.multilang.JsonSerializer
18342 [Thread-22-__system] INFO  backtype.storm.daemon.executor - Prepared bolt __system:(-1)
19029 [Thread-20-parse-tweet-bolt] INFO  backtype.storm.task.ShellBolt - Launched subprocess with pid 3275
19137 [Thread-20-parse-tweet-bolt] INFO  backtype.storm.task.ShellBolt - Start checking heartbeat...
19137 [Thread-20-parse-tweet-bolt] INFO  backtype.storm.daemon.executor - Prepared bolt parse-tweet-bolt:(6)
19333 [Thread-12-count-bolt] INFO  backtype.storm.task.ShellBolt - Launched subprocess with pid 3279
19381 [Thread-15-parse-tweet-bolt] INFO  backtype.storm.task.ShellBolt - Launched subprocess with pid 3277
19392 [Thread-12-count-bolt] INFO  backtype.storm.task.ShellBolt - Start checking heartbeat...
19393 [Thread-12-count-bolt] INFO  backtype.storm.daemon.executor - Prepared bolt count-bolt:(3)
19443 [Thread-16-count-bolt] INFO  backtype.storm.task.ShellBolt - Launched subprocess with pid 3273
19479 [Thread-15-parse-tweet-bolt] INFO  backtype.storm.task.ShellBolt - Start checking heartbeat...
19479 [Thread-15-parse-tweet-bolt] INFO  backtype.storm.daemon.executor - Prepared bolt parse-tweet-bolt:(5)
19494 [Thread-31] ERROR backtype.storm.daemon.executor - 
java.lang.Exception: Shell Process Exception: Python NameError raised
Traceback (most recent call last):
  File "/usr/lib/python2.7/site-packages/streamparse/storm/component.py", line 487, in run
    self.initialize(storm_conf, context)
  File "bolts/tweetcounter.py", line 12, in initialize
    self.redis = StrictRedis()
NameError: global name 'StrictRedis' is not defined

	at backtype.storm.task.ShellBolt.handleError(ShellBolt.java:188) [storm-core-0.9.5.jar:0.9.5]
	at backtype.storm.task.ShellBolt.access$1100(ShellBolt.java:69) [storm-core-0.9.5.jar:0.9.5]
	at backtype.storm.task.ShellBolt$BoltReaderRunnable.run(ShellBolt.java:331) [storm-core-0.9.5.jar:0.9.5]
	at java.lang.Thread.run(Thread.java:745) [na:1.7.0_79]
19499 [Thread-16-count-bolt] INFO  backtype.storm.task.ShellBolt - Start checking heartbeat...
19499 [Thread-16-count-bolt] INFO  backtype.storm.daemon.executor - Prepared bolt count-bolt:(4)
19543 [Thread-35] ERROR backtype.storm.daemon.executor - 
java.lang.Exception: Shell Process Exception: Python NameError raised
Traceback (most recent call last):
  File "/usr/lib/python2.7/site-packages/streamparse/storm/component.py", line 487, in run
    self.initialize(storm_conf, context)
  File "bolts/tweetcounter.py", line 12, in initialize
    self.redis = StrictRedis()
NameError: global name 'StrictRedis' is not defined

	at backtype.storm.task.ShellBolt.handleError(ShellBolt.java:188) [storm-core-0.9.5.jar:0.9.5]
	at backtype.storm.task.ShellBolt.access$1100(ShellBolt.java:69) [storm-core-0.9.5.jar:0.9.5]
	at backtype.storm.task.ShellBolt$BoltReaderRunnable.run(ShellBolt.java:331) [storm-core-0.9.5.jar:0.9.5]
	at java.lang.Thread.run(Thread.java:745) [na:1.7.0_79]
19614 [Thread-31] ERROR backtype.storm.task.ShellBolt - Halting process: ShellBolt died.
java.lang.RuntimeException: backtype.storm.multilang.NoOutputException: Pipe to subprocess seems to be broken! No output read.
Serializer Exception:


	at backtype.storm.utils.ShellProcess.readShellMsg(ShellProcess.java:101) ~[storm-core-0.9.5.jar:0.9.5]
	at backtype.storm.task.ShellBolt$BoltReaderRunnable.run(ShellBolt.java:318) ~[storm-core-0.9.5.jar:0.9.5]
	at java.lang.Thread.run(Thread.java:745) [na:1.7.0_79]
19614 [Thread-35] ERROR backtype.storm.task.ShellBolt - Halting process: ShellBolt died.
java.lang.RuntimeException: backtype.storm.multilang.NoOutputException: Pipe to subprocess seems to be broken! No output read.
Serializer Exception:


	at backtype.storm.utils.ShellProcess.readShellMsg(ShellProcess.java:101) ~[storm-core-0.9.5.jar:0.9.5]
	at backtype.storm.task.ShellBolt$BoltReaderRunnable.run(ShellBolt.java:318) ~[storm-core-0.9.5.jar:0.9.5]
	at java.lang.Thread.run(Thread.java:745) [na:1.7.0_79]
19614 [Thread-35] ERROR backtype.storm.daemon.executor - 
java.lang.RuntimeException: backtype.storm.multilang.NoOutputException: Pipe to subprocess seems to be broken! No output read.
Serializer Exception:


	at backtype.storm.utils.ShellProcess.readShellMsg(ShellProcess.java:101) ~[storm-core-0.9.5.jar:0.9.5]
	at backtype.storm.task.ShellBolt$BoltReaderRunnable.run(ShellBolt.java:318) ~[storm-core-0.9.5.jar:0.9.5]
	at java.lang.Thread.run(Thread.java:745) [na:1.7.0_79]
19615 [Thread-31] ERROR backtype.storm.daemon.executor - 
java.lang.RuntimeException: backtype.storm.multilang.NoOutputException: Pipe to subprocess seems to be broken! No output read.
Serializer Exception:


	at backtype.storm.utils.ShellProcess.readShellMsg(ShellProcess.java:101) ~[storm-core-0.9.5.jar:0.9.5]
	at backtype.storm.task.ShellBolt$BoltReaderRunnable.run(ShellBolt.java:318) ~[storm-core-0.9.5.jar:0.9.5]
	at java.lang.Thread.run(Thread.java:745) [na:1.7.0_79]
Traceback (most recent call last):
  File "/usr/bin/sparse", line 9, in <module>
    load_entry_point('streamparse==2.1.4', 'console_scripts', 'sparse')()
  File "/usr/lib/python2.7/site-packages/streamparse/cli/sparse.py", line 57, in main
    args.func(args)
  File "/usr/lib/python2.7/site-packages/streamparse/cli/run.py", line 81, in main
    debug=args.debug)
  File "/usr/lib/python2.7/site-packages/streamparse/cli/run.py", line 52, in run_local_topology
    run(full_cmd)
  File "/usr/lib/python2.7/site-packages/invoke/__init__.py", line 32, in run
    return Context().run(command, **kwargs)
  File "/usr/lib/python2.7/site-packages/invoke/context.py", line 53, in run
    return runner_class(context=self).run(command, **kwargs)
  File "/usr/lib/python2.7/site-packages/invoke/runners.py", line 363, in run
    raise Failure(result)
invoke.exceptions.Failure: Command execution failure!

Exit code: 11

Stderr:




[root@ip-172-31-4-51 tweetwordcount]# cd ..
[root@ip-172-31-4-51 exercise_2]# cd ..
[root@ip-172-31-4-51 ~]# ls -l
total 720
-rw-------  1 root root    287 Sep 22  2015 dans_bash_history.txt
drwxr-xr-x  4 root root   4096 Aug  5 20:01 exercise_2
-rw-r--r--  1 root root  12402 Jul 11 18:07 ez_setup.py
-rw-r--r--  1 root root    763 Aug  5 17:04 finalresults.py
-rw-r--r--  1 root root    446 Aug  5 16:38 histogram.py
drwxr-xr-x 11 root root   4096 May  4  2015 ipython
drwxr-xr-x  5 root root   4096 May  4  2015 pgxl-deployment-tools
-rw-r--r--  1 root root 655364 Jul 11 18:07 setuptools-24.0.2.zip
-rwxr-xr-x  1 root root    221 Sep 22  2015 start-hadoop.sh
-rwxr-xr-x  1 root root    252 Sep 22  2015 start-hadoop.sh~
-rwxr-xr-x  1 root root    209 Sep 22  2015 stop-hadoop.sh
-rwxr-xr-x  1 root root    222 Sep 22  2015 stop-hadoop.sh~
drwxr-xr-x 11 root root   4096 May  4  2015 streamparse
drwxr-xr-x  8 root root   4096 Jul 11 19:33 tweetcount
drwxr-xr-x  8 root root   4096 Aug  5 18:44 tweetwordcount
-rw-r--r--  1 root root    765 Jul 29 01:42 Twittercredentials.py
[root@ip-172-31-4-51 ~]# rm tweetwordcount/
rm: cannot remove `tweetwordcount/': Is a directory
[root@ip-172-31-4-51 ~]# rm -rf  tweetwordcount/
[root@ip-172-31-4-51 ~]# ls -l
total 716
-rw-------  1 root root    287 Sep 22  2015 dans_bash_history.txt
drwxr-xr-x  4 root root   4096 Aug  5 20:01 exercise_2
-rw-r--r--  1 root root  12402 Jul 11 18:07 ez_setup.py
-rw-r--r--  1 root root    763 Aug  5 17:04 finalresults.py
-rw-r--r--  1 root root    446 Aug  5 16:38 histogram.py
drwxr-xr-x 11 root root   4096 May  4  2015 ipython
drwxr-xr-x  5 root root   4096 May  4  2015 pgxl-deployment-tools
-rw-r--r--  1 root root 655364 Jul 11 18:07 setuptools-24.0.2.zip
-rwxr-xr-x  1 root root    221 Sep 22  2015 start-hadoop.sh
-rwxr-xr-x  1 root root    252 Sep 22  2015 start-hadoop.sh~
-rwxr-xr-x  1 root root    209 Sep 22  2015 stop-hadoop.sh
-rwxr-xr-x  1 root root    222 Sep 22  2015 stop-hadoop.sh~
drwxr-xr-x 11 root root   4096 May  4  2015 streamparse
drwxr-xr-x  8 root root   4096 Jul 11 19:33 tweetcount
-rw-r--r--  1 root root    765 Jul 29 01:42 Twittercredentials.py
[root@ip-172-31-4-51 ~]# sparse quickstart tweetcount
error: folder "tweetcount" already exists
[root@ip-172-31-4-51 ~]# sparse quickstart tweetwordcount

Creating your tweetwordcount streamparse project...
    create    tweetwordcount
    create    tweetwordcount/.gitignore
    create    tweetwordcount/config.json
    create    tweetwordcount/fabfile.py
    create    tweetwordcount/project.clj
    create    tweetwordcount/README.md
    create    tweetwordcount/src
    create    tweetwordcount/src/bolts
    create    tweetwordcount/src/bolts/__init__.py
    create    tweetwordcount/src/bolts/wordcount.py
    create    tweetwordcount/src/spouts
    create    tweetwordcount/src/spouts/__init__.py
    create    tweetwordcount/src/spouts/words.py
    create    tweetwordcount/tasks.py
    create    tweetwordcount/topologies
    create    tweetwordcount/topologies/wordcount.clj
    create    tweetwordcount/virtualenvs
    create    tweetwordcount/virtualenvs/wordcount.txt
Done.

Try running your topology locally with:

	cd tweetwordcount
	sparse run
[root@ip-172-31-4-51 ~]# cd tweetwordcount/
[root@ip-172-31-4-51 tweetwordcount]# sparse run
Running wordcount topology...
Routing Python logging to /root/tweetwordcount/logs.
Running lein command to run local cluster:
lein run -m streamparse.commands.run/-main topologies/wordcount.clj -t 0 --option 'topology.workers=2' --option 'topology.acker.executors=2' --option 'streamparse.log.path="/root/tweetwordcount/logs"' --option 'streamparse.log.level="debug"'
WARNING: You're currently running as root; probably by accident.
Press control-C to abort or Enter to continue as root.
Set LEIN_ROOT to disable this warning.

4684 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:zookeeper.version=3.4.6-1569965, built on 02/20/2014 09:09 GMT
4696 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:host.name=ip-172-31-4-51.ec2.internal
4696 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:java.version=1.7.0_79
4696 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:java.vendor=Oracle Corporation
4696 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:java.home=/opt/jdk1.7.0_79/jre
4696 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:java.class.path=/root/tweetwordcount/test:/root/tweetwordcount/topologies:/root/tweetwordcount/dev-resources:/root/tweetwordcount/_resources:/root/tweetwordcount/_build/classes:/root/.m2/repository/ch/qos/logback/logback-classic/1.0.13/logback-classic-1.0.13.jar:/root/.m2/repository/org/clojure/tools.macro/0.1.0/tools.macro-0.1.0.jar:/root/.m2/repository/ring/ring-core/1.1.5/ring-core-1.1.5.jar:/root/.m2/repository/hiccup/hiccup/0.3.6/hiccup-0.3.6.jar:/root/.m2/repository/ring/ring-servlet/0.3.11/ring-servlet-0.3.11.jar:/root/.m2/repository/com/googlecode/json-simple/json-simple/1.1/json-simple-1.1.jar:/root/.m2/repository/org/clojure/math.numeric-tower/0.0.1/math.numeric-tower-0.0.1.jar:/root/.m2/repository/clj-time/clj-time/0.4.1/clj-time-0.4.1.jar:/root/.m2/repository/org/objenesis/objenesis/1.2/objenesis-1.2.jar:/root/.m2/repository/com/twitter/chill-java/0.3.5/chill-java-0.3.5.jar:/root/.m2/repository/com/parsely/streamparse/0.0.4-SNAPSHOT/streamparse-0.0.4-SNAPSHOT.jar:/root/.m2/repository/ring/ring-jetty-adapter/0.3.11/ring-jetty-adapter-0.3.11.jar:/root/.m2/repository/jline/jline/2.11/jline-2.11.jar:/root/.m2/repository/clj-stacktrace/clj-stacktrace/0.2.2/clj-stacktrace-0.2.2.jar:/root/.m2/repository/org/clojure/tools.nrepl/0.2.12/tools.nrepl-0.2.12.jar:/root/.m2/repository/org/slf4j/slf4j-api/1.7.5/slf4j-api-1.7.5.jar:/root/.m2/repository/ring/ring-devel/0.3.11/ring-devel-0.3.11.jar:/root/.m2/repository/org/mortbay/jetty/jetty-util/6.1.26/jetty-util-6.1.26.jar:/root/.m2/repository/javax/servlet/servlet-api/2.5/servlet-api-2.5.jar:/root/.m2/repository/clojure-complete/clojure-complete/0.2.4/clojure-complete-0.2.4.jar:/root/.m2/repository/org/yaml/snakeyaml/1.11/snakeyaml-1.11.jar:/root/.m2/repository/ch/qos/logback/logback-core/1.0.13/logback-core-1.0.13.jar:/root/.m2/repository/commons-lang/commons-lang/2.5/commons-lang-2.5.jar:/root/.m2/repository/org/mortbay/jetty/jetty/6.1.26/jetty-6.1.26.jar:/root/.m2/repository/joda-time/joda-time/2.0/joda-time-2.0.jar:/root/.m2/repository/commons-io/commons-io/2.4/commons-io-2.4.jar:/root/.m2/repository/commons-logging/commons-logging/1.1.3/commons-logging-1.1.3.jar:/root/.m2/repository/com/esotericsoftware/kryo/kryo/2.21/kryo-2.21.jar:/root/.m2/repository/com/esotericsoftware/minlog/minlog/1.2/minlog-1.2.jar:/root/.m2/repository/org/apache/storm/storm-core/0.9.5/storm-core-0.9.5.jar:/root/.m2/repository/compojure/compojure/1.1.3/compojure-1.1.3.jar:/root/.m2/repository/com/esotericsoftware/reflectasm/reflectasm/1.07/reflectasm-1.07-shaded.jar:/root/.m2/repository/com/twitter/carbonite/1.4.0/carbonite-1.4.0.jar:/root/.m2/repository/commons-codec/commons-codec/1.6/commons-codec-1.6.jar:/root/.m2/repository/commons-fileupload/commons-fileupload/1.2.1/commons-fileupload-1.2.1.jar:/root/.m2/repository/org/clojure/data.json/0.2.6/data.json-0.2.6.jar:/root/.m2/repository/org/slf4j/log4j-over-slf4j/1.6.6/log4j-over-slf4j-1.6.6.jar:/root/.m2/repository/org/jgrapht/jgrapht-core/0.9.0/jgrapht-core-0.9.0.jar:/root/.m2/repository/org/clojure/clojure/1.5.1/clojure-1.5.1.jar:/root/.m2/repository/org/clojure/tools.logging/0.2.3/tools.logging-0.2.3.jar:/root/.m2/repository/org/ow2/asm/asm/4.0/asm-4.0.jar:/root/.m2/repository/clout/clout/1.0.1/clout-1.0.1.jar:/root/.m2/repository/org/apache/commons/commons-exec/1.1/commons-exec-1.1.jar:/root/.m2/repository/com/googlecode/disruptor/disruptor/2.10.1/disruptor-2.10.1.jar:/root/.m2/repository/org/clojure/core.incubator/0.1.0/core.incubator-0.1.0.jar:/root/.m2/repository/org/clojure/tools.cli/0.2.4/tools.cli-0.2.4.jar
4696 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:java.library.path=/usr/java/packages/lib/amd64:/usr/lib64:/lib64:/lib:/usr/lib
4697 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:java.io.tmpdir=/tmp
4697 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:java.compiler=<NA>
4697 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:os.name=Linux
4697 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:os.arch=amd64
4697 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:os.version=2.6.32-504.12.2.el6.centos.plus.x86_64
4697 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:user.name=root
4697 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:user.home=/root
4698 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:user.dir=/root/tweetwordcount
4759 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:zookeeper.version=3.4.6-1569965, built on 02/20/2014 09:09 GMT
4759 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:host.name=ip-172-31-4-51.ec2.internal
4759 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:java.version=1.7.0_79
4759 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:java.vendor=Oracle Corporation
4759 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:java.home=/opt/jdk1.7.0_79/jre
4759 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:java.class.path=/root/tweetwordcount/test:/root/tweetwordcount/topologies:/root/tweetwordcount/dev-resources:/root/tweetwordcount/_resources:/root/tweetwordcount/_build/classes:/root/.m2/repository/ch/qos/logback/logback-classic/1.0.13/logback-classic-1.0.13.jar:/root/.m2/repository/org/clojure/tools.macro/0.1.0/tools.macro-0.1.0.jar:/root/.m2/repository/ring/ring-core/1.1.5/ring-core-1.1.5.jar:/root/.m2/repository/hiccup/hiccup/0.3.6/hiccup-0.3.6.jar:/root/.m2/repository/ring/ring-servlet/0.3.11/ring-servlet-0.3.11.jar:/root/.m2/repository/com/googlecode/json-simple/json-simple/1.1/json-simple-1.1.jar:/root/.m2/repository/org/clojure/math.numeric-tower/0.0.1/math.numeric-tower-0.0.1.jar:/root/.m2/repository/clj-time/clj-time/0.4.1/clj-time-0.4.1.jar:/root/.m2/repository/org/objenesis/objenesis/1.2/objenesis-1.2.jar:/root/.m2/repository/com/twitter/chill-java/0.3.5/chill-java-0.3.5.jar:/root/.m2/repository/com/parsely/streamparse/0.0.4-SNAPSHOT/streamparse-0.0.4-SNAPSHOT.jar:/root/.m2/repository/ring/ring-jetty-adapter/0.3.11/ring-jetty-adapter-0.3.11.jar:/root/.m2/repository/jline/jline/2.11/jline-2.11.jar:/root/.m2/repository/clj-stacktrace/clj-stacktrace/0.2.2/clj-stacktrace-0.2.2.jar:/root/.m2/repository/org/clojure/tools.nrepl/0.2.12/tools.nrepl-0.2.12.jar:/root/.m2/repository/org/slf4j/slf4j-api/1.7.5/slf4j-api-1.7.5.jar:/root/.m2/repository/ring/ring-devel/0.3.11/ring-devel-0.3.11.jar:/root/.m2/repository/org/mortbay/jetty/jetty-util/6.1.26/jetty-util-6.1.26.jar:/root/.m2/repository/javax/servlet/servlet-api/2.5/servlet-api-2.5.jar:/root/.m2/repository/clojure-complete/clojure-complete/0.2.4/clojure-complete-0.2.4.jar:/root/.m2/repository/org/yaml/snakeyaml/1.11/snakeyaml-1.11.jar:/root/.m2/repository/ch/qos/logback/logback-core/1.0.13/logback-core-1.0.13.jar:/root/.m2/repository/commons-lang/commons-lang/2.5/commons-lang-2.5.jar:/root/.m2/repository/org/mortbay/jetty/jetty/6.1.26/jetty-6.1.26.jar:/root/.m2/repository/joda-time/joda-time/2.0/joda-time-2.0.jar:/root/.m2/repository/commons-io/commons-io/2.4/commons-io-2.4.jar:/root/.m2/repository/commons-logging/commons-logging/1.1.3/commons-logging-1.1.3.jar:/root/.m2/repository/com/esotericsoftware/kryo/kryo/2.21/kryo-2.21.jar:/root/.m2/repository/com/esotericsoftware/minlog/minlog/1.2/minlog-1.2.jar:/root/.m2/repository/org/apache/storm/storm-core/0.9.5/storm-core-0.9.5.jar:/root/.m2/repository/compojure/compojure/1.1.3/compojure-1.1.3.jar:/root/.m2/repository/com/esotericsoftware/reflectasm/reflectasm/1.07/reflectasm-1.07-shaded.jar:/root/.m2/repository/com/twitter/carbonite/1.4.0/carbonite-1.4.0.jar:/root/.m2/repository/commons-codec/commons-codec/1.6/commons-codec-1.6.jar:/root/.m2/repository/commons-fileupload/commons-fileupload/1.2.1/commons-fileupload-1.2.1.jar:/root/.m2/repository/org/clojure/data.json/0.2.6/data.json-0.2.6.jar:/root/.m2/repository/org/slf4j/log4j-over-slf4j/1.6.6/log4j-over-slf4j-1.6.6.jar:/root/.m2/repository/org/jgrapht/jgrapht-core/0.9.0/jgrapht-core-0.9.0.jar:/root/.m2/repository/org/clojure/clojure/1.5.1/clojure-1.5.1.jar:/root/.m2/repository/org/clojure/tools.logging/0.2.3/tools.logging-0.2.3.jar:/root/.m2/repository/org/ow2/asm/asm/4.0/asm-4.0.jar:/root/.m2/repository/clout/clout/1.0.1/clout-1.0.1.jar:/root/.m2/repository/org/apache/commons/commons-exec/1.1/commons-exec-1.1.jar:/root/.m2/repository/com/googlecode/disruptor/disruptor/2.10.1/disruptor-2.10.1.jar:/root/.m2/repository/org/clojure/core.incubator/0.1.0/core.incubator-0.1.0.jar:/root/.m2/repository/org/clojure/tools.cli/0.2.4/tools.cli-0.2.4.jar
4759 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:java.library.path=/usr/java/packages/lib/amd64:/usr/lib64:/lib64:/lib:/usr/lib
4759 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:java.io.tmpdir=/tmp
4759 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:java.compiler=<NA>
4759 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:os.name=Linux
4759 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:os.arch=amd64
4760 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:os.version=2.6.32-504.12.2.el6.centos.plus.x86_64
4760 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:user.name=root
4760 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:user.home=/root
4760 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:user.dir=/root/tweetwordcount
6827 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Created server with tickTime 2000 minSessionTimeout 4000 maxSessionTimeout 40000 datadir /tmp/d2cb28bf-d49b-4a64-b048-24e92e77e487/version-2 snapdir /tmp/d2cb28bf-d49b-4a64-b048-24e92e77e487/version-2
6870 [main] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - binding to port 0.0.0.0/0.0.0.0:2000
6884 [main] INFO  backtype.storm.zookeeper - Starting inprocess zookeeper at port 2000 and dir /tmp/d2cb28bf-d49b-4a64-b048-24e92e77e487
7340 [main] INFO  backtype.storm.daemon.nimbus - Starting Nimbus with conf {"dev.zookeeper.path" "/tmp/dev-storm-zookeeper", "topology.tick.tuple.freq.secs" nil, "topology.builtin.metrics.bucket.size.secs" 60, "topology.fall.back.on.java.serialization" true, "topology.max.error.report.per.interval" 5, "zmq.linger.millis" 0, "topology.skip.missing.kryo.registrations" true, "storm.messaging.netty.client_worker_threads" 1, "ui.childopts" "-Xmx768m", "storm.zookeeper.session.timeout" 20000, "nimbus.reassign" true, "topology.trident.batch.emit.interval.millis" 50, "storm.messaging.netty.flush.check.interval.ms" 10, "nimbus.monitor.freq.secs" 10, "logviewer.childopts" "-Xmx128m", "java.library.path" "/usr/local/lib:/opt/local/lib:/usr/lib", "topology.executor.send.buffer.size" 1024, "storm.local.dir" "/tmp/1fb571c5-7dfe-429f-bdd2-1ebfa3397e3c", "storm.messaging.netty.buffer_size" 5242880, "supervisor.worker.start.timeout.secs" 120, "topology.enable.message.timeouts" true, "nimbus.cleanup.inbox.freq.secs" 600, "nimbus.inbox.jar.expiration.secs" 3600, "drpc.worker.threads" 64, "storm.meta.serialization.delegate" "backtype.storm.serialization.DefaultSerializationDelegate", "topology.worker.shared.thread.pool.size" 4, "nimbus.host" "localhost", "storm.messaging.netty.min_wait_ms" 100, "storm.zookeeper.port" 2000, "transactional.zookeeper.port" nil, "topology.executor.receive.buffer.size" 1024, "transactional.zookeeper.servers" nil, "storm.zookeeper.root" "/storm", "storm.zookeeper.retry.intervalceiling.millis" 30000, "supervisor.enable" true, "storm.messaging.netty.server_worker_threads" 1, "storm.zookeeper.servers" ["localhost"], "transactional.zookeeper.root" "/transactional", "topology.acker.executors" nil, "topology.transfer.buffer.size" 1024, "topology.worker.childopts" nil, "drpc.queue.size" 128, "worker.childopts" "-Xmx768m", "supervisor.heartbeat.frequency.secs" 5, "topology.error.throttle.interval.secs" 10, "zmq.hwm" 0, "drpc.port" 3772, "supervisor.monitor.frequency.secs" 3, "drpc.childopts" "-Xmx768m", "topology.receiver.buffer.size" 8, "task.heartbeat.frequency.secs" 3, "topology.tasks" nil, "storm.messaging.netty.max_retries" 300, "topology.spout.wait.strategy" "backtype.storm.spout.SleepSpoutWaitStrategy", "nimbus.thrift.max_buffer_size" 1048576, "topology.max.spout.pending" nil, "storm.zookeeper.retry.interval" 1000, "topology.sleep.spout.wait.strategy.time.ms" 1, "nimbus.topology.validator" "backtype.storm.nimbus.DefaultTopologyValidator", "supervisor.slots.ports" [6700 6701 6702 6703], "topology.environment" nil, "topology.debug" false, "nimbus.task.launch.secs" 120, "nimbus.supervisor.timeout.secs" 60, "topology.message.timeout.secs" 30, "task.refresh.poll.secs" 10, "topology.workers" 1, "supervisor.childopts" "-Xmx256m", "nimbus.thrift.port" 6627, "topology.stats.sample.rate" 0.05, "worker.heartbeat.frequency.secs" 1, "topology.tuple.serializer" "backtype.storm.serialization.types.ListDelegateSerializer", "topology.disruptor.wait.strategy" "com.lmax.disruptor.BlockingWaitStrategy", "topology.multilang.serializer" "backtype.storm.multilang.JsonSerializer", "nimbus.task.timeout.secs" 30, "storm.zookeeper.connection.timeout" 15000, "topology.kryo.factory" "backtype.storm.serialization.DefaultKryoFactory", "drpc.invocations.port" 3773, "logviewer.port" 8000, "zmq.threads" 1, "storm.zookeeper.retry.times" 5, "topology.worker.receiver.thread.count" 1, "storm.thrift.transport" "backtype.storm.security.auth.SimpleTransportPlugin", "topology.state.synchronization.timeout.secs" 60, "supervisor.worker.timeout.secs" 30, "nimbus.file.copy.expiration.secs" 600, "storm.messaging.transport" "backtype.storm.messaging.netty.Context", "logviewer.appender.name" "A1", "storm.messaging.netty.max_wait_ms" 1000, "drpc.request.timeout.secs" 600, "storm.local.mode.zmq" false, "ui.port" 8080, "nimbus.childopts" "-Xmx1024m", "storm.cluster.mode" "local", "topology.max.task.parallelism" nil, "storm.messaging.netty.transfer.batch.size" 262144, "topology.classpath" nil}
7358 [main] INFO  backtype.storm.daemon.nimbus - Using default scheduler
7376 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
7619 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
7631 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000 sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@1dd6bc36
7668 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
7678 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
7681 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55528
7686 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55528
7689 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.persistence.FileTxnLog - Creating new log file: log.1
7714 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c4f03e80000, negotiated timeout = 20000
7716 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
7718 [main-EventThread] INFO  backtype.storm.zookeeper - Zookeeper state update: :connected:none
7727 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c4f03e80000 with negotiated timeout 20000 for client /127.0.0.1:55528
8779 [ProcessThread(sid:0 cport:-1):] INFO  org.apache.storm.zookeeper.server.PrepRequestProcessor - Processed session termination for sessionid: 0x1565c4f03e80000
8790 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxn - Closed socket connection for client /127.0.0.1:55528 which had sessionid 0x1565c4f03e80000
8790 [main-EventThread] INFO  org.apache.storm.zookeeper.ClientCnxn - EventThread shut down
8791 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Session: 0x1565c4f03e80000 closed
8792 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
8793 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
8793 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000/storm sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@4678ccfc
8806 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
8806 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
8807 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55529
8807 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55529
8808 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c4f03e80001 with negotiated timeout 20000 for client /127.0.0.1:55529
8809 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c4f03e80001, negotiated timeout = 20000
8809 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
8873 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
8874 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
8874 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000 sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@150796b
8876 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
8876 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55530
8877 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
8877 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55530
8889 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c4f03e80002 with negotiated timeout 20000 for client /127.0.0.1:55530
8889 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c4f03e80002, negotiated timeout = 20000
8889 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
8890 [main-EventThread] INFO  backtype.storm.zookeeper - Zookeeper state update: :connected:none
8893 [ProcessThread(sid:0 cport:-1):] INFO  org.apache.storm.zookeeper.server.PrepRequestProcessor - Processed session termination for sessionid: 0x1565c4f03e80002
8903 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Session: 0x1565c4f03e80002 closed
8903 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
8904 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
8904 [main-EventThread] INFO  org.apache.storm.zookeeper.ClientCnxn - EventThread shut down
8907 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000/storm sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@613cbb6e
8908 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
8908 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
8910 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] WARN  org.apache.storm.zookeeper.server.NIOServerCnxn - caught end of stream exception
org.apache.storm.zookeeper.server.ServerCnxn$EndOfStreamException: Unable to read additional data from client sessionid 0x1565c4f03e80002, likely client has closed socket
	at org.apache.storm.zookeeper.server.NIOServerCnxn.doIO(NIOServerCnxn.java:228) ~[storm-core-0.9.5.jar:0.9.5]
	at org.apache.storm.zookeeper.server.NIOServerCnxnFactory.run(NIOServerCnxnFactory.java:208) [storm-core-0.9.5.jar:0.9.5]
	at java.lang.Thread.run(Thread.java:745) [na:1.7.0_79]
8911 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
8913 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
8929 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxn - Closed socket connection for client /127.0.0.1:55530 which had sessionid 0x1565c4f03e80002
8929 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55531
8929 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55531
8930 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000 sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@78e554fc
8940 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c4f03e80003 with negotiated timeout 20000 for client /127.0.0.1:55531
8940 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c4f03e80003, negotiated timeout = 20000
8940 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
8941 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
8942 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55532
8942 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
8942 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55532
8944 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c4f03e80004 with negotiated timeout 20000 for client /127.0.0.1:55532
8944 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c4f03e80004, negotiated timeout = 20000
8944 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
8944 [main-EventThread] INFO  backtype.storm.zookeeper - Zookeeper state update: :connected:none
9947 [ProcessThread(sid:0 cport:-1):] INFO  org.apache.storm.zookeeper.server.PrepRequestProcessor - Processed session termination for sessionid: 0x1565c4f03e80004
9952 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Session: 0x1565c4f03e80004 closed
9952 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
9952 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
9953 [main-EventThread] INFO  org.apache.storm.zookeeper.ClientCnxn - EventThread shut down
9953 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxn - Closed socket connection for client /127.0.0.1:55532 which had sessionid 0x1565c4f03e80004
9953 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000/storm sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@68d10be4
9954 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
9955 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55534
9955 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
9955 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55534
9959 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c4f03e80005 with negotiated timeout 20000 for client /127.0.0.1:55534
9959 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c4f03e80005, negotiated timeout = 20000
9959 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
11033 [main] INFO  backtype.storm.daemon.supervisor - Starting Supervisor with conf {"dev.zookeeper.path" "/tmp/dev-storm-zookeeper", "topology.tick.tuple.freq.secs" nil, "topology.builtin.metrics.bucket.size.secs" 60, "topology.fall.back.on.java.serialization" true, "topology.max.error.report.per.interval" 5, "zmq.linger.millis" 0, "topology.skip.missing.kryo.registrations" true, "storm.messaging.netty.client_worker_threads" 1, "ui.childopts" "-Xmx768m", "storm.zookeeper.session.timeout" 20000, "nimbus.reassign" true, "topology.trident.batch.emit.interval.millis" 50, "storm.messaging.netty.flush.check.interval.ms" 10, "nimbus.monitor.freq.secs" 10, "logviewer.childopts" "-Xmx128m", "java.library.path" "/usr/local/lib:/opt/local/lib:/usr/lib", "topology.executor.send.buffer.size" 1024, "storm.local.dir" "/tmp/a30dfbbc-3171-47fe-874a-faf71a71834d", "storm.messaging.netty.buffer_size" 5242880, "supervisor.worker.start.timeout.secs" 120, "topology.enable.message.timeouts" true, "nimbus.cleanup.inbox.freq.secs" 600, "nimbus.inbox.jar.expiration.secs" 3600, "drpc.worker.threads" 64, "storm.meta.serialization.delegate" "backtype.storm.serialization.DefaultSerializationDelegate", "topology.worker.shared.thread.pool.size" 4, "nimbus.host" "localhost", "storm.messaging.netty.min_wait_ms" 100, "storm.zookeeper.port" 2000, "transactional.zookeeper.port" nil, "topology.executor.receive.buffer.size" 1024, "transactional.zookeeper.servers" nil, "storm.zookeeper.root" "/storm", "storm.zookeeper.retry.intervalceiling.millis" 30000, "supervisor.enable" true, "storm.messaging.netty.server_worker_threads" 1, "storm.zookeeper.servers" ["localhost"], "transactional.zookeeper.root" "/transactional", "topology.acker.executors" nil, "topology.transfer.buffer.size" 1024, "topology.worker.childopts" nil, "drpc.queue.size" 128, "worker.childopts" "-Xmx768m", "supervisor.heartbeat.frequency.secs" 5, "topology.error.throttle.interval.secs" 10, "zmq.hwm" 0, "drpc.port" 3772, "supervisor.monitor.frequency.secs" 3, "drpc.childopts" "-Xmx768m", "topology.receiver.buffer.size" 8, "task.heartbeat.frequency.secs" 3, "topology.tasks" nil, "storm.messaging.netty.max_retries" 300, "topology.spout.wait.strategy" "backtype.storm.spout.SleepSpoutWaitStrategy", "nimbus.thrift.max_buffer_size" 1048576, "topology.max.spout.pending" nil, "storm.zookeeper.retry.interval" 1000, "topology.sleep.spout.wait.strategy.time.ms" 1, "nimbus.topology.validator" "backtype.storm.nimbus.DefaultTopologyValidator", "supervisor.slots.ports" (1024 1025 1026), "topology.environment" nil, "topology.debug" false, "nimbus.task.launch.secs" 120, "nimbus.supervisor.timeout.secs" 60, "topology.message.timeout.secs" 30, "task.refresh.poll.secs" 10, "topology.workers" 1, "supervisor.childopts" "-Xmx256m", "nimbus.thrift.port" 6627, "topology.stats.sample.rate" 0.05, "worker.heartbeat.frequency.secs" 1, "topology.tuple.serializer" "backtype.storm.serialization.types.ListDelegateSerializer", "topology.disruptor.wait.strategy" "com.lmax.disruptor.BlockingWaitStrategy", "topology.multilang.serializer" "backtype.storm.multilang.JsonSerializer", "nimbus.task.timeout.secs" 30, "storm.zookeeper.connection.timeout" 15000, "topology.kryo.factory" "backtype.storm.serialization.DefaultKryoFactory", "drpc.invocations.port" 3773, "logviewer.port" 8000, "zmq.threads" 1, "storm.zookeeper.retry.times" 5, "topology.worker.receiver.thread.count" 1, "storm.thrift.transport" "backtype.storm.security.auth.SimpleTransportPlugin", "topology.state.synchronization.timeout.secs" 60, "supervisor.worker.timeout.secs" 30, "nimbus.file.copy.expiration.secs" 600, "storm.messaging.transport" "backtype.storm.messaging.netty.Context", "logviewer.appender.name" "A1", "storm.messaging.netty.max_wait_ms" 1000, "drpc.request.timeout.secs" 600, "storm.local.mode.zmq" false, "ui.port" 8080, "nimbus.childopts" "-Xmx1024m", "storm.cluster.mode" "local", "topology.max.task.parallelism" nil, "storm.messaging.netty.transfer.batch.size" 262144, "topology.classpath" nil}
11051 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
11051 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
11052 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000 sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@5ce5250d
11053 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
11053 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55535
11053 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
11054 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55535
11056 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c4f03e80006 with negotiated timeout 20000 for client /127.0.0.1:55535
11056 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c4f03e80006, negotiated timeout = 20000
11056 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
11065 [main-EventThread] INFO  backtype.storm.zookeeper - Zookeeper state update: :connected:none
12070 [ProcessThread(sid:0 cport:-1):] INFO  org.apache.storm.zookeeper.server.PrepRequestProcessor - Processed session termination for sessionid: 0x1565c4f03e80006
12072 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Session: 0x1565c4f03e80006 closed
12072 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
12073 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
12073 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxn - Closed socket connection for client /127.0.0.1:55535 which had sessionid 0x1565c4f03e80006
12073 [main-EventThread] INFO  org.apache.storm.zookeeper.ClientCnxn - EventThread shut down
12074 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000/storm sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@6704e2a0
12075 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
12075 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55536
12075 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
12076 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55536
12079 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c4f03e80007 with negotiated timeout 20000 for client /127.0.0.1:55536
12079 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c4f03e80007, negotiated timeout = 20000
12079 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
13116 [main] INFO  backtype.storm.daemon.supervisor - Starting supervisor with id a1308e44-b048-4add-bc32-018de26ec83e at host ip-172-31-4-51.ec2.internal
13131 [main] INFO  backtype.storm.daemon.supervisor - Starting Supervisor with conf {"dev.zookeeper.path" "/tmp/dev-storm-zookeeper", "topology.tick.tuple.freq.secs" nil, "topology.builtin.metrics.bucket.size.secs" 60, "topology.fall.back.on.java.serialization" true, "topology.max.error.report.per.interval" 5, "zmq.linger.millis" 0, "topology.skip.missing.kryo.registrations" true, "storm.messaging.netty.client_worker_threads" 1, "ui.childopts" "-Xmx768m", "storm.zookeeper.session.timeout" 20000, "nimbus.reassign" true, "topology.trident.batch.emit.interval.millis" 50, "storm.messaging.netty.flush.check.interval.ms" 10, "nimbus.monitor.freq.secs" 10, "logviewer.childopts" "-Xmx128m", "java.library.path" "/usr/local/lib:/opt/local/lib:/usr/lib", "topology.executor.send.buffer.size" 1024, "storm.local.dir" "/tmp/8b7e68be-5531-44f7-a8a9-225b529dcf92", "storm.messaging.netty.buffer_size" 5242880, "supervisor.worker.start.timeout.secs" 120, "topology.enable.message.timeouts" true, "nimbus.cleanup.inbox.freq.secs" 600, "nimbus.inbox.jar.expiration.secs" 3600, "drpc.worker.threads" 64, "storm.meta.serialization.delegate" "backtype.storm.serialization.DefaultSerializationDelegate", "topology.worker.shared.thread.pool.size" 4, "nimbus.host" "localhost", "storm.messaging.netty.min_wait_ms" 100, "storm.zookeeper.port" 2000, "transactional.zookeeper.port" nil, "topology.executor.receive.buffer.size" 1024, "transactional.zookeeper.servers" nil, "storm.zookeeper.root" "/storm", "storm.zookeeper.retry.intervalceiling.millis" 30000, "supervisor.enable" true, "storm.messaging.netty.server_worker_threads" 1, "storm.zookeeper.servers" ["localhost"], "transactional.zookeeper.root" "/transactional", "topology.acker.executors" nil, "topology.transfer.buffer.size" 1024, "topology.worker.childopts" nil, "drpc.queue.size" 128, "worker.childopts" "-Xmx768m", "supervisor.heartbeat.frequency.secs" 5, "topology.error.throttle.interval.secs" 10, "zmq.hwm" 0, "drpc.port" 3772, "supervisor.monitor.frequency.secs" 3, "drpc.childopts" "-Xmx768m", "topology.receiver.buffer.size" 8, "task.heartbeat.frequency.secs" 3, "topology.tasks" nil, "storm.messaging.netty.max_retries" 300, "topology.spout.wait.strategy" "backtype.storm.spout.SleepSpoutWaitStrategy", "nimbus.thrift.max_buffer_size" 1048576, "topology.max.spout.pending" nil, "storm.zookeeper.retry.interval" 1000, "topology.sleep.spout.wait.strategy.time.ms" 1, "nimbus.topology.validator" "backtype.storm.nimbus.DefaultTopologyValidator", "supervisor.slots.ports" (1027 1028 1029), "topology.environment" nil, "topology.debug" false, "nimbus.task.launch.secs" 120, "nimbus.supervisor.timeout.secs" 60, "topology.message.timeout.secs" 30, "task.refresh.poll.secs" 10, "topology.workers" 1, "supervisor.childopts" "-Xmx256m", "nimbus.thrift.port" 6627, "topology.stats.sample.rate" 0.05, "worker.heartbeat.frequency.secs" 1, "topology.tuple.serializer" "backtype.storm.serialization.types.ListDelegateSerializer", "topology.disruptor.wait.strategy" "com.lmax.disruptor.BlockingWaitStrategy", "topology.multilang.serializer" "backtype.storm.multilang.JsonSerializer", "nimbus.task.timeout.secs" 30, "storm.zookeeper.connection.timeout" 15000, "topology.kryo.factory" "backtype.storm.serialization.DefaultKryoFactory", "drpc.invocations.port" 3773, "logviewer.port" 8000, "zmq.threads" 1, "storm.zookeeper.retry.times" 5, "topology.worker.receiver.thread.count" 1, "storm.thrift.transport" "backtype.storm.security.auth.SimpleTransportPlugin", "topology.state.synchronization.timeout.secs" 60, "supervisor.worker.timeout.secs" 30, "nimbus.file.copy.expiration.secs" 600, "storm.messaging.transport" "backtype.storm.messaging.netty.Context", "logviewer.appender.name" "A1", "storm.messaging.netty.max_wait_ms" 1000, "drpc.request.timeout.secs" 600, "storm.local.mode.zmq" false, "ui.port" 8080, "nimbus.childopts" "-Xmx1024m", "storm.cluster.mode" "local", "topology.max.task.parallelism" nil, "storm.messaging.netty.transfer.batch.size" 262144, "topology.classpath" nil}
13134 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
13134 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
13144 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000 sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@58ea2d51
13144 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
13145 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55537
13145 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
13146 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55537
13147 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c4f03e80008 with negotiated timeout 20000 for client /127.0.0.1:55537
13147 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c4f03e80008, negotiated timeout = 20000
13148 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
13148 [main-EventThread] INFO  backtype.storm.zookeeper - Zookeeper state update: :connected:none
13164 [ProcessThread(sid:0 cport:-1):] INFO  org.apache.storm.zookeeper.server.PrepRequestProcessor - Processed session termination for sessionid: 0x1565c4f03e80008
13166 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxn - Closed socket connection for client /127.0.0.1:55537 which had sessionid 0x1565c4f03e80008
13166 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Session: 0x1565c4f03e80008 closed
13166 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
13166 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
13167 [main-EventThread] INFO  org.apache.storm.zookeeper.ClientCnxn - EventThread shut down
13176 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000/storm sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@5335ed79
13176 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
13177 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55538
13177 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
13178 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55538
13181 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c4f03e80009 with negotiated timeout 20000 for client /127.0.0.1:55538
13181 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c4f03e80009, negotiated timeout = 20000
13181 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
14190 [main] INFO  backtype.storm.daemon.supervisor - Starting supervisor with id 26a3d3d0-953d-4089-acdd-719464f28315 at host ip-172-31-4-51.ec2.internal
14291 [main] INFO  backtype.storm.daemon.nimbus - Received topology submission for wordcount with conf {"storm.id" "wordcount-1-1470427504", "topology.acker.executors" 2, "streamparse.log.path" "/root/tweetwordcount/logs", "topology.kryo.decorators" (), "topology.name" "wordcount", "topology.max.spout.pending" 5000, "topology.debug" false, "topology.kryo.register" nil, "topology.message.timeout.secs" 60, "topology.workers" 2, "topology.max.task.parallelism" nil, "streamparse.log.level" "debug"}
14380 [main] INFO  backtype.storm.daemon.nimbus - Activating wordcount: wordcount-1-1470427504
14580 [main] INFO  backtype.storm.scheduler.EvenScheduler - Available slots: (["a1308e44-b048-4add-bc32-018de26ec83e" 1024] ["a1308e44-b048-4add-bc32-018de26ec83e" 1025] ["a1308e44-b048-4add-bc32-018de26ec83e" 1026] ["26a3d3d0-953d-4089-acdd-719464f28315" 1027] ["26a3d3d0-953d-4089-acdd-719464f28315" 1028] ["26a3d3d0-953d-4089-acdd-719464f28315" 1029])
14772 [main] INFO  backtype.storm.daemon.nimbus - Setting new assignment for topology id wordcount-1-1470427504: #backtype.storm.daemon.common.Assignment{:master-code-dir "/tmp/1fb571c5-7dfe-429f-bdd2-1ebfa3397e3c/nimbus/stormdist/wordcount-1-1470427504", :node->host {"26a3d3d0-953d-4089-acdd-719464f28315" "ip-172-31-4-51.ec2.internal", "a1308e44-b048-4add-bc32-018de26ec83e" "ip-172-31-4-51.ec2.internal"}, :executor->node+port {[3 3] ["a1308e44-b048-4add-bc32-018de26ec83e" 1024], [5 5] ["a1308e44-b048-4add-bc32-018de26ec83e" 1024], [4 4] ["26a3d3d0-953d-4089-acdd-719464f28315" 1027], [2 2] ["26a3d3d0-953d-4089-acdd-719464f28315" 1027], [1 1] ["a1308e44-b048-4add-bc32-018de26ec83e" 1024]}, :executor->start-time-secs {[5 5] 1470427505, [3 3] 1470427505, [1 1] 1470427505, [4 4] 1470427505, [2 2] 1470427505}}
16360 [Thread-3] INFO  backtype.storm.daemon.supervisor - Copying resources at file:/root/tweetwordcount/_resources/resources to /tmp/a30dfbbc-3171-47fe-874a-faf71a71834d/supervisor/stormdist/wordcount-1-1470427504/resources
16375 [Thread-5] INFO  backtype.storm.daemon.supervisor - Copying resources at file:/root/tweetwordcount/_resources/resources to /tmp/8b7e68be-5531-44f7-a8a9-225b529dcf92/supervisor/stormdist/wordcount-1-1470427504/resources
16511 [Thread-6] INFO  backtype.storm.daemon.supervisor - Launching worker with assignment #backtype.storm.daemon.supervisor.LocalAssignment{:storm-id "wordcount-1-1470427504", :executors ([4 4] [2 2])} for this supervisor 26a3d3d0-953d-4089-acdd-719464f28315 on port 1027 with id 33973706-4ef7-4062-bd86-c6148498a38a
16529 [Thread-6] INFO  backtype.storm.daemon.worker - Launching worker for wordcount-1-1470427504 on 26a3d3d0-953d-4089-acdd-719464f28315:1027 with id 33973706-4ef7-4062-bd86-c6148498a38a and conf {"dev.zookeeper.path" "/tmp/dev-storm-zookeeper", "topology.tick.tuple.freq.secs" nil, "topology.builtin.metrics.bucket.size.secs" 60, "topology.fall.back.on.java.serialization" true, "topology.max.error.report.per.interval" 5, "zmq.linger.millis" 0, "topology.skip.missing.kryo.registrations" true, "storm.messaging.netty.client_worker_threads" 1, "ui.childopts" "-Xmx768m", "storm.zookeeper.session.timeout" 20000, "nimbus.reassign" true, "topology.trident.batch.emit.interval.millis" 50, "storm.messaging.netty.flush.check.interval.ms" 10, "nimbus.monitor.freq.secs" 10, "logviewer.childopts" "-Xmx128m", "java.library.path" "/usr/local/lib:/opt/local/lib:/usr/lib", "topology.executor.send.buffer.size" 1024, "storm.local.dir" "/tmp/8b7e68be-5531-44f7-a8a9-225b529dcf92", "storm.messaging.netty.buffer_size" 5242880, "supervisor.worker.start.timeout.secs" 120, "topology.enable.message.timeouts" true, "nimbus.cleanup.inbox.freq.secs" 600, "nimbus.inbox.jar.expiration.secs" 3600, "drpc.worker.threads" 64, "storm.meta.serialization.delegate" "backtype.storm.serialization.DefaultSerializationDelegate", "topology.worker.shared.thread.pool.size" 4, "nimbus.host" "localhost", "storm.messaging.netty.min_wait_ms" 100, "storm.zookeeper.port" 2000, "transactional.zookeeper.port" nil, "topology.executor.receive.buffer.size" 1024, "transactional.zookeeper.servers" nil, "storm.zookeeper.root" "/storm", "storm.zookeeper.retry.intervalceiling.millis" 30000, "supervisor.enable" true, "storm.messaging.netty.server_worker_threads" 1, "storm.zookeeper.servers" ["localhost"], "transactional.zookeeper.root" "/transactional", "topology.acker.executors" nil, "topology.transfer.buffer.size" 1024, "topology.worker.childopts" nil, "drpc.queue.size" 128, "worker.childopts" "-Xmx768m", "supervisor.heartbeat.frequency.secs" 5, "topology.error.throttle.interval.secs" 10, "zmq.hwm" 0, "drpc.port" 3772, "supervisor.monitor.frequency.secs" 3, "drpc.childopts" "-Xmx768m", "topology.receiver.buffer.size" 8, "task.heartbeat.frequency.secs" 3, "topology.tasks" nil, "storm.messaging.netty.max_retries" 300, "topology.spout.wait.strategy" "backtype.storm.spout.SleepSpoutWaitStrategy", "nimbus.thrift.max_buffer_size" 1048576, "topology.max.spout.pending" nil, "storm.zookeeper.retry.interval" 1000, "topology.sleep.spout.wait.strategy.time.ms" 1, "nimbus.topology.validator" "backtype.storm.nimbus.DefaultTopologyValidator", "supervisor.slots.ports" (1027 1028 1029), "topology.environment" nil, "topology.debug" false, "nimbus.task.launch.secs" 120, "nimbus.supervisor.timeout.secs" 60, "topology.message.timeout.secs" 30, "task.refresh.poll.secs" 10, "topology.workers" 1, "supervisor.childopts" "-Xmx256m", "nimbus.thrift.port" 6627, "topology.stats.sample.rate" 0.05, "worker.heartbeat.frequency.secs" 1, "topology.tuple.serializer" "backtype.storm.serialization.types.ListDelegateSerializer", "topology.disruptor.wait.strategy" "com.lmax.disruptor.BlockingWaitStrategy", "topology.multilang.serializer" "backtype.storm.multilang.JsonSerializer", "nimbus.task.timeout.secs" 30, "storm.zookeeper.connection.timeout" 15000, "topology.kryo.factory" "backtype.storm.serialization.DefaultKryoFactory", "drpc.invocations.port" 3773, "logviewer.port" 8000, "zmq.threads" 1, "storm.zookeeper.retry.times" 5, "topology.worker.receiver.thread.count" 1, "storm.thrift.transport" "backtype.storm.security.auth.SimpleTransportPlugin", "topology.state.synchronization.timeout.secs" 60, "supervisor.worker.timeout.secs" 30, "nimbus.file.copy.expiration.secs" 600, "storm.messaging.transport" "backtype.storm.messaging.netty.Context", "logviewer.appender.name" "A1", "storm.messaging.netty.max_wait_ms" 1000, "drpc.request.timeout.secs" 600, "storm.local.mode.zmq" false, "ui.port" 8080, "nimbus.childopts" "-Xmx1024m", "storm.cluster.mode" "local", "topology.max.task.parallelism" nil, "storm.messaging.netty.transfer.batch.size" 262144, "topology.classpath" nil}
16531 [Thread-6] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
16532 [Thread-6] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
16534 [Thread-6] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000 sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@27f07e81
16535 [Thread-6-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
16535 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55539
16536 [Thread-6-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
16536 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55539
16537 [Thread-4] INFO  backtype.storm.daemon.supervisor - Launching worker with assignment #backtype.storm.daemon.supervisor.LocalAssignment{:storm-id "wordcount-1-1470427504", :executors ([3 3] [5 5] [1 1])} for this supervisor a1308e44-b048-4add-bc32-018de26ec83e on port 1024 with id eb1742c3-27ed-4005-b2a2-2ec4700a08be
16552 [Thread-6-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c4f03e8000a, negotiated timeout = 20000
16538 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c4f03e8000a with negotiated timeout 20000 for client /127.0.0.1:55539
16579 [Thread-6-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
16579 [Thread-6-EventThread] INFO  backtype.storm.zookeeper - Zookeeper state update: :connected:none
16581 [ProcessThread(sid:0 cport:-1):] INFO  org.apache.storm.zookeeper.server.PrepRequestProcessor - Processed session termination for sessionid: 0x1565c4f03e8000a
16582 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxn - Closed socket connection for client /127.0.0.1:55539 which had sessionid 0x1565c4f03e8000a
16583 [Thread-6] INFO  org.apache.storm.zookeeper.ZooKeeper - Session: 0x1565c4f03e8000a closed
16583 [Thread-6] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
16583 [Thread-6] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
16584 [Thread-6-EventThread] INFO  org.apache.storm.zookeeper.ClientCnxn - EventThread shut down
16586 [Thread-6] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000/storm sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@377c404e
16612 [Thread-4] INFO  backtype.storm.daemon.worker - Launching worker for wordcount-1-1470427504 on a1308e44-b048-4add-bc32-018de26ec83e:1024 with id eb1742c3-27ed-4005-b2a2-2ec4700a08be and conf {"dev.zookeeper.path" "/tmp/dev-storm-zookeeper", "topology.tick.tuple.freq.secs" nil, "topology.builtin.metrics.bucket.size.secs" 60, "topology.fall.back.on.java.serialization" true, "topology.max.error.report.per.interval" 5, "zmq.linger.millis" 0, "topology.skip.missing.kryo.registrations" true, "storm.messaging.netty.client_worker_threads" 1, "ui.childopts" "-Xmx768m", "storm.zookeeper.session.timeout" 20000, "nimbus.reassign" true, "topology.trident.batch.emit.interval.millis" 50, "storm.messaging.netty.flush.check.interval.ms" 10, "nimbus.monitor.freq.secs" 10, "logviewer.childopts" "-Xmx128m", "java.library.path" "/usr/local/lib:/opt/local/lib:/usr/lib", "topology.executor.send.buffer.size" 1024, "storm.local.dir" "/tmp/a30dfbbc-3171-47fe-874a-faf71a71834d", "storm.messaging.netty.buffer_size" 5242880, "supervisor.worker.start.timeout.secs" 120, "topology.enable.message.timeouts" true, "nimbus.cleanup.inbox.freq.secs" 600, "nimbus.inbox.jar.expiration.secs" 3600, "drpc.worker.threads" 64, "storm.meta.serialization.delegate" "backtype.storm.serialization.DefaultSerializationDelegate", "topology.worker.shared.thread.pool.size" 4, "nimbus.host" "localhost", "storm.messaging.netty.min_wait_ms" 100, "storm.zookeeper.port" 2000, "transactional.zookeeper.port" nil, "topology.executor.receive.buffer.size" 1024, "transactional.zookeeper.servers" nil, "storm.zookeeper.root" "/storm", "storm.zookeeper.retry.intervalceiling.millis" 30000, "supervisor.enable" true, "storm.messaging.netty.server_worker_threads" 1, "storm.zookeeper.servers" ["localhost"], "transactional.zookeeper.root" "/transactional", "topology.acker.executors" nil, "topology.transfer.buffer.size" 1024, "topology.worker.childopts" nil, "drpc.queue.size" 128, "worker.childopts" "-Xmx768m", "supervisor.heartbeat.frequency.secs" 5, "topology.error.throttle.interval.secs" 10, "zmq.hwm" 0, "drpc.port" 3772, "supervisor.monitor.frequency.secs" 3, "drpc.childopts" "-Xmx768m", "topology.receiver.buffer.size" 8, "task.heartbeat.frequency.secs" 3, "topology.tasks" nil, "storm.messaging.netty.max_retries" 300, "topology.spout.wait.strategy" "backtype.storm.spout.SleepSpoutWaitStrategy", "nimbus.thrift.max_buffer_size" 1048576, "topology.max.spout.pending" nil, "storm.zookeeper.retry.interval" 1000, "topology.sleep.spout.wait.strategy.time.ms" 1, "nimbus.topology.validator" "backtype.storm.nimbus.DefaultTopologyValidator", "supervisor.slots.ports" (1024 1025 1026), "topology.environment" nil, "topology.debug" false, "nimbus.task.launch.secs" 120, "nimbus.supervisor.timeout.secs" 60, "topology.message.timeout.secs" 30, "task.refresh.poll.secs" 10, "topology.workers" 1, "supervisor.childopts" "-Xmx256m", "nimbus.thrift.port" 6627, "topology.stats.sample.rate" 0.05, "worker.heartbeat.frequency.secs" 1, "topology.tuple.serializer" "backtype.storm.serialization.types.ListDelegateSerializer", "topology.disruptor.wait.strategy" "com.lmax.disruptor.BlockingWaitStrategy", "topology.multilang.serializer" "backtype.storm.multilang.JsonSerializer", "nimbus.task.timeout.secs" 30, "storm.zookeeper.connection.timeout" 15000, "topology.kryo.factory" "backtype.storm.serialization.DefaultKryoFactory", "drpc.invocations.port" 3773, "logviewer.port" 8000, "zmq.threads" 1, "storm.zookeeper.retry.times" 5, "topology.worker.receiver.thread.count" 1, "storm.thrift.transport" "backtype.storm.security.auth.SimpleTransportPlugin", "topology.state.synchronization.timeout.secs" 60, "supervisor.worker.timeout.secs" 30, "nimbus.file.copy.expiration.secs" 600, "storm.messaging.transport" "backtype.storm.messaging.netty.Context", "logviewer.appender.name" "A1", "storm.messaging.netty.max_wait_ms" 1000, "drpc.request.timeout.secs" 600, "storm.local.mode.zmq" false, "ui.port" 8080, "nimbus.childopts" "-Xmx1024m", "storm.cluster.mode" "local", "topology.max.task.parallelism" nil, "storm.messaging.netty.transfer.batch.size" 262144, "topology.classpath" nil}
16612 [Thread-4] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
16612 [Thread-4] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
16613 [Thread-4] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000 sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@3dcecfaa
16614 [Thread-4-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
16614 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55540
16614 [Thread-4-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
16615 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55540
16616 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c4f03e8000b with negotiated timeout 20000 for client /127.0.0.1:55540
16616 [Thread-4-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c4f03e8000b, negotiated timeout = 20000
16617 [Thread-4-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
16628 [Thread-6-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
16628 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55541
16629 [Thread-6-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
16629 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55541
16631 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c4f03e8000c with negotiated timeout 20000 for client /127.0.0.1:55541
16631 [Thread-6-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c4f03e8000c, negotiated timeout = 20000
16632 [Thread-6-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
16635 [Thread-4-EventThread] INFO  backtype.storm.zookeeper - Zookeeper state update: :connected:none
17656 [ProcessThread(sid:0 cport:-1):] INFO  org.apache.storm.zookeeper.server.PrepRequestProcessor - Processed session termination for sessionid: 0x1565c4f03e8000b
17660 [Thread-4] INFO  org.apache.storm.zookeeper.ZooKeeper - Session: 0x1565c4f03e8000b closed
17660 [Thread-4] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
17660 [Thread-4] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
17660 [Thread-4-EventThread] INFO  org.apache.storm.zookeeper.ClientCnxn - EventThread shut down
17661 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] WARN  org.apache.storm.zookeeper.server.NIOServerCnxn - caught end of stream exception
org.apache.storm.zookeeper.server.ServerCnxn$EndOfStreamException: Unable to read additional data from client sessionid 0x1565c4f03e8000b, likely client has closed socket
	at org.apache.storm.zookeeper.server.NIOServerCnxn.doIO(NIOServerCnxn.java:228) ~[storm-core-0.9.5.jar:0.9.5]
	at org.apache.storm.zookeeper.server.NIOServerCnxnFactory.run(NIOServerCnxnFactory.java:208) [storm-core-0.9.5.jar:0.9.5]
	at java.lang.Thread.run(Thread.java:745) [na:1.7.0_79]
17661 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxn - Closed socket connection for client /127.0.0.1:55540 which had sessionid 0x1565c4f03e8000b
17664 [Thread-4] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000/storm sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@7a85b031
17673 [Thread-4-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
17673 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55542
17678 [Thread-4-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
17678 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55542
17692 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c4f03e8000d with negotiated timeout 20000 for client /127.0.0.1:55542
17692 [Thread-4-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c4f03e8000d, negotiated timeout = 20000
17692 [Thread-4-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
17699 [Thread-6] INFO  backtype.storm.daemon.worker - Reading Assignments.
17750 [Thread-4] INFO  backtype.storm.daemon.worker - Reading Assignments.
17950 [Thread-4] INFO  backtype.storm.daemon.worker - Launching receive-thread for a1308e44-b048-4add-bc32-018de26ec83e:1024
17952 [Thread-6] INFO  backtype.storm.daemon.worker - Launching receive-thread for 26a3d3d0-953d-4089-acdd-719464f28315:1027
17969 [Thread-7-worker-receiver-thread-0] INFO  backtype.storm.messaging.loader - Starting receive-thread: [stormId: wordcount-1-1470427504, port: 1024, thread-id: 0 ]
17987 [Thread-8-worker-receiver-thread-0] INFO  backtype.storm.messaging.loader - Starting receive-thread: [stormId: wordcount-1-1470427504, port: 1027, thread-id: 0 ]
18777 [Thread-6] INFO  backtype.storm.daemon.executor - Loading executor __acker:[2 2]
18778 [Thread-4] INFO  backtype.storm.daemon.executor - Loading executor count-bolt:[3 3]
18794 [Thread-6] INFO  backtype.storm.daemon.executor - Loaded executor tasks __acker:[2 2]
18811 [Thread-6] INFO  backtype.storm.daemon.executor - Timeouts disabled for executor __acker:[2 2]
18812 [Thread-6] INFO  backtype.storm.daemon.executor - Finished loading executor __acker:[2 2]
18855 [Thread-4] INFO  backtype.storm.daemon.executor - Loaded executor tasks count-bolt:[3 3]
18856 [Thread-6] INFO  backtype.storm.daemon.executor - Loading executor count-bolt:[4 4]
18872 [Thread-6] INFO  backtype.storm.daemon.executor - Loaded executor tasks count-bolt:[4 4]
18872 [Thread-4] INFO  backtype.storm.daemon.executor - Finished loading executor count-bolt:[3 3]
18874 [refresh-active-timer] INFO  backtype.storm.daemon.worker - All connections are ready for worker a1308e44-b048-4add-bc32-018de26ec83e:1024 with id eb1742c3-27ed-4005-b2a2-2ec4700a08be
18892 [refresh-active-timer] INFO  backtype.storm.daemon.worker - All connections are ready for worker 26a3d3d0-953d-4089-acdd-719464f28315:1027 with id 33973706-4ef7-4062-bd86-c6148498a38a
18895 [Thread-6] INFO  backtype.storm.daemon.executor - Finished loading executor count-bolt:[4 4]
18912 [Thread-4] INFO  backtype.storm.daemon.executor - Loading executor word-spout:[5 5]
18917 [Thread-4] INFO  backtype.storm.daemon.executor - Loaded executor tasks word-spout:[5 5]
18943 [Thread-4] INFO  backtype.storm.daemon.executor - Finished loading executor word-spout:[5 5]
18962 [Thread-6] INFO  backtype.storm.daemon.executor - Loading executor __system:[-1 -1]
18964 [Thread-6] INFO  backtype.storm.daemon.executor - Loaded executor tasks __system:[-1 -1]
18977 [Thread-6] INFO  backtype.storm.daemon.executor - Finished loading executor __system:[-1 -1]
18983 [Thread-6] INFO  backtype.storm.daemon.worker - Worker has topology config {"storm.id" "wordcount-1-1470427504", "dev.zookeeper.path" "/tmp/dev-storm-zookeeper", "topology.tick.tuple.freq.secs" nil, "topology.builtin.metrics.bucket.size.secs" 60, "topology.fall.back.on.java.serialization" true, "topology.max.error.report.per.interval" 5, "zmq.linger.millis" 0, "topology.skip.missing.kryo.registrations" true, "storm.messaging.netty.client_worker_threads" 1, "ui.childopts" "-Xmx768m", "storm.zookeeper.session.timeout" 20000, "nimbus.reassign" true, "topology.trident.batch.emit.interval.millis" 50, "storm.messaging.netty.flush.check.interval.ms" 10, "nimbus.monitor.freq.secs" 10, "logviewer.childopts" "-Xmx128m", "java.library.path" "/usr/local/lib:/opt/local/lib:/usr/lib", "topology.executor.send.buffer.size" 1024, "storm.local.dir" "/tmp/8b7e68be-5531-44f7-a8a9-225b529dcf92", "storm.messaging.netty.buffer_size" 5242880, "supervisor.worker.start.timeout.secs" 120, "topology.enable.message.timeouts" true, "nimbus.cleanup.inbox.freq.secs" 600, "nimbus.inbox.jar.expiration.secs" 3600, "drpc.worker.threads" 64, "storm.meta.serialization.delegate" "backtype.storm.serialization.DefaultSerializationDelegate", "topology.worker.shared.thread.pool.size" 4, "nimbus.host" "localhost", "storm.messaging.netty.min_wait_ms" 100, "storm.zookeeper.port" 2000, "transactional.zookeeper.port" nil, "topology.executor.receive.buffer.size" 1024, "transactional.zookeeper.servers" nil, "storm.zookeeper.root" "/storm", "storm.zookeeper.retry.intervalceiling.millis" 30000, "supervisor.enable" true, "storm.messaging.netty.server_worker_threads" 1, "storm.zookeeper.servers" ["localhost"], "transactional.zookeeper.root" "/transactional", "topology.acker.executors" 2, "streamparse.log.path" "/root/tweetwordcount/logs", "topology.kryo.decorators" (), "topology.name" "wordcount", "topology.transfer.buffer.size" 1024, "topology.worker.childopts" nil, "drpc.queue.size" 128, "worker.childopts" "-Xmx768m", "supervisor.heartbeat.frequency.secs" 5, "topology.error.throttle.interval.secs" 10, "zmq.hwm" 0, "drpc.port" 3772, "supervisor.monitor.frequency.secs" 3, "drpc.childopts" "-Xmx768m", "topology.receiver.buffer.size" 8, "task.heartbeat.frequency.secs" 3, "topology.tasks" nil, "storm.messaging.netty.max_retries" 300, "topology.spout.wait.strategy" "backtype.storm.spout.SleepSpoutWaitStrategy", "nimbus.thrift.max_buffer_size" 1048576, "topology.max.spout.pending" 5000, "storm.zookeeper.retry.interval" 1000, "topology.sleep.spout.wait.strategy.time.ms" 1, "nimbus.topology.validator" "backtype.storm.nimbus.DefaultTopologyValidator", "supervisor.slots.ports" (1027 1028 1029), "topology.environment" nil, "topology.debug" false, "nimbus.task.launch.secs" 120, "nimbus.supervisor.timeout.secs" 60, "topology.kryo.register" nil, "topology.message.timeout.secs" 60, "task.refresh.poll.secs" 10, "topology.workers" 2, "supervisor.childopts" "-Xmx256m", "nimbus.thrift.port" 6627, "topology.stats.sample.rate" 0.05, "worker.heartbeat.frequency.secs" 1, "topology.tuple.serializer" "backtype.storm.serialization.types.ListDelegateSerializer", "topology.disruptor.wait.strategy" "com.lmax.disruptor.BlockingWaitStrategy", "topology.multilang.serializer" "backtype.storm.multilang.JsonSerializer", "nimbus.task.timeout.secs" 30, "storm.zookeeper.connection.timeout" 15000, "topology.kryo.factory" "backtype.storm.serialization.DefaultKryoFactory", "drpc.invocations.port" 3773, "logviewer.port" 8000, "zmq.threads" 1, "storm.zookeeper.retry.times" 5, "topology.worker.receiver.thread.count" 1, "storm.thrift.transport" "backtype.storm.security.auth.SimpleTransportPlugin", "topology.state.synchronization.timeout.secs" 60, "supervisor.worker.timeout.secs" 30, "nimbus.file.copy.expiration.secs" 600, "storm.messaging.transport" "backtype.storm.messaging.netty.Context", "logviewer.appender.name" "A1", "storm.messaging.netty.max_wait_ms" 1000, "drpc.request.timeout.secs" 600, "storm.local.mode.zmq" false, "ui.port" 8080, "nimbus.childopts" "-Xmx1024m", "storm.cluster.mode" "local", "topology.max.task.parallelism" nil, "storm.messaging.netty.transfer.batch.size" 262144, "topology.classpath" nil, "streamparse.log.level" "debug"}
18984 [Thread-6] INFO  backtype.storm.daemon.worker - Worker 33973706-4ef7-4062-bd86-c6148498a38a for storm wordcount-1-1470427504 on 26a3d3d0-953d-4089-acdd-719464f28315:1027 has finished loading
19002 [Thread-4] INFO  backtype.storm.daemon.executor - Loading executor __system:[-1 -1]
19003 [Thread-4] INFO  backtype.storm.daemon.executor - Loaded executor tasks __system:[-1 -1]
19015 [Thread-4] INFO  backtype.storm.daemon.executor - Finished loading executor __system:[-1 -1]
19022 [Thread-4] INFO  backtype.storm.daemon.executor - Loading executor __acker:[1 1]
19022 [Thread-4] INFO  backtype.storm.daemon.executor - Loaded executor tasks __acker:[1 1]
19038 [Thread-4] INFO  backtype.storm.daemon.executor - Timeouts disabled for executor __acker:[1 1]
19038 [Thread-4] INFO  backtype.storm.daemon.executor - Finished loading executor __acker:[1 1]
19042 [Thread-4] INFO  backtype.storm.daemon.worker - Worker has topology config {"storm.id" "wordcount-1-1470427504", "dev.zookeeper.path" "/tmp/dev-storm-zookeeper", "topology.tick.tuple.freq.secs" nil, "topology.builtin.metrics.bucket.size.secs" 60, "topology.fall.back.on.java.serialization" true, "topology.max.error.report.per.interval" 5, "zmq.linger.millis" 0, "topology.skip.missing.kryo.registrations" true, "storm.messaging.netty.client_worker_threads" 1, "ui.childopts" "-Xmx768m", "storm.zookeeper.session.timeout" 20000, "nimbus.reassign" true, "topology.trident.batch.emit.interval.millis" 50, "storm.messaging.netty.flush.check.interval.ms" 10, "nimbus.monitor.freq.secs" 10, "logviewer.childopts" "-Xmx128m", "java.library.path" "/usr/local/lib:/opt/local/lib:/usr/lib", "topology.executor.send.buffer.size" 1024, "storm.local.dir" "/tmp/a30dfbbc-3171-47fe-874a-faf71a71834d", "storm.messaging.netty.buffer_size" 5242880, "supervisor.worker.start.timeout.secs" 120, "topology.enable.message.timeouts" true, "nimbus.cleanup.inbox.freq.secs" 600, "nimbus.inbox.jar.expiration.secs" 3600, "drpc.worker.threads" 64, "storm.meta.serialization.delegate" "backtype.storm.serialization.DefaultSerializationDelegate", "topology.worker.shared.thread.pool.size" 4, "nimbus.host" "localhost", "storm.messaging.netty.min_wait_ms" 100, "storm.zookeeper.port" 2000, "transactional.zookeeper.port" nil, "topology.executor.receive.buffer.size" 1024, "transactional.zookeeper.servers" nil, "storm.zookeeper.root" "/storm", "storm.zookeeper.retry.intervalceiling.millis" 30000, "supervisor.enable" true, "storm.messaging.netty.server_worker_threads" 1, "storm.zookeeper.servers" ["localhost"], "transactional.zookeeper.root" "/transactional", "topology.acker.executors" 2, "streamparse.log.path" "/root/tweetwordcount/logs", "topology.kryo.decorators" (), "topology.name" "wordcount", "topology.transfer.buffer.size" 1024, "topology.worker.childopts" nil, "drpc.queue.size" 128, "worker.childopts" "-Xmx768m", "supervisor.heartbeat.frequency.secs" 5, "topology.error.throttle.interval.secs" 10, "zmq.hwm" 0, "drpc.port" 3772, "supervisor.monitor.frequency.secs" 3, "drpc.childopts" "-Xmx768m", "topology.receiver.buffer.size" 8, "task.heartbeat.frequency.secs" 3, "topology.tasks" nil, "storm.messaging.netty.max_retries" 300, "topology.spout.wait.strategy" "backtype.storm.spout.SleepSpoutWaitStrategy", "nimbus.thrift.max_buffer_size" 1048576, "topology.max.spout.pending" 5000, "storm.zookeeper.retry.interval" 1000, "topology.sleep.spout.wait.strategy.time.ms" 1, "nimbus.topology.validator" "backtype.storm.nimbus.DefaultTopologyValidator", "supervisor.slots.ports" (1024 1025 1026), "topology.environment" nil, "topology.debug" false, "nimbus.task.launch.secs" 120, "nimbus.supervisor.timeout.secs" 60, "topology.kryo.register" nil, "topology.message.timeout.secs" 60, "task.refresh.poll.secs" 10, "topology.workers" 2, "supervisor.childopts" "-Xmx256m", "nimbus.thrift.port" 6627, "topology.stats.sample.rate" 0.05, "worker.heartbeat.frequency.secs" 1, "topology.tuple.serializer" "backtype.storm.serialization.types.ListDelegateSerializer", "topology.disruptor.wait.strategy" "com.lmax.disruptor.BlockingWaitStrategy", "topology.multilang.serializer" "backtype.storm.multilang.JsonSerializer", "nimbus.task.timeout.secs" 30, "storm.zookeeper.connection.timeout" 15000, "topology.kryo.factory" "backtype.storm.serialization.DefaultKryoFactory", "drpc.invocations.port" 3773, "logviewer.port" 8000, "zmq.threads" 1, "storm.zookeeper.retry.times" 5, "topology.worker.receiver.thread.count" 1, "storm.thrift.transport" "backtype.storm.security.auth.SimpleTransportPlugin", "topology.state.synchronization.timeout.secs" 60, "supervisor.worker.timeout.secs" 30, "nimbus.file.copy.expiration.secs" 600, "storm.messaging.transport" "backtype.storm.messaging.netty.Context", "logviewer.appender.name" "A1", "storm.messaging.netty.max_wait_ms" 1000, "drpc.request.timeout.secs" 600, "storm.local.mode.zmq" false, "ui.port" 8080, "nimbus.childopts" "-Xmx1024m", "storm.cluster.mode" "local", "topology.max.task.parallelism" nil, "storm.messaging.netty.transfer.batch.size" 262144, "topology.classpath" nil, "streamparse.log.level" "debug"}
19042 [Thread-4] INFO  backtype.storm.daemon.worker - Worker eb1742c3-27ed-4005-b2a2-2ec4700a08be for storm wordcount-1-1470427504 on a1308e44-b048-4add-bc32-018de26ec83e:1024 has finished loading
20036 [Thread-12-count-bolt] INFO  backtype.storm.daemon.executor - Preparing bolt count-bolt:(3)
20038 [Thread-10-__acker] INFO  backtype.storm.daemon.executor - Preparing bolt __acker:(2)
20096 [Thread-21-__system] INFO  backtype.storm.daemon.executor - Preparing bolt __system:(-1)
20096 [Thread-14-count-bolt] INFO  backtype.storm.daemon.executor - Preparing bolt count-bolt:(4)
20097 [Thread-16-word-spout] INFO  backtype.storm.daemon.executor - Opening spout word-spout:(5)
20098 [Thread-23-__acker] INFO  backtype.storm.daemon.executor - Preparing bolt __acker:(1)
20099 [Thread-18-__system] INFO  backtype.storm.daemon.executor - Preparing bolt __system:(-1)
20157 [Thread-18-__system] INFO  backtype.storm.daemon.executor - Prepared bolt __system:(-1)
20170 [Thread-21-__system] INFO  backtype.storm.daemon.executor - Prepared bolt __system:(-1)
20174 [Thread-10-__acker] INFO  backtype.storm.daemon.executor - Prepared bolt __acker:(2)
20174 [Thread-23-__acker] INFO  backtype.storm.daemon.executor - Prepared bolt __acker:(1)
20199 [Thread-12-count-bolt] INFO  backtype.storm.utils.ShellProcess - Storm multilang serializer: backtype.storm.multilang.JsonSerializer
20209 [Thread-14-count-bolt] INFO  backtype.storm.utils.ShellProcess - Storm multilang serializer: backtype.storm.multilang.JsonSerializer
20211 [Thread-16-word-spout] INFO  backtype.storm.utils.ShellProcess - Storm multilang serializer: backtype.storm.multilang.JsonSerializer
20691 [Thread-16-word-spout] INFO  backtype.storm.spout.ShellSpout - Launched subprocess with pid 3483
20713 [Thread-12-count-bolt] INFO  backtype.storm.task.ShellBolt - Launched subprocess with pid 3484
20741 [Thread-16-word-spout] INFO  backtype.storm.daemon.executor - Opened spout word-spout:(5)
20742 [Thread-14-count-bolt] INFO  backtype.storm.task.ShellBolt - Launched subprocess with pid 3482
20744 [Thread-16-word-spout] INFO  backtype.storm.daemon.executor - Activating spout word-spout:(5)
20744 [Thread-16-word-spout] INFO  backtype.storm.spout.ShellSpout - Start checking heartbeat...
20762 [Thread-14-count-bolt] INFO  backtype.storm.task.ShellBolt - Start checking heartbeat...
20763 [Thread-14-count-bolt] INFO  backtype.storm.daemon.executor - Prepared bolt count-bolt:(4)
20763 [Thread-12-count-bolt] INFO  backtype.storm.task.ShellBolt - Start checking heartbeat...
20809 [Thread-12-count-bolt] INFO  backtype.storm.daemon.executor - Prepared bolt count-bolt:(3)
20831 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 1
20832 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 1
20841 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 1
20843 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 1
20844 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 1
20845 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 1
20845 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 1
20846 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 2
20847 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 2
20858 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 2
20861 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 3
20863 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 3
20873 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 1
20875 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 2
20876 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 2
20877 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 2
20878 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 3
20879 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 3
20881 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 4
20894 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 4
20896 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 3
20906 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 3
20910 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 5
20927 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 5
20930 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 4
20933 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 4
20944 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 2
20947 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 4
20948 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 2
20949 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 4
20961 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 3
20964 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 3
20966 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 5
20977 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 5
20981 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 6
20994 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 6
20997 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 4
21053 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 6
21053 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 6
21054 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 4
21064 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 5
21081 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 5
21082 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 5
21083 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 7
21084 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 7
21084 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 8
21088 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 5
21089 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 7
21090 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 7
21091 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 8
21104 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 6
21105 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 6
21106 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 8
21122 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 7
21124 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 9
21125 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 9
21142 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 6
21143 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 6
21157 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 10
21201 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 8
21202 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 7
21203 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 9
21208 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 9
21222 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 8
21223 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 7
21224 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 9
21234 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 11
21235 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 10
21241 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 10
21251 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 8
21252 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 7
21253 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 9
21254 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 11
21256 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 8
21267 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 10
21267 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 8
21296 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 10
21300 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 10
21302 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 12
21305 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 12
21321 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 11
21324 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 13
21337 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 12
21340 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 14
21353 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 13
21355 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 9
21358 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 11
21361 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 10
21373 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 12
21376 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 11
21395 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 11
21430 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 14
21431 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 12
21458 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 13
21463 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 12
21498 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 15
21499 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 13
21499 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 16
21500 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 14
21516 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 14
21579 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 13
21580 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 9
21581 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 11
21581 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 10
21597 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 17
21597 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 15
21644 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 12
21644 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 18
21645 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 15
21655 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 19
21656 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 11
21657 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 16
21659 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 20
21660 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 16
21671 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 13
21672 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 17
21677 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 21
21678 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 17
21678 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 22
21687 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 18
21705 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 14
21707 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 12
21730 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 14
21731 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 18
21741 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 15
21742 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 13
21743 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 16
21743 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 14
21744 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 15
21746 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 19
21747 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 17
21748 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 23
21748 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 15
21749 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 18
21750 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 19
21764 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 15
21770 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 16
21771 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 19
21772 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 20
21773 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 16
21773 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 20
21774 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 24
21775 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 16
21790 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 21
21791 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 13
21795 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 17
21796 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 17
21797 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 21
21798 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 22
21799 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 17
21800 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 25
21816 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 22
21817 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 20
21817 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 18
21818 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 14
21820 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 18
21862 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 15
21863 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 19
21863 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 23
21864 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 19
21865 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 16
21868 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 20
21868 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 24
21878 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 18
21879 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 21
21884 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 19
21885 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 23
21898 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 20
21898 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 24
21899 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 26
21900 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 22
21901 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 27
21912 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 23
21913 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 28
21940 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 25
21941 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 29
21942 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 26
21985 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 21
21986 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 21
21987 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 24
21988 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 22
21989 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 27
22000 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 30
22001 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 25
22002 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 31
22002 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 26
22003 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 32
22004 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 28
22004 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 33
22005 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 29
22017 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 34
22018 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 27
22019 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 23
22038 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 17
22047 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 22
22048 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 25
22049 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 20
22050 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 18
22050 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 21
22051 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 19
22052 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 23
22052 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 20
22054 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 28
22054 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 24
22055 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 30
22080 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 24
22081 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 26
22082 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 22
22082 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 27
22085 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 23
22087 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 28
22096 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 25
22097 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 29
22098 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 26
22099 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 21
22099 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 24
22100 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 22
22101 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 27
22101 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 30
22102 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 25
22103 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 31
22103 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 26
22112 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 32
22147 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 25
22148 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 31
22149 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 26
22149 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 29
22113 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 28
22150 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 33
22151 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 29
22151 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 34
22152 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 27
22173 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 27
22174 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 23
22175 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 28
22190 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 24
22190 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 30
22191 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 25
22234 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 31
22230 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 32
22236 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 26
22248 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 29
22249 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 27
22253 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 32
22255 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 35
22272 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 30
22274 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 36
22275 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 31
22276 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 28
22291 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 32
22292 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 29
22293 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 33
22293 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 30
22294 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 34
22310 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 37
22237 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 35
22363 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 30
22364 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 35
22365 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 36
22366 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 38
22376 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 31
22377 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 33
22378 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 28
22379 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 39
22380 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 32
22381 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 36
22382 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 29
22383 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 40
22393 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 33
22393 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 37
22395 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 30
22396 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 34
22408 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 37
22409 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 35
22411 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 38
22412 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 33
22412 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 39
22413 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 36
22414 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 40
22414 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 37
22415 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 41
22425 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 38
22426 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 31
22427 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 39
22478 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 32
22478 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 41
22490 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 40
22492 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 42
22493 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 41
22495 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 33
22496 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 34
22522 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 38
22523 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 31
22524 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 39
22524 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 32
22525 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 40
22528 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 43
22529 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 35
22538 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 44
22541 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 42
22541 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 41
22542 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 33
22543 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 42
22544 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 34
22544 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 45
22545 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 43
22545 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 43
22546 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 35
22547 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 34
22548 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 44
22549 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 36
22549 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 42
22564 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 45
22565 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 43
22565 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 34
22566 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 36
22579 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 35
22579 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 44
22580 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 46
22581 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 37
22582 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 47
22597 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 38
22599 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 36
22601 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 45
22603 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 48
22616 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 39
22619 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 37
22620 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 46
22637 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 35
22639 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 44
22648 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 46
22651 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 37
22652 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 47
22655 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 38
22689 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 38
22689 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 47
22690 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 49
22691 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 48
22693 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 50
22694 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 49
22711 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 39
22733 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 36
22734 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 45
22735 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 48
22736 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 39
22737 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 37
22737 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 46
22738 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 38
22739 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 47
22740 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 49
22740 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 48
22741 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 50
22742 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 49
22743 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 39
22744 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 50
22757 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 50
22758 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 51
22759 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 51
22760 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 40
22760 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 52
22761 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 41
22764 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 53
22781 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 42
22879 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 54
22880 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 51
22881 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 52
22882 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 51
22882 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 55
22883 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 40
22884 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 53
22885 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 40
22885 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 52
22894 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 54
22899 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 41
22905 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 56
22919 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 55
22919 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 57
22920 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 43
22921 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 41
22921 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 56
22922 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 42
22923 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 57
22923 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 43
22924 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 44
22925 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 44
22925 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 45
22935 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 53
22936 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 42
22937 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 54
22937 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 52
22938 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 55
22942 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 53
22943 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 40
22944 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 54
22945 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 56
22946 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 55
22946 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 57
22960 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 45
22963 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 46
22965 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 58
23030 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 58
23031 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 59
23041 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 47
23045 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 46
23045 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 48
23046 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 47
23050 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 59
23051 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 60
23068 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 49
23069 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 48
23070 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 43
23071 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 41
23071 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 56
23072 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 42
23072 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 60
23075 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 49
23075 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 61
23076 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 50
23085 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 57
23085 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 43
23086 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 44
23086 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 44
23087 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 45
23097 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 45
23098 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 46
23098 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 58
23099 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 58
23100 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 59
23101 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 47
23102 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 46
23102 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 48
23103 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 47
23104 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 59
23104 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 60
23105 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 49
23105 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 48
23106 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 60
23107 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 50
23108 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 61
23125 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 49
23126 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 61
23127 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 50
23127 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 50
23128 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 61
23129 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 51
23144 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 62
23149 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 62
23108 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 51
23199 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 62
23200 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 62
23201 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 63
23211 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 52
23212 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 63
23213 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 52
23213 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 51
23229 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 51
23230 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 53
23231 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 64
23262 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 53
23263 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 54
23264 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 64
23266 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 65
23275 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 54
23277 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 63
23277 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 65
23279 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 63
23281 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 52
23282 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 64
23292 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 53
23294 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 65
23296 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 54
23330 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 52
23340 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 64
23341 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 53
23342 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 65
23343 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 54
23344 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 66
23344 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 66
23345 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 67
23356 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 67
23356 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 66
23357 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 66
23358 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 67
23359 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 67
23359 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 68
23360 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 55
23389 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 68
23390 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 55
23391 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 69
23394 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 69
23396 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 56
23406 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 56
23410 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 55
23411 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 55
23421 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 68
23422 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 68
23424 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 56
23427 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 69
23457 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 56
23458 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 69
23459 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 57
23460 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 70
23460 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 58
23461 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 57
23477 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 59
23506 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 57
23507 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 70
23508 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 58
23509 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 57
23523 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 59
23523 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 58
23525 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 58
23525 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 60
23526 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 59
23527 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 60
23529 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 59
23530 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 70
23540 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 70
23543 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 60
23544 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 60
23546 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 71
23572 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 71
23577 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 61
23614 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 71
23632 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 72
23633 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 62
23634 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 61
23635 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 63
23671 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 71
23685 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 62
23704 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 61
23708 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 72
23717 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 62
23718 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 72
23719 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 73
23720 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 73
23721 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 74
23723 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 64
23724 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 75
23727 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 74
23728 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 63
23791 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 61
23793 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 63
23794 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 62
23794 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 72
23796 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 73
23811 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 65
23812 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 64
23813 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 75
23814 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 76
23815 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 66
23815 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 77
23816 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 76
23830 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 78
23831 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 77
23832 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 79
23832 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 78
23833 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 65
23834 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 67
23835 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 80
23835 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 79
23836 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 66
23836 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 68
23837 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 67
23838 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 73
23839 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 74
23839 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 64
23840 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 75
23841 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 74
23842 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 63
23855 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 80
23856 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 81
23856 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 81
23857 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 82
23858 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 69
23858 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 83
23859 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 70
23872 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 68
23874 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 71
23879 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 84
23882 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 82
23888 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 85
23896 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 72
23897 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 86
23911 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 65
23914 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 64
23919 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 75
23928 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 83
23936 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 76
23936 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 66
23937 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 77
23962 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 87
23968 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 84
23969 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 69
23970 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 73
23971 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 88
23996 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 76
24001 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 78
24001 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 77
24002 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 79
24010 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 85
24011 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 70
24011 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 74
24011 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 71
24025 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 78
24026 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 65
24033 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 86
24033 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 72
24034 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 75
24035 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 89
24035 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 67
24036 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 80
24041 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 79
24042 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 66
24044 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 76
24075 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 68
24075 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 67
24082 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 80
24083 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 81
24084 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 81
24085 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 82
24089 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 69
24090 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 83
24091 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 70
24091 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 68
24092 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 71
24092 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 84
24138 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 73
24139 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 87
24140 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 90
24141 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 88
24165 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 82
24166 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 85
24183 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 74
24184 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 77
24191 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 75
24191 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 78
24192 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 76
24193 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 89
24239 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 77
24240 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 90
24242 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 91
24255 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 91
24255 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 92
24257 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 92
24258 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 93
24258 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 79
24270 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 78
24272 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 80
24274 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 79
24281 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 72
24282 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 86
24288 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 81
24306 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 83
24307 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 87
24307 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 84
24308 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 69
24314 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 94
24315 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 93
24316 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 73
24321 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 88
24322 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 85
24322 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 70
24323 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 74
24324 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 71
24324 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 86
24325 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 72
24330 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 75
24331 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 89
24331 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 76
24332 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 73
24332 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 87
24333 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 90
24338 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 88
24338 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 74
24339 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 77
24340 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 75
24340 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 78
24342 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 76
24343 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 89
24344 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 77
24344 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 90
24345 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 91
24347 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 91
24348 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 92
24358 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 95
24361 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 94
24362 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 92
24363 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 93
24363 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 79
24364 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 78
24381 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 80
24383 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 95
24399 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 81
24402 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 82
24404 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 82
24405 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 96
24425 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 80
24426 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 79
24427 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 81
24428 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 94
24428 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 93
24452 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 96
24454 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 83
24457 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 83
24466 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 95
24469 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 94
24469 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 80
24470 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 95
24471 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 81
24471 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 82
24472 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 82
24472 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 96
24475 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 96
24476 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 83
24477 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 83
24492 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 84
24494 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 84
24495 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 84
24497 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 84
24507 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 85
24508 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 85
24515 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 85
24517 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 97
24527 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 85
24528 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 97
24530 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 86
24531 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 86
24545 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 86
24547 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 97
24550 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 87
24534 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 86
24613 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 98
24614 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 98
24615 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 99
24615 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 99
24627 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 87
24627 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 100
24628 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 100
24629 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 101
24629 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 88
24630 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 88
24641 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 89
24643 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 89
24644 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 101
24644 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 102
24646 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 90
24657 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 97
24657 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 87
24658 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 98
24659 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 98
24659 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 99
24660 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 99
24660 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 87
24661 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 100
24661 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 100
24662 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 101
24663 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 88
24663 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 88
24664 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 89
24674 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 103
24676 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 102
24679 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 90
24705 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 89
24706 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 101
24707 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 102
24707 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 90
24718 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 91
24720 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 104
24722 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 92
24723 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 103
24724 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 102
24725 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 90
24725 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 91
24726 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 104
24727 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 105
24742 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 103
24760 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 92
24761 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 105
24761 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 103
24762 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 91
24762 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 104
24763 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 92
24763 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 93
24764 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 93
24780 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 105
24781 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 94
24791 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 91
24796 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 104
24797 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 92
24798 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 93
24812 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 94
24824 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 106
24827 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 106
24829 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 107
24831 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 107
24834 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 108
24848 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 93
24849 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 105
24849 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 94
24852 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 94
24853 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 106
24853 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 106
24854 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 107
24864 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 107
24865 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 108
24871 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 108
24873 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 108
24889 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 95
24892 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 95
24893 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 109
24895 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 109
24906 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 96
24908 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 110
24910 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 97
24920 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 111
24961 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 110
24962 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 112
24963 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 98
24964 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 113
24964 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 95
24965 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 95
24965 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 109
24966 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 109
24966 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 96
24967 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 110
24968 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 97
24977 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 99
24979 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 96
24979 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 111
24980 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 114
24981 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 112
24982 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 97
24984 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 100
24993 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 111
24994 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 110
24994 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 112
24995 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 98
24995 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 113
24996 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 99
24997 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 96
24997 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 111
24998 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 114
24998 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 112
24999 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 97
24999 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 100
25000 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 115
25010 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 115
25012 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 113
25013 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 113
25014 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 116
25015 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 116
25016 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 114
25027 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 114
25029 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 117
25030 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 117
25032 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 101
25042 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 101
25044 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 118
25045 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 118
25047 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 115
25048 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 115
25058 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 98
25061 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 98
25062 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 116
25064 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 116
25065 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 119
25075 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 119
25077 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 102
25079 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 102
25080 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 120
25081 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 120
25091 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 117
25096 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 117
25106 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 99
25108 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 99
25110 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 103
25111 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 121
25123 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 104
25125 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 122
25127 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 105
25129 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 100
25140 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 106
25141 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 123
25144 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 107
25146 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 101
25177 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 103
25181 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 121
25205 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 104
25205 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 122
25206 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 105
25206 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 100
25207 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 106
25216 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 123
25252 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 118
25253 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 124
25254 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 119
25254 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 125
25255 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 120
25264 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 107
25265 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 101
25266 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 118
25267 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 124
25268 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 119
25269 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 125
25284 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 120
25286 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 126
25287 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 126
25289 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 108
25290 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 108
25292 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 102
25307 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 102
25359 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 109
25359 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 103
25360 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 121
25361 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 127
25370 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 122
25370 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 128
25371 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 123
25371 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 109
25372 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 103
25372 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 121
25373 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 127
25374 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 122
25374 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 128
25375 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 123
25377 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 104
25386 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 104
25391 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 124
25392 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 124
25438 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 129
25455 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 129
25456 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 125
25467 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 125
25468 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 130
25471 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 110
25473 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 105
25501 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 130
25502 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 110
25513 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 126
25513 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 131
25514 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 111
25516 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 106
25518 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 112
25547 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 105
25549 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 126
25549 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 132
25550 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 131
25551 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 127
25551 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 111
25560 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 133
25561 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 106
25561 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 113
25562 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 134
25569 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 114
25570 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 135
25572 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 128
25574 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 136
25585 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 129
25596 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 112
25603 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 132
25604 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 127
25605 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 133
25606 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 113
25606 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 134
25607 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 114
25608 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 135
25617 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 128
25618 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 107
25619 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 115
25619 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 137
25623 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 116
25624 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 138
25633 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 136
25634 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 129
25635 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 107
25635 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 115
25636 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 137
25649 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 116
25651 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 138
25652 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 117
25654 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 117
25655 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 139
25656 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 139
25667 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 130
25668 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 130
25669 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 140
25671 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 140
25673 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 131
25683 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 131
25684 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 108
25686 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 108
25688 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 132
25689 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 132
25699 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 141
25700 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 141
25701 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 133
25703 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 133
25715 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 109
25717 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 109
25718 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 134
25720 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 134
25721 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 142
25734 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 118
25736 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 110
25737 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 135
25763 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 142
25765 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 118
25765 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 110
25769 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 135
25781 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 111
25781 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 136
25782 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 112
25783 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 137
25783 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 143
25784 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 119
25784 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 113
25785 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 120
25786 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 114
25786 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 121
25797 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 144
25799 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 138
25802 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 145
25812 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 139
25814 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 115
25816 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 140
25818 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 146
25829 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 122
25864 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 111
25866 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 136
25880 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 112
25882 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 137
25883 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 143
25884 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 119
25887 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 113
25896 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 120
25897 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 114
25898 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 116
25898 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 123
25899 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 147
25899 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 124
25899 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 121
25900 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 144
25901 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 138
25901 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 145
25902 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 139
25902 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 115
25903 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 140
25903 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 146
25912 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 122
25914 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 148
25916 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 125
25931 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 116
25934 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 123
25935 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 147
25936 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 124
:25939 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 148
25957 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 125
25959 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 117
25960 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 117
25969 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 141
25971 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 141
25972 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 118
25974 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 126
25976 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 119
25978 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 127
25980 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 120
25995 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 128
25998 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 149
25999 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 142
26001 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 121
26013 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 118
26014 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 126
26014 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 119
26015 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 127
26016 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 120
26017 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 128
26017 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 149
26018 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 142
26031 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 121
26033 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 129
26034 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 129
26036 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 150
26046 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 143
26048 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 122
26050 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 130
26051 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 123
26094 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 150
26095 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 143
26096 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 122
26096 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 130
26097 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 123
26098 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 144
26099 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 151
26100 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 145
26111 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 144
26113 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 151
26114 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 145
26115 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 152
26116 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 146
26116 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 153
26117 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 131
26130 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 152
26131 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 146
26132 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 153
26133 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 131
26133 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 124
26161 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 132
26161 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 154
26162 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 124
26163 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 132
26164 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 154
26164 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 133
26165 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 125
26180 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 133
26182 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 125
26247 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 147
26247 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 126
26248 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 148
26261 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 155
26261 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 134
26262 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 147
26262 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 126
26263 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 148
26264 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 155
26264 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 134
26265 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 156
26265 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 149
26266 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 157
26266 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 135
26271 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 127
26271 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 136
26270 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 156
26281 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 149
26283 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 157
26284 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 135
26284 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 127
26293 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 136
26299 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 158
26299 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 150
26300 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 159
26300 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 137
26301 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 160
26302 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 151
26323 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 161
26324 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 138
26325 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 128
26325 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 152
26326 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 129
26329 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 158
26330 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 150
26331 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 159
26331 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 137
26332 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 139
26332 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 162
26346 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 153
26347 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 163
26347 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 140
26348 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 130
26349 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 160
26350 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 151
26350 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 154
26351 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 161
26352 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 164
26352 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 138
26353 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 155
26354 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 128
26354 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 131
26355 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 152
26356 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 141
26357 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 129
26357 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 165
26367 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 142
26369 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 132
26371 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 143
26382 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 166
26425 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 144
26425 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 133
26426 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 145
26427 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 134
26429 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 146
26454 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 139
26456 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 162
26456 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 153
26457 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 163
26472 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 167
26472 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 147
26474 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 135
26484 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 148
26508 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 140
26509 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 130
26509 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 136
26510 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 154
26511 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 164
26511 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 149
26512 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 168
26512 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 155
26513 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 150
26514 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 131
26514 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 141
26515 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 137
26524 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 156
26525 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 169
26526 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 157
26527 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 138
26527 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 158
26528 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 170
26529 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 159
26529 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 171
26531 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 160
26531 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 172
26532 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 161
26533 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 139
26533 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 151
26534 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 173
26535 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 162
26536 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 174
26557 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 165
26557 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 142
26558 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 132
26559 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 143
26559 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 166
26560 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 144
26560 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 133
26561 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 145
26561 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 134
26562 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 146
26563 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 167
26563 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 152
26564 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 147
26573 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 175
26574 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 153
26574 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 140
26575 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 154
26576 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 176
26578 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 155
q26622 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 135
26623 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 148
26623 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 136
26624 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 149
26624 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 168
26625 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 150
26625 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 137
26626 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 156
26627 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 169
26627 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 157
26628 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 177
26629 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 163
26629 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 141
26630 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 164
26630 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 178
26631 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 165
26649 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 142
26649 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 166
26650 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 179
26651 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 167
26651 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 180
26652 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 168
26653 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 181
26663 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 156
26665 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 143
26667 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 157
26678 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 182
26682 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 138
26684 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 158
26685 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 170
26686 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 159
26687 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 171
26730 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 160
26739 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 172
26776 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 169
26776 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 183
26777 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 158
26778 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 144
26780 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 161
26781 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 170
26782 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 184
26791 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 159
26792 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 185
26793 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 171
26793 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 145
26794 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 172
26794 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 139
26795 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 151
26796 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 173
26796 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 162
26797 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 174
26798 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 152
26798 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 186
26799 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 173
26799 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 187
26800 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 160
26801 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 146
26802 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 175
26803 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 153
26817 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 161
26818 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 147
26818 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 162
26819 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 188
26820 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 163
26820 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 189
26821 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 164
26821 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 148
26823 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 165
26825 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 149
26841 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 174
26843 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 150
26845 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 175
26848 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 190
26856 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 140
26857 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 154
26858 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 176
26858 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 155
26860 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 177
26861 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 163
26861 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 141
26862 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 164
26865 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 166
26881 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 178
26882 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 165
26883 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 142
26883 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 166
26884 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 179
26885 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 167
26888 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 180
26915 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 168
26916 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 181
26916 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 156
26917 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 143
26917 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 157
26918 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 182
26919 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 169
26919 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 183
26920 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 158
26920 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 144
26921 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 170
26922 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 184
26922 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 159
26923 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 185
26940 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 171
26941 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 145
26941 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 172
26942 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 186
26943 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 173
26945 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 151
26954 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 187
26955 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 160
26958 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 146
26959 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 161
26959 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 147
26960 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 162
26960 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 188
26961 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 163
26970 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 189
26971 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 164
26971 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 148
26973 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 165
26974 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 149
26974 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 174
26975 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 150
26975 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 175
26976 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 190
26976 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 166
26987 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 151
26988 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 176
26989 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 176
26991 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 191
26992 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 191
26993 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 177
27008 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 177
27010 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 152
27025 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 152
27036 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 178
27038 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 192
27040 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 179
27041 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 193
27051 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 167
27054 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 194
27055 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 168
27057 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 153
27083 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 178
27084 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 192
27085 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 179
27086 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 193
27086 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 167
27087 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 194
27087 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 168
27088 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 153
27089 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 180
27091 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 154
27101 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 180
27103 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 154
27104 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 181
27105 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 155
27106 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 182
27107 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 195
27132 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 169
27133 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 196
27133 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 183
27134 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 197
27134 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 184
27136 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 181
27138 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 155
27139 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 182
27151 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 156
27154 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 170
27165 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 195
27166 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 169
27166 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 196
27167 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 183
27167 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 197
27168 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 184
27168 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 156
27169 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 170
27170 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 157
27171 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 157
27210 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 171
27212 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 171
27212 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 198
27213 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 185
27213 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 158
27214 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 172
27215 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 159
27215 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 173
27216 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 160
27228 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 198
27228 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 185
27229 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 158
27229 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 172
27230 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 159
27230 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 173
27231 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 160
27231 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 174
27232 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 161
27232 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 186
27216 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 174
27262 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 161
27265 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 162
27274 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 186
27275 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 162
27275 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 187
27276 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 163
27276 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 175
27277 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 199
27278 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 188
27291 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 164
27292 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 189
27292 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 200
27293 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 187
27294 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 163
27294 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 175
27297 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 199
27308 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 176
27311 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 165
27312 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 190
27315 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 166
27330 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 177
27346 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 188
27347 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 164
27348 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 189
27348 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 200
27349 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 176
27349 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 165
27350 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 190
27350 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 166
27351 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 177
27351 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 167
27352 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 191
27353 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 168
27354 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 192
27365 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 201
27365 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 167
27367 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 193
27367 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 191
27369 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 168
27370 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 202
27379 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 192
27380 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 201
27396 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 193
27397 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 202
27397 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 194
27398 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 203
27399 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 195
27400 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 204
27400 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 178
27401 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 194
27402 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 203
27402 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 195
27403 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 204
27412 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 205
27414 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 196
27417 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 169
27427 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 179
27445 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 178
27445 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 205
27446 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 196
27447 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 169
27447 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 179
27448 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 206
27449 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 206
27449 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 197
27451 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 170
27451 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 197
27460 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 180
27461 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 170
27462 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 180
27462 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 171
27463 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 181
27464 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 172
27479 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 182
27483 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 173
27493 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 183
27495 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 174
27497 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 184
27499 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 207
27511 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 171
27512 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 181
27512 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 172
27513 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 182
27514 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 173
27529 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 183
27530 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 174
27531 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 184
27532 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 207
27534 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 198
27536 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 208
27536 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 199
27545 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 209
27546 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 200
27546 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 210
27548 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 185
27549 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 211
27552 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 201
27552 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 212
27553 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 186
27567 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 198
27583 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 208
27583 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 199
27584 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 209
27584 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 200
27585 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 210
27585 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 185
27598 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 213
27599 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 187
27600 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 214
27608 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 202
27608 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 215
27609 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 188
27655 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 211
27656 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 201
27656 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 212
27659 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 186
27661 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 213
27662 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 187
27662 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 214
27663 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 202
27664 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 215
27665 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 188
27665 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 175
27666 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 203
27695 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 175
27696 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 203
27696 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 216
27697 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 204
27697 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 176
27698 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 189
27698 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 217
27699 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 205
27700 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 177
27700 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 206
27701 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 218
27701 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 207
27702 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 178
27715 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 208
27716 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 179
27716 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 190
27717 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 219
27731 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 191
27731 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 220
27732 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 192
27733 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 221
27733 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 209
27734 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 222
27734 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 193
27735 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 223
27744 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 216
27744 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 204
27745 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 176
27745 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 189
27746 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 217
27746 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 205
27747 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 177
27750 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 206
27751 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 218
27761 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 194
27764 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 180
27765 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 210
27776 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 224
27781 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 207
27783 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 178
27793 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 208
27793 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 179
27794 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 190
27795 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 219
27795 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 191
27796 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 220
27797 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 192
27797 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 221
27798 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 209
27799 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 222
27799 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 193
27800 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 223
27809 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 194
27809 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 180
27810 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 210
27811 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 211
27812 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 181
27812 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 212
27812 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 225
27813 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 224
27813 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 211
27816 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 181
27825 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 213
27829 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 182
27831 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 195
27847 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 212
27848 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 225
27860 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 213
27860 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 182
27861 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 195
27862 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 183
27862 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 196
27863 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 184
27863 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 214
27864 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 185
27873 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 183
27874 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 196
27875 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 184
27875 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 214
27876 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 185
27877 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 215
27878 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 226
27878 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 197
27880 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 215
27880 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 226
27881 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 197
27890 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 227
27891 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 227
27892 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 198
27894 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 198
27895 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 228
27896 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 228
27907 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 216
27908 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 186
27910 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 199
27912 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 229
27923 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 217
27924 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 187
27927 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 218
27928 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 188
27957 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 216
27960 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 186
27961 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 199
27961 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 229
27973 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 217
27973 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 187
27974 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 218
27976 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 188
27977 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 200
27987 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 200
27988 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 189
27989 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 189
28000 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 201
28004 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 201
28006 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 190
28032 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 190
28035 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 202
28037 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 202
28039 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 230
28050 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 230
28051 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 203
28052 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 203
28054 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 231
28056 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 231
28058 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 204
28059 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 204
28075 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 232
28076 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 232
28078 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 219
28079 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 219
28080 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 233
28082 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 233
28093 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 205
28095 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 205
28096 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 191
28097 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 191
28098 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 206
28099 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 206
28129 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 234
28131 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 234
28132 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 207
28133 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt cat: 207
28134 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 235
28136 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 235
28137 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 220
28138 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 220
28154 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 236
28156 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 236
28157 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 221
28158 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 221
28159 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 192
28171 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 222
28173 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 237
28176 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 223
28207 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt elephant: 192
28208 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 222
28209 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt zebra: 237
28218 [Thread-25] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3484, name:count-bolt dog: 223
28222 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 193
28222 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 224
28223 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 238
28224 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt dog: 208
28224 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 239
28224 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 225
28251 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 240
28251 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 226
28252 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 241
28253 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 227
28254 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt elephant: 242
28255 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 228
28256 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt zebra: 194
28276 [Thread-27] INFO  backtype.storm.task.ShellBolt - ShellLog pid:3482, name:count-bolt cat: 229
Traceback (most recent call last):
  File "/usr/bin/sparse", line 9, in <module>
    load_entry_point('streamparse==2.1.4', 'console_scripts', 'sparse')()
  File "/usr/lib/python2.7/site-packages/streamparse/cli/sparse.py", line 57, in main
    args.func(args)
  File "/usr/lib/python2.7/site-packages/streamparse/cli/run.py", line 81, in main
    debug=args.debug)
  File "/usr/lib/python2.7/site-packages/streamparse/cli/run.py", line 52, in run_local_topology
    run(full_cmd)
  File "/usr/lib/python2.7/site-packages/invoke/__init__.py", line 32, in run
    return Context().run(command, **kwargs)
  File "/usr/lib/python2.7/site-packages/invoke/context.py", line 53, in run
    return runner_class(context=self).run(command, **kwargs)
  File "/usr/lib/python2.7/site-packages/invoke/runners.py", line 335, in run
    raise exception
KeyboardInterrupt
[root@ip-172-31-4-51 tweetwordcount]# ls -l
total 40
drwxr-xr-x 4 root root 4096 Aug  5 20:04 _build
-rw-r--r-- 1 root root  428 Aug  5 20:04 config.json
-rw-r--r-- 1 root root  456 Aug  5 20:04 fabfile.py
drwxr-xr-x 2 root root 4096 Aug  5 20:05 logs
-rw-r--r-- 1 root root  528 Aug  5 20:04 project.clj
-rw-r--r-- 1 root root    0 Aug  5 20:04 README.md
drwxr-xr-x 3 root root 4096 Aug  5 20:04 _resources
drwxr-xr-x 4 root root 4096 Aug  5 20:04 src
-rw-r--r-- 1 root root  456 Aug  5 20:04 tasks.py
drwxr-xr-x 2 root root 4096 Aug  5 20:04 topologies
drwxr-xr-x 2 root root 4096 Aug  5 20:04 virtualenvs
[root@ip-172-31-4-51 tweetwordcount]# cd src
[root@ip-172-31-4-51 src]# ls -l
total 8
drwxr-xr-x 2 root root 4096 Aug  5 20:04 bolts
drwxr-xr-x 2 root root 4096 Aug  5 20:04 spouts
[root@ip-172-31-4-51 src]# cd bolts/
[root@ip-172-31-4-51 bolts]# ls -l
total 4
-rw-r--r-- 1 root root   0 Aug  5 20:04 __init__.py
-rw-r--r-- 1 root root 426 Aug  5 20:04 wordcount.py
[root@ip-172-31-4-51 bolts]# cd ..
[root@ip-172-31-4-51 src]# cd spouts/
[root@ip-172-31-4-51 spouts]# ls -l
total 4
-rw-r--r-- 1 root root   0 Aug  5 20:04 __init__.py
-rw-r--r-- 1 root root 396 Aug  5 20:04 words.py
[root@ip-172-31-4-51 spouts]# vi words.py 
[root@ip-172-31-4-51 spouts]# cd ..
[root@ip-172-31-4-51 src]# cd ..
[root@ip-172-31-4-51 tweetwordcount]# cd topologies/
[root@ip-172-31-4-51 topologies]# vi wordcount.clj 
[root@ip-172-31-4-51 topologies]# cd ..
[root@ip-172-31-4-51 tweetwordcount]# cd src
[root@ip-172-31-4-51 src]# cd spouts/
[root@ip-172-31-4-51 spouts]# ls -l
total 4
-rw-r--r-- 1 root root    0 Aug  5 20:04 __init__.py
-rw-r--r-- 1 root root 2306 Aug  5 20:14 words.py
[root@ip-172-31-4-51 spouts]# vi words.py 
[root@ip-172-31-4-51 spouts]# pwd
/root/tweetwordcount/src/spouts
[root@ip-172-31-4-51 spouts]# cp /root/tweetwordcount/src/spouts/words.py /root/tweets.py
[root@ip-172-31-4-51 spouts]# cd ..
[root@ip-172-31-4-51 src]# cd ..
[root@ip-172-31-4-51 tweetwordcount]# cd ..
[root@ip-172-31-4-51 ~]# ls -l
total 724
-rw-------  1 root root    287 Sep 22  2015 dans_bash_history.txt
drwxr-xr-x  4 root root   4096 Aug  5 20:01 exercise_2
-rw-r--r--  1 root root  12402 Jul 11 18:07 ez_setup.py
-rw-r--r--  1 root root    763 Aug  5 17:04 finalresults.py
-rw-r--r--  1 root root    446 Aug  5 16:38 histogram.py
drwxr-xr-x 11 root root   4096 May  4  2015 ipython
drwxr-xr-x  5 root root   4096 May  4  2015 pgxl-deployment-tools
-rw-r--r--  1 root root 655364 Jul 11 18:07 setuptools-24.0.2.zip
-rwxr-xr-x  1 root root    221 Sep 22  2015 start-hadoop.sh
-rwxr-xr-x  1 root root    252 Sep 22  2015 start-hadoop.sh~
-rwxr-xr-x  1 root root    209 Sep 22  2015 stop-hadoop.sh
-rwxr-xr-x  1 root root    222 Sep 22  2015 stop-hadoop.sh~
drwxr-xr-x 11 root root   4096 May  4  2015 streamparse
drwxr-xr-x  8 root root   4096 Jul 11 19:33 tweetcount
-rw-r--r--  1 root root   2306 Aug  5 20:16 tweets.py
drwxr-xr-x  8 root root   4096 Aug  5 20:04 tweetwordcount
-rw-r--r--  1 root root    765 Jul 29 01:42 Twittercredentials.py
[root@ip-172-31-4-51 ~]# vi tweets.py
[root@ip-172-31-4-51 ~]# cd tweet
-bash: cd: tweet: No such file or directory
[root@ip-172-31-4-51 ~]# cd tweetcount/
[root@ip-172-31-4-51 tweetcount]# ls -l
total 40
drwxr-xr-x 4 root root 4096 Jul 11 19:33 _build
-rw-r--r-- 1 root root  428 Jul 11 18:27 config.json
-rw-r--r-- 1 root root  456 Jul 11 18:27 fabfile.py
drwxr-xr-x 2 root root 4096 Aug  5 18:39 logs
-rw-r--r-- 1 root root  524 Jul 11 18:27 project.clj
-rw-r--r-- 1 root root    0 Jul 11 18:27 README.md
drwxr-xr-x 3 root root 4096 Aug  5 18:39 _resources
drwxr-xr-x 4 root root 4096 Jul 11 18:27 src
-rw-r--r-- 1 root root  456 Jul 11 18:27 tasks.py
drwxr-xr-x 2 root root 4096 Aug  2 19:26 topologies
drwxr-xr-x 2 root root 4096 Jul 11 18:27 virtualenvs
[root@ip-172-31-4-51 tweetcount]# cd src
[root@ip-172-31-4-51 src]# cd bolts/
[root@ip-172-31-4-51 bolts]# cd ..
[root@ip-172-31-4-51 src]# cd spouts/
[root@ip-172-31-4-51 spouts]# ls -l
total 4
-rw-r--r-- 1 root root   0 Jul 11 18:27 __init__.py
-rw-r--r-- 1 root root 730 Jul 13 01:52 sentences.py
[root@ip-172-31-4-51 spouts]# rm sentences.py 
[root@ip-172-31-4-51 spouts]# cp /root/tweets.py 
cp: missing destination file operand after `/root/tweets.py'
Try `cp --help' for more information.
[root@ip-172-31-4-51 spouts]# pwd
/root/tweetcount/src/spouts
[root@ip-172-31-4-51 spouts]# cp /root/tweets.py /root/tweetcount/src/spouts/tweets.py
[root@ip-172-31-4-51 spouts]# ls -l
total 4
-rw-r--r-- 1 root root    0 Jul 11 18:27 __init__.py
-rw-r--r-- 1 root root 2307 Aug  5 20:18 tweets.py
[root@ip-172-31-4-51 spouts]# cd ..
[root@ip-172-31-4-51 src]# cd ..
[root@ip-172-31-4-51 tweetcount]# cd t
-bash: cd: t: No such file or directory
[root@ip-172-31-4-51 tweetcount]# cd topologies/
[root@ip-172-31-4-51 topologies]# ls -l
total 4
-rw-r--r-- 1 root root 562 Jul 13 03:10 tweetcount.clj
[root@ip-172-31-4-51 topologies]# vi tweetcount.clj 
[root@ip-172-31-4-51 topologies]# cd ..
[root@ip-172-31-4-51 tweetcount]# cd src
[root@ip-172-31-4-51 src]# cd spouts/
[root@ip-172-31-4-51 spouts]# ls -l
total 4
-rw-r--r-- 1 root root    0 Jul 11 18:27 __init__.py
-rw-r--r-- 1 root root 2307 Aug  5 20:18 tweets.py
[root@ip-172-31-4-51 spouts]# vi tweets.py 
[root@ip-172-31-4-51 spouts]# cd ..
[root@ip-172-31-4-51 src]# cd ..
[root@ip-172-31-4-51 tweetcount]# cd topologies/
[root@ip-172-31-4-51 topologies]# ls -l
total 4
-rw-r--r-- 1 root root 550 Aug  5 20:19 tweetcount.clj
[root@ip-172-31-4-51 topologies]# vi tweetcount.clj 
[root@ip-172-31-4-51 topologies]# cd ..
[root@ip-172-31-4-51 tweetcount]# cd src
[root@ip-172-31-4-51 src]# cd bolts/
[root@ip-172-31-4-51 bolts]# ls -l
total 8
-rw-r--r-- 1 root root   0 Jul 11 18:27 __init__.py
-rw-r--r-- 1 root root 656 Jul 13 01:58 parse.py
-rw-r--r-- 1 root root 393 Jul 13 02:21 tweetcounter.py
[root@ip-172-31-4-51 bolts]# vi tweetcounter.py 
[root@ip-172-31-4-51 bolts]# cd ..
[root@ip-172-31-4-51 src]# cd ..
[root@ip-172-31-4-51 tweetcount]# cd topologies/
[root@ip-172-31-4-51 topologies]# ls -l
total 4
-rw-r--r-- 1 root root 554 Aug  5 20:20 tweetcount.clj
[root@ip-172-31-4-51 topologies]# vi tweetcount.clj 
[root@ip-172-31-4-51 topologies]# cd ..
[root@ip-172-31-4-51 tweetcount]# cd src
[root@ip-172-31-4-51 src]# cd bolts/
[root@ip-172-31-4-51 bolts]# ls -l
total 8
-rw-r--r-- 1 root root   0 Jul 11 18:27 __init__.py
-rw-r--r-- 1 root root 656 Jul 13 01:58 parse.py
-rw-r--r-- 1 root root 854 Aug  5 20:24 tweetcounter.py
[root@ip-172-31-4-51 bolts]# vi parse.py 
[root@ip-172-31-4-51 bolts]# cd ..
[root@ip-172-31-4-51 src]# cd ..
[root@ip-172-31-4-51 tweetcount]# sparse run
Running tweetcount topology...
Routing Python logging to /root/tweetcount/logs.
Running lein command to run local cluster:
lein run -m streamparse.commands.run/-main topologies/tweetcount.clj -t 0 --option 'topology.workers=2' --option 'topology.acker.executors=2' --option 'streamparse.log.path="/root/tweetcount/logs"' --option 'streamparse.log.level="debug"'
WARNING: You're currently running as root; probably by accident.
Press control-C to abort or Enter to continue as root.
Set LEIN_ROOT to disable this warning.

3925 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:zookeeper.version=3.4.6-1569965, built on 02/20/2014 09:09 GMT
3955 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:host.name=ip-172-31-4-51.ec2.internal
3955 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:java.version=1.7.0_79
3955 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:java.vendor=Oracle Corporation
3956 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:java.home=/opt/jdk1.7.0_79/jre
3956 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:java.class.path=/root/tweetcount/test:/root/tweetcount/topologies:/root/tweetcount/dev-resources:/root/tweetcount/_resources:/root/tweetcount/_build/classes:/root/.m2/repository/ch/qos/logback/logback-classic/1.0.13/logback-classic-1.0.13.jar:/root/.m2/repository/org/clojure/tools.macro/0.1.0/tools.macro-0.1.0.jar:/root/.m2/repository/ring/ring-core/1.1.5/ring-core-1.1.5.jar:/root/.m2/repository/hiccup/hiccup/0.3.6/hiccup-0.3.6.jar:/root/.m2/repository/ring/ring-servlet/0.3.11/ring-servlet-0.3.11.jar:/root/.m2/repository/com/googlecode/json-simple/json-simple/1.1/json-simple-1.1.jar:/root/.m2/repository/org/clojure/math.numeric-tower/0.0.1/math.numeric-tower-0.0.1.jar:/root/.m2/repository/clj-time/clj-time/0.4.1/clj-time-0.4.1.jar:/root/.m2/repository/org/objenesis/objenesis/1.2/objenesis-1.2.jar:/root/.m2/repository/com/twitter/chill-java/0.3.5/chill-java-0.3.5.jar:/root/.m2/repository/com/parsely/streamparse/0.0.4-SNAPSHOT/streamparse-0.0.4-SNAPSHOT.jar:/root/.m2/repository/ring/ring-jetty-adapter/0.3.11/ring-jetty-adapter-0.3.11.jar:/root/.m2/repository/jline/jline/2.11/jline-2.11.jar:/root/.m2/repository/clj-stacktrace/clj-stacktrace/0.2.2/clj-stacktrace-0.2.2.jar:/root/.m2/repository/org/clojure/tools.nrepl/0.2.12/tools.nrepl-0.2.12.jar:/root/.m2/repository/org/slf4j/slf4j-api/1.7.5/slf4j-api-1.7.5.jar:/root/.m2/repository/ring/ring-devel/0.3.11/ring-devel-0.3.11.jar:/root/.m2/repository/org/mortbay/jetty/jetty-util/6.1.26/jetty-util-6.1.26.jar:/root/.m2/repository/javax/servlet/servlet-api/2.5/servlet-api-2.5.jar:/root/.m2/repository/clojure-complete/clojure-complete/0.2.4/clojure-complete-0.2.4.jar:/root/.m2/repository/org/yaml/snakeyaml/1.11/snakeyaml-1.11.jar:/root/.m2/repository/ch/qos/logback/logback-core/1.0.13/logback-core-1.0.13.jar:/root/.m2/repository/commons-lang/commons-lang/2.5/commons-lang-2.5.jar:/root/.m2/repository/org/mortbay/jetty/jetty/6.1.26/jetty-6.1.26.jar:/root/.m2/repository/joda-time/joda-time/2.0/joda-time-2.0.jar:/root/.m2/repository/commons-io/commons-io/2.4/commons-io-2.4.jar:/root/.m2/repository/commons-logging/commons-logging/1.1.3/commons-logging-1.1.3.jar:/root/.m2/repository/com/esotericsoftware/kryo/kryo/2.21/kryo-2.21.jar:/root/.m2/repository/com/esotericsoftware/minlog/minlog/1.2/minlog-1.2.jar:/root/.m2/repository/org/apache/storm/storm-core/0.9.5/storm-core-0.9.5.jar:/root/.m2/repository/compojure/compojure/1.1.3/compojure-1.1.3.jar:/root/.m2/repository/com/esotericsoftware/reflectasm/reflectasm/1.07/reflectasm-1.07-shaded.jar:/root/.m2/repository/com/twitter/carbonite/1.4.0/carbonite-1.4.0.jar:/root/.m2/repository/commons-codec/commons-codec/1.6/commons-codec-1.6.jar:/root/.m2/repository/commons-fileupload/commons-fileupload/1.2.1/commons-fileupload-1.2.1.jar:/root/.m2/repository/org/clojure/data.json/0.2.6/data.json-0.2.6.jar:/root/.m2/repository/org/slf4j/log4j-over-slf4j/1.6.6/log4j-over-slf4j-1.6.6.jar:/root/.m2/repository/org/jgrapht/jgrapht-core/0.9.0/jgrapht-core-0.9.0.jar:/root/.m2/repository/org/clojure/clojure/1.5.1/clojure-1.5.1.jar:/root/.m2/repository/org/clojure/tools.logging/0.2.3/tools.logging-0.2.3.jar:/root/.m2/repository/org/ow2/asm/asm/4.0/asm-4.0.jar:/root/.m2/repository/clout/clout/1.0.1/clout-1.0.1.jar:/root/.m2/repository/org/apache/commons/commons-exec/1.1/commons-exec-1.1.jar:/root/.m2/repository/com/googlecode/disruptor/disruptor/2.10.1/disruptor-2.10.1.jar:/root/.m2/repository/org/clojure/core.incubator/0.1.0/core.incubator-0.1.0.jar:/root/.m2/repository/org/clojure/tools.cli/0.2.4/tools.cli-0.2.4.jar
3956 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:java.library.path=/usr/java/packages/lib/amd64:/usr/lib64:/lib64:/lib:/usr/lib
3956 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:java.io.tmpdir=/tmp
3956 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:java.compiler=<NA>
3956 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:os.name=Linux
3957 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:os.arch=amd64
3957 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:os.version=2.6.32-504.12.2.el6.centos.plus.x86_64
3957 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:user.name=root
3957 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:user.home=/root
3957 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:user.dir=/root/tweetcount
4019 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:zookeeper.version=3.4.6-1569965, built on 02/20/2014 09:09 GMT
4019 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:host.name=ip-172-31-4-51.ec2.internal
4019 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:java.version=1.7.0_79
4019 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:java.vendor=Oracle Corporation
4019 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:java.home=/opt/jdk1.7.0_79/jre
4019 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:java.class.path=/root/tweetcount/test:/root/tweetcount/topologies:/root/tweetcount/dev-resources:/root/tweetcount/_resources:/root/tweetcount/_build/classes:/root/.m2/repository/ch/qos/logback/logback-classic/1.0.13/logback-classic-1.0.13.jar:/root/.m2/repository/org/clojure/tools.macro/0.1.0/tools.macro-0.1.0.jar:/root/.m2/repository/ring/ring-core/1.1.5/ring-core-1.1.5.jar:/root/.m2/repository/hiccup/hiccup/0.3.6/hiccup-0.3.6.jar:/root/.m2/repository/ring/ring-servlet/0.3.11/ring-servlet-0.3.11.jar:/root/.m2/repository/com/googlecode/json-simple/json-simple/1.1/json-simple-1.1.jar:/root/.m2/repository/org/clojure/math.numeric-tower/0.0.1/math.numeric-tower-0.0.1.jar:/root/.m2/repository/clj-time/clj-time/0.4.1/clj-time-0.4.1.jar:/root/.m2/repository/org/objenesis/objenesis/1.2/objenesis-1.2.jar:/root/.m2/repository/com/twitter/chill-java/0.3.5/chill-java-0.3.5.jar:/root/.m2/repository/com/parsely/streamparse/0.0.4-SNAPSHOT/streamparse-0.0.4-SNAPSHOT.jar:/root/.m2/repository/ring/ring-jetty-adapter/0.3.11/ring-jetty-adapter-0.3.11.jar:/root/.m2/repository/jline/jline/2.11/jline-2.11.jar:/root/.m2/repository/clj-stacktrace/clj-stacktrace/0.2.2/clj-stacktrace-0.2.2.jar:/root/.m2/repository/org/clojure/tools.nrepl/0.2.12/tools.nrepl-0.2.12.jar:/root/.m2/repository/org/slf4j/slf4j-api/1.7.5/slf4j-api-1.7.5.jar:/root/.m2/repository/ring/ring-devel/0.3.11/ring-devel-0.3.11.jar:/root/.m2/repository/org/mortbay/jetty/jetty-util/6.1.26/jetty-util-6.1.26.jar:/root/.m2/repository/javax/servlet/servlet-api/2.5/servlet-api-2.5.jar:/root/.m2/repository/clojure-complete/clojure-complete/0.2.4/clojure-complete-0.2.4.jar:/root/.m2/repository/org/yaml/snakeyaml/1.11/snakeyaml-1.11.jar:/root/.m2/repository/ch/qos/logback/logback-core/1.0.13/logback-core-1.0.13.jar:/root/.m2/repository/commons-lang/commons-lang/2.5/commons-lang-2.5.jar:/root/.m2/repository/org/mortbay/jetty/jetty/6.1.26/jetty-6.1.26.jar:/root/.m2/repository/joda-time/joda-time/2.0/joda-time-2.0.jar:/root/.m2/repository/commons-io/commons-io/2.4/commons-io-2.4.jar:/root/.m2/repository/commons-logging/commons-logging/1.1.3/commons-logging-1.1.3.jar:/root/.m2/repository/com/esotericsoftware/kryo/kryo/2.21/kryo-2.21.jar:/root/.m2/repository/com/esotericsoftware/minlog/minlog/1.2/minlog-1.2.jar:/root/.m2/repository/org/apache/storm/storm-core/0.9.5/storm-core-0.9.5.jar:/root/.m2/repository/compojure/compojure/1.1.3/compojure-1.1.3.jar:/root/.m2/repository/com/esotericsoftware/reflectasm/reflectasm/1.07/reflectasm-1.07-shaded.jar:/root/.m2/repository/com/twitter/carbonite/1.4.0/carbonite-1.4.0.jar:/root/.m2/repository/commons-codec/commons-codec/1.6/commons-codec-1.6.jar:/root/.m2/repository/commons-fileupload/commons-fileupload/1.2.1/commons-fileupload-1.2.1.jar:/root/.m2/repository/org/clojure/data.json/0.2.6/data.json-0.2.6.jar:/root/.m2/repository/org/slf4j/log4j-over-slf4j/1.6.6/log4j-over-slf4j-1.6.6.jar:/root/.m2/repository/org/jgrapht/jgrapht-core/0.9.0/jgrapht-core-0.9.0.jar:/root/.m2/repository/org/clojure/clojure/1.5.1/clojure-1.5.1.jar:/root/.m2/repository/org/clojure/tools.logging/0.2.3/tools.logging-0.2.3.jar:/root/.m2/repository/org/ow2/asm/asm/4.0/asm-4.0.jar:/root/.m2/repository/clout/clout/1.0.1/clout-1.0.1.jar:/root/.m2/repository/org/apache/commons/commons-exec/1.1/commons-exec-1.1.jar:/root/.m2/repository/com/googlecode/disruptor/disruptor/2.10.1/disruptor-2.10.1.jar:/root/.m2/repository/org/clojure/core.incubator/0.1.0/core.incubator-0.1.0.jar:/root/.m2/repository/org/clojure/tools.cli/0.2.4/tools.cli-0.2.4.jar
4019 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:java.library.path=/usr/java/packages/lib/amd64:/usr/lib64:/lib64:/lib:/usr/lib
4019 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:java.io.tmpdir=/tmp
4019 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:java.compiler=<NA>
4019 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:os.name=Linux
4019 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:os.arch=amd64
4019 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:os.version=2.6.32-504.12.2.el6.centos.plus.x86_64
4019 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:user.name=root
4019 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:user.home=/root
4019 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:user.dir=/root/tweetcount
6017 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Created server with tickTime 2000 minSessionTimeout 4000 maxSessionTimeout 40000 datadir /tmp/b4778b6c-308d-427d-a3e7-967d34b05155/version-2 snapdir /tmp/b4778b6c-308d-427d-a3e7-967d34b05155/version-2
6039 [main] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - binding to port 0.0.0.0/0.0.0.0:2000
6051 [main] INFO  backtype.storm.zookeeper - Starting inprocess zookeeper at port 2000 and dir /tmp/b4778b6c-308d-427d-a3e7-967d34b05155
6660 [main] INFO  backtype.storm.daemon.nimbus - Starting Nimbus with conf {"dev.zookeeper.path" "/tmp/dev-storm-zookeeper", "topology.tick.tuple.freq.secs" nil, "topology.builtin.metrics.bucket.size.secs" 60, "topology.fall.back.on.java.serialization" true, "topology.max.error.report.per.interval" 5, "zmq.linger.millis" 0, "topology.skip.missing.kryo.registrations" true, "storm.messaging.netty.client_worker_threads" 1, "ui.childopts" "-Xmx768m", "storm.zookeeper.session.timeout" 20000, "nimbus.reassign" true, "topology.trident.batch.emit.interval.millis" 50, "storm.messaging.netty.flush.check.interval.ms" 10, "nimbus.monitor.freq.secs" 10, "logviewer.childopts" "-Xmx128m", "java.library.path" "/usr/local/lib:/opt/local/lib:/usr/lib", "topology.executor.send.buffer.size" 1024, "storm.local.dir" "/tmp/2ce2c843-de53-4c01-be62-dc5d475742e9", "storm.messaging.netty.buffer_size" 5242880, "supervisor.worker.start.timeout.secs" 120, "topology.enable.message.timeouts" true, "nimbus.cleanup.inbox.freq.secs" 600, "nimbus.inbox.jar.expiration.secs" 3600, "drpc.worker.threads" 64, "storm.meta.serialization.delegate" "backtype.storm.serialization.DefaultSerializationDelegate", "topology.worker.shared.thread.pool.size" 4, "nimbus.host" "localhost", "storm.messaging.netty.min_wait_ms" 100, "storm.zookeeper.port" 2000, "transactional.zookeeper.port" nil, "topology.executor.receive.buffer.size" 1024, "transactional.zookeeper.servers" nil, "storm.zookeeper.root" "/storm", "storm.zookeeper.retry.intervalceiling.millis" 30000, "supervisor.enable" true, "storm.messaging.netty.server_worker_threads" 1, "storm.zookeeper.servers" ["localhost"], "transactional.zookeeper.root" "/transactional", "topology.acker.executors" nil, "topology.transfer.buffer.size" 1024, "topology.worker.childopts" nil, "drpc.queue.size" 128, "worker.childopts" "-Xmx768m", "supervisor.heartbeat.frequency.secs" 5, "topology.error.throttle.interval.secs" 10, "zmq.hwm" 0, "drpc.port" 3772, "supervisor.monitor.frequency.secs" 3, "drpc.childopts" "-Xmx768m", "topology.receiver.buffer.size" 8, "task.heartbeat.frequency.secs" 3, "topology.tasks" nil, "storm.messaging.netty.max_retries" 300, "topology.spout.wait.strategy" "backtype.storm.spout.SleepSpoutWaitStrategy", "nimbus.thrift.max_buffer_size" 1048576, "topology.max.spout.pending" nil, "storm.zookeeper.retry.interval" 1000, "topology.sleep.spout.wait.strategy.time.ms" 1, "nimbus.topology.validator" "backtype.storm.nimbus.DefaultTopologyValidator", "supervisor.slots.ports" [6700 6701 6702 6703], "topology.environment" nil, "topology.debug" false, "nimbus.task.launch.secs" 120, "nimbus.supervisor.timeout.secs" 60, "topology.message.timeout.secs" 30, "task.refresh.poll.secs" 10, "topology.workers" 1, "supervisor.childopts" "-Xmx256m", "nimbus.thrift.port" 6627, "topology.stats.sample.rate" 0.05, "worker.heartbeat.frequency.secs" 1, "topology.tuple.serializer" "backtype.storm.serialization.types.ListDelegateSerializer", "topology.disruptor.wait.strategy" "com.lmax.disruptor.BlockingWaitStrategy", "topology.multilang.serializer" "backtype.storm.multilang.JsonSerializer", "nimbus.task.timeout.secs" 30, "storm.zookeeper.connection.timeout" 15000, "topology.kryo.factory" "backtype.storm.serialization.DefaultKryoFactory", "drpc.invocations.port" 3773, "logviewer.port" 8000, "zmq.threads" 1, "storm.zookeeper.retry.times" 5, "topology.worker.receiver.thread.count" 1, "storm.thrift.transport" "backtype.storm.security.auth.SimpleTransportPlugin", "topology.state.synchronization.timeout.secs" 60, "supervisor.worker.timeout.secs" 30, "nimbus.file.copy.expiration.secs" 600, "storm.messaging.transport" "backtype.storm.messaging.netty.Context", "logviewer.appender.name" "A1", "storm.messaging.netty.max_wait_ms" 1000, "drpc.request.timeout.secs" 600, "storm.local.mode.zmq" false, "ui.port" 8080, "nimbus.childopts" "-Xmx1024m", "storm.cluster.mode" "local", "topology.max.task.parallelism" nil, "storm.messaging.netty.transfer.batch.size" 262144, "topology.classpath" nil}
6681 [main] INFO  backtype.storm.daemon.nimbus - Using default scheduler
6691 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
6955 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
6958 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000 sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@4b94b3b3
6992 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
6995 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55670
7006 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
7024 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55670
7027 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.persistence.FileTxnLog - Creating new log file: log.1
7048 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c6291f30000, negotiated timeout = 20000
7056 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c6291f30000 with negotiated timeout 20000 for client /127.0.0.1:55670
7075 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
7077 [main-EventThread] INFO  backtype.storm.zookeeper - Zookeeper state update: :connected:none
8131 [ProcessThread(sid:0 cport:-1):] INFO  org.apache.storm.zookeeper.server.PrepRequestProcessor - Processed session termination for sessionid: 0x1565c6291f30000
8134 [main-EventThread] INFO  org.apache.storm.zookeeper.ClientCnxn - EventThread shut down
8134 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Session: 0x1565c6291f30000 closed
8135 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
8136 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
8136 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000/storm sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@326ee73c
8148 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
8149 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
8149 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxn - Closed socket connection for client /127.0.0.1:55670 which had sessionid 0x1565c6291f30000
8150 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55671
8150 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55671
8153 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c6291f30001 with negotiated timeout 20000 for client /127.0.0.1:55671
8153 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c6291f30001, negotiated timeout = 20000
8153 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
8227 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
8228 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
8228 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000 sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@3071681
8229 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
8230 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55672
8230 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
8230 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55672
8232 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c6291f30002 with negotiated timeout 20000 for client /127.0.0.1:55672
8232 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c6291f30002, negotiated timeout = 20000
8233 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
8233 [main-EventThread] INFO  backtype.storm.zookeeper - Zookeeper state update: :connected:none
9236 [ProcessThread(sid:0 cport:-1):] INFO  org.apache.storm.zookeeper.server.PrepRequestProcessor - Processed session termination for sessionid: 0x1565c6291f30002
9238 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Session: 0x1565c6291f30002 closed
9238 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
9239 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
9239 [main-EventThread] INFO  org.apache.storm.zookeeper.ClientCnxn - EventThread shut down
9239 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxn - Closed socket connection for client /127.0.0.1:55672 which had sessionid 0x1565c6291f30002
9240 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000/storm sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@4529977a
9241 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
9241 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55673
9241 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
9242 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55673
9243 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
9243 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
9244 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000 sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@4302667
9245 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
9245 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55674
9246 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
9246 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55674
9256 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c6291f30003 with negotiated timeout 20000 for client /127.0.0.1:55673
9257 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c6291f30003, negotiated timeout = 20000
9257 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
9258 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c6291f30004 with negotiated timeout 20000 for client /127.0.0.1:55674
9258 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c6291f30004, negotiated timeout = 20000
9258 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
9258 [main-EventThread] INFO  backtype.storm.zookeeper - Zookeeper state update: :connected:none
9260 [ProcessThread(sid:0 cport:-1):] INFO  org.apache.storm.zookeeper.server.PrepRequestProcessor - Processed session termination for sessionid: 0x1565c6291f30004
9261 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Session: 0x1565c6291f30004 closed
9262 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
9262 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
9262 [main-EventThread] INFO  org.apache.storm.zookeeper.ClientCnxn - EventThread shut down
9263 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000/storm sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@7c4392c2
9263 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
9264 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
9266 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxn - Closed socket connection for client /127.0.0.1:55674 which had sessionid 0x1565c6291f30004
9267 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55675
9267 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55675
9277 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c6291f30005 with negotiated timeout 20000 for client /127.0.0.1:55675
9277 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c6291f30005, negotiated timeout = 20000
9277 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
10323 [main] INFO  backtype.storm.daemon.supervisor - Starting Supervisor with conf {"dev.zookeeper.path" "/tmp/dev-storm-zookeeper", "topology.tick.tuple.freq.secs" nil, "topology.builtin.metrics.bucket.size.secs" 60, "topology.fall.back.on.java.serialization" true, "topology.max.error.report.per.interval" 5, "zmq.linger.millis" 0, "topology.skip.missing.kryo.registrations" true, "storm.messaging.netty.client_worker_threads" 1, "ui.childopts" "-Xmx768m", "storm.zookeeper.session.timeout" 20000, "nimbus.reassign" true, "topology.trident.batch.emit.interval.millis" 50, "storm.messaging.netty.flush.check.interval.ms" 10, "nimbus.monitor.freq.secs" 10, "logviewer.childopts" "-Xmx128m", "java.library.path" "/usr/local/lib:/opt/local/lib:/usr/lib", "topology.executor.send.buffer.size" 1024, "storm.local.dir" "/tmp/2a6d7c88-eb16-4e5e-99a5-44d5f55b374a", "storm.messaging.netty.buffer_size" 5242880, "supervisor.worker.start.timeout.secs" 120, "topology.enable.message.timeouts" true, "nimbus.cleanup.inbox.freq.secs" 600, "nimbus.inbox.jar.expiration.secs" 3600, "drpc.worker.threads" 64, "storm.meta.serialization.delegate" "backtype.storm.serialization.DefaultSerializationDelegate", "topology.worker.shared.thread.pool.size" 4, "nimbus.host" "localhost", "storm.messaging.netty.min_wait_ms" 100, "storm.zookeeper.port" 2000, "transactional.zookeeper.port" nil, "topology.executor.receive.buffer.size" 1024, "transactional.zookeeper.servers" nil, "storm.zookeeper.root" "/storm", "storm.zookeeper.retry.intervalceiling.millis" 30000, "supervisor.enable" true, "storm.messaging.netty.server_worker_threads" 1, "storm.zookeeper.servers" ["localhost"], "transactional.zookeeper.root" "/transactional", "topology.acker.executors" nil, "topology.transfer.buffer.size" 1024, "topology.worker.childopts" nil, "drpc.queue.size" 128, "worker.childopts" "-Xmx768m", "supervisor.heartbeat.frequency.secs" 5, "topology.error.throttle.interval.secs" 10, "zmq.hwm" 0, "drpc.port" 3772, "supervisor.monitor.frequency.secs" 3, "drpc.childopts" "-Xmx768m", "topology.receiver.buffer.size" 8, "task.heartbeat.frequency.secs" 3, "topology.tasks" nil, "storm.messaging.netty.max_retries" 300, "topology.spout.wait.strategy" "backtype.storm.spout.SleepSpoutWaitStrategy", "nimbus.thrift.max_buffer_size" 1048576, "topology.max.spout.pending" nil, "storm.zookeeper.retry.interval" 1000, "topology.sleep.spout.wait.strategy.time.ms" 1, "nimbus.topology.validator" "backtype.storm.nimbus.DefaultTopologyValidator", "supervisor.slots.ports" (1024 1025 1026), "topology.environment" nil, "topology.debug" false, "nimbus.task.launch.secs" 120, "nimbus.supervisor.timeout.secs" 60, "topology.message.timeout.secs" 30, "task.refresh.poll.secs" 10, "topology.workers" 1, "supervisor.childopts" "-Xmx256m", "nimbus.thrift.port" 6627, "topology.stats.sample.rate" 0.05, "worker.heartbeat.frequency.secs" 1, "topology.tuple.serializer" "backtype.storm.serialization.types.ListDelegateSerializer", "topology.disruptor.wait.strategy" "com.lmax.disruptor.BlockingWaitStrategy", "topology.multilang.serializer" "backtype.storm.multilang.JsonSerializer", "nimbus.task.timeout.secs" 30, "storm.zookeeper.connection.timeout" 15000, "topology.kryo.factory" "backtype.storm.serialization.DefaultKryoFactory", "drpc.invocations.port" 3773, "logviewer.port" 8000, "zmq.threads" 1, "storm.zookeeper.retry.times" 5, "topology.worker.receiver.thread.count" 1, "storm.thrift.transport" "backtype.storm.security.auth.SimpleTransportPlugin", "topology.state.synchronization.timeout.secs" 60, "supervisor.worker.timeout.secs" 30, "nimbus.file.copy.expiration.secs" 600, "storm.messaging.transport" "backtype.storm.messaging.netty.Context", "logviewer.appender.name" "A1", "storm.messaging.netty.max_wait_ms" 1000, "drpc.request.timeout.secs" 600, "storm.local.mode.zmq" false, "ui.port" 8080, "nimbus.childopts" "-Xmx1024m", "storm.cluster.mode" "local", "topology.max.task.parallelism" nil, "storm.messaging.netty.transfer.batch.size" 262144, "topology.classpath" nil}
10356 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
10357 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
10357 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000 sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@2e43a9ef
10358 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
10358 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55676
10359 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
10359 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55676
10361 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c6291f30006 with negotiated timeout 20000 for client /127.0.0.1:55676
10361 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c6291f30006, negotiated timeout = 20000
10362 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
10370 [main-EventThread] INFO  backtype.storm.zookeeper - Zookeeper state update: :connected:none
11372 [ProcessThread(sid:0 cport:-1):] INFO  org.apache.storm.zookeeper.server.PrepRequestProcessor - Processed session termination for sessionid: 0x1565c6291f30006
11374 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxn - Closed socket connection for client /127.0.0.1:55676 which had sessionid 0x1565c6291f30006
11375 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Session: 0x1565c6291f30006 closed
11375 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
11375 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
11376 [main-EventThread] INFO  org.apache.storm.zookeeper.ClientCnxn - EventThread shut down
11376 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000/storm sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@dd5b524
11377 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
11377 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55677
11378 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
11380 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55677
11391 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c6291f30007 with negotiated timeout 20000 for client /127.0.0.1:55677
11392 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c6291f30007, negotiated timeout = 20000
11393 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
12431 [main] INFO  backtype.storm.daemon.supervisor - Starting supervisor with id 742a787e-905e-4823-8e37-bd95a1ec43bd at host ip-172-31-4-51.ec2.internal
12438 [main] INFO  backtype.storm.daemon.supervisor - Starting Supervisor with conf {"dev.zookeeper.path" "/tmp/dev-storm-zookeeper", "topology.tick.tuple.freq.secs" nil, "topology.builtin.metrics.bucket.size.secs" 60, "topology.fall.back.on.java.serialization" true, "topology.max.error.report.per.interval" 5, "zmq.linger.millis" 0, "topology.skip.missing.kryo.registrations" true, "storm.messaging.netty.client_worker_threads" 1, "ui.childopts" "-Xmx768m", "storm.zookeeper.session.timeout" 20000, "nimbus.reassign" true, "topology.trident.batch.emit.interval.millis" 50, "storm.messaging.netty.flush.check.interval.ms" 10, "nimbus.monitor.freq.secs" 10, "logviewer.childopts" "-Xmx128m", "java.library.path" "/usr/local/lib:/opt/local/lib:/usr/lib", "topology.executor.send.buffer.size" 1024, "storm.local.dir" "/tmp/40c0f8f4-af76-4437-8267-fb2e4156f559", "storm.messaging.netty.buffer_size" 5242880, "supervisor.worker.start.timeout.secs" 120, "topology.enable.message.timeouts" true, "nimbus.cleanup.inbox.freq.secs" 600, "nimbus.inbox.jar.expiration.secs" 3600, "drpc.worker.threads" 64, "storm.meta.serialization.delegate" "backtype.storm.serialization.DefaultSerializationDelegate", "topology.worker.shared.thread.pool.size" 4, "nimbus.host" "localhost", "storm.messaging.netty.min_wait_ms" 100, "storm.zookeeper.port" 2000, "transactional.zookeeper.port" nil, "topology.executor.receive.buffer.size" 1024, "transactional.zookeeper.servers" nil, "storm.zookeeper.root" "/storm", "storm.zookeeper.retry.intervalceiling.millis" 30000, "supervisor.enable" true, "storm.messaging.netty.server_worker_threads" 1, "storm.zookeeper.servers" ["localhost"], "transactional.zookeeper.root" "/transactional", "topology.acker.executors" nil, "topology.transfer.buffer.size" 1024, "topology.worker.childopts" nil, "drpc.queue.size" 128, "worker.childopts" "-Xmx768m", "supervisor.heartbeat.frequency.secs" 5, "topology.error.throttle.interval.secs" 10, "zmq.hwm" 0, "drpc.port" 3772, "supervisor.monitor.frequency.secs" 3, "drpc.childopts" "-Xmx768m", "topology.receiver.buffer.size" 8, "task.heartbeat.frequency.secs" 3, "topology.tasks" nil, "storm.messaging.netty.max_retries" 300, "topology.spout.wait.strategy" "backtype.storm.spout.SleepSpoutWaitStrategy", "nimbus.thrift.max_buffer_size" 1048576, "topology.max.spout.pending" nil, "storm.zookeeper.retry.interval" 1000, "topology.sleep.spout.wait.strategy.time.ms" 1, "nimbus.topology.validator" "backtype.storm.nimbus.DefaultTopologyValidator", "supervisor.slots.ports" (1027 1028 1029), "topology.environment" nil, "topology.debug" false, "nimbus.task.launch.secs" 120, "nimbus.supervisor.timeout.secs" 60, "topology.message.timeout.secs" 30, "task.refresh.poll.secs" 10, "topology.workers" 1, "supervisor.childopts" "-Xmx256m", "nimbus.thrift.port" 6627, "topology.stats.sample.rate" 0.05, "worker.heartbeat.frequency.secs" 1, "topology.tuple.serializer" "backtype.storm.serialization.types.ListDelegateSerializer", "topology.disruptor.wait.strategy" "com.lmax.disruptor.BlockingWaitStrategy", "topology.multilang.serializer" "backtype.storm.multilang.JsonSerializer", "nimbus.task.timeout.secs" 30, "storm.zookeeper.connection.timeout" 15000, "topology.kryo.factory" "backtype.storm.serialization.DefaultKryoFactory", "drpc.invocations.port" 3773, "logviewer.port" 8000, "zmq.threads" 1, "storm.zookeeper.retry.times" 5, "topology.worker.receiver.thread.count" 1, "storm.thrift.transport" "backtype.storm.security.auth.SimpleTransportPlugin", "topology.state.synchronization.timeout.secs" 60, "supervisor.worker.timeout.secs" 30, "nimbus.file.copy.expiration.secs" 600, "storm.messaging.transport" "backtype.storm.messaging.netty.Context", "logviewer.appender.name" "A1", "storm.messaging.netty.max_wait_ms" 1000, "drpc.request.timeout.secs" 600, "storm.local.mode.zmq" false, "ui.port" 8080, "nimbus.childopts" "-Xmx1024m", "storm.cluster.mode" "local", "topology.max.task.parallelism" nil, "storm.messaging.netty.transfer.batch.size" 262144, "topology.classpath" nil}
12450 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
12450 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
12451 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000 sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@5782899e
12451 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
12463 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55679
12464 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
12464 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55679
12466 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c6291f30008 with negotiated timeout 20000 for client /127.0.0.1:55679
12466 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c6291f30008, negotiated timeout = 20000
12466 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
12466 [main-EventThread] INFO  backtype.storm.zookeeper - Zookeeper state update: :connected:none
12468 [ProcessThread(sid:0 cport:-1):] INFO  org.apache.storm.zookeeper.server.PrepRequestProcessor - Processed session termination for sessionid: 0x1565c6291f30008
12469 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxn - Closed socket connection for client /127.0.0.1:55679 which had sessionid 0x1565c6291f30008
12470 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Session: 0x1565c6291f30008 closed
12470 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
12470 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
12470 [main-EventThread] INFO  org.apache.storm.zookeeper.ClientCnxn - EventThread shut down
12471 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000/storm sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@5549fe36
12492 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
12492 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
12493 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55680
12494 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55680
12495 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c6291f30009 with negotiated timeout 20000 for client /127.0.0.1:55680
12495 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c6291f30009, negotiated timeout = 20000
12496 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
12516 [main] INFO  backtype.storm.daemon.supervisor - Starting supervisor with id 7f32f0ba-543b-451d-aa3e-40c120e1863a at host ip-172-31-4-51.ec2.internal
12647 [main] INFO  backtype.storm.daemon.nimbus - Received topology submission for tweetcount with conf {"storm.id" "tweetcount-1-1470428785", "topology.acker.executors" 2, "streamparse.log.path" "/root/tweetcount/logs", "topology.kryo.decorators" (), "topology.name" "tweetcount", "topology.max.spout.pending" 5000, "topology.debug" false, "topology.kryo.register" nil, "topology.message.timeout.secs" 60, "topology.workers" 2, "topology.max.task.parallelism" nil, "streamparse.log.level" "debug"}
12751 [main] INFO  backtype.storm.daemon.nimbus - Activating tweetcount: tweetcount-1-1470428785
12984 [main] INFO  backtype.storm.scheduler.EvenScheduler - Available slots: (["7f32f0ba-543b-451d-aa3e-40c120e1863a" 1027] ["7f32f0ba-543b-451d-aa3e-40c120e1863a" 1028] ["7f32f0ba-543b-451d-aa3e-40c120e1863a" 1029] ["742a787e-905e-4823-8e37-bd95a1ec43bd" 1024] ["742a787e-905e-4823-8e37-bd95a1ec43bd" 1025] ["742a787e-905e-4823-8e37-bd95a1ec43bd" 1026])
13180 [main] INFO  backtype.storm.daemon.nimbus - Setting new assignment for topology id tweetcount-1-1470428785: #backtype.storm.daemon.common.Assignment{:master-code-dir "/tmp/2ce2c843-de53-4c01-be62-dc5d475742e9/nimbus/stormdist/tweetcount-1-1470428785", :node->host {"742a787e-905e-4823-8e37-bd95a1ec43bd" "ip-172-31-4-51.ec2.internal", "7f32f0ba-543b-451d-aa3e-40c120e1863a" "ip-172-31-4-51.ec2.internal"}, :executor->node+port {[3 3] ["7f32f0ba-543b-451d-aa3e-40c120e1863a" 1027], [6 6] ["742a787e-905e-4823-8e37-bd95a1ec43bd" 1024], [5 5] ["7f32f0ba-543b-451d-aa3e-40c120e1863a" 1027], [4 4] ["742a787e-905e-4823-8e37-bd95a1ec43bd" 1024], [7 7] ["7f32f0ba-543b-451d-aa3e-40c120e1863a" 1027], [2 2] ["742a787e-905e-4823-8e37-bd95a1ec43bd" 1024], [1 1] ["7f32f0ba-543b-451d-aa3e-40c120e1863a" 1027]}, :executor->start-time-secs {[7 7] 1470428785, [5 5] 1470428785, [3 3] 1470428785, [1 1] 1470428785, [6 6] 1470428785, [4 4] 1470428785, [2 2] 1470428785}}
14853 [Thread-3] INFO  backtype.storm.daemon.supervisor - Copying resources at file:/root/tweetcount/_resources/resources to /tmp/2a6d7c88-eb16-4e5e-99a5-44d5f55b374a/supervisor/stormdist/tweetcount-1-1470428785/resources
14874 [Thread-5] INFO  backtype.storm.daemon.supervisor - Copying resources at file:/root/tweetcount/_resources/resources to /tmp/40c0f8f4-af76-4437-8267-fb2e4156f559/supervisor/stormdist/tweetcount-1-1470428785/resources
15017 [Thread-6] INFO  backtype.storm.daemon.supervisor - Launching worker with assignment #backtype.storm.daemon.supervisor.LocalAssignment{:storm-id "tweetcount-1-1470428785", :executors ([3 3] [5 5] [7 7] [1 1])} for this supervisor 7f32f0ba-543b-451d-aa3e-40c120e1863a on port 1027 with id 733e34ff-c280-4412-ac4f-f7c4bf97ec04
15018 [Thread-4] INFO  backtype.storm.daemon.supervisor - Launching worker with assignment #backtype.storm.daemon.supervisor.LocalAssignment{:storm-id "tweetcount-1-1470428785", :executors ([6 6] [4 4] [2 2])} for this supervisor 742a787e-905e-4823-8e37-bd95a1ec43bd on port 1024 with id f371fa87-60d4-4ec7-9208-34bc76645bb0
15022 [Thread-6] INFO  backtype.storm.daemon.worker - Launching worker for tweetcount-1-1470428785 on 7f32f0ba-543b-451d-aa3e-40c120e1863a:1027 with id 733e34ff-c280-4412-ac4f-f7c4bf97ec04 and conf {"dev.zookeeper.path" "/tmp/dev-storm-zookeeper", "topology.tick.tuple.freq.secs" nil, "topology.builtin.metrics.bucket.size.secs" 60, "topology.fall.back.on.java.serialization" true, "topology.max.error.report.per.interval" 5, "zmq.linger.millis" 0, "topology.skip.missing.kryo.registrations" true, "storm.messaging.netty.client_worker_threads" 1, "ui.childopts" "-Xmx768m", "storm.zookeeper.session.timeout" 20000, "nimbus.reassign" true, "topology.trident.batch.emit.interval.millis" 50, "storm.messaging.netty.flush.check.interval.ms" 10, "nimbus.monitor.freq.secs" 10, "logviewer.childopts" "-Xmx128m", "java.library.path" "/usr/local/lib:/opt/local/lib:/usr/lib", "topology.executor.send.buffer.size" 1024, "storm.local.dir" "/tmp/40c0f8f4-af76-4437-8267-fb2e4156f559", "storm.messaging.netty.buffer_size" 5242880, "supervisor.worker.start.timeout.secs" 120, "topology.enable.message.timeouts" true, "nimbus.cleanup.inbox.freq.secs" 600, "nimbus.inbox.jar.expiration.secs" 3600, "drpc.worker.threads" 64, "storm.meta.serialization.delegate" "backtype.storm.serialization.DefaultSerializationDelegate", "topology.worker.shared.thread.pool.size" 4, "nimbus.host" "localhost", "storm.messaging.netty.min_wait_ms" 100, "storm.zookeeper.port" 2000, "transactional.zookeeper.port" nil, "topology.executor.receive.buffer.size" 1024, "transactional.zookeeper.servers" nil, "storm.zookeeper.root" "/storm", "storm.zookeeper.retry.intervalceiling.millis" 30000, "supervisor.enable" true, "storm.messaging.netty.server_worker_threads" 1, "storm.zookeeper.servers" ["localhost"], "transactional.zookeeper.root" "/transactional", "topology.acker.executors" nil, "topology.transfer.buffer.size" 1024, "topology.worker.childopts" nil, "drpc.queue.size" 128, "worker.childopts" "-Xmx768m", "supervisor.heartbeat.frequency.secs" 5, "topology.error.throttle.interval.secs" 10, "zmq.hwm" 0, "drpc.port" 3772, "supervisor.monitor.frequency.secs" 3, "drpc.childopts" "-Xmx768m", "topology.receiver.buffer.size" 8, "task.heartbeat.frequency.secs" 3, "topology.tasks" nil, "storm.messaging.netty.max_retries" 300, "topology.spout.wait.strategy" "backtype.storm.spout.SleepSpoutWaitStrategy", "nimbus.thrift.max_buffer_size" 1048576, "topology.max.spout.pending" nil, "storm.zookeeper.retry.interval" 1000, "topology.sleep.spout.wait.strategy.time.ms" 1, "nimbus.topology.validator" "backtype.storm.nimbus.DefaultTopologyValidator", "supervisor.slots.ports" (1027 1028 1029), "topology.environment" nil, "topology.debug" false, "nimbus.task.launch.secs" 120, "nimbus.supervisor.timeout.secs" 60, "topology.message.timeout.secs" 30, "task.refresh.poll.secs" 10, "topology.workers" 1, "supervisor.childopts" "-Xmx256m", "nimbus.thrift.port" 6627, "topology.stats.sample.rate" 0.05, "worker.heartbeat.frequency.secs" 1, "topology.tuple.serializer" "backtype.storm.serialization.types.ListDelegateSerializer", "topology.disruptor.wait.strategy" "com.lmax.disruptor.BlockingWaitStrategy", "topology.multilang.serializer" "backtype.storm.multilang.JsonSerializer", "nimbus.task.timeout.secs" 30, "storm.zookeeper.connection.timeout" 15000, "topology.kryo.factory" "backtype.storm.serialization.DefaultKryoFactory", "drpc.invocations.port" 3773, "logviewer.port" 8000, "zmq.threads" 1, "storm.zookeeper.retry.times" 5, "topology.worker.receiver.thread.count" 1, "storm.thrift.transport" "backtype.storm.security.auth.SimpleTransportPlugin", "topology.state.synchronization.timeout.secs" 60, "supervisor.worker.timeout.secs" 30, "nimbus.file.copy.expiration.secs" 600, "storm.messaging.transport" "backtype.storm.messaging.netty.Context", "logviewer.appender.name" "A1", "storm.messaging.netty.max_wait_ms" 1000, "drpc.request.timeout.secs" 600, "storm.local.mode.zmq" false, "ui.port" 8080, "nimbus.childopts" "-Xmx1024m", "storm.cluster.mode" "local", "topology.max.task.parallelism" nil, "storm.messaging.netty.transfer.batch.size" 262144, "topology.classpath" nil}
15023 [Thread-6] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
15023 [Thread-6] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
15023 [Thread-4] INFO  backtype.storm.daemon.worker - Launching worker for tweetcount-1-1470428785 on 742a787e-905e-4823-8e37-bd95a1ec43bd:1024 with id f371fa87-60d4-4ec7-9208-34bc76645bb0 and conf {"dev.zookeeper.path" "/tmp/dev-storm-zookeeper", "topology.tick.tuple.freq.secs" nil, "topology.builtin.metrics.bucket.size.secs" 60, "topology.fall.back.on.java.serialization" true, "topology.max.error.report.per.interval" 5, "zmq.linger.millis" 0, "topology.skip.missing.kryo.registrations" true, "storm.messaging.netty.client_worker_threads" 1, "ui.childopts" "-Xmx768m", "storm.zookeeper.session.timeout" 20000, "nimbus.reassign" true, "topology.trident.batch.emit.interval.millis" 50, "storm.messaging.netty.flush.check.interval.ms" 10, "nimbus.monitor.freq.secs" 10, "logviewer.childopts" "-Xmx128m", "java.library.path" "/usr/local/lib:/opt/local/lib:/usr/lib", "topology.executor.send.buffer.size" 1024, "storm.local.dir" "/tmp/2a6d7c88-eb16-4e5e-99a5-44d5f55b374a", "storm.messaging.netty.buffer_size" 5242880, "supervisor.worker.start.timeout.secs" 120, "topology.enable.message.timeouts" true, "nimbus.cleanup.inbox.freq.secs" 600, "nimbus.inbox.jar.expiration.secs" 3600, "drpc.worker.threads" 64, "storm.meta.serialization.delegate" "backtype.storm.serialization.DefaultSerializationDelegate", "topology.worker.shared.thread.pool.size" 4, "nimbus.host" "localhost", "storm.messaging.netty.min_wait_ms" 100, "storm.zookeeper.port" 2000, "transactional.zookeeper.port" nil, "topology.executor.receive.buffer.size" 1024, "transactional.zookeeper.servers" nil, "storm.zookeeper.root" "/storm", "storm.zookeeper.retry.intervalceiling.millis" 30000, "supervisor.enable" true, "storm.messaging.netty.server_worker_threads" 1, "storm.zookeeper.servers" ["localhost"], "transactional.zookeeper.root" "/transactional", "topology.acker.executors" nil, "topology.transfer.buffer.size" 1024, "topology.worker.childopts" nil, "drpc.queue.size" 128, "worker.childopts" "-Xmx768m", "supervisor.heartbeat.frequency.secs" 5, "topology.error.throttle.interval.secs" 10, "zmq.hwm" 0, "drpc.port" 3772, "supervisor.monitor.frequency.secs" 3, "drpc.childopts" "-Xmx768m", "topology.receiver.buffer.size" 8, "task.heartbeat.frequency.secs" 3, "topology.tasks" nil, "storm.messaging.netty.max_retries" 300, "topology.spout.wait.strategy" "backtype.storm.spout.SleepSpoutWaitStrategy", "nimbus.thrift.max_buffer_size" 1048576, "topology.max.spout.pending" nil, "storm.zookeeper.retry.interval" 1000, "topology.sleep.spout.wait.strategy.time.ms" 1, "nimbus.topology.validator" "backtype.storm.nimbus.DefaultTopologyValidator", "supervisor.slots.ports" (1024 1025 1026), "topology.environment" nil, "topology.debug" false, "nimbus.task.launch.secs" 120, "nimbus.supervisor.timeout.secs" 60, "topology.message.timeout.secs" 30, "task.refresh.poll.secs" 10, "topology.workers" 1, "supervisor.childopts" "-Xmx256m", "nimbus.thrift.port" 6627, "topology.stats.sample.rate" 0.05, "worker.heartbeat.frequency.secs" 1, "topology.tuple.serializer" "backtype.storm.serialization.types.ListDelegateSerializer", "topology.disruptor.wait.strategy" "com.lmax.disruptor.BlockingWaitStrategy", "topology.multilang.serializer" "backtype.storm.multilang.JsonSerializer", "nimbus.task.timeout.secs" 30, "storm.zookeeper.connection.timeout" 15000, "topology.kryo.factory" "backtype.storm.serialization.DefaultKryoFactory", "drpc.invocations.port" 3773, "logviewer.port" 8000, "zmq.threads" 1, "storm.zookeeper.retry.times" 5, "topology.worker.receiver.thread.count" 1, "storm.thrift.transport" "backtype.storm.security.auth.SimpleTransportPlugin", "topology.state.synchronization.timeout.secs" 60, "supervisor.worker.timeout.secs" 30, "nimbus.file.copy.expiration.secs" 600, "storm.messaging.transport" "backtype.storm.messaging.netty.Context", "logviewer.appender.name" "A1", "storm.messaging.netty.max_wait_ms" 1000, "drpc.request.timeout.secs" 600, "storm.local.mode.zmq" false, "ui.port" 8080, "nimbus.childopts" "-Xmx1024m", "storm.cluster.mode" "local", "topology.max.task.parallelism" nil, "storm.messaging.netty.transfer.batch.size" 262144, "topology.classpath" nil}
15024 [Thread-4] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
15028 [Thread-6] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000 sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@66febc27
15029 [Thread-6-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
15030 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55681
15030 [Thread-6-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
15031 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55681
15032 [Thread-4] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
15045 [Thread-4] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000 sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@124a7b26
15046 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c6291f3000a with negotiated timeout 20000 for client /127.0.0.1:55681
15046 [Thread-6-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c6291f3000a, negotiated timeout = 20000
15047 [Thread-4-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
15047 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55682
15047 [Thread-4-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
15048 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55682
15049 [Thread-6-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
15049 [Thread-6-EventThread] INFO  backtype.storm.zookeeper - Zookeeper state update: :connected:none
15049 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c6291f3000b with negotiated timeout 20000 for client /127.0.0.1:55682
15052 [ProcessThread(sid:0 cport:-1):] INFO  org.apache.storm.zookeeper.server.PrepRequestProcessor - Processed session termination for sessionid: 0x1565c6291f3000a
15077 [Thread-4-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c6291f3000b, negotiated timeout = 20000
15077 [Thread-4-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
15078 [Thread-4-EventThread] INFO  backtype.storm.zookeeper - Zookeeper state update: :connected:none
15080 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxn - Closed socket connection for client /127.0.0.1:55681 which had sessionid 0x1565c6291f3000a
15080 [Thread-6] INFO  org.apache.storm.zookeeper.ZooKeeper - Session: 0x1565c6291f3000a closed
15081 [Thread-6] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
15081 [Thread-6] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
15081 [Thread-6-EventThread] INFO  org.apache.storm.zookeeper.ClientCnxn - EventThread shut down
15083 [Thread-6] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000/storm sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@3ddb3b45
15083 [Thread-6-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
15084 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55683
15084 [Thread-6-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
15085 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55683
15101 [ProcessThread(sid:0 cport:-1):] INFO  org.apache.storm.zookeeper.server.PrepRequestProcessor - Processed session termination for sessionid: 0x1565c6291f3000b
15105 [Thread-6-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c6291f3000c, negotiated timeout = 20000
15105 [Thread-6-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
15113 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c6291f3000c with negotiated timeout 20000 for client /127.0.0.1:55683
15115 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxn - Closed socket connection for client /127.0.0.1:55682 which had sessionid 0x1565c6291f3000b
15115 [Thread-4] INFO  org.apache.storm.zookeeper.ZooKeeper - Session: 0x1565c6291f3000b closed
15115 [Thread-4] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
15115 [Thread-4] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
15116 [Thread-4-EventThread] INFO  org.apache.storm.zookeeper.ClientCnxn - EventThread shut down
15117 [Thread-4] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000/storm sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@678e2ffc
15117 [Thread-4-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
15118 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55684
15118 [Thread-4-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
15118 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55684
15135 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c6291f3000d with negotiated timeout 20000 for client /127.0.0.1:55684
15135 [Thread-4-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c6291f3000d, negotiated timeout = 20000
15135 [Thread-4-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
15153 [Thread-6] INFO  backtype.storm.daemon.worker - Reading Assignments.
15297 [Thread-6] INFO  backtype.storm.daemon.worker - Launching receive-thread for 7f32f0ba-543b-451d-aa3e-40c120e1863a:1027
15337 [Thread-7-worker-receiver-thread-0] INFO  backtype.storm.messaging.loader - Starting receive-thread: [stormId: tweetcount-1-1470428785, port: 1027, thread-id: 0 ]
16095 [Thread-6] INFO  backtype.storm.daemon.executor - Loading executor counter-bolt:[3 3]
16119 [Thread-6] INFO  backtype.storm.daemon.executor - Loaded executor tasks counter-bolt:[3 3]
16128 [Thread-6] INFO  backtype.storm.daemon.executor - Finished loading executor counter-bolt:[3 3]
16149 [Thread-4] INFO  backtype.storm.daemon.worker - Reading Assignments.
16207 [Thread-4] INFO  backtype.storm.daemon.worker - Launching receive-thread for 742a787e-905e-4823-8e37-bd95a1ec43bd:1024
16216 [Thread-10-worker-receiver-thread-0] INFO  backtype.storm.messaging.loader - Starting receive-thread: [stormId: tweetcount-1-1470428785, port: 1024, thread-id: 0 ]
16233 [refresh-active-timer] INFO  backtype.storm.daemon.worker - All connections are ready for worker 7f32f0ba-543b-451d-aa3e-40c120e1863a:1027 with id 733e34ff-c280-4412-ac4f-f7c4bf97ec04
16258 [Thread-6] INFO  backtype.storm.daemon.executor - Loading executor parse-bolt:[5 5]
16272 [Thread-6] INFO  backtype.storm.daemon.executor - Loaded executor tasks parse-bolt:[5 5]
16274 [Thread-6] INFO  backtype.storm.daemon.executor - Finished loading executor parse-bolt:[5 5]
16283 [Thread-6] INFO  backtype.storm.daemon.executor - Loading executor tweet-spout:[7 7]
16292 [Thread-6] INFO  backtype.storm.daemon.executor - Loaded executor tasks tweet-spout:[7 7]
16320 [Thread-6] INFO  backtype.storm.daemon.executor - Finished loading executor tweet-spout:[7 7]
16342 [Thread-6] INFO  backtype.storm.daemon.executor - Loading executor __system:[-1 -1]
16343 [Thread-6] INFO  backtype.storm.daemon.executor - Loaded executor tasks __system:[-1 -1]
16358 [Thread-6] INFO  backtype.storm.daemon.executor - Finished loading executor __system:[-1 -1]
16361 [Thread-4] INFO  backtype.storm.daemon.executor - Loading executor __acker:[2 2]
16370 [Thread-4] INFO  backtype.storm.daemon.executor - Loaded executor tasks __acker:[2 2]
16372 [Thread-4] INFO  backtype.storm.daemon.executor - Timeouts disabled for executor __acker:[2 2]
16372 [Thread-4] INFO  backtype.storm.daemon.executor - Finished loading executor __acker:[2 2]
16389 [Thread-6] INFO  backtype.storm.daemon.executor - Loading executor __acker:[1 1]
16390 [Thread-6] INFO  backtype.storm.daemon.executor - Loaded executor tasks __acker:[1 1]
16392 [Thread-6] INFO  backtype.storm.daemon.executor - Timeouts disabled for executor __acker:[1 1]
16392 [Thread-6] INFO  backtype.storm.daemon.executor - Finished loading executor __acker:[1 1]
16406 [Thread-6] INFO  backtype.storm.daemon.worker - Worker has topology config {"storm.id" "tweetcount-1-1470428785", "dev.zookeeper.path" "/tmp/dev-storm-zookeeper", "topology.tick.tuple.freq.secs" nil, "topology.builtin.metrics.bucket.size.secs" 60, "topology.fall.back.on.java.serialization" true, "topology.max.error.report.per.interval" 5, "zmq.linger.millis" 0, "topology.skip.missing.kryo.registrations" true, "storm.messaging.netty.client_worker_threads" 1, "ui.childopts" "-Xmx768m", "storm.zookeeper.session.timeout" 20000, "nimbus.reassign" true, "topology.trident.batch.emit.interval.millis" 50, "storm.messaging.netty.flush.check.interval.ms" 10, "nimbus.monitor.freq.secs" 10, "logviewer.childopts" "-Xmx128m", "java.library.path" "/usr/local/lib:/opt/local/lib:/usr/lib", "topology.executor.send.buffer.size" 1024, "storm.local.dir" "/tmp/40c0f8f4-af76-4437-8267-fb2e4156f559", "storm.messaging.netty.buffer_size" 5242880, "supervisor.worker.start.timeout.secs" 120, "topology.enable.message.timeouts" true, "nimbus.cleanup.inbox.freq.secs" 600, "nimbus.inbox.jar.expiration.secs" 3600, "drpc.worker.threads" 64, "storm.meta.serialization.delegate" "backtype.storm.serialization.DefaultSerializationDelegate", "topology.worker.shared.thread.pool.size" 4, "nimbus.host" "localhost", "storm.messaging.netty.min_wait_ms" 100, "storm.zookeeper.port" 2000, "transactional.zookeeper.port" nil, "topology.executor.receive.buffer.size" 1024, "transactional.zookeeper.servers" nil, "storm.zookeeper.root" "/storm", "storm.zookeeper.retry.intervalceiling.millis" 30000, "supervisor.enable" true, "storm.messaging.netty.server_worker_threads" 1, "storm.zookeeper.servers" ["localhost"], "transactional.zookeeper.root" "/transactional", "topology.acker.executors" 2, "streamparse.log.path" "/root/tweetcount/logs", "topology.kryo.decorators" (), "topology.name" "tweetcount", "topology.transfer.buffer.size" 1024, "topology.worker.childopts" nil, "drpc.queue.size" 128, "worker.childopts" "-Xmx768m", "supervisor.heartbeat.frequency.secs" 5, "topology.error.throttle.interval.secs" 10, "zmq.hwm" 0, "drpc.port" 3772, "supervisor.monitor.frequency.secs" 3, "drpc.childopts" "-Xmx768m", "topology.receiver.buffer.size" 8, "task.heartbeat.frequency.secs" 3, "topology.tasks" nil, "storm.messaging.netty.max_retries" 300, "topology.spout.wait.strategy" "backtype.storm.spout.SleepSpoutWaitStrategy", "nimbus.thrift.max_buffer_size" 1048576, "topology.max.spout.pending" 5000, "storm.zookeeper.retry.interval" 1000, "topology.sleep.spout.wait.strategy.time.ms" 1, "nimbus.topology.validator" "backtype.storm.nimbus.DefaultTopologyValidator", "supervisor.slots.ports" (1027 1028 1029), "topology.environment" nil, "topology.debug" false, "nimbus.task.launch.secs" 120, "nimbus.supervisor.timeout.secs" 60, "topology.kryo.register" nil, "topology.message.timeout.secs" 60, "task.refresh.poll.secs" 10, "topology.workers" 2, "supervisor.childopts" "-Xmx256m", "nimbus.thrift.port" 6627, "topology.stats.sample.rate" 0.05, "worker.heartbeat.frequency.secs" 1, "topology.tuple.serializer" "backtype.storm.serialization.types.ListDelegateSerializer", "topology.disruptor.wait.strategy" "com.lmax.disruptor.BlockingWaitStrategy", "topology.multilang.serializer" "backtype.storm.multilang.JsonSerializer", "nimbus.task.timeout.secs" 30, "storm.zookeeper.connection.timeout" 15000, "topology.kryo.factory" "backtype.storm.serialization.DefaultKryoFactory", "drpc.invocations.port" 3773, "logviewer.port" 8000, "zmq.threads" 1, "storm.zookeeper.retry.times" 5, "topology.worker.receiver.thread.count" 1, "storm.thrift.transport" "backtype.storm.security.auth.SimpleTransportPlugin", "topology.state.synchronization.timeout.secs" 60, "supervisor.worker.timeout.secs" 30, "nimbus.file.copy.expiration.secs" 600, "storm.messaging.transport" "backtype.storm.messaging.netty.Context", "logviewer.appender.name" "A1", "storm.messaging.netty.max_wait_ms" 1000, "drpc.request.timeout.secs" 600, "storm.local.mode.zmq" false, "ui.port" 8080, "nimbus.childopts" "-Xmx1024m", "storm.cluster.mode" "local", "topology.max.task.parallelism" nil, "storm.messaging.netty.transfer.batch.size" 262144, "topology.classpath" nil, "streamparse.log.level" "debug"}
16418 [Thread-4] INFO  backtype.storm.daemon.executor - Loading executor counter-bolt:[4 4]
16422 [Thread-6] INFO  backtype.storm.daemon.worker - Worker 733e34ff-c280-4412-ac4f-f7c4bf97ec04 for storm tweetcount-1-1470428785 on 7f32f0ba-543b-451d-aa3e-40c120e1863a:1027 has finished loading
16434 [Thread-4] INFO  backtype.storm.daemon.executor - Loaded executor tasks counter-bolt:[4 4]
16438 [Thread-4] INFO  backtype.storm.daemon.executor - Finished loading executor counter-bolt:[4 4]
16462 [Thread-4] INFO  backtype.storm.daemon.executor - Loading executor parse-bolt:[6 6]
16465 [Thread-4] INFO  backtype.storm.daemon.executor - Loaded executor tasks parse-bolt:[6 6]
16477 [Thread-4] INFO  backtype.storm.daemon.executor - Finished loading executor parse-bolt:[6 6]
16509 [Thread-4] INFO  backtype.storm.daemon.executor - Loading executor __system:[-1 -1]
16510 [Thread-4] INFO  backtype.storm.daemon.executor - Loaded executor tasks __system:[-1 -1]
16523 [Thread-4] INFO  backtype.storm.daemon.executor - Finished loading executor __system:[-1 -1]
16528 [Thread-4] INFO  backtype.storm.daemon.worker - Worker has topology config {"storm.id" "tweetcount-1-1470428785", "dev.zookeeper.path" "/tmp/dev-storm-zookeeper", "topology.tick.tuple.freq.secs" nil, "topology.builtin.metrics.bucket.size.secs" 60, "topology.fall.back.on.java.serialization" true, "topology.max.error.report.per.interval" 5, "zmq.linger.millis" 0, "topology.skip.missing.kryo.registrations" true, "storm.messaging.netty.client_worker_threads" 1, "ui.childopts" "-Xmx768m", "storm.zookeeper.session.timeout" 20000, "nimbus.reassign" true, "topology.trident.batch.emit.interval.millis" 50, "storm.messaging.netty.flush.check.interval.ms" 10, "nimbus.monitor.freq.secs" 10, "logviewer.childopts" "-Xmx128m", "java.library.path" "/usr/local/lib:/opt/local/lib:/usr/lib", "topology.executor.send.buffer.size" 1024, "storm.local.dir" "/tmp/2a6d7c88-eb16-4e5e-99a5-44d5f55b374a", "storm.messaging.netty.buffer_size" 5242880, "supervisor.worker.start.timeout.secs" 120, "topology.enable.message.timeouts" true, "nimbus.cleanup.inbox.freq.secs" 600, "nimbus.inbox.jar.expiration.secs" 3600, "drpc.worker.threads" 64, "storm.meta.serialization.delegate" "backtype.storm.serialization.DefaultSerializationDelegate", "topology.worker.shared.thread.pool.size" 4, "nimbus.host" "localhost", "storm.messaging.netty.min_wait_ms" 100, "storm.zookeeper.port" 2000, "transactional.zookeeper.port" nil, "topology.executor.receive.buffer.size" 1024, "transactional.zookeeper.servers" nil, "storm.zookeeper.root" "/storm", "storm.zookeeper.retry.intervalceiling.millis" 30000, "supervisor.enable" true, "storm.messaging.netty.server_worker_threads" 1, "storm.zookeeper.servers" ["localhost"], "transactional.zookeeper.root" "/transactional", "topology.acker.executors" 2, "streamparse.log.path" "/root/tweetcount/logs", "topology.kryo.decorators" (), "topology.name" "tweetcount", "topology.transfer.buffer.size" 1024, "topology.worker.childopts" nil, "drpc.queue.size" 128, "worker.childopts" "-Xmx768m", "supervisor.heartbeat.frequency.secs" 5, "topology.error.throttle.interval.secs" 10, "zmq.hwm" 0, "drpc.port" 3772, "supervisor.monitor.frequency.secs" 3, "drpc.childopts" "-Xmx768m", "topology.receiver.buffer.size" 8, "task.heartbeat.frequency.secs" 3, "topology.tasks" nil, "storm.messaging.netty.max_retries" 300, "topology.spout.wait.strategy" "backtype.storm.spout.SleepSpoutWaitStrategy", "nimbus.thrift.max_buffer_size" 1048576, "topology.max.spout.pending" 5000, "storm.zookeeper.retry.interval" 1000, "topology.sleep.spout.wait.strategy.time.ms" 1, "nimbus.topology.validator" "backtype.storm.nimbus.DefaultTopologyValidator", "supervisor.slots.ports" (1024 1025 1026), "topology.environment" nil, "topology.debug" false, "nimbus.task.launch.secs" 120, "nimbus.supervisor.timeout.secs" 60, "topology.kryo.register" nil, "topology.message.timeout.secs" 60, "task.refresh.poll.secs" 10, "topology.workers" 2, "supervisor.childopts" "-Xmx256m", "nimbus.thrift.port" 6627, "topology.stats.sample.rate" 0.05, "worker.heartbeat.frequency.secs" 1, "topology.tuple.serializer" "backtype.storm.serialization.types.ListDelegateSerializer", "topology.disruptor.wait.strategy" "com.lmax.disruptor.BlockingWaitStrategy", "topology.multilang.serializer" "backtype.storm.multilang.JsonSerializer", "nimbus.task.timeout.secs" 30, "storm.zookeeper.connection.timeout" 15000, "topology.kryo.factory" "backtype.storm.serialization.DefaultKryoFactory", "drpc.invocations.port" 3773, "logviewer.port" 8000, "zmq.threads" 1, "storm.zookeeper.retry.times" 5, "topology.worker.receiver.thread.count" 1, "storm.thrift.transport" "backtype.storm.security.auth.SimpleTransportPlugin", "topology.state.synchronization.timeout.secs" 60, "supervisor.worker.timeout.secs" 30, "nimbus.file.copy.expiration.secs" 600, "storm.messaging.transport" "backtype.storm.messaging.netty.Context", "logviewer.appender.name" "A1", "storm.messaging.netty.max_wait_ms" 1000, "drpc.request.timeout.secs" 600, "storm.local.mode.zmq" false, "ui.port" 8080, "nimbus.childopts" "-Xmx1024m", "storm.cluster.mode" "local", "topology.max.task.parallelism" nil, "storm.messaging.netty.transfer.batch.size" 262144, "topology.classpath" nil, "streamparse.log.level" "debug"}
16528 [Thread-4] INFO  backtype.storm.daemon.worker - Worker f371fa87-60d4-4ec7-9208-34bc76645bb0 for storm tweetcount-1-1470428785 on 742a787e-905e-4823-8e37-bd95a1ec43bd:1024 has finished loading
17180 [refresh-active-timer] INFO  backtype.storm.daemon.worker - All connections are ready for worker 742a787e-905e-4823-8e37-bd95a1ec43bd:1024 with id f371fa87-60d4-4ec7-9208-34bc76645bb0
17289 [Thread-18-__acker] INFO  backtype.storm.daemon.executor - Preparing bolt __acker:(2)
17291 [Thread-23-counter-bolt] INFO  backtype.storm.daemon.executor - Preparing bolt counter-bolt:(4)
17291 [Thread-27-__system] INFO  backtype.storm.daemon.executor - Preparing bolt __system:(-1)
17292 [Thread-25-parse-bolt] INFO  backtype.storm.daemon.executor - Preparing bolt parse-bolt:(6)
17309 [Thread-12-parse-bolt] INFO  backtype.storm.daemon.executor - Preparing bolt parse-bolt:(5)
17313 [Thread-27-__system] INFO  backtype.storm.daemon.executor - Prepared bolt __system:(-1)
17315 [Thread-20-__acker] INFO  backtype.storm.daemon.executor - Preparing bolt __acker:(1)
17332 [Thread-25-parse-bolt] INFO  backtype.storm.utils.ShellProcess - Storm multilang serializer: backtype.storm.multilang.JsonSerializer
17334 [Thread-12-parse-bolt] INFO  backtype.storm.utils.ShellProcess - Storm multilang serializer: backtype.storm.multilang.JsonSerializer
17347 [Thread-23-counter-bolt] INFO  backtype.storm.utils.ShellProcess - Storm multilang serializer: backtype.storm.multilang.JsonSerializer
17348 [Thread-14-tweet-spout] INFO  backtype.storm.daemon.executor - Opening spout tweet-spout:(7)
17351 [Thread-14-tweet-spout] INFO  backtype.storm.utils.ShellProcess - Storm multilang serializer: backtype.storm.multilang.JsonSerializer
17483 [Thread-16-__system] INFO  backtype.storm.daemon.executor - Preparing bolt __system:(-1)
17485 [Thread-9-counter-bolt] INFO  backtype.storm.daemon.executor - Preparing bolt counter-bolt:(3)
17486 [Thread-9-counter-bolt] INFO  backtype.storm.utils.ShellProcess - Storm multilang serializer: backtype.storm.multilang.JsonSerializer
17624 [Thread-18-__acker] INFO  backtype.storm.daemon.executor - Prepared bolt __acker:(2)
17634 [Thread-20-__acker] INFO  backtype.storm.daemon.executor - Prepared bolt __acker:(1)
17698 [Thread-16-__system] INFO  backtype.storm.daemon.executor - Prepared bolt __system:(-1)
18308 [Thread-25-parse-bolt] INFO  backtype.storm.task.ShellBolt - Launched subprocess with pid 3795
18338 [Thread-25-parse-bolt] INFO  backtype.storm.task.ShellBolt - Start checking heartbeat...
18338 [Thread-25-parse-bolt] INFO  backtype.storm.daemon.executor - Prepared bolt parse-bolt:(6)
18393 [Thread-23-counter-bolt] INFO  backtype.storm.task.ShellBolt - Launched subprocess with pid 3796
18409 [Thread-23-counter-bolt] INFO  backtype.storm.task.ShellBolt - Start checking heartbeat...
18409 [Thread-23-counter-bolt] INFO  backtype.storm.daemon.executor - Prepared bolt counter-bolt:(4)
18534 [Thread-31] ERROR backtype.storm.daemon.executor - 
java.lang.Exception: Shell Process Exception: Python NameError raised
Traceback (most recent call last):
  File "/usr/lib/python2.7/site-packages/streamparse/storm/component.py", line 487, in run
    self.initialize(storm_conf, context)
  File "bolts/tweetcounter.py", line 9, in initialize
    self.redis = Strict.Redis()
NameError: global name 'Strict' is not defined

	at backtype.storm.task.ShellBolt.handleError(ShellBolt.java:188) [storm-core-0.9.5.jar:0.9.5]
	at backtype.storm.task.ShellBolt.access$1100(ShellBolt.java:69) [storm-core-0.9.5.jar:0.9.5]
	at backtype.storm.task.ShellBolt$BoltReaderRunnable.run(ShellBolt.java:331) [storm-core-0.9.5.jar:0.9.5]
	at java.lang.Thread.run(Thread.java:745) [na:1.7.0_79]
18601 [Thread-31] ERROR backtype.storm.task.ShellBolt - Halting process: ShellBolt died.
java.lang.RuntimeException: backtype.storm.multilang.NoOutputException: Pipe to subprocess seems to be broken! No output read.
Serializer Exception:


	at backtype.storm.utils.ShellProcess.readShellMsg(ShellProcess.java:101) ~[storm-core-0.9.5.jar:0.9.5]
	at backtype.storm.task.ShellBolt$BoltReaderRunnable.run(ShellBolt.java:318) ~[storm-core-0.9.5.jar:0.9.5]
	at java.lang.Thread.run(Thread.java:745) [na:1.7.0_79]
18601 [Thread-31] ERROR backtype.storm.daemon.executor - 
java.lang.RuntimeException: backtype.storm.multilang.NoOutputException: Pipe to subprocess seems to be broken! No output read.
Serializer Exception:


	at backtype.storm.utils.ShellProcess.readShellMsg(ShellProcess.java:101) ~[storm-core-0.9.5.jar:0.9.5]
	at backtype.storm.task.ShellBolt$BoltReaderRunnable.run(ShellBolt.java:318) ~[storm-core-0.9.5.jar:0.9.5]
	at java.lang.Thread.run(Thread.java:745) [na:1.7.0_79]
18619 [Thread-12-parse-bolt] INFO  backtype.storm.task.ShellBolt - Launched subprocess with pid 3794
18640 [Thread-12-parse-bolt] INFO  backtype.storm.task.ShellBolt - Start checking heartbeat...
18640 [Thread-12-parse-bolt] INFO  backtype.storm.daemon.executor - Prepared bolt parse-bolt:(5)
18691 [Thread-9-counter-bolt] INFO  backtype.storm.task.ShellBolt - Launched subprocess with pid 3800
18695 [Thread-9-counter-bolt] ERROR backtype.storm.util - Async loop died!
java.lang.IllegalStateException: Shutdown in progress
	at java.lang.ApplicationShutdownHooks.add(ApplicationShutdownHooks.java:66) ~[na:1.7.0_79]
	at java.lang.Runtime.addShutdownHook(Runtime.java:211) ~[na:1.7.0_79]
	at org.apache.storm.guava.util.concurrent.MoreExecutors$Application.addShutdownHook(MoreExecutors.java:223) ~[storm-core-0.9.5.jar:0.9.5]
	at org.apache.storm.guava.util.concurrent.MoreExecutors$Application.addDelayedShutdownHook(MoreExecutors.java:195) ~[storm-core-0.9.5.jar:0.9.5]
	at org.apache.storm.guava.util.concurrent.MoreExecutors$Application.getExitingScheduledExecutorService(MoreExecutors.java:187) ~[storm-core-0.9.5.jar:0.9.5]
	at org.apache.storm.guava.util.concurrent.MoreExecutors$Application.getExitingScheduledExecutorService(MoreExecutors.java:219) ~[storm-core-0.9.5.jar:0.9.5]
	at org.apache.storm.guava.util.concurrent.MoreExecutors.getExitingScheduledExecutorService(MoreExecutors.java:169) ~[storm-core-0.9.5.jar:0.9.5]
	at backtype.storm.task.ShellBolt.prepare(ShellBolt.java:127) ~[storm-core-0.9.5.jar:0.9.5]
	at backtype.storm.daemon.executor$fn__3439$fn__3451.invoke(executor.clj:692) ~[storm-core-0.9.5.jar:0.9.5]
	at backtype.storm.util$async_loop$fn__460.invoke(util.clj:461) ~[storm-core-0.9.5.jar:0.9.5]
	at clojure.lang.AFn.run(AFn.java:24) [clojure-1.5.1.jar:na]
	at java.lang.Thread.run(Thread.java:745) [na:1.7.0_79]
18696 [Thread-9-counter-bolt] ERROR backtype.storm.daemon.executor - 
java.lang.IllegalStateException: Shutdown in progress
	at java.lang.ApplicationShutdownHooks.add(ApplicationShutdownHooks.java:66) ~[na:1.7.0_79]
	at java.lang.Runtime.addShutdownHook(Runtime.java:211) ~[na:1.7.0_79]
	at org.apache.storm.guava.util.concurrent.MoreExecutors$Application.addShutdownHook(MoreExecutors.java:223) ~[storm-core-0.9.5.jar:0.9.5]
	at org.apache.storm.guava.util.concurrent.MoreExecutors$Application.addDelayedShutdownHook(MoreExecutors.java:195) ~[storm-core-0.9.5.jar:0.9.5]
	at org.apache.storm.guava.util.concurrent.MoreExecutors$Application.getExitingScheduledExecutorService(MoreExecutors.java:187) ~[storm-core-0.9.5.jar:0.9.5]
	at org.apache.storm.guava.util.concurrent.MoreExecutors$Application.getExitingScheduledExecutorService(MoreExecutors.java:219) ~[storm-core-0.9.5.jar:0.9.5]
	at org.apache.storm.guava.util.concurrent.MoreExecutors.getExitingScheduledExecutorService(MoreExecutors.java:169) ~[storm-core-0.9.5.jar:0.9.5]
	at backtype.storm.task.ShellBolt.prepare(ShellBolt.java:127) ~[storm-core-0.9.5.jar:0.9.5]
	at backtype.storm.daemon.executor$fn__3439$fn__3451.invoke(executor.clj:692) ~[storm-core-0.9.5.jar:0.9.5]
	at backtype.storm.util$async_loop$fn__460.invoke(util.clj:461) ~[storm-core-0.9.5.jar:0.9.5]
	at clojure.lang.AFn.run(AFn.java:24) [clojure-1.5.1.jar:na]
	at java.lang.Thread.run(Thread.java:745) [na:1.7.0_79]
18707 [Thread-35] ERROR backtype.storm.daemon.executor - 
java.lang.Exception: Shell Process Exception: Python NameError raised
Traceback (most recent call last):
  File "/usr/lib/python2.7/site-packages/streamparse/storm/component.py", line 487, in run
    self.initialize(storm_conf, context)
  File "bolts/tweetcounter.py", line 9, in initialize
    self.redis = Strict.Redis()
NameError: global name 'Strict' is not defined

	at backtype.storm.task.ShellBolt.handleError(ShellBolt.java:188) [storm-core-0.9.5.jar:0.9.5]
	at backtype.storm.task.ShellBolt.access$1100(ShellBolt.java:69) [storm-core-0.9.5.jar:0.9.5]
	at backtype.storm.task.ShellBolt$BoltReaderRunnable.run(ShellBolt.java:331) [storm-core-0.9.5.jar:0.9.5]
	at java.lang.Thread.run(Thread.java:745) [na:1.7.0_79]
Traceback (most recent call last):
  File "/usr/bin/sparse", line 9, in <module>
    load_entry_point('streamparse==2.1.4', 'console_scripts', 'sparse')()
  File "/usr/lib/python2.7/site-packages/streamparse/cli/sparse.py", line 57, in main
    args.func(args)
  File "/usr/lib/python2.7/site-packages/streamparse/cli/run.py", line 81, in main
    debug=args.debug)
  File "/usr/lib/python2.7/site-packages/streamparse/cli/run.py", line 52, in run_local_topology
    run(full_cmd)
  File "/usr/lib/python2.7/site-packages/invoke/__init__.py", line 32, in run
    return Context().run(command, **kwargs)
  File "/usr/lib/python2.7/site-packages/invoke/context.py", line 53, in run
    return runner_class(context=self).run(command, **kwargs)
  File "/usr/lib/python2.7/site-packages/invoke/runners.py", line 363, in run
    raise Failure(result)
invoke.exceptions.Failure: Command execution failure!

Exit code: 11

Stderr:




[root@ip-172-31-4-51 tweetcount]# cd ..
[root@ip-172-31-4-51 ~]# cd tweetcount/
[root@ip-172-31-4-51 tweetcount]# ls -l
total 40
drwxr-xr-x 4 root root 4096 Jul 11 19:33 _build
-rw-r--r-- 1 root root  428 Jul 11 18:27 config.json
-rw-r--r-- 1 root root  456 Jul 11 18:27 fabfile.py
drwxr-xr-x 2 root root 4096 Aug  5 20:26 logs
-rw-r--r-- 1 root root  524 Jul 11 18:27 project.clj
-rw-r--r-- 1 root root    0 Jul 11 18:27 README.md
drwxr-xr-x 3 root root 4096 Aug  5 20:26 _resources
drwxr-xr-x 4 root root 4096 Jul 11 18:27 src
-rw-r--r-- 1 root root  456 Jul 11 18:27 tasks.py
drwxr-xr-x 2 root root 4096 Aug  5 20:25 topologies
drwxr-xr-x 2 root root 4096 Jul 11 18:27 virtualenvs
[root@ip-172-31-4-51 tweetcount]# cd logs/
[root@ip-172-31-4-51 logs]# ls -l
total 56
-rw-r--r-- 1 root root    0 Aug  3 02:21 streamparse_tweetcount_counter-bolt_3_3314.log
-rw-r--r-- 1 root root    0 Jul 29 02:19 streamparse_tweetcount_counter-bolt_3_3748.log
-rw-r--r-- 1 root root    0 Aug  5 18:39 streamparse_tweetcount_counter-bolt_3_3763.log
-rw-r--r-- 1 root root  396 Aug  5 20:26 streamparse_tweetcount_counter-bolt_3_3800.log
-rw-r--r-- 1 root root    0 Jul 13 03:11 streamparse_tweetcount_counter-bolt_3_4652.log
-rw-r--r-- 1 root root    0 Aug  3 03:51 streamparse_tweetcount_counter-bolt_3_5844.log
-rw-r--r-- 1 root root    0 Aug  3 02:21 streamparse_tweetcount_counter-bolt_4_3316.log
-rw-r--r-- 1 root root    0 Jul 29 02:19 streamparse_tweetcount_counter-bolt_4_3744.log
-rw-r--r-- 1 root root    0 Aug  5 18:39 streamparse_tweetcount_counter-bolt_4_3755.log
-rw-r--r-- 1 root root  396 Aug  5 20:26 streamparse_tweetcount_counter-bolt_4_3796.log
-rw-r--r-- 1 root root    0 Jul 13 03:11 streamparse_tweetcount_counter-bolt_4_4654.log
-rw-r--r-- 1 root root    0 Aug  3 03:51 streamparse_tweetcount_counter-bolt_4_5842.log
-rw-r--r-- 1 root root    0 Jul 13 03:01 streamparse_tweetcount_parse-bolt_3_4458.log
-rw-r--r-- 1 root root    0 Jul 13 03:01 streamparse_tweetcount_parse-bolt_4_4454.log
-rw-r--r-- 1 root root    0 Aug  3 02:21 streamparse_tweetcount_parse-bolt_5_3317.log
-rw-r--r-- 1 root root    0 Jul 29 02:19 streamparse_tweetcount_parse-bolt_5_3747.log
-rw-r--r-- 1 root root    0 Aug  5 18:39 streamparse_tweetcount_parse-bolt_5_3758.log
-rw-r--r-- 1 root root  152 Aug  5 20:26 streamparse_tweetcount_parse-bolt_5_3794.log
-rw-r--r-- 1 root root    0 Jul 13 03:11 streamparse_tweetcount_parse-bolt_5_4651.log
-rw-r--r-- 1 root root    0 Aug  3 03:51 streamparse_tweetcount_parse-bolt_5_5843.log
-rw-r--r-- 1 root root    0 Aug  3 02:21 streamparse_tweetcount_parse-bolt_6_3313.log
-rw-r--r-- 1 root root    0 Jul 29 02:19 streamparse_tweetcount_parse-bolt_6_3743.log
-rw-r--r-- 1 root root    0 Aug  5 18:39 streamparse_tweetcount_parse-bolt_6_3756.log
-rw-r--r-- 1 root root  152 Aug  5 20:26 streamparse_tweetcount_parse-bolt_6_3795.log
-rw-r--r-- 1 root root    0 Jul 13 03:11 streamparse_tweetcount_parse-bolt_6_4649.log
-rw-r--r-- 1 root root    0 Aug  3 03:51 streamparse_tweetcount_parse-bolt_6_5845.log
-rw-r--r-- 1 root root    0 Jul 13 03:01 streamparse_tweetcount_sentence-spout_5_4455.log
-rw-r--r-- 1 root root    0 Aug  3 02:21 streamparse_tweetcount_sentence-spout_7_3315.log
-rw-r--r-- 1 root root    0 Jul 29 02:19 streamparse_tweetcount_sentence-spout_7_3749.log
-rw-r--r-- 1 root root    0 Aug  5 18:39 streamparse_tweetcount_sentence-spout_7_3757.log
-rw-r--r-- 1 root root    0 Jul 13 03:11 streamparse_tweetcount_sentence-spout_7_4653.log
-rw-r--r-- 1 root root    0 Aug  3 03:51 streamparse_tweetcount_sentence-spout_7_5846.log
-rw-r--r-- 1 root root 3266 Aug  5 20:26 streamparse_tweetcount_tweet-spout_7_3797.log
-rw-r--r-- 1 root root  152 Jul 12 05:09 streamparse_wordcount_parse-bolt_3_3146.log
-rw-r--r-- 1 root root  152 Jul 11 23:10 streamparse_wordcount_parse-bolt_3_3147.log
-rw-r--r-- 1 root root  152 Jul 13 01:46 streamparse_wordcount_parse-bolt_3_3151.log
-rw-r--r-- 1 root root  152 Jul 11 20:18 streamparse_wordcount_parse-bolt_3_3165.log
-rw-r--r-- 1 root root  152 Jul 13 01:47 streamparse_wordcount_parse-bolt_3_3318.log
-rw-r--r-- 1 root root    0 Jul 13 02:00 streamparse_wordcount_parse-bolt_3_3503.log
-rw-r--r-- 1 root root    0 Jul 13 02:13 streamparse_wordcount_parse-bolt_3_3707.log
-rw-r--r-- 1 root root    0 Jul 13 02:22 streamparse_wordcount_parse-bolt_3_3881.log
-rw-r--r-- 1 root root    0 Jul 13 02:24 streamparse_wordcount_parse-bolt_3_4051.log
-rw-r--r-- 1 root root    0 Jul 13 02:31 streamparse_wordcount_parse-bolt_3_4236.log
-rw-r--r-- 1 root root  304 Jul 12 05:09 streamparse_wordcount_parse-bolt_4_3145.log
-rw-r--r-- 1 root root  152 Jul 13 01:46 streamparse_wordcount_parse-bolt_4_3154.log
-rw-r--r-- 1 root root  152 Jul 11 20:18 streamparse_wordcount_parse-bolt_4_3166.log
-rw-r--r-- 1 root root  152 Jul 13 01:47 streamparse_wordcount_parse-bolt_4_3311.log
-rw-r--r-- 1 root root    0 Jul 13 02:00 streamparse_wordcount_parse-bolt_4_3504.log
-rw-r--r-- 1 root root    0 Jul 13 02:13 streamparse_wordcount_parse-bolt_4_3708.log
-rw-r--r-- 1 root root    0 Jul 13 02:22 streamparse_wordcount_parse-bolt_4_3882.log
-rw-r--r-- 1 root root    0 Jul 13 02:24 streamparse_wordcount_parse-bolt_4_4054.log
-rw-r--r-- 1 root root    0 Jul 13 02:31 streamparse_wordcount_parse-bolt_4_4237.log
-rw-r--r-- 1 root root    0 Jul 13 02:00 streamparse_wordcount_sentence-spout_5_3501.log
-rw-r--r-- 1 root root    0 Jul 13 02:13 streamparse_wordcount_sentence-spout_5_3709.log
-rw-r--r-- 1 root root    0 Jul 13 02:22 streamparse_wordcount_sentence-spout_5_3883.log
-rw-r--r-- 1 root root    0 Jul 13 02:24 streamparse_wordcount_sentence-spout_5_4049.log
-rw-r--r-- 1 root root    0 Jul 13 02:31 streamparse_wordcount_sentence-spout_5_4238.log
[root@ip-172-31-4-51 logs]# cd ..
[root@ip-172-31-4-51 tweetcount]# cd src
[root@ip-172-31-4-51 src]# cd bolts/
[root@ip-172-31-4-51 bolts]# ls -l
total 8
-rw-r--r-- 1 root root   0 Jul 11 18:27 __init__.py
-rw-r--r-- 1 root root 656 Jul 13 01:58 parse.py
-rw-r--r-- 1 root root 854 Aug  5 20:24 tweetcounter.py
[root@ip-172-31-4-51 bolts]# vi tweetcounter.py 
[root@ip-172-31-4-51 bolts]# cd ..
[root@ip-172-31-4-51 src]# cd ..
[root@ip-172-31-4-51 tweetcount]# sparse run
Running tweetcount topology...
Routing Python logging to /root/tweetcount/logs.
Running lein command to run local cluster:
lein run -m streamparse.commands.run/-main topologies/tweetcount.clj -t 0 --option 'topology.workers=2' --option 'topology.acker.executors=2' --option 'streamparse.log.path="/root/tweetcount/logs"' --option 'streamparse.log.level="debug"'
WARNING: You're currently running as root; probably by accident.
Press control-C to abort or Enter to continue as root.
Set LEIN_ROOT to disable this warning.

3315 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:zookeeper.version=3.4.6-1569965, built on 02/20/2014 09:09 GMT
3319 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:host.name=ip-172-31-4-51.ec2.internal
3319 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:java.version=1.7.0_79
3319 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:java.vendor=Oracle Corporation
3319 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:java.home=/opt/jdk1.7.0_79/jre
3319 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:java.class.path=/root/tweetcount/test:/root/tweetcount/topologies:/root/tweetcount/dev-resources:/root/tweetcount/_resources:/root/tweetcount/_build/classes:/root/.m2/repository/ch/qos/logback/logback-classic/1.0.13/logback-classic-1.0.13.jar:/root/.m2/repository/org/clojure/tools.macro/0.1.0/tools.macro-0.1.0.jar:/root/.m2/repository/ring/ring-core/1.1.5/ring-core-1.1.5.jar:/root/.m2/repository/hiccup/hiccup/0.3.6/hiccup-0.3.6.jar:/root/.m2/repository/ring/ring-servlet/0.3.11/ring-servlet-0.3.11.jar:/root/.m2/repository/com/googlecode/json-simple/json-simple/1.1/json-simple-1.1.jar:/root/.m2/repository/org/clojure/math.numeric-tower/0.0.1/math.numeric-tower-0.0.1.jar:/root/.m2/repository/clj-time/clj-time/0.4.1/clj-time-0.4.1.jar:/root/.m2/repository/org/objenesis/objenesis/1.2/objenesis-1.2.jar:/root/.m2/repository/com/twitter/chill-java/0.3.5/chill-java-0.3.5.jar:/root/.m2/repository/com/parsely/streamparse/0.0.4-SNAPSHOT/streamparse-0.0.4-SNAPSHOT.jar:/root/.m2/repository/ring/ring-jetty-adapter/0.3.11/ring-jetty-adapter-0.3.11.jar:/root/.m2/repository/jline/jline/2.11/jline-2.11.jar:/root/.m2/repository/clj-stacktrace/clj-stacktrace/0.2.2/clj-stacktrace-0.2.2.jar:/root/.m2/repository/org/clojure/tools.nrepl/0.2.12/tools.nrepl-0.2.12.jar:/root/.m2/repository/org/slf4j/slf4j-api/1.7.5/slf4j-api-1.7.5.jar:/root/.m2/repository/ring/ring-devel/0.3.11/ring-devel-0.3.11.jar:/root/.m2/repository/org/mortbay/jetty/jetty-util/6.1.26/jetty-util-6.1.26.jar:/root/.m2/repository/javax/servlet/servlet-api/2.5/servlet-api-2.5.jar:/root/.m2/repository/clojure-complete/clojure-complete/0.2.4/clojure-complete-0.2.4.jar:/root/.m2/repository/org/yaml/snakeyaml/1.11/snakeyaml-1.11.jar:/root/.m2/repository/ch/qos/logback/logback-core/1.0.13/logback-core-1.0.13.jar:/root/.m2/repository/commons-lang/commons-lang/2.5/commons-lang-2.5.jar:/root/.m2/repository/org/mortbay/jetty/jetty/6.1.26/jetty-6.1.26.jar:/root/.m2/repository/joda-time/joda-time/2.0/joda-time-2.0.jar:/root/.m2/repository/commons-io/commons-io/2.4/commons-io-2.4.jar:/root/.m2/repository/commons-logging/commons-logging/1.1.3/commons-logging-1.1.3.jar:/root/.m2/repository/com/esotericsoftware/kryo/kryo/2.21/kryo-2.21.jar:/root/.m2/repository/com/esotericsoftware/minlog/minlog/1.2/minlog-1.2.jar:/root/.m2/repository/org/apache/storm/storm-core/0.9.5/storm-core-0.9.5.jar:/root/.m2/repository/compojure/compojure/1.1.3/compojure-1.1.3.jar:/root/.m2/repository/com/esotericsoftware/reflectasm/reflectasm/1.07/reflectasm-1.07-shaded.jar:/root/.m2/repository/com/twitter/carbonite/1.4.0/carbonite-1.4.0.jar:/root/.m2/repository/commons-codec/commons-codec/1.6/commons-codec-1.6.jar:/root/.m2/repository/commons-fileupload/commons-fileupload/1.2.1/commons-fileupload-1.2.1.jar:/root/.m2/repository/org/clojure/data.json/0.2.6/data.json-0.2.6.jar:/root/.m2/repository/org/slf4j/log4j-over-slf4j/1.6.6/log4j-over-slf4j-1.6.6.jar:/root/.m2/repository/org/jgrapht/jgrapht-core/0.9.0/jgrapht-core-0.9.0.jar:/root/.m2/repository/org/clojure/clojure/1.5.1/clojure-1.5.1.jar:/root/.m2/repository/org/clojure/tools.logging/0.2.3/tools.logging-0.2.3.jar:/root/.m2/repository/org/ow2/asm/asm/4.0/asm-4.0.jar:/root/.m2/repository/clout/clout/1.0.1/clout-1.0.1.jar:/root/.m2/repository/org/apache/commons/commons-exec/1.1/commons-exec-1.1.jar:/root/.m2/repository/com/googlecode/disruptor/disruptor/2.10.1/disruptor-2.10.1.jar:/root/.m2/repository/org/clojure/core.incubator/0.1.0/core.incubator-0.1.0.jar:/root/.m2/repository/org/clojure/tools.cli/0.2.4/tools.cli-0.2.4.jar
3320 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:java.library.path=/usr/java/packages/lib/amd64:/usr/lib64:/lib64:/lib:/usr/lib
3320 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:java.io.tmpdir=/tmp
3320 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:java.compiler=<NA>
3320 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:os.name=Linux
3320 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:os.arch=amd64
3320 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:os.version=2.6.32-504.12.2.el6.centos.plus.x86_64
3320 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:user.name=root
3321 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:user.home=/root
3321 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:user.dir=/root/tweetcount
3369 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:zookeeper.version=3.4.6-1569965, built on 02/20/2014 09:09 GMT
3369 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:host.name=ip-172-31-4-51.ec2.internal
3369 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:java.version=1.7.0_79
3369 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:java.vendor=Oracle Corporation
3369 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:java.home=/opt/jdk1.7.0_79/jre
3369 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:java.class.path=/root/tweetcount/test:/root/tweetcount/topologies:/root/tweetcount/dev-resources:/root/tweetcount/_resources:/root/tweetcount/_build/classes:/root/.m2/repository/ch/qos/logback/logback-classic/1.0.13/logback-classic-1.0.13.jar:/root/.m2/repository/org/clojure/tools.macro/0.1.0/tools.macro-0.1.0.jar:/root/.m2/repository/ring/ring-core/1.1.5/ring-core-1.1.5.jar:/root/.m2/repository/hiccup/hiccup/0.3.6/hiccup-0.3.6.jar:/root/.m2/repository/ring/ring-servlet/0.3.11/ring-servlet-0.3.11.jar:/root/.m2/repository/com/googlecode/json-simple/json-simple/1.1/json-simple-1.1.jar:/root/.m2/repository/org/clojure/math.numeric-tower/0.0.1/math.numeric-tower-0.0.1.jar:/root/.m2/repository/clj-time/clj-time/0.4.1/clj-time-0.4.1.jar:/root/.m2/repository/org/objenesis/objenesis/1.2/objenesis-1.2.jar:/root/.m2/repository/com/twitter/chill-java/0.3.5/chill-java-0.3.5.jar:/root/.m2/repository/com/parsely/streamparse/0.0.4-SNAPSHOT/streamparse-0.0.4-SNAPSHOT.jar:/root/.m2/repository/ring/ring-jetty-adapter/0.3.11/ring-jetty-adapter-0.3.11.jar:/root/.m2/repository/jline/jline/2.11/jline-2.11.jar:/root/.m2/repository/clj-stacktrace/clj-stacktrace/0.2.2/clj-stacktrace-0.2.2.jar:/root/.m2/repository/org/clojure/tools.nrepl/0.2.12/tools.nrepl-0.2.12.jar:/root/.m2/repository/org/slf4j/slf4j-api/1.7.5/slf4j-api-1.7.5.jar:/root/.m2/repository/ring/ring-devel/0.3.11/ring-devel-0.3.11.jar:/root/.m2/repository/org/mortbay/jetty/jetty-util/6.1.26/jetty-util-6.1.26.jar:/root/.m2/repository/javax/servlet/servlet-api/2.5/servlet-api-2.5.jar:/root/.m2/repository/clojure-complete/clojure-complete/0.2.4/clojure-complete-0.2.4.jar:/root/.m2/repository/org/yaml/snakeyaml/1.11/snakeyaml-1.11.jar:/root/.m2/repository/ch/qos/logback/logback-core/1.0.13/logback-core-1.0.13.jar:/root/.m2/repository/commons-lang/commons-lang/2.5/commons-lang-2.5.jar:/root/.m2/repository/org/mortbay/jetty/jetty/6.1.26/jetty-6.1.26.jar:/root/.m2/repository/joda-time/joda-time/2.0/joda-time-2.0.jar:/root/.m2/repository/commons-io/commons-io/2.4/commons-io-2.4.jar:/root/.m2/repository/commons-logging/commons-logging/1.1.3/commons-logging-1.1.3.jar:/root/.m2/repository/com/esotericsoftware/kryo/kryo/2.21/kryo-2.21.jar:/root/.m2/repository/com/esotericsoftware/minlog/minlog/1.2/minlog-1.2.jar:/root/.m2/repository/org/apache/storm/storm-core/0.9.5/storm-core-0.9.5.jar:/root/.m2/repository/compojure/compojure/1.1.3/compojure-1.1.3.jar:/root/.m2/repository/com/esotericsoftware/reflectasm/reflectasm/1.07/reflectasm-1.07-shaded.jar:/root/.m2/repository/com/twitter/carbonite/1.4.0/carbonite-1.4.0.jar:/root/.m2/repository/commons-codec/commons-codec/1.6/commons-codec-1.6.jar:/root/.m2/repository/commons-fileupload/commons-fileupload/1.2.1/commons-fileupload-1.2.1.jar:/root/.m2/repository/org/clojure/data.json/0.2.6/data.json-0.2.6.jar:/root/.m2/repository/org/slf4j/log4j-over-slf4j/1.6.6/log4j-over-slf4j-1.6.6.jar:/root/.m2/repository/org/jgrapht/jgrapht-core/0.9.0/jgrapht-core-0.9.0.jar:/root/.m2/repository/org/clojure/clojure/1.5.1/clojure-1.5.1.jar:/root/.m2/repository/org/clojure/tools.logging/0.2.3/tools.logging-0.2.3.jar:/root/.m2/repository/org/ow2/asm/asm/4.0/asm-4.0.jar:/root/.m2/repository/clout/clout/1.0.1/clout-1.0.1.jar:/root/.m2/repository/org/apache/commons/commons-exec/1.1/commons-exec-1.1.jar:/root/.m2/repository/com/googlecode/disruptor/disruptor/2.10.1/disruptor-2.10.1.jar:/root/.m2/repository/org/clojure/core.incubator/0.1.0/core.incubator-0.1.0.jar:/root/.m2/repository/org/clojure/tools.cli/0.2.4/tools.cli-0.2.4.jar
3369 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:java.library.path=/usr/java/packages/lib/amd64:/usr/lib64:/lib64:/lib:/usr/lib
3369 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:java.io.tmpdir=/tmp
3369 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:java.compiler=<NA>
3369 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:os.name=Linux
3369 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:os.arch=amd64
3369 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:os.version=2.6.32-504.12.2.el6.centos.plus.x86_64
3369 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:user.name=root
3369 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:user.home=/root
3369 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:user.dir=/root/tweetcount
5715 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Created server with tickTime 2000 minSessionTimeout 4000 maxSessionTimeout 40000 datadir /tmp/0a34cbc5-b20c-4f47-aa6f-3c5d810c50a7/version-2 snapdir /tmp/0a34cbc5-b20c-4f47-aa6f-3c5d810c50a7/version-2
5745 [main] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - binding to port 0.0.0.0/0.0.0.0:2000
5757 [main] INFO  backtype.storm.zookeeper - Starting inprocess zookeeper at port 2000 and dir /tmp/0a34cbc5-b20c-4f47-aa6f-3c5d810c50a7
6278 [main] INFO  backtype.storm.daemon.nimbus - Starting Nimbus with conf {"dev.zookeeper.path" "/tmp/dev-storm-zookeeper", "topology.tick.tuple.freq.secs" nil, "topology.builtin.metrics.bucket.size.secs" 60, "topology.fall.back.on.java.serialization" true, "topology.max.error.report.per.interval" 5, "zmq.linger.millis" 0, "topology.skip.missing.kryo.registrations" true, "storm.messaging.netty.client_worker_threads" 1, "ui.childopts" "-Xmx768m", "storm.zookeeper.session.timeout" 20000, "nimbus.reassign" true, "topology.trident.batch.emit.interval.millis" 50, "storm.messaging.netty.flush.check.interval.ms" 10, "nimbus.monitor.freq.secs" 10, "logviewer.childopts" "-Xmx128m", "java.library.path" "/usr/local/lib:/opt/local/lib:/usr/lib", "topology.executor.send.buffer.size" 1024, "storm.local.dir" "/tmp/9d37bcde-d265-4c4c-9bf6-47c616faa230", "storm.messaging.netty.buffer_size" 5242880, "supervisor.worker.start.timeout.secs" 120, "topology.enable.message.timeouts" true, "nimbus.cleanup.inbox.freq.secs" 600, "nimbus.inbox.jar.expiration.secs" 3600, "drpc.worker.threads" 64, "storm.meta.serialization.delegate" "backtype.storm.serialization.DefaultSerializationDelegate", "topology.worker.shared.thread.pool.size" 4, "nimbus.host" "localhost", "storm.messaging.netty.min_wait_ms" 100, "storm.zookeeper.port" 2000, "transactional.zookeeper.port" nil, "topology.executor.receive.buffer.size" 1024, "transactional.zookeeper.servers" nil, "storm.zookeeper.root" "/storm", "storm.zookeeper.retry.intervalceiling.millis" 30000, "supervisor.enable" true, "storm.messaging.netty.server_worker_threads" 1, "storm.zookeeper.servers" ["localhost"], "transactional.zookeeper.root" "/transactional", "topology.acker.executors" nil, "topology.transfer.buffer.size" 1024, "topology.worker.childopts" nil, "drpc.queue.size" 128, "worker.childopts" "-Xmx768m", "supervisor.heartbeat.frequency.secs" 5, "topology.error.throttle.interval.secs" 10, "zmq.hwm" 0, "drpc.port" 3772, "supervisor.monitor.frequency.secs" 3, "drpc.childopts" "-Xmx768m", "topology.receiver.buffer.size" 8, "task.heartbeat.frequency.secs" 3, "topology.tasks" nil, "storm.messaging.netty.max_retries" 300, "topology.spout.wait.strategy" "backtype.storm.spout.SleepSpoutWaitStrategy", "nimbus.thrift.max_buffer_size" 1048576, "topology.max.spout.pending" nil, "storm.zookeeper.retry.interval" 1000, "topology.sleep.spout.wait.strategy.time.ms" 1, "nimbus.topology.validator" "backtype.storm.nimbus.DefaultTopologyValidator", "supervisor.slots.ports" [6700 6701 6702 6703], "topology.environment" nil, "topology.debug" false, "nimbus.task.launch.secs" 120, "nimbus.supervisor.timeout.secs" 60, "topology.message.timeout.secs" 30, "task.refresh.poll.secs" 10, "topology.workers" 1, "supervisor.childopts" "-Xmx256m", "nimbus.thrift.port" 6627, "topology.stats.sample.rate" 0.05, "worker.heartbeat.frequency.secs" 1, "topology.tuple.serializer" "backtype.storm.serialization.types.ListDelegateSerializer", "topology.disruptor.wait.strategy" "com.lmax.disruptor.BlockingWaitStrategy", "topology.multilang.serializer" "backtype.storm.multilang.JsonSerializer", "nimbus.task.timeout.secs" 30, "storm.zookeeper.connection.timeout" 15000, "topology.kryo.factory" "backtype.storm.serialization.DefaultKryoFactory", "drpc.invocations.port" 3773, "logviewer.port" 8000, "zmq.threads" 1, "storm.zookeeper.retry.times" 5, "topology.worker.receiver.thread.count" 1, "storm.thrift.transport" "backtype.storm.security.auth.SimpleTransportPlugin", "topology.state.synchronization.timeout.secs" 60, "supervisor.worker.timeout.secs" 30, "nimbus.file.copy.expiration.secs" 600, "storm.messaging.transport" "backtype.storm.messaging.netty.Context", "logviewer.appender.name" "A1", "storm.messaging.netty.max_wait_ms" 1000, "drpc.request.timeout.secs" 600, "storm.local.mode.zmq" false, "ui.port" 8080, "nimbus.childopts" "-Xmx1024m", "storm.cluster.mode" "local", "topology.max.task.parallelism" nil, "storm.messaging.netty.transfer.batch.size" 262144, "topology.classpath" nil}
6292 [main] INFO  backtype.storm.daemon.nimbus - Using default scheduler
6310 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
6555 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
6558 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000 sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@4b94b3b3
6608 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
6611 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55709
6615 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
6628 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55709
6630 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.persistence.FileTxnLog - Creating new log file: log.1
6656 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c663a8b0000 with negotiated timeout 20000 for client /127.0.0.1:55709
6657 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c663a8b0000, negotiated timeout = 20000
6659 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
6661 [main-EventThread] INFO  backtype.storm.zookeeper - Zookeeper state update: :connected:none
7722 [ProcessThread(sid:0 cport:-1):] INFO  org.apache.storm.zookeeper.server.PrepRequestProcessor - Processed session termination for sessionid: 0x1565c663a8b0000
7724 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Session: 0x1565c663a8b0000 closed
7725 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
7726 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
7726 [main-EventThread] INFO  org.apache.storm.zookeeper.ClientCnxn - EventThread shut down
7726 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000/storm sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@355dddf2
7732 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
7732 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
7733 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxn - Closed socket connection for client /127.0.0.1:55709 which had sessionid 0x1565c663a8b0000
7733 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55710
7733 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55710
7748 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c663a8b0001 with negotiated timeout 20000 for client /127.0.0.1:55710
7748 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c663a8b0001, negotiated timeout = 20000
7748 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
7808 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
7809 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
7809 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000 sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@4ca16872
7810 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
7820 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55711
7820 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
7820 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55711
7822 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c663a8b0002 with negotiated timeout 20000 for client /127.0.0.1:55711
7822 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c663a8b0002, negotiated timeout = 20000
7823 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
7823 [main-EventThread] INFO  backtype.storm.zookeeper - Zookeeper state update: :connected:none
7836 [ProcessThread(sid:0 cport:-1):] INFO  org.apache.storm.zookeeper.server.PrepRequestProcessor - Processed session termination for sessionid: 0x1565c663a8b0002
7837 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Session: 0x1565c663a8b0002 closed
7837 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
7838 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
7838 [main-EventThread] INFO  org.apache.storm.zookeeper.ClientCnxn - EventThread shut down
7838 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000/storm sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@306435cd
7839 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
7840 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
7841 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
7841 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
7842 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000 sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@e8a8eb3
7843 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
7843 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
7846 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxn - Closed socket connection for client /127.0.0.1:55711 which had sessionid 0x1565c663a8b0002
7846 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55712
7846 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55713
7846 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55712
7846 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55713
7860 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c663a8b0003 with negotiated timeout 20000 for client /127.0.0.1:55712
7860 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c663a8b0003, negotiated timeout = 20000
7860 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
7861 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c663a8b0004 with negotiated timeout 20000 for client /127.0.0.1:55713
7861 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c663a8b0004, negotiated timeout = 20000
7861 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
7862 [main-EventThread] INFO  backtype.storm.zookeeper - Zookeeper state update: :connected:none
8864 [ProcessThread(sid:0 cport:-1):] INFO  org.apache.storm.zookeeper.server.PrepRequestProcessor - Processed session termination for sessionid: 0x1565c663a8b0004
8866 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxn - Closed socket connection for client /127.0.0.1:55713 which had sessionid 0x1565c663a8b0004
8866 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Session: 0x1565c663a8b0004 closed
8867 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
8867 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
8867 [main-EventThread] INFO  org.apache.storm.zookeeper.ClientCnxn - EventThread shut down
8867 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000/storm sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@498f5e80
8868 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
8869 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55714
8869 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
8869 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55714
8881 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c663a8b0005 with negotiated timeout 20000 for client /127.0.0.1:55714
8881 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c663a8b0005, negotiated timeout = 20000
8881 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
8949 [main] INFO  backtype.storm.daemon.supervisor - Starting Supervisor with conf {"dev.zookeeper.path" "/tmp/dev-storm-zookeeper", "topology.tick.tuple.freq.secs" nil, "topology.builtin.metrics.bucket.size.secs" 60, "topology.fall.back.on.java.serialization" true, "topology.max.error.report.per.interval" 5, "zmq.linger.millis" 0, "topology.skip.missing.kryo.registrations" true, "storm.messaging.netty.client_worker_threads" 1, "ui.childopts" "-Xmx768m", "storm.zookeeper.session.timeout" 20000, "nimbus.reassign" true, "topology.trident.batch.emit.interval.millis" 50, "storm.messaging.netty.flush.check.interval.ms" 10, "nimbus.monitor.freq.secs" 10, "logviewer.childopts" "-Xmx128m", "java.library.path" "/usr/local/lib:/opt/local/lib:/usr/lib", "topology.executor.send.buffer.size" 1024, "storm.local.dir" "/tmp/c3728666-660e-44b9-b0bc-8f26afef4c11", "storm.messaging.netty.buffer_size" 5242880, "supervisor.worker.start.timeout.secs" 120, "topology.enable.message.timeouts" true, "nimbus.cleanup.inbox.freq.secs" 600, "nimbus.inbox.jar.expiration.secs" 3600, "drpc.worker.threads" 64, "storm.meta.serialization.delegate" "backtype.storm.serialization.DefaultSerializationDelegate", "topology.worker.shared.thread.pool.size" 4, "nimbus.host" "localhost", "storm.messaging.netty.min_wait_ms" 100, "storm.zookeeper.port" 2000, "transactional.zookeeper.port" nil, "topology.executor.receive.buffer.size" 1024, "transactional.zookeeper.servers" nil, "storm.zookeeper.root" "/storm", "storm.zookeeper.retry.intervalceiling.millis" 30000, "supervisor.enable" true, "storm.messaging.netty.server_worker_threads" 1, "storm.zookeeper.servers" ["localhost"], "transactional.zookeeper.root" "/transactional", "topology.acker.executors" nil, "topology.transfer.buffer.size" 1024, "topology.worker.childopts" nil, "drpc.queue.size" 128, "worker.childopts" "-Xmx768m", "supervisor.heartbeat.frequency.secs" 5, "topology.error.throttle.interval.secs" 10, "zmq.hwm" 0, "drpc.port" 3772, "supervisor.monitor.frequency.secs" 3, "drpc.childopts" "-Xmx768m", "topology.receiver.buffer.size" 8, "task.heartbeat.frequency.secs" 3, "topology.tasks" nil, "storm.messaging.netty.max_retries" 300, "topology.spout.wait.strategy" "backtype.storm.spout.SleepSpoutWaitStrategy", "nimbus.thrift.max_buffer_size" 1048576, "topology.max.spout.pending" nil, "storm.zookeeper.retry.interval" 1000, "topology.sleep.spout.wait.strategy.time.ms" 1, "nimbus.topology.validator" "backtype.storm.nimbus.DefaultTopologyValidator", "supervisor.slots.ports" (1024 1025 1026), "topology.environment" nil, "topology.debug" false, "nimbus.task.launch.secs" 120, "nimbus.supervisor.timeout.secs" 60, "topology.message.timeout.secs" 30, "task.refresh.poll.secs" 10, "topology.workers" 1, "supervisor.childopts" "-Xmx256m", "nimbus.thrift.port" 6627, "topology.stats.sample.rate" 0.05, "worker.heartbeat.frequency.secs" 1, "topology.tuple.serializer" "backtype.storm.serialization.types.ListDelegateSerializer", "topology.disruptor.wait.strategy" "com.lmax.disruptor.BlockingWaitStrategy", "topology.multilang.serializer" "backtype.storm.multilang.JsonSerializer", "nimbus.task.timeout.secs" 30, "storm.zookeeper.connection.timeout" 15000, "topology.kryo.factory" "backtype.storm.serialization.DefaultKryoFactory", "drpc.invocations.port" 3773, "logviewer.port" 8000, "zmq.threads" 1, "storm.zookeeper.retry.times" 5, "topology.worker.receiver.thread.count" 1, "storm.thrift.transport" "backtype.storm.security.auth.SimpleTransportPlugin", "topology.state.synchronization.timeout.secs" 60, "supervisor.worker.timeout.secs" 30, "nimbus.file.copy.expiration.secs" 600, "storm.messaging.transport" "backtype.storm.messaging.netty.Context", "logviewer.appender.name" "A1", "storm.messaging.netty.max_wait_ms" 1000, "drpc.request.timeout.secs" 600, "storm.local.mode.zmq" false, "ui.port" 8080, "nimbus.childopts" "-Xmx1024m", "storm.cluster.mode" "local", "topology.max.task.parallelism" nil, "storm.messaging.netty.transfer.batch.size" 262144, "topology.classpath" nil}
8966 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
8968 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
8969 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000 sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@6a55c240
8980 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
8980 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55715
8981 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
8981 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55715
8983 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c663a8b0006 with negotiated timeout 20000 for client /127.0.0.1:55715
8983 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c663a8b0006, negotiated timeout = 20000
8983 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
8984 [main-EventThread] INFO  backtype.storm.zookeeper - Zookeeper state update: :connected:none
9994 [ProcessThread(sid:0 cport:-1):] INFO  org.apache.storm.zookeeper.server.PrepRequestProcessor - Processed session termination for sessionid: 0x1565c663a8b0006
9996 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Session: 0x1565c663a8b0006 closed
9996 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
9996 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
9996 [main-EventThread] INFO  org.apache.storm.zookeeper.ClientCnxn - EventThread shut down
9997 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000/storm sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@1f238d32
9998 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
9998 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
10001 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxn - Closed socket connection for client /127.0.0.1:55715 which had sessionid 0x1565c663a8b0006
10001 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55716
10002 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55716
10018 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c663a8b0007 with negotiated timeout 20000 for client /127.0.0.1:55716
10018 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c663a8b0007, negotiated timeout = 20000
10018 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
10069 [main] INFO  backtype.storm.daemon.supervisor - Starting supervisor with id 8ff408a1-9f77-498d-9b38-1ee2db483375 at host ip-172-31-4-51.ec2.internal
10086 [main] INFO  backtype.storm.daemon.supervisor - Starting Supervisor with conf {"dev.zookeeper.path" "/tmp/dev-storm-zookeeper", "topology.tick.tuple.freq.secs" nil, "topology.builtin.metrics.bucket.size.secs" 60, "topology.fall.back.on.java.serialization" true, "topology.max.error.report.per.interval" 5, "zmq.linger.millis" 0, "topology.skip.missing.kryo.registrations" true, "storm.messaging.netty.client_worker_threads" 1, "ui.childopts" "-Xmx768m", "storm.zookeeper.session.timeout" 20000, "nimbus.reassign" true, "topology.trident.batch.emit.interval.millis" 50, "storm.messaging.netty.flush.check.interval.ms" 10, "nimbus.monitor.freq.secs" 10, "logviewer.childopts" "-Xmx128m", "java.library.path" "/usr/local/lib:/opt/local/lib:/usr/lib", "topology.executor.send.buffer.size" 1024, "storm.local.dir" "/tmp/493a705c-ac2d-440e-826b-eb9047b3d9fd", "storm.messaging.netty.buffer_size" 5242880, "supervisor.worker.start.timeout.secs" 120, "topology.enable.message.timeouts" true, "nimbus.cleanup.inbox.freq.secs" 600, "nimbus.inbox.jar.expiration.secs" 3600, "drpc.worker.threads" 64, "storm.meta.serialization.delegate" "backtype.storm.serialization.DefaultSerializationDelegate", "topology.worker.shared.thread.pool.size" 4, "nimbus.host" "localhost", "storm.messaging.netty.min_wait_ms" 100, "storm.zookeeper.port" 2000, "transactional.zookeeper.port" nil, "topology.executor.receive.buffer.size" 1024, "transactional.zookeeper.servers" nil, "storm.zookeeper.root" "/storm", "storm.zookeeper.retry.intervalceiling.millis" 30000, "supervisor.enable" true, "storm.messaging.netty.server_worker_threads" 1, "storm.zookeeper.servers" ["localhost"], "transactional.zookeeper.root" "/transactional", "topology.acker.executors" nil, "topology.transfer.buffer.size" 1024, "topology.worker.childopts" nil, "drpc.queue.size" 128, "worker.childopts" "-Xmx768m", "supervisor.heartbeat.frequency.secs" 5, "topology.error.throttle.interval.secs" 10, "zmq.hwm" 0, "drpc.port" 3772, "supervisor.monitor.frequency.secs" 3, "drpc.childopts" "-Xmx768m", "topology.receiver.buffer.size" 8, "task.heartbeat.frequency.secs" 3, "topology.tasks" nil, "storm.messaging.netty.max_retries" 300, "topology.spout.wait.strategy" "backtype.storm.spout.SleepSpoutWaitStrategy", "nimbus.thrift.max_buffer_size" 1048576, "topology.max.spout.pending" nil, "storm.zookeeper.retry.interval" 1000, "topology.sleep.spout.wait.strategy.time.ms" 1, "nimbus.topology.validator" "backtype.storm.nimbus.DefaultTopologyValidator", "supervisor.slots.ports" (1027 1028 1029), "topology.environment" nil, "topology.debug" false, "nimbus.task.launch.secs" 120, "nimbus.supervisor.timeout.secs" 60, "topology.message.timeout.secs" 30, "task.refresh.poll.secs" 10, "topology.workers" 1, "supervisor.childopts" "-Xmx256m", "nimbus.thrift.port" 6627, "topology.stats.sample.rate" 0.05, "worker.heartbeat.frequency.secs" 1, "topology.tuple.serializer" "backtype.storm.serialization.types.ListDelegateSerializer", "topology.disruptor.wait.strategy" "com.lmax.disruptor.BlockingWaitStrategy", "topology.multilang.serializer" "backtype.storm.multilang.JsonSerializer", "nimbus.task.timeout.secs" 30, "storm.zookeeper.connection.timeout" 15000, "topology.kryo.factory" "backtype.storm.serialization.DefaultKryoFactory", "drpc.invocations.port" 3773, "logviewer.port" 8000, "zmq.threads" 1, "storm.zookeeper.retry.times" 5, "topology.worker.receiver.thread.count" 1, "storm.thrift.transport" "backtype.storm.security.auth.SimpleTransportPlugin", "topology.state.synchronization.timeout.secs" 60, "supervisor.worker.timeout.secs" 30, "nimbus.file.copy.expiration.secs" 600, "storm.messaging.transport" "backtype.storm.messaging.netty.Context", "logviewer.appender.name" "A1", "storm.messaging.netty.max_wait_ms" 1000, "drpc.request.timeout.secs" 600, "storm.local.mode.zmq" false, "ui.port" 8080, "nimbus.childopts" "-Xmx1024m", "storm.cluster.mode" "local", "topology.max.task.parallelism" nil, "storm.messaging.netty.transfer.batch.size" 262144, "topology.classpath" nil}
10089 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
10089 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
10090 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000 sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@6aa8217b
10091 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
10099 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
10111 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55717
10111 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55717
10121 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c663a8b0008 with negotiated timeout 20000 for client /127.0.0.1:55717
10121 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c663a8b0008, negotiated timeout = 20000
10121 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
10122 [main-EventThread] INFO  backtype.storm.zookeeper - Zookeeper state update: :connected:none
10130 [ProcessThread(sid:0 cport:-1):] INFO  org.apache.storm.zookeeper.server.PrepRequestProcessor - Processed session termination for sessionid: 0x1565c663a8b0008
10131 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxn - Closed socket connection for client /127.0.0.1:55717 which had sessionid 0x1565c663a8b0008
10140 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Session: 0x1565c663a8b0008 closed
10140 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
10141 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
10141 [main-EventThread] INFO  org.apache.storm.zookeeper.ClientCnxn - EventThread shut down
10141 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000/storm sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@3b90a564
10142 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
10142 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55718
10143 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
10143 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55718
10147 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c663a8b0009 with negotiated timeout 20000 for client /127.0.0.1:55718
10147 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c663a8b0009, negotiated timeout = 20000
10147 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
11156 [main] INFO  backtype.storm.daemon.supervisor - Starting supervisor with id 02219054-6d8b-4e5f-8530-28de4f937cbc at host ip-172-31-4-51.ec2.internal
11289 [main] INFO  backtype.storm.daemon.nimbus - Received topology submission for tweetcount with conf {"storm.id" "tweetcount-1-1470429024", "topology.acker.executors" 2, "streamparse.log.path" "/root/tweetcount/logs", "topology.kryo.decorators" (), "topology.name" "tweetcount", "topology.max.spout.pending" 5000, "topology.debug" false, "topology.kryo.register" nil, "topology.message.timeout.secs" 60, "topology.workers" 2, "topology.max.task.parallelism" nil, "streamparse.log.level" "debug"}
11355 [main] INFO  backtype.storm.daemon.nimbus - Activating tweetcount: tweetcount-1-1470429024
11578 [main] INFO  backtype.storm.scheduler.EvenScheduler - Available slots: (["8ff408a1-9f77-498d-9b38-1ee2db483375" 1024] ["8ff408a1-9f77-498d-9b38-1ee2db483375" 1025] ["8ff408a1-9f77-498d-9b38-1ee2db483375" 1026] ["02219054-6d8b-4e5f-8530-28de4f937cbc" 1027] ["02219054-6d8b-4e5f-8530-28de4f937cbc" 1028] ["02219054-6d8b-4e5f-8530-28de4f937cbc" 1029])
11742 [main] INFO  backtype.storm.daemon.nimbus - Setting new assignment for topology id tweetcount-1-1470429024: #backtype.storm.daemon.common.Assignment{:master-code-dir "/tmp/9d37bcde-d265-4c4c-9bf6-47c616faa230/nimbus/stormdist/tweetcount-1-1470429024", :node->host {"8ff408a1-9f77-498d-9b38-1ee2db483375" "ip-172-31-4-51.ec2.internal", "02219054-6d8b-4e5f-8530-28de4f937cbc" "ip-172-31-4-51.ec2.internal"}, :executor->node+port {[3 3] ["8ff408a1-9f77-498d-9b38-1ee2db483375" 1024], [6 6] ["02219054-6d8b-4e5f-8530-28de4f937cbc" 1027], [5 5] ["8ff408a1-9f77-498d-9b38-1ee2db483375" 1024], [4 4] ["02219054-6d8b-4e5f-8530-28de4f937cbc" 1027], [7 7] ["8ff408a1-9f77-498d-9b38-1ee2db483375" 1024], [2 2] ["02219054-6d8b-4e5f-8530-28de4f937cbc" 1027], [1 1] ["8ff408a1-9f77-498d-9b38-1ee2db483375" 1024]}, :executor->start-time-secs {[7 7] 1470429024, [5 5] 1470429024, [3 3] 1470429024, [1 1] 1470429024, [6 6] 1470429024, [4 4] 1470429024, [2 2] 1470429024}}
13340 [Thread-3] INFO  backtype.storm.daemon.supervisor - Copying resources at file:/root/tweetcount/_resources/resources to /tmp/c3728666-660e-44b9-b0bc-8f26afef4c11/supervisor/stormdist/tweetcount-1-1470429024/resources
13398 [Thread-5] INFO  backtype.storm.daemon.supervisor - Copying resources at file:/root/tweetcount/_resources/resources to /tmp/493a705c-ac2d-440e-826b-eb9047b3d9fd/supervisor/stormdist/tweetcount-1-1470429024/resources
13496 [Thread-6] INFO  backtype.storm.daemon.supervisor - Launching worker with assignment #backtype.storm.daemon.supervisor.LocalAssignment{:storm-id "tweetcount-1-1470429024", :executors ([6 6] [4 4] [2 2])} for this supervisor 02219054-6d8b-4e5f-8530-28de4f937cbc on port 1027 with id 1ca1329b-6cb6-4e0e-b243-7dcee2666126
13507 [Thread-4] INFO  backtype.storm.daemon.supervisor - Launching worker with assignment #backtype.storm.daemon.supervisor.LocalAssignment{:storm-id "tweetcount-1-1470429024", :executors ([3 3] [5 5] [7 7] [1 1])} for this supervisor 8ff408a1-9f77-498d-9b38-1ee2db483375 on port 1024 with id 9d26885e-5525-4560-86d7-e18d7a6abb87
13513 [Thread-4] INFO  backtype.storm.daemon.worker - Launching worker for tweetcount-1-1470429024 on 8ff408a1-9f77-498d-9b38-1ee2db483375:1024 with id 9d26885e-5525-4560-86d7-e18d7a6abb87 and conf {"dev.zookeeper.path" "/tmp/dev-storm-zookeeper", "topology.tick.tuple.freq.secs" nil, "topology.builtin.metrics.bucket.size.secs" 60, "topology.fall.back.on.java.serialization" true, "topology.max.error.report.per.interval" 5, "zmq.linger.millis" 0, "topology.skip.missing.kryo.registrations" true, "storm.messaging.netty.client_worker_threads" 1, "ui.childopts" "-Xmx768m", "storm.zookeeper.session.timeout" 20000, "nimbus.reassign" true, "topology.trident.batch.emit.interval.millis" 50, "storm.messaging.netty.flush.check.interval.ms" 10, "nimbus.monitor.freq.secs" 10, "logviewer.childopts" "-Xmx128m", "java.library.path" "/usr/local/lib:/opt/local/lib:/usr/lib", "topology.executor.send.buffer.size" 1024, "storm.local.dir" "/tmp/c3728666-660e-44b9-b0bc-8f26afef4c11", "storm.messaging.netty.buffer_size" 5242880, "supervisor.worker.start.timeout.secs" 120, "topology.enable.message.timeouts" true, "nimbus.cleanup.inbox.freq.secs" 600, "nimbus.inbox.jar.expiration.secs" 3600, "drpc.worker.threads" 64, "storm.meta.serialization.delegate" "backtype.storm.serialization.DefaultSerializationDelegate", "topology.worker.shared.thread.pool.size" 4, "nimbus.host" "localhost", "storm.messaging.netty.min_wait_ms" 100, "storm.zookeeper.port" 2000, "transactional.zookeeper.port" nil, "topology.executor.receive.buffer.size" 1024, "transactional.zookeeper.servers" nil, "storm.zookeeper.root" "/storm", "storm.zookeeper.retry.intervalceiling.millis" 30000, "supervisor.enable" true, "storm.messaging.netty.server_worker_threads" 1, "storm.zookeeper.servers" ["localhost"], "transactional.zookeeper.root" "/transactional", "topology.acker.executors" nil, "topology.transfer.buffer.size" 1024, "topology.worker.childopts" nil, "drpc.queue.size" 128, "worker.childopts" "-Xmx768m", "supervisor.heartbeat.frequency.secs" 5, "topology.error.throttle.interval.secs" 10, "zmq.hwm" 0, "drpc.port" 3772, "supervisor.monitor.frequency.secs" 3, "drpc.childopts" "-Xmx768m", "topology.receiver.buffer.size" 8, "task.heartbeat.frequency.secs" 3, "topology.tasks" nil, "storm.messaging.netty.max_retries" 300, "topology.spout.wait.strategy" "backtype.storm.spout.SleepSpoutWaitStrategy", "nimbus.thrift.max_buffer_size" 1048576, "topology.max.spout.pending" nil, "storm.zookeeper.retry.interval" 1000, "topology.sleep.spout.wait.strategy.time.ms" 1, "nimbus.topology.validator" "backtype.storm.nimbus.DefaultTopologyValidator", "supervisor.slots.ports" (1024 1025 1026), "topology.environment" nil, "topology.debug" false, "nimbus.task.launch.secs" 120, "nimbus.supervisor.timeout.secs" 60, "topology.message.timeout.secs" 30, "task.refresh.poll.secs" 10, "topology.workers" 1, "supervisor.childopts" "-Xmx256m", "nimbus.thrift.port" 6627, "topology.stats.sample.rate" 0.05, "worker.heartbeat.frequency.secs" 1, "topology.tuple.serializer" "backtype.storm.serialization.types.ListDelegateSerializer", "topology.disruptor.wait.strategy" "com.lmax.disruptor.BlockingWaitStrategy", "topology.multilang.serializer" "backtype.storm.multilang.JsonSerializer", "nimbus.task.timeout.secs" 30, "storm.zookeeper.connection.timeout" 15000, "topology.kryo.factory" "backtype.storm.serialization.DefaultKryoFactory", "drpc.invocations.port" 3773, "logviewer.port" 8000, "zmq.threads" 1, "storm.zookeeper.retry.times" 5, "topology.worker.receiver.thread.count" 1, "storm.thrift.transport" "backtype.storm.security.auth.SimpleTransportPlugin", "topology.state.synchronization.timeout.secs" 60, "supervisor.worker.timeout.secs" 30, "nimbus.file.copy.expiration.secs" 600, "storm.messaging.transport" "backtype.storm.messaging.netty.Context", "logviewer.appender.name" "A1", "storm.messaging.netty.max_wait_ms" 1000, "drpc.request.timeout.secs" 600, "storm.local.mode.zmq" false, "ui.port" 8080, "nimbus.childopts" "-Xmx1024m", "storm.cluster.mode" "local", "topology.max.task.parallelism" nil, "storm.messaging.netty.transfer.batch.size" 262144, "topology.classpath" nil}
13514 [Thread-4] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
13514 [Thread-4] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
13523 [Thread-4] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000 sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@57db052b
13524 [Thread-4-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
13524 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55720
13525 [Thread-4-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
13525 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55720
13534 [Thread-6] INFO  backtype.storm.daemon.worker - Launching worker for tweetcount-1-1470429024 on 02219054-6d8b-4e5f-8530-28de4f937cbc:1027 with id 1ca1329b-6cb6-4e0e-b243-7dcee2666126 and conf {"dev.zookeeper.path" "/tmp/dev-storm-zookeeper", "topology.tick.tuple.freq.secs" nil, "topology.builtin.metrics.bucket.size.secs" 60, "topology.fall.back.on.java.serialization" true, "topology.max.error.report.per.interval" 5, "zmq.linger.millis" 0, "topology.skip.missing.kryo.registrations" true, "storm.messaging.netty.client_worker_threads" 1, "ui.childopts" "-Xmx768m", "storm.zookeeper.session.timeout" 20000, "nimbus.reassign" true, "topology.trident.batch.emit.interval.millis" 50, "storm.messaging.netty.flush.check.interval.ms" 10, "nimbus.monitor.freq.secs" 10, "logviewer.childopts" "-Xmx128m", "java.library.path" "/usr/local/lib:/opt/local/lib:/usr/lib", "topology.executor.send.buffer.size" 1024, "storm.local.dir" "/tmp/493a705c-ac2d-440e-826b-eb9047b3d9fd", "storm.messaging.netty.buffer_size" 5242880, "supervisor.worker.start.timeout.secs" 120, "topology.enable.message.timeouts" true, "nimbus.cleanup.inbox.freq.secs" 600, "nimbus.inbox.jar.expiration.secs" 3600, "drpc.worker.threads" 64, "storm.meta.serialization.delegate" "backtype.storm.serialization.DefaultSerializationDelegate", "topology.worker.shared.thread.pool.size" 4, "nimbus.host" "localhost", "storm.messaging.netty.min_wait_ms" 100, "storm.zookeeper.port" 2000, "transactional.zookeeper.port" nil, "topology.executor.receive.buffer.size" 1024, "transactional.zookeeper.servers" nil, "storm.zookeeper.root" "/storm", "storm.zookeeper.retry.intervalceiling.millis" 30000, "supervisor.enable" true, "storm.messaging.netty.server_worker_threads" 1, "storm.zookeeper.servers" ["localhost"], "transactional.zookeeper.root" "/transactional", "topology.acker.executors" nil, "topology.transfer.buffer.size" 1024, "topology.worker.childopts" nil, "drpc.queue.size" 128, "worker.childopts" "-Xmx768m", "supervisor.heartbeat.frequency.secs" 5, "topology.error.throttle.interval.secs" 10, "zmq.hwm" 0, "drpc.port" 3772, "supervisor.monitor.frequency.secs" 3, "drpc.childopts" "-Xmx768m", "topology.receiver.buffer.size" 8, "task.heartbeat.frequency.secs" 3, "topology.tasks" nil, "storm.messaging.netty.max_retries" 300, "topology.spout.wait.strategy" "backtype.storm.spout.SleepSpoutWaitStrategy", "nimbus.thrift.max_buffer_size" 1048576, "topology.max.spout.pending" nil, "storm.zookeeper.retry.interval" 1000, "topology.sleep.spout.wait.strategy.time.ms" 1, "nimbus.topology.validator" "backtype.storm.nimbus.DefaultTopologyValidator", "supervisor.slots.ports" (1027 1028 1029), "topology.environment" nil, "topology.debug" false, "nimbus.task.launch.secs" 120, "nimbus.supervisor.timeout.secs" 60, "topology.message.timeout.secs" 30, "task.refresh.poll.secs" 10, "topology.workers" 1, "supervisor.childopts" "-Xmx256m", "nimbus.thrift.port" 6627, "topology.stats.sample.rate" 0.05, "worker.heartbeat.frequency.secs" 1, "topology.tuple.serializer" "backtype.storm.serialization.types.ListDelegateSerializer", "topology.disruptor.wait.strategy" "com.lmax.disruptor.BlockingWaitStrategy", "topology.multilang.serializer" "backtype.storm.multilang.JsonSerializer", "nimbus.task.timeout.secs" 30, "storm.zookeeper.connection.timeout" 15000, "topology.kryo.factory" "backtype.storm.serialization.DefaultKryoFactory", "drpc.invocations.port" 3773, "logviewer.port" 8000, "zmq.threads" 1, "storm.zookeeper.retry.times" 5, "topology.worker.receiver.thread.count" 1, "storm.thrift.transport" "backtype.storm.security.auth.SimpleTransportPlugin", "topology.state.synchronization.timeout.secs" 60, "supervisor.worker.timeout.secs" 30, "nimbus.file.copy.expiration.secs" 600, "storm.messaging.transport" "backtype.storm.messaging.netty.Context", "logviewer.appender.name" "A1", "storm.messaging.netty.max_wait_ms" 1000, "drpc.request.timeout.secs" 600, "storm.local.mode.zmq" false, "ui.port" 8080, "nimbus.childopts" "-Xmx1024m", "storm.cluster.mode" "local", "topology.max.task.parallelism" nil, "storm.messaging.netty.transfer.batch.size" 262144, "topology.classpath" nil}
13543 [Thread-6] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
13544 [Thread-6] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
13548 [Thread-6] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000 sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@8dc66b6
13555 [Thread-6-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
13556 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55721
13556 [Thread-6-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
13557 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55721
13562 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c663a8b000a with negotiated timeout 20000 for client /127.0.0.1:55720
13563 [Thread-4-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c663a8b000a, negotiated timeout = 20000
13563 [Thread-4-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
13563 [Thread-4-EventThread] INFO  backtype.storm.zookeeper - Zookeeper state update: :connected:none
13564 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c663a8b000b with negotiated timeout 20000 for client /127.0.0.1:55721
13565 [Thread-6-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c663a8b000b, negotiated timeout = 20000
13566 [ProcessThread(sid:0 cport:-1):] INFO  org.apache.storm.zookeeper.server.PrepRequestProcessor - Processed session termination for sessionid: 0x1565c663a8b000a
13566 [Thread-6-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
13566 [Thread-6-EventThread] INFO  backtype.storm.zookeeper - Zookeeper state update: :connected:none
13576 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxn - Closed socket connection for client /127.0.0.1:55720 which had sessionid 0x1565c663a8b000a
13576 [Thread-4] INFO  org.apache.storm.zookeeper.ZooKeeper - Session: 0x1565c663a8b000a closed
13576 [Thread-4] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
13576 [Thread-4] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
13577 [Thread-4-EventThread] INFO  org.apache.storm.zookeeper.ClientCnxn - EventThread shut down
13579 [Thread-4] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000/storm sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@27f07e81
13580 [Thread-4-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
13581 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55722
13581 [Thread-4-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
13582 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55722
13583 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c663a8b000c with negotiated timeout 20000 for client /127.0.0.1:55722
13583 [Thread-4-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c663a8b000c, negotiated timeout = 20000
13592 [Thread-4-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
14568 [ProcessThread(sid:0 cport:-1):] INFO  org.apache.storm.zookeeper.server.PrepRequestProcessor - Processed session termination for sessionid: 0x1565c663a8b000b
14570 [Thread-6] INFO  org.apache.storm.zookeeper.ZooKeeper - Session: 0x1565c663a8b000b closed
14570 [Thread-6] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
14570 [Thread-6] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
14570 [Thread-6-EventThread] INFO  org.apache.storm.zookeeper.ClientCnxn - EventThread shut down
14571 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxn - Closed socket connection for client /127.0.0.1:55721 which had sessionid 0x1565c663a8b000b
14571 [Thread-6] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000/storm sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@b0a9ac0
14572 [Thread-6-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
14573 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55723
14573 [Thread-6-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
14573 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55723
14576 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c663a8b000d with negotiated timeout 20000 for client /127.0.0.1:55723
14577 [Thread-6-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c663a8b000d, negotiated timeout = 20000
14589 [Thread-6-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
14618 [Thread-4] INFO  backtype.storm.daemon.worker - Reading Assignments.
14730 [Thread-4] INFO  backtype.storm.daemon.worker - Launching receive-thread for 8ff408a1-9f77-498d-9b38-1ee2db483375:1024
14751 [Thread-7-worker-receiver-thread-0] INFO  backtype.storm.messaging.loader - Starting receive-thread: [stormId: tweetcount-1-1470429024, port: 1024, thread-id: 0 ]
15485 [Thread-4] INFO  backtype.storm.daemon.executor - Loading executor counter-bolt:[3 3]
15519 [Thread-4] INFO  backtype.storm.daemon.executor - Loaded executor tasks counter-bolt:[3 3]
15534 [Thread-4] INFO  backtype.storm.daemon.executor - Finished loading executor counter-bolt:[3 3]
15569 [Thread-4] INFO  backtype.storm.daemon.executor - Loading executor parse-bolt:[5 5]
15586 [Thread-4] INFO  backtype.storm.daemon.executor - Loaded executor tasks parse-bolt:[5 5]
15587 [Thread-4] INFO  backtype.storm.daemon.executor - Finished loading executor parse-bolt:[5 5]
15606 [Thread-4] INFO  backtype.storm.daemon.executor - Loading executor tweet-spout:[7 7]
15607 [Thread-4] INFO  backtype.storm.daemon.executor - Loaded executor tasks tweet-spout:[7 7]
15624 [Thread-6] INFO  backtype.storm.daemon.worker - Reading Assignments.
15649 [Thread-4] INFO  backtype.storm.daemon.executor - Finished loading executor tweet-spout:[7 7]
15672 [Thread-4] INFO  backtype.storm.daemon.executor - Loading executor __system:[-1 -1]
15673 [Thread-4] INFO  backtype.storm.daemon.executor - Loaded executor tasks __system:[-1 -1]
15692 [refresh-active-timer] INFO  backtype.storm.daemon.worker - All connections are ready for worker 8ff408a1-9f77-498d-9b38-1ee2db483375:1024 with id 9d26885e-5525-4560-86d7-e18d7a6abb87
15743 [Thread-4] INFO  backtype.storm.daemon.executor - Finished loading executor __system:[-1 -1]
15761 [Thread-4] INFO  backtype.storm.daemon.executor - Loading executor __acker:[1 1]
15762 [Thread-4] INFO  backtype.storm.daemon.executor - Loaded executor tasks __acker:[1 1]
15772 [Thread-4] INFO  backtype.storm.daemon.executor - Timeouts disabled for executor __acker:[1 1]
15772 [Thread-4] INFO  backtype.storm.daemon.executor - Finished loading executor __acker:[1 1]
15788 [Thread-6] INFO  backtype.storm.daemon.worker - Launching receive-thread for 02219054-6d8b-4e5f-8530-28de4f937cbc:1027
15792 [Thread-19-worker-receiver-thread-0] INFO  backtype.storm.messaging.loader - Starting receive-thread: [stormId: tweetcount-1-1470429024, port: 1027, thread-id: 0 ]
15808 [Thread-4] INFO  backtype.storm.daemon.worker - Worker has topology config {"storm.id" "tweetcount-1-1470429024", "dev.zookeeper.path" "/tmp/dev-storm-zookeeper", "topology.tick.tuple.freq.secs" nil, "topology.builtin.metrics.bucket.size.secs" 60, "topology.fall.back.on.java.serialization" true, "topology.max.error.report.per.interval" 5, "zmq.linger.millis" 0, "topology.skip.missing.kryo.registrations" true, "storm.messaging.netty.client_worker_threads" 1, "ui.childopts" "-Xmx768m", "storm.zookeeper.session.timeout" 20000, "nimbus.reassign" true, "topology.trident.batch.emit.interval.millis" 50, "storm.messaging.netty.flush.check.interval.ms" 10, "nimbus.monitor.freq.secs" 10, "logviewer.childopts" "-Xmx128m", "java.library.path" "/usr/local/lib:/opt/local/lib:/usr/lib", "topology.executor.send.buffer.size" 1024, "storm.local.dir" "/tmp/c3728666-660e-44b9-b0bc-8f26afef4c11", "storm.messaging.netty.buffer_size" 5242880, "supervisor.worker.start.timeout.secs" 120, "topology.enable.message.timeouts" true, "nimbus.cleanup.inbox.freq.secs" 600, "nimbus.inbox.jar.expiration.secs" 3600, "drpc.worker.threads" 64, "storm.meta.serialization.delegate" "backtype.storm.serialization.DefaultSerializationDelegate", "topology.worker.shared.thread.pool.size" 4, "nimbus.host" "localhost", "storm.messaging.netty.min_wait_ms" 100, "storm.zookeeper.port" 2000, "transactional.zookeeper.port" nil, "topology.executor.receive.buffer.size" 1024, "transactional.zookeeper.servers" nil, "storm.zookeeper.root" "/storm", "storm.zookeeper.retry.intervalceiling.millis" 30000, "supervisor.enable" true, "storm.messaging.netty.server_worker_threads" 1, "storm.zookeeper.servers" ["localhost"], "transactional.zookeeper.root" "/transactional", "topology.acker.executors" 2, "streamparse.log.path" "/root/tweetcount/logs", "topology.kryo.decorators" (), "topology.name" "tweetcount", "topology.transfer.buffer.size" 1024, "topology.worker.childopts" nil, "drpc.queue.size" 128, "worker.childopts" "-Xmx768m", "supervisor.heartbeat.frequency.secs" 5, "topology.error.throttle.interval.secs" 10, "zmq.hwm" 0, "drpc.port" 3772, "supervisor.monitor.frequency.secs" 3, "drpc.childopts" "-Xmx768m", "topology.receiver.buffer.size" 8, "task.heartbeat.frequency.secs" 3, "topology.tasks" nil, "storm.messaging.netty.max_retries" 300, "topology.spout.wait.strategy" "backtype.storm.spout.SleepSpoutWaitStrategy", "nimbus.thrift.max_buffer_size" 1048576, "topology.max.spout.pending" 5000, "storm.zookeeper.retry.interval" 1000, "topology.sleep.spout.wait.strategy.time.ms" 1, "nimbus.topology.validator" "backtype.storm.nimbus.DefaultTopologyValidator", "supervisor.slots.ports" (1024 1025 1026), "topology.environment" nil, "topology.debug" false, "nimbus.task.launch.secs" 120, "nimbus.supervisor.timeout.secs" 60, "topology.kryo.register" nil, "topology.message.timeout.secs" 60, "task.refresh.poll.secs" 10, "topology.workers" 2, "supervisor.childopts" "-Xmx256m", "nimbus.thrift.port" 6627, "topology.stats.sample.rate" 0.05, "worker.heartbeat.frequency.secs" 1, "topology.tuple.serializer" "backtype.storm.serialization.types.ListDelegateSerializer", "topology.disruptor.wait.strategy" "com.lmax.disruptor.BlockingWaitStrategy", "topology.multilang.serializer" "backtype.storm.multilang.JsonSerializer", "nimbus.task.timeout.secs" 30, "storm.zookeeper.connection.timeout" 15000, "topology.kryo.factory" "backtype.storm.serialization.DefaultKryoFactory", "drpc.invocations.port" 3773, "logviewer.port" 8000, "zmq.threads" 1, "storm.zookeeper.retry.times" 5, "topology.worker.receiver.thread.count" 1, "storm.thrift.transport" "backtype.storm.security.auth.SimpleTransportPlugin", "topology.state.synchronization.timeout.secs" 60, "supervisor.worker.timeout.secs" 30, "nimbus.file.copy.expiration.secs" 600, "storm.messaging.transport" "backtype.storm.messaging.netty.Context", "logviewer.appender.name" "A1", "storm.messaging.netty.max_wait_ms" 1000, "drpc.request.timeout.secs" 600, "storm.local.mode.zmq" false, "ui.port" 8080, "nimbus.childopts" "-Xmx1024m", "storm.cluster.mode" "local", "topology.max.task.parallelism" nil, "storm.messaging.netty.transfer.batch.size" 262144, "topology.classpath" nil, "streamparse.log.level" "debug"}
15809 [Thread-4] INFO  backtype.storm.daemon.worker - Worker 9d26885e-5525-4560-86d7-e18d7a6abb87 for storm tweetcount-1-1470429024 on 8ff408a1-9f77-498d-9b38-1ee2db483375:1024 has finished loading
15857 [Thread-6] INFO  backtype.storm.daemon.executor - Loading executor __acker:[2 2]
15858 [Thread-6] INFO  backtype.storm.daemon.executor - Loaded executor tasks __acker:[2 2]
15860 [Thread-6] INFO  backtype.storm.daemon.executor - Timeouts disabled for executor __acker:[2 2]
15860 [Thread-6] INFO  backtype.storm.daemon.executor - Finished loading executor __acker:[2 2]
15897 [Thread-6] INFO  backtype.storm.daemon.executor - Loading executor counter-bolt:[4 4]
15900 [Thread-6] INFO  backtype.storm.daemon.executor - Loaded executor tasks counter-bolt:[4 4]
15902 [Thread-6] INFO  backtype.storm.daemon.executor - Finished loading executor counter-bolt:[4 4]
15923 [Thread-6] INFO  backtype.storm.daemon.executor - Loading executor parse-bolt:[6 6]
15925 [Thread-6] INFO  backtype.storm.daemon.executor - Loaded executor tasks parse-bolt:[6 6]
15942 [Thread-6] INFO  backtype.storm.daemon.executor - Finished loading executor parse-bolt:[6 6]
15947 [Thread-6] INFO  backtype.storm.daemon.executor - Loading executor __system:[-1 -1]
15948 [Thread-6] INFO  backtype.storm.daemon.executor - Loaded executor tasks __system:[-1 -1]
15950 [Thread-6] INFO  backtype.storm.daemon.executor - Finished loading executor __system:[-1 -1]
15952 [Thread-6] INFO  backtype.storm.daemon.worker - Worker has topology config {"storm.id" "tweetcount-1-1470429024", "dev.zookeeper.path" "/tmp/dev-storm-zookeeper", "topology.tick.tuple.freq.secs" nil, "topology.builtin.metrics.bucket.size.secs" 60, "topology.fall.back.on.java.serialization" true, "topology.max.error.report.per.interval" 5, "zmq.linger.millis" 0, "topology.skip.missing.kryo.registrations" true, "storm.messaging.netty.client_worker_threads" 1, "ui.childopts" "-Xmx768m", "storm.zookeeper.session.timeout" 20000, "nimbus.reassign" true, "topology.trident.batch.emit.interval.millis" 50, "storm.messaging.netty.flush.check.interval.ms" 10, "nimbus.monitor.freq.secs" 10, "logviewer.childopts" "-Xmx128m", "java.library.path" "/usr/local/lib:/opt/local/lib:/usr/lib", "topology.executor.send.buffer.size" 1024, "storm.local.dir" "/tmp/493a705c-ac2d-440e-826b-eb9047b3d9fd", "storm.messaging.netty.buffer_size" 5242880, "supervisor.worker.start.timeout.secs" 120, "topology.enable.message.timeouts" true, "nimbus.cleanup.inbox.freq.secs" 600, "nimbus.inbox.jar.expiration.secs" 3600, "drpc.worker.threads" 64, "storm.meta.serialization.delegate" "backtype.storm.serialization.DefaultSerializationDelegate", "topology.worker.shared.thread.pool.size" 4, "nimbus.host" "localhost", "storm.messaging.netty.min_wait_ms" 100, "storm.zookeeper.port" 2000, "transactional.zookeeper.port" nil, "topology.executor.receive.buffer.size" 1024, "transactional.zookeeper.servers" nil, "storm.zookeeper.root" "/storm", "storm.zookeeper.retry.intervalceiling.millis" 30000, "supervisor.enable" true, "storm.messaging.netty.server_worker_threads" 1, "storm.zookeeper.servers" ["localhost"], "transactional.zookeeper.root" "/transactional", "topology.acker.executors" 2, "streamparse.log.path" "/root/tweetcount/logs", "topology.kryo.decorators" (), "topology.name" "tweetcount", "topology.transfer.buffer.size" 1024, "topology.worker.childopts" nil, "drpc.queue.size" 128, "worker.childopts" "-Xmx768m", "supervisor.heartbeat.frequency.secs" 5, "topology.error.throttle.interval.secs" 10, "zmq.hwm" 0, "drpc.port" 3772, "supervisor.monitor.frequency.secs" 3, "drpc.childopts" "-Xmx768m", "topology.receiver.buffer.size" 8, "task.heartbeat.frequency.secs" 3, "topology.tasks" nil, "storm.messaging.netty.max_retries" 300, "topology.spout.wait.strategy" "backtype.storm.spout.SleepSpoutWaitStrategy", "nimbus.thrift.max_buffer_size" 1048576, "topology.max.spout.pending" 5000, "storm.zookeeper.retry.interval" 1000, "topology.sleep.spout.wait.strategy.time.ms" 1, "nimbus.topology.validator" "backtype.storm.nimbus.DefaultTopologyValidator", "supervisor.slots.ports" (1027 1028 1029), "topology.environment" nil, "topology.debug" false, "nimbus.task.launch.secs" 120, "nimbus.supervisor.timeout.secs" 60, "topology.kryo.register" nil, "topology.message.timeout.secs" 60, "task.refresh.poll.secs" 10, "topology.workers" 2, "supervisor.childopts" "-Xmx256m", "nimbus.thrift.port" 6627, "topology.stats.sample.rate" 0.05, "worker.heartbeat.frequency.secs" 1, "topology.tuple.serializer" "backtype.storm.serialization.types.ListDelegateSerializer", "topology.disruptor.wait.strategy" "com.lmax.disruptor.BlockingWaitStrategy", "topology.multilang.serializer" "backtype.storm.multilang.JsonSerializer", "nimbus.task.timeout.secs" 30, "storm.zookeeper.connection.timeout" 15000, "topology.kryo.factory" "backtype.storm.serialization.DefaultKryoFactory", "drpc.invocations.port" 3773, "logviewer.port" 8000, "zmq.threads" 1, "storm.zookeeper.retry.times" 5, "topology.worker.receiver.thread.count" 1, "storm.thrift.transport" "backtype.storm.security.auth.SimpleTransportPlugin", "topology.state.synchronization.timeout.secs" 60, "supervisor.worker.timeout.secs" 30, "nimbus.file.copy.expiration.secs" 600, "storm.messaging.transport" "backtype.storm.messaging.netty.Context", "logviewer.appender.name" "A1", "storm.messaging.netty.max_wait_ms" 1000, "drpc.request.timeout.secs" 600, "storm.local.mode.zmq" false, "ui.port" 8080, "nimbus.childopts" "-Xmx1024m", "storm.cluster.mode" "local", "topology.max.task.parallelism" nil, "storm.messaging.netty.transfer.batch.size" 262144, "topology.classpath" nil, "streamparse.log.level" "debug"}
15953 [Thread-6] INFO  backtype.storm.daemon.worker - Worker 1ca1329b-6cb6-4e0e-b243-7dcee2666126 for storm tweetcount-1-1470429024 on 02219054-6d8b-4e5f-8530-28de4f937cbc:1027 has finished loading
16673 [refresh-active-timer] INFO  backtype.storm.daemon.worker - All connections are ready for worker 02219054-6d8b-4e5f-8530-28de4f937cbc:1027 with id 1ca1329b-6cb6-4e0e-b243-7dcee2666126
16969 [Thread-23-counter-bolt] INFO  backtype.storm.daemon.executor - Preparing bolt counter-bolt:(4)
16978 [Thread-27-__system] INFO  backtype.storm.daemon.executor - Preparing bolt __system:(-1)
16979 [Thread-13-tweet-spout] INFO  backtype.storm.daemon.executor - Opening spout tweet-spout:(7)
16980 [Thread-11-parse-bolt] INFO  backtype.storm.daemon.executor - Preparing bolt parse-bolt:(5)
16981 [Thread-17-__acker] INFO  backtype.storm.daemon.executor - Preparing bolt __acker:(1)
16981 [Thread-25-parse-bolt] INFO  backtype.storm.daemon.executor - Preparing bolt parse-bolt:(6)
16981 [Thread-21-__acker] INFO  backtype.storm.daemon.executor - Preparing bolt __acker:(2)
16997 [Thread-21-__acker] INFO  backtype.storm.daemon.executor - Prepared bolt __acker:(2)
17005 [Thread-17-__acker] INFO  backtype.storm.daemon.executor - Prepared bolt __acker:(1)
17006 [Thread-15-__system] INFO  backtype.storm.daemon.executor - Preparing bolt __system:(-1)
17026 [Thread-9-counter-bolt] INFO  backtype.storm.daemon.executor - Preparing bolt counter-bolt:(3)
17114 [Thread-27-__system] INFO  backtype.storm.daemon.executor - Prepared bolt __system:(-1)
17115 [Thread-15-__system] INFO  backtype.storm.daemon.executor - Prepared bolt __system:(-1)
17129 [Thread-13-tweet-spout] INFO  backtype.storm.utils.ShellProcess - Storm multilang serializer: backtype.storm.multilang.JsonSerializer
17131 [Thread-25-parse-bolt] INFO  backtype.storm.utils.ShellProcess - Storm multilang serializer: backtype.storm.multilang.JsonSerializer
17132 [Thread-23-counter-bolt] INFO  backtype.storm.utils.ShellProcess - Storm multilang serializer: backtype.storm.multilang.JsonSerializer
17132 [Thread-9-counter-bolt] INFO  backtype.storm.utils.ShellProcess - Storm multilang serializer: backtype.storm.multilang.JsonSerializer
17132 [Thread-11-parse-bolt] INFO  backtype.storm.utils.ShellProcess - Storm multilang serializer: backtype.storm.multilang.JsonSerializer
17838 [Thread-11-parse-bolt] INFO  backtype.storm.task.ShellBolt - Launched subprocess with pid 4000
17896 [Thread-11-parse-bolt] INFO  backtype.storm.task.ShellBolt - Start checking heartbeat...
17897 [Thread-11-parse-bolt] INFO  backtype.storm.daemon.executor - Prepared bolt parse-bolt:(5)
17959 [Thread-9-counter-bolt] INFO  backtype.storm.task.ShellBolt - Launched subprocess with pid 4001
17977 [Thread-9-counter-bolt] INFO  backtype.storm.task.ShellBolt - Start checking heartbeat...
17978 [Thread-9-counter-bolt] INFO  backtype.storm.daemon.executor - Prepared bolt counter-bolt:(3)
18076 [Thread-23-counter-bolt] INFO  backtype.storm.task.ShellBolt - Launched subprocess with pid 4002
18090 [Thread-23-counter-bolt] INFO  backtype.storm.task.ShellBolt - Start checking heartbeat...
18090 [Thread-23-counter-bolt] INFO  backtype.storm.daemon.executor - Prepared bolt counter-bolt:(4)
18110 [Thread-25-parse-bolt] INFO  backtype.storm.task.ShellBolt - Launched subprocess with pid 4003
18123 [Thread-25-parse-bolt] INFO  backtype.storm.task.ShellBolt - Start checking heartbeat...
18123 [Thread-25-parse-bolt] INFO  backtype.storm.daemon.executor - Prepared bolt parse-bolt:(6)
18290 [Thread-13-tweet-spout] INFO  backtype.storm.spout.ShellSpout - Launched subprocess with pid 4004
18312 [Thread-13-tweet-spout] INFO  backtype.storm.daemon.executor - Opened spout tweet-spout:(7)
18314 [Thread-13-tweet-spout] INFO  backtype.storm.daemon.executor - Activating spout tweet-spout:(7)
18314 [Thread-13-tweet-spout] INFO  backtype.storm.spout.ShellSpout - Start checking heartbeat...
18425 [Thread-13-tweet-spout] INFO  backtype.storm.spout.ShellSpout - ShellLog pid:4004, name:tweet-spout Empty queue exception 
18441 [Thread-13-tweet-spout] ERROR backtype.storm.daemon.executor - 
java.lang.Exception: Shell Process Exception: Python NameError raised
Traceback (most recent call last):
  File "/usr/lib/python2.7/site-packages/streamparse/storm/component.py", line 489, in run
    self._run()
  File "/usr/lib/python2.7/site-packages/streamparse/storm/spout.py", line 150, in _run
    self.next_tuple()
  File "spouts/tweets.py", line 76, in next_tuple
    time.sleep(0.1)
NameError: global name 'time' is not defined

	at backtype.storm.spout.ShellSpout.handleError(ShellSpout.java:212) [storm-core-0.9.5.jar:0.9.5]
	at backtype.storm.spout.ShellSpout.querySubprocess(ShellSpout.java:158) [storm-core-0.9.5.jar:0.9.5]
	at backtype.storm.spout.ShellSpout.nextTuple(ShellSpout.java:91) [storm-core-0.9.5.jar:0.9.5]
	at backtype.storm.daemon.executor$fn__3371$fn__3386$fn__3415.invoke(executor.clj:565) [storm-core-0.9.5.jar:0.9.5]
	at backtype.storm.util$async_loop$fn__460.invoke(util.clj:463) [storm-core-0.9.5.jar:0.9.5]
	at clojure.lang.AFn.run(AFn.java:24) [clojure-1.5.1.jar:na]
	at java.lang.Thread.run(Thread.java:745) [na:1.7.0_79]
18552 [Thread-13-tweet-spout] INFO  parse-bolt - /usr/lib/python2.7/site-packages/requests/packages/urllib3/util/ssl_.py:318: SNIMissingWarning: An HTTPS request has been made, but the SNI (Subject Name Indication) extension to TLS is not available on this platform. This may cause the server to present an incorrect TLS certificate, which can cause validation failures. You can upgrade to a newer version of Python to solve this. For more information, see https://urllib3.readthedocs.org/en/latest/security.html#snimissingwarning.
  SNIMissingWarning
/usr/lib/python2.7/site-packages/requests/packages/urllib3/util/ssl_.py:122: InsecurePlatformWarning: A true SSLContext object is not available. This prevents urllib3 from configuring SSL appropriately and may cause certain SSL connections to fail. You can upgrade to a newer version of Python to solve this. For more information, see https://urllib3.readthedocs.org/en/latest/security.html#insecureplatformwarning.
  InsecurePlatformWarning

19811 [Thread-13-tweet-spout] ERROR backtype.storm.util - Async loop died!
java.lang.RuntimeException: pid:4004, name:tweet-spout exitCode:-1, errorString: 
	at backtype.storm.spout.ShellSpout.querySubprocess(ShellSpout.java:180) ~[storm-core-0.9.5.jar:0.9.5]
	at backtype.storm.spout.ShellSpout.nextTuple(ShellSpout.java:91) ~[storm-core-0.9.5.jar:0.9.5]
	at backtype.storm.daemon.executor$fn__3371$fn__3386$fn__3415.invoke(executor.clj:565) ~[storm-core-0.9.5.jar:0.9.5]
	at backtype.storm.util$async_loop$fn__460.invoke(util.clj:463) ~[storm-core-0.9.5.jar:0.9.5]
	at clojure.lang.AFn.run(AFn.java:24) [clojure-1.5.1.jar:na]
	at java.lang.Thread.run(Thread.java:745) [na:1.7.0_79]
Caused by: java.lang.RuntimeException: backtype.storm.multilang.NoOutputException: Pipe to subprocess seems to be broken! No output read.
Serializer Exception:
Exception in thread Thread-1:
Traceback (most recent call last):
  File "/usr/lib64/python2.7/threading.py", line 551, in __bootstrap_inner
    self.run()
  File "/usr/lib64/python2.7/threading.py", line 504, in run
    self.__target(*self.__args, **self.__kwargs)
  File "/usr/lib/python2.7/site-packages/tweepy/streaming.py", line 294, in _run
    raise exception
Full



	at backtype.storm.utils.ShellProcess.readShellMsg(ShellProcess.java:101) ~[storm-core-0.9.5.jar:0.9.5]
	at backtype.storm.spout.ShellSpout.querySubprocess(ShellSpout.java:145) ~[storm-core-0.9.5.jar:0.9.5]
	... 5 common frames omitted
19811 [Thread-13-tweet-spout] ERROR backtype.storm.daemon.executor - 
java.lang.RuntimeException: pid:4004, name:tweet-spout exitCode:-1, errorString: 
	at backtype.storm.spout.ShellSpout.querySubprocess(ShellSpout.java:180) ~[storm-core-0.9.5.jar:0.9.5]
	at backtype.storm.spout.ShellSpout.nextTuple(ShellSpout.java:91) ~[storm-core-0.9.5.jar:0.9.5]
	at backtype.storm.daemon.executor$fn__3371$fn__3386$fn__3415.invoke(executor.clj:565) ~[storm-core-0.9.5.jar:0.9.5]
	at backtype.storm.util$async_loop$fn__460.invoke(util.clj:463) ~[storm-core-0.9.5.jar:0.9.5]
	at clojure.lang.AFn.run(AFn.java:24) [clojure-1.5.1.jar:na]
	at java.lang.Thread.run(Thread.java:745) [na:1.7.0_79]
Caused by: java.lang.RuntimeException: backtype.storm.multilang.NoOutputException: Pipe to subprocess seems to be broken! No output read.
Serializer Exception:
Exception in thread Thread-1:
Traceback (most recent call last):
  File "/usr/lib64/python2.7/threading.py", line 551, in __bootstrap_inner
    self.run()
  File "/usr/lib64/python2.7/threading.py", line 504, in run
    self.__target(*self.__args, **self.__kwargs)
  File "/usr/lib/python2.7/site-packages/tweepy/streaming.py", line 294, in _run
    raise exception
Full



	at backtype.storm.utils.ShellProcess.readShellMsg(ShellProcess.java:101) ~[storm-core-0.9.5.jar:0.9.5]
	at backtype.storm.spout.ShellSpout.querySubprocess(ShellSpout.java:145) ~[storm-core-0.9.5.jar:0.9.5]
	... 5 common frames omitted
19855 [Thread-13-tweet-spout] ERROR backtype.storm.util - Halting process: ("Worker died")
java.lang.RuntimeException: ("Worker died")
	at backtype.storm.util$exit_process_BANG_.doInvoke(util.clj:325) [storm-core-0.9.5.jar:0.9.5]
	at clojure.lang.RestFn.invoke(RestFn.java:423) [clojure-1.5.1.jar:na]
	at backtype.storm.daemon.worker$fn__4694$fn__4695.invoke(worker.clj:493) [storm-core-0.9.5.jar:0.9.5]
	at backtype.storm.daemon.executor$mk_executor_data$fn__3272$fn__3273.invoke(executor.clj:240) [storm-core-0.9.5.jar:0.9.5]
	at backtype.storm.util$async_loop$fn__460.invoke(util.clj:473) [storm-core-0.9.5.jar:0.9.5]
	at clojure.lang.AFn.run(AFn.java:24) [clojure-1.5.1.jar:na]
	at java.lang.Thread.run(Thread.java:745) [na:1.7.0_79]
Traceback (most recent call last):
  File "/usr/bin/sparse", line 9, in <module>
    load_entry_point('streamparse==2.1.4', 'console_scripts', 'sparse')()
  File "/usr/lib/python2.7/site-packages/streamparse/cli/sparse.py", line 57, in main
    args.func(args)
  File "/usr/lib/python2.7/site-packages/streamparse/cli/run.py", line 81, in main
    debug=args.debug)
  File "/usr/lib/python2.7/site-packages/streamparse/cli/run.py", line 52, in run_local_topology
    run(full_cmd)
  File "/usr/lib/python2.7/site-packages/invoke/__init__.py", line 32, in run
    return Context().run(command, **kwargs)
  File "/usr/lib/python2.7/site-packages/invoke/context.py", line 53, in run
    return runner_class(context=self).run(command, **kwargs)
  File "/usr/lib/python2.7/site-packages/invoke/runners.py", line 363, in run
    raise Failure(result)
invoke.exceptions.Failure: Command execution failure!

Exit code: 1

Stderr:




[root@ip-172-31-4-51 tweetcount]# sparse run -d -t 80 -n tweetcount
Running tweetcount topology...
Routing Python logging to /root/tweetcount/logs.
Running lein command to run local cluster:
lein run -m streamparse.commands.run/-main topologies/tweetcount.clj -t 80 --debug --option 'topology.workers=2' --option 'topology.acker.executors=2' --option 'streamparse.log.path="/root/tweetcount/logs"' --option 'streamparse.log.level="debug"'
WARNING: You're currently running as root; probably by accident.
Press control-C to abort or Enter to continue as root.
Set LEIN_ROOT to disable this warning.

3141 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:zookeeper.version=3.4.6-1569965, built on 02/20/2014 09:09 GMT
3145 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:host.name=ip-172-31-4-51.ec2.internal
3145 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:java.version=1.7.0_79
3145 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:java.vendor=Oracle Corporation
3146 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:java.home=/opt/jdk1.7.0_79/jre
3146 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:java.class.path=/root/tweetcount/test:/root/tweetcount/topologies:/root/tweetcount/dev-resources:/root/tweetcount/_resources:/root/tweetcount/_build/classes:/root/.m2/repository/ch/qos/logback/logback-classic/1.0.13/logback-classic-1.0.13.jar:/root/.m2/repository/org/clojure/tools.macro/0.1.0/tools.macro-0.1.0.jar:/root/.m2/repository/ring/ring-core/1.1.5/ring-core-1.1.5.jar:/root/.m2/repository/hiccup/hiccup/0.3.6/hiccup-0.3.6.jar:/root/.m2/repository/ring/ring-servlet/0.3.11/ring-servlet-0.3.11.jar:/root/.m2/repository/com/googlecode/json-simple/json-simple/1.1/json-simple-1.1.jar:/root/.m2/repository/org/clojure/math.numeric-tower/0.0.1/math.numeric-tower-0.0.1.jar:/root/.m2/repository/clj-time/clj-time/0.4.1/clj-time-0.4.1.jar:/root/.m2/repository/org/objenesis/objenesis/1.2/objenesis-1.2.jar:/root/.m2/repository/com/twitter/chill-java/0.3.5/chill-java-0.3.5.jar:/root/.m2/repository/com/parsely/streamparse/0.0.4-SNAPSHOT/streamparse-0.0.4-SNAPSHOT.jar:/root/.m2/repository/ring/ring-jetty-adapter/0.3.11/ring-jetty-adapter-0.3.11.jar:/root/.m2/repository/jline/jline/2.11/jline-2.11.jar:/root/.m2/repository/clj-stacktrace/clj-stacktrace/0.2.2/clj-stacktrace-0.2.2.jar:/root/.m2/repository/org/clojure/tools.nrepl/0.2.12/tools.nrepl-0.2.12.jar:/root/.m2/repository/org/slf4j/slf4j-api/1.7.5/slf4j-api-1.7.5.jar:/root/.m2/repository/ring/ring-devel/0.3.11/ring-devel-0.3.11.jar:/root/.m2/repository/org/mortbay/jetty/jetty-util/6.1.26/jetty-util-6.1.26.jar:/root/.m2/repository/javax/servlet/servlet-api/2.5/servlet-api-2.5.jar:/root/.m2/repository/clojure-complete/clojure-complete/0.2.4/clojure-complete-0.2.4.jar:/root/.m2/repository/org/yaml/snakeyaml/1.11/snakeyaml-1.11.jar:/root/.m2/repository/ch/qos/logback/logback-core/1.0.13/logback-core-1.0.13.jar:/root/.m2/repository/commons-lang/commons-lang/2.5/commons-lang-2.5.jar:/root/.m2/repository/org/mortbay/jetty/jetty/6.1.26/jetty-6.1.26.jar:/root/.m2/repository/joda-time/joda-time/2.0/joda-time-2.0.jar:/root/.m2/repository/commons-io/commons-io/2.4/commons-io-2.4.jar:/root/.m2/repository/commons-logging/commons-logging/1.1.3/commons-logging-1.1.3.jar:/root/.m2/repository/com/esotericsoftware/kryo/kryo/2.21/kryo-2.21.jar:/root/.m2/repository/com/esotericsoftware/minlog/minlog/1.2/minlog-1.2.jar:/root/.m2/repository/org/apache/storm/storm-core/0.9.5/storm-core-0.9.5.jar:/root/.m2/repository/compojure/compojure/1.1.3/compojure-1.1.3.jar:/root/.m2/repository/com/esotericsoftware/reflectasm/reflectasm/1.07/reflectasm-1.07-shaded.jar:/root/.m2/repository/com/twitter/carbonite/1.4.0/carbonite-1.4.0.jar:/root/.m2/repository/commons-codec/commons-codec/1.6/commons-codec-1.6.jar:/root/.m2/repository/commons-fileupload/commons-fileupload/1.2.1/commons-fileupload-1.2.1.jar:/root/.m2/repository/org/clojure/data.json/0.2.6/data.json-0.2.6.jar:/root/.m2/repository/org/slf4j/log4j-over-slf4j/1.6.6/log4j-over-slf4j-1.6.6.jar:/root/.m2/repository/org/jgrapht/jgrapht-core/0.9.0/jgrapht-core-0.9.0.jar:/root/.m2/repository/org/clojure/clojure/1.5.1/clojure-1.5.1.jar:/root/.m2/repository/org/clojure/tools.logging/0.2.3/tools.logging-0.2.3.jar:/root/.m2/repository/org/ow2/asm/asm/4.0/asm-4.0.jar:/root/.m2/repository/clout/clout/1.0.1/clout-1.0.1.jar:/root/.m2/repository/org/apache/commons/commons-exec/1.1/commons-exec-1.1.jar:/root/.m2/repository/com/googlecode/disruptor/disruptor/2.10.1/disruptor-2.10.1.jar:/root/.m2/repository/org/clojure/core.incubator/0.1.0/core.incubator-0.1.0.jar:/root/.m2/repository/org/clojure/tools.cli/0.2.4/tools.cli-0.2.4.jar
3146 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:java.library.path=/usr/java/packages/lib/amd64:/usr/lib64:/lib64:/lib:/usr/lib
3146 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:java.io.tmpdir=/tmp
3146 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:java.compiler=<NA>
3146 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:os.name=Linux
3146 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:os.arch=amd64
3147 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:os.version=2.6.32-504.12.2.el6.centos.plus.x86_64
3147 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:user.name=root
3147 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:user.home=/root
3147 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:user.dir=/root/tweetcount
3218 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:zookeeper.version=3.4.6-1569965, built on 02/20/2014 09:09 GMT
3218 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:host.name=ip-172-31-4-51.ec2.internal
3218 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:java.version=1.7.0_79
3218 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:java.vendor=Oracle Corporation
3218 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:java.home=/opt/jdk1.7.0_79/jre
3218 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:java.class.path=/root/tweetcount/test:/root/tweetcount/topologies:/root/tweetcount/dev-resources:/root/tweetcount/_resources:/root/tweetcount/_build/classes:/root/.m2/repository/ch/qos/logback/logback-classic/1.0.13/logback-classic-1.0.13.jar:/root/.m2/repository/org/clojure/tools.macro/0.1.0/tools.macro-0.1.0.jar:/root/.m2/repository/ring/ring-core/1.1.5/ring-core-1.1.5.jar:/root/.m2/repository/hiccup/hiccup/0.3.6/hiccup-0.3.6.jar:/root/.m2/repository/ring/ring-servlet/0.3.11/ring-servlet-0.3.11.jar:/root/.m2/repository/com/googlecode/json-simple/json-simple/1.1/json-simple-1.1.jar:/root/.m2/repository/org/clojure/math.numeric-tower/0.0.1/math.numeric-tower-0.0.1.jar:/root/.m2/repository/clj-time/clj-time/0.4.1/clj-time-0.4.1.jar:/root/.m2/repository/org/objenesis/objenesis/1.2/objenesis-1.2.jar:/root/.m2/repository/com/twitter/chill-java/0.3.5/chill-java-0.3.5.jar:/root/.m2/repository/com/parsely/streamparse/0.0.4-SNAPSHOT/streamparse-0.0.4-SNAPSHOT.jar:/root/.m2/repository/ring/ring-jetty-adapter/0.3.11/ring-jetty-adapter-0.3.11.jar:/root/.m2/repository/jline/jline/2.11/jline-2.11.jar:/root/.m2/repository/clj-stacktrace/clj-stacktrace/0.2.2/clj-stacktrace-0.2.2.jar:/root/.m2/repository/org/clojure/tools.nrepl/0.2.12/tools.nrepl-0.2.12.jar:/root/.m2/repository/org/slf4j/slf4j-api/1.7.5/slf4j-api-1.7.5.jar:/root/.m2/repository/ring/ring-devel/0.3.11/ring-devel-0.3.11.jar:/root/.m2/repository/org/mortbay/jetty/jetty-util/6.1.26/jetty-util-6.1.26.jar:/root/.m2/repository/javax/servlet/servlet-api/2.5/servlet-api-2.5.jar:/root/.m2/repository/clojure-complete/clojure-complete/0.2.4/clojure-complete-0.2.4.jar:/root/.m2/repository/org/yaml/snakeyaml/1.11/snakeyaml-1.11.jar:/root/.m2/repository/ch/qos/logback/logback-core/1.0.13/logback-core-1.0.13.jar:/root/.m2/repository/commons-lang/commons-lang/2.5/commons-lang-2.5.jar:/root/.m2/repository/org/mortbay/jetty/jetty/6.1.26/jetty-6.1.26.jar:/root/.m2/repository/joda-time/joda-time/2.0/joda-time-2.0.jar:/root/.m2/repository/commons-io/commons-io/2.4/commons-io-2.4.jar:/root/.m2/repository/commons-logging/commons-logging/1.1.3/commons-logging-1.1.3.jar:/root/.m2/repository/com/esotericsoftware/kryo/kryo/2.21/kryo-2.21.jar:/root/.m2/repository/com/esotericsoftware/minlog/minlog/1.2/minlog-1.2.jar:/root/.m2/repository/org/apache/storm/storm-core/0.9.5/storm-core-0.9.5.jar:/root/.m2/repository/compojure/compojure/1.1.3/compojure-1.1.3.jar:/root/.m2/repository/com/esotericsoftware/reflectasm/reflectasm/1.07/reflectasm-1.07-shaded.jar:/root/.m2/repository/com/twitter/carbonite/1.4.0/carbonite-1.4.0.jar:/root/.m2/repository/commons-codec/commons-codec/1.6/commons-codec-1.6.jar:/root/.m2/repository/commons-fileupload/commons-fileupload/1.2.1/commons-fileupload-1.2.1.jar:/root/.m2/repository/org/clojure/data.json/0.2.6/data.json-0.2.6.jar:/root/.m2/repository/org/slf4j/log4j-over-slf4j/1.6.6/log4j-over-slf4j-1.6.6.jar:/root/.m2/repository/org/jgrapht/jgrapht-core/0.9.0/jgrapht-core-0.9.0.jar:/root/.m2/repository/org/clojure/clojure/1.5.1/clojure-1.5.1.jar:/root/.m2/repository/org/clojure/tools.logging/0.2.3/tools.logging-0.2.3.jar:/root/.m2/repository/org/ow2/asm/asm/4.0/asm-4.0.jar:/root/.m2/repository/clout/clout/1.0.1/clout-1.0.1.jar:/root/.m2/repository/org/apache/commons/commons-exec/1.1/commons-exec-1.1.jar:/root/.m2/repository/com/googlecode/disruptor/disruptor/2.10.1/disruptor-2.10.1.jar:/root/.m2/repository/org/clojure/core.incubator/0.1.0/core.incubator-0.1.0.jar:/root/.m2/repository/org/clojure/tools.cli/0.2.4/tools.cli-0.2.4.jar
3219 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:java.library.path=/usr/java/packages/lib/amd64:/usr/lib64:/lib64:/lib:/usr/lib
3219 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:java.io.tmpdir=/tmp
3219 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:java.compiler=<NA>
3219 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:os.name=Linux
3219 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:os.arch=amd64
3219 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:os.version=2.6.32-504.12.2.el6.centos.plus.x86_64
3219 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:user.name=root
3219 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:user.home=/root
3219 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:user.dir=/root/tweetcount
5172 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Created server with tickTime 2000 minSessionTimeout 4000 maxSessionTimeout 40000 datadir /tmp/65643540-5e7c-4ff1-8cec-5fa2e419032d/version-2 snapdir /tmp/65643540-5e7c-4ff1-8cec-5fa2e419032d/version-2
5264 [main] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - binding to port 0.0.0.0/0.0.0.0:2000
5268 [main] INFO  backtype.storm.zookeeper - Starting inprocess zookeeper at port 2000 and dir /tmp/65643540-5e7c-4ff1-8cec-5fa2e419032d
5770 [main] INFO  backtype.storm.daemon.nimbus - Starting Nimbus with conf {"dev.zookeeper.path" "/tmp/dev-storm-zookeeper", "topology.tick.tuple.freq.secs" nil, "topology.builtin.metrics.bucket.size.secs" 60, "topology.fall.back.on.java.serialization" true, "topology.max.error.report.per.interval" 5, "zmq.linger.millis" 0, "topology.skip.missing.kryo.registrations" true, "storm.messaging.netty.client_worker_threads" 1, "ui.childopts" "-Xmx768m", "storm.zookeeper.session.timeout" 20000, "nimbus.reassign" true, "topology.trident.batch.emit.interval.millis" 50, "storm.messaging.netty.flush.check.interval.ms" 10, "nimbus.monitor.freq.secs" 10, "logviewer.childopts" "-Xmx128m", "java.library.path" "/usr/local/lib:/opt/local/lib:/usr/lib", "topology.executor.send.buffer.size" 1024, "storm.local.dir" "/tmp/937314f4-7c19-486b-8f28-81c7c6de5a7e", "storm.messaging.netty.buffer_size" 5242880, "supervisor.worker.start.timeout.secs" 120, "topology.enable.message.timeouts" true, "nimbus.cleanup.inbox.freq.secs" 600, "nimbus.inbox.jar.expiration.secs" 3600, "drpc.worker.threads" 64, "storm.meta.serialization.delegate" "backtype.storm.serialization.DefaultSerializationDelegate", "topology.worker.shared.thread.pool.size" 4, "nimbus.host" "localhost", "storm.messaging.netty.min_wait_ms" 100, "storm.zookeeper.port" 2000, "transactional.zookeeper.port" nil, "topology.executor.receive.buffer.size" 1024, "transactional.zookeeper.servers" nil, "storm.zookeeper.root" "/storm", "storm.zookeeper.retry.intervalceiling.millis" 30000, "supervisor.enable" true, "storm.messaging.netty.server_worker_threads" 1, "storm.zookeeper.servers" ["localhost"], "transactional.zookeeper.root" "/transactional", "topology.acker.executors" nil, "topology.transfer.buffer.size" 1024, "topology.worker.childopts" nil, "drpc.queue.size" 128, "worker.childopts" "-Xmx768m", "supervisor.heartbeat.frequency.secs" 5, "topology.error.throttle.interval.secs" 10, "zmq.hwm" 0, "drpc.port" 3772, "supervisor.monitor.frequency.secs" 3, "drpc.childopts" "-Xmx768m", "topology.receiver.buffer.size" 8, "task.heartbeat.frequency.secs" 3, "topology.tasks" nil, "storm.messaging.netty.max_retries" 300, "topology.spout.wait.strategy" "backtype.storm.spout.SleepSpoutWaitStrategy", "nimbus.thrift.max_buffer_size" 1048576, "topology.max.spout.pending" nil, "storm.zookeeper.retry.interval" 1000, "topology.sleep.spout.wait.strategy.time.ms" 1, "nimbus.topology.validator" "backtype.storm.nimbus.DefaultTopologyValidator", "supervisor.slots.ports" [6700 6701 6702 6703], "topology.environment" nil, "topology.debug" false, "nimbus.task.launch.secs" 120, "nimbus.supervisor.timeout.secs" 60, "topology.message.timeout.secs" 30, "task.refresh.poll.secs" 10, "topology.workers" 1, "supervisor.childopts" "-Xmx256m", "nimbus.thrift.port" 6627, "topology.stats.sample.rate" 0.05, "worker.heartbeat.frequency.secs" 1, "topology.tuple.serializer" "backtype.storm.serialization.types.ListDelegateSerializer", "topology.disruptor.wait.strategy" "com.lmax.disruptor.BlockingWaitStrategy", "topology.multilang.serializer" "backtype.storm.multilang.JsonSerializer", "nimbus.task.timeout.secs" 30, "storm.zookeeper.connection.timeout" 15000, "topology.kryo.factory" "backtype.storm.serialization.DefaultKryoFactory", "drpc.invocations.port" 3773, "logviewer.port" 8000, "zmq.threads" 1, "storm.zookeeper.retry.times" 5, "topology.worker.receiver.thread.count" 1, "storm.thrift.transport" "backtype.storm.security.auth.SimpleTransportPlugin", "topology.state.synchronization.timeout.secs" 60, "supervisor.worker.timeout.secs" 30, "nimbus.file.copy.expiration.secs" 600, "storm.messaging.transport" "backtype.storm.messaging.netty.Context", "logviewer.appender.name" "A1", "storm.messaging.netty.max_wait_ms" 1000, "drpc.request.timeout.secs" 600, "storm.local.mode.zmq" false, "ui.port" 8080, "nimbus.childopts" "-Xmx1024m", "storm.cluster.mode" "local", "topology.max.task.parallelism" nil, "storm.messaging.netty.transfer.batch.size" 262144, "topology.classpath" nil}
5776 [main] INFO  backtype.storm.daemon.nimbus - Using default scheduler
5797 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
6035 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
6038 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000 sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@4b94b3b3
6085 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
6096 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
6099 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55731
6111 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55731
6114 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.persistence.FileTxnLog - Creating new log file: log.1
6131 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c6752710000, negotiated timeout = 20000
6133 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
6144 [main-EventThread] INFO  backtype.storm.zookeeper - Zookeeper state update: :connected:none
6144 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c6752710000 with negotiated timeout 20000 for client /127.0.0.1:55731
6202 [ProcessThread(sid:0 cport:-1):] INFO  org.apache.storm.zookeeper.server.PrepRequestProcessor - Processed session termination for sessionid: 0x1565c6752710000
6213 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxn - Closed socket connection for client /127.0.0.1:55731 which had sessionid 0x1565c6752710000
6213 [main-EventThread] INFO  org.apache.storm.zookeeper.ClientCnxn - EventThread shut down
6214 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Session: 0x1565c6752710000 closed
6215 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
6218 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
6218 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000/storm sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@39a44754
6231 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
6232 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
6232 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55732
6232 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55732
6235 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c6752710001 with negotiated timeout 20000 for client /127.0.0.1:55732
6235 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c6752710001, negotiated timeout = 20000
6235 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
6295 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
6295 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
6305 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000 sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@a632536
6306 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
6306 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55733
6307 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
6307 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55733
6309 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c6752710002 with negotiated timeout 20000 for client /127.0.0.1:55733
6309 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c6752710002, negotiated timeout = 20000
6309 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
6310 [main-EventThread] INFO  backtype.storm.zookeeper - Zookeeper state update: :connected:none
7313 [ProcessThread(sid:0 cport:-1):] INFO  org.apache.storm.zookeeper.server.PrepRequestProcessor - Processed session termination for sessionid: 0x1565c6752710002
7315 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxn - Closed socket connection for client /127.0.0.1:55733 which had sessionid 0x1565c6752710002
7315 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Session: 0x1565c6752710002 closed
7315 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
7316 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
7316 [main-EventThread] INFO  org.apache.storm.zookeeper.ClientCnxn - EventThread shut down
7316 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000/storm sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@659a1780
7317 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
7317 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55734
7318 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
7318 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55734
7319 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
7320 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
7320 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000 sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@43d95624
7332 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c6752710003 with negotiated timeout 20000 for client /127.0.0.1:55734
7332 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c6752710003, negotiated timeout = 20000
7332 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
7333 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
7333 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55735
7333 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
7334 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55735
7335 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c6752710004 with negotiated timeout 20000 for client /127.0.0.1:55735
7336 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c6752710004, negotiated timeout = 20000
7336 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
7336 [main-EventThread] INFO  backtype.storm.zookeeper - Zookeeper state update: :connected:none
7353 [ProcessThread(sid:0 cport:-1):] INFO  org.apache.storm.zookeeper.server.PrepRequestProcessor - Processed session termination for sessionid: 0x1565c6752710004
7363 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Session: 0x1565c6752710004 closed
7363 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
7363 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
7363 [main-EventThread] INFO  org.apache.storm.zookeeper.ClientCnxn - EventThread shut down
7368 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] WARN  org.apache.storm.zookeeper.server.NIOServerCnxn - caught end of stream exception
org.apache.storm.zookeeper.server.ServerCnxn$EndOfStreamException: Unable to read additional data from client sessionid 0x1565c6752710004, likely client has closed socket
	at org.apache.storm.zookeeper.server.NIOServerCnxn.doIO(NIOServerCnxn.java:228) ~[storm-core-0.9.5.jar:0.9.5]
	at org.apache.storm.zookeeper.server.NIOServerCnxnFactory.run(NIOServerCnxnFactory.java:208) [storm-core-0.9.5.jar:0.9.5]
	at java.lang.Thread.run(Thread.java:745) [na:1.7.0_79]
7368 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000/storm sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@2d3767f1
7371 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
7371 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
7374 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxn - Closed socket connection for client /127.0.0.1:55735 which had sessionid 0x1565c6752710004
7387 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55736
7387 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55736
7389 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c6752710005 with negotiated timeout 20000 for client /127.0.0.1:55736
7389 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c6752710005, negotiated timeout = 20000
7389 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
7441 [main] INFO  backtype.storm.daemon.supervisor - Starting Supervisor with conf {"dev.zookeeper.path" "/tmp/dev-storm-zookeeper", "topology.tick.tuple.freq.secs" nil, "topology.builtin.metrics.bucket.size.secs" 60, "topology.fall.back.on.java.serialization" true, "topology.max.error.report.per.interval" 5, "zmq.linger.millis" 0, "topology.skip.missing.kryo.registrations" true, "storm.messaging.netty.client_worker_threads" 1, "ui.childopts" "-Xmx768m", "storm.zookeeper.session.timeout" 20000, "nimbus.reassign" true, "topology.trident.batch.emit.interval.millis" 50, "storm.messaging.netty.flush.check.interval.ms" 10, "nimbus.monitor.freq.secs" 10, "logviewer.childopts" "-Xmx128m", "java.library.path" "/usr/local/lib:/opt/local/lib:/usr/lib", "topology.executor.send.buffer.size" 1024, "storm.local.dir" "/tmp/f71eda67-1617-4056-82c4-5820a56fc606", "storm.messaging.netty.buffer_size" 5242880, "supervisor.worker.start.timeout.secs" 120, "topology.enable.message.timeouts" true, "nimbus.cleanup.inbox.freq.secs" 600, "nimbus.inbox.jar.expiration.secs" 3600, "drpc.worker.threads" 64, "storm.meta.serialization.delegate" "backtype.storm.serialization.DefaultSerializationDelegate", "topology.worker.shared.thread.pool.size" 4, "nimbus.host" "localhost", "storm.messaging.netty.min_wait_ms" 100, "storm.zookeeper.port" 2000, "transactional.zookeeper.port" nil, "topology.executor.receive.buffer.size" 1024, "transactional.zookeeper.servers" nil, "storm.zookeeper.root" "/storm", "storm.zookeeper.retry.intervalceiling.millis" 30000, "supervisor.enable" true, "storm.messaging.netty.server_worker_threads" 1, "storm.zookeeper.servers" ["localhost"], "transactional.zookeeper.root" "/transactional", "topology.acker.executors" nil, "topology.transfer.buffer.size" 1024, "topology.worker.childopts" nil, "drpc.queue.size" 128, "worker.childopts" "-Xmx768m", "supervisor.heartbeat.frequency.secs" 5, "topology.error.throttle.interval.secs" 10, "zmq.hwm" 0, "drpc.port" 3772, "supervisor.monitor.frequency.secs" 3, "drpc.childopts" "-Xmx768m", "topology.receiver.buffer.size" 8, "task.heartbeat.frequency.secs" 3, "topology.tasks" nil, "storm.messaging.netty.max_retries" 300, "topology.spout.wait.strategy" "backtype.storm.spout.SleepSpoutWaitStrategy", "nimbus.thrift.max_buffer_size" 1048576, "topology.max.spout.pending" nil, "storm.zookeeper.retry.interval" 1000, "topology.sleep.spout.wait.strategy.time.ms" 1, "nimbus.topology.validator" "backtype.storm.nimbus.DefaultTopologyValidator", "supervisor.slots.ports" (1024 1025 1026), "topology.environment" nil, "topology.debug" false, "nimbus.task.launch.secs" 120, "nimbus.supervisor.timeout.secs" 60, "topology.message.timeout.secs" 30, "task.refresh.poll.secs" 10, "topology.workers" 1, "supervisor.childopts" "-Xmx256m", "nimbus.thrift.port" 6627, "topology.stats.sample.rate" 0.05, "worker.heartbeat.frequency.secs" 1, "topology.tuple.serializer" "backtype.storm.serialization.types.ListDelegateSerializer", "topology.disruptor.wait.strategy" "com.lmax.disruptor.BlockingWaitStrategy", "topology.multilang.serializer" "backtype.storm.multilang.JsonSerializer", "nimbus.task.timeout.secs" 30, "storm.zookeeper.connection.timeout" 15000, "topology.kryo.factory" "backtype.storm.serialization.DefaultKryoFactory", "drpc.invocations.port" 3773, "logviewer.port" 8000, "zmq.threads" 1, "storm.zookeeper.retry.times" 5, "topology.worker.receiver.thread.count" 1, "storm.thrift.transport" "backtype.storm.security.auth.SimpleTransportPlugin", "topology.state.synchronization.timeout.secs" 60, "supervisor.worker.timeout.secs" 30, "nimbus.file.copy.expiration.secs" 600, "storm.messaging.transport" "backtype.storm.messaging.netty.Context", "logviewer.appender.name" "A1", "storm.messaging.netty.max_wait_ms" 1000, "drpc.request.timeout.secs" 600, "storm.local.mode.zmq" false, "ui.port" 8080, "nimbus.childopts" "-Xmx1024m", "storm.cluster.mode" "local", "topology.max.task.parallelism" nil, "storm.messaging.netty.transfer.batch.size" 262144, "topology.classpath" nil}
7472 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
7473 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
7473 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000 sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@cb0c187
7474 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
7475 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55737
7475 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
7475 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55737
7477 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c6752710006 with negotiated timeout 20000 for client /127.0.0.1:55737
7477 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c6752710006, negotiated timeout = 20000
7478 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
7478 [main-EventThread] INFO  backtype.storm.zookeeper - Zookeeper state update: :connected:none
8480 [ProcessThread(sid:0 cport:-1):] INFO  org.apache.storm.zookeeper.server.PrepRequestProcessor - Processed session termination for sessionid: 0x1565c6752710006
8482 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxn - Closed socket connection for client /127.0.0.1:55737 which had sessionid 0x1565c6752710006
8482 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Session: 0x1565c6752710006 closed
8482 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
8483 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
8484 [main-EventThread] INFO  org.apache.storm.zookeeper.ClientCnxn - EventThread shut down
8484 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000/storm sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@544daf24
8485 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
8485 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55738
8486 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
8486 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55738
8497 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c6752710007 with negotiated timeout 20000 for client /127.0.0.1:55738
8497 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c6752710007, negotiated timeout = 20000
8497 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
8534 [main] INFO  backtype.storm.daemon.supervisor - Starting supervisor with id ba0eed9a-f418-4b06-9bb5-47397052d7d3 at host ip-172-31-4-51.ec2.internal
8553 [main] INFO  backtype.storm.daemon.supervisor - Starting Supervisor with conf {"dev.zookeeper.path" "/tmp/dev-storm-zookeeper", "topology.tick.tuple.freq.secs" nil, "topology.builtin.metrics.bucket.size.secs" 60, "topology.fall.back.on.java.serialization" true, "topology.max.error.report.per.interval" 5, "zmq.linger.millis" 0, "topology.skip.missing.kryo.registrations" true, "storm.messaging.netty.client_worker_threads" 1, "ui.childopts" "-Xmx768m", "storm.zookeeper.session.timeout" 20000, "nimbus.reassign" true, "topology.trident.batch.emit.interval.millis" 50, "storm.messaging.netty.flush.check.interval.ms" 10, "nimbus.monitor.freq.secs" 10, "logviewer.childopts" "-Xmx128m", "java.library.path" "/usr/local/lib:/opt/local/lib:/usr/lib", "topology.executor.send.buffer.size" 1024, "storm.local.dir" "/tmp/96d5a0cf-cb8f-426a-9fba-0c72e8756952", "storm.messaging.netty.buffer_size" 5242880, "supervisor.worker.start.timeout.secs" 120, "topology.enable.message.timeouts" true, "nimbus.cleanup.inbox.freq.secs" 600, "nimbus.inbox.jar.expiration.secs" 3600, "drpc.worker.threads" 64, "storm.meta.serialization.delegate" "backtype.storm.serialization.DefaultSerializationDelegate", "topology.worker.shared.thread.pool.size" 4, "nimbus.host" "localhost", "storm.messaging.netty.min_wait_ms" 100, "storm.zookeeper.port" 2000, "transactional.zookeeper.port" nil, "topology.executor.receive.buffer.size" 1024, "transactional.zookeeper.servers" nil, "storm.zookeeper.root" "/storm", "storm.zookeeper.retry.intervalceiling.millis" 30000, "supervisor.enable" true, "storm.messaging.netty.server_worker_threads" 1, "storm.zookeeper.servers" ["localhost"], "transactional.zookeeper.root" "/transactional", "topology.acker.executors" nil, "topology.transfer.buffer.size" 1024, "topology.worker.childopts" nil, "drpc.queue.size" 128, "worker.childopts" "-Xmx768m", "supervisor.heartbeat.frequency.secs" 5, "topology.error.throttle.interval.secs" 10, "zmq.hwm" 0, "drpc.port" 3772, "supervisor.monitor.frequency.secs" 3, "drpc.childopts" "-Xmx768m", "topology.receiver.buffer.size" 8, "task.heartbeat.frequency.secs" 3, "topology.tasks" nil, "storm.messaging.netty.max_retries" 300, "topology.spout.wait.strategy" "backtype.storm.spout.SleepSpoutWaitStrategy", "nimbus.thrift.max_buffer_size" 1048576, "topology.max.spout.pending" nil, "storm.zookeeper.retry.interval" 1000, "topology.sleep.spout.wait.strategy.time.ms" 1, "nimbus.topology.validator" "backtype.storm.nimbus.DefaultTopologyValidator", "supervisor.slots.ports" (1027 1028 1029), "topology.environment" nil, "topology.debug" false, "nimbus.task.launch.secs" 120, "nimbus.supervisor.timeout.secs" 60, "topology.message.timeout.secs" 30, "task.refresh.poll.secs" 10, "topology.workers" 1, "supervisor.childopts" "-Xmx256m", "nimbus.thrift.port" 6627, "topology.stats.sample.rate" 0.05, "worker.heartbeat.frequency.secs" 1, "topology.tuple.serializer" "backtype.storm.serialization.types.ListDelegateSerializer", "topology.disruptor.wait.strategy" "com.lmax.disruptor.BlockingWaitStrategy", "topology.multilang.serializer" "backtype.storm.multilang.JsonSerializer", "nimbus.task.timeout.secs" 30, "storm.zookeeper.connection.timeout" 15000, "topology.kryo.factory" "backtype.storm.serialization.DefaultKryoFactory", "drpc.invocations.port" 3773, "logviewer.port" 8000, "zmq.threads" 1, "storm.zookeeper.retry.times" 5, "topology.worker.receiver.thread.count" 1, "storm.thrift.transport" "backtype.storm.security.auth.SimpleTransportPlugin", "topology.state.synchronization.timeout.secs" 60, "supervisor.worker.timeout.secs" 30, "nimbus.file.copy.expiration.secs" 600, "storm.messaging.transport" "backtype.storm.messaging.netty.Context", "logviewer.appender.name" "A1", "storm.messaging.netty.max_wait_ms" 1000, "drpc.request.timeout.secs" 600, "storm.local.mode.zmq" false, "ui.port" 8080, "nimbus.childopts" "-Xmx1024m", "storm.cluster.mode" "local", "topology.max.task.parallelism" nil, "storm.messaging.netty.transfer.batch.size" 262144, "topology.classpath" nil}
8602 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
8602 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
8603 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000 sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@5416493f
8606 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
8607 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55739
8608 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
8608 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55739
8610 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c6752710008 with negotiated timeout 20000 for client /127.0.0.1:55739
8629 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c6752710008, negotiated timeout = 20000
8631 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
8631 [main-EventThread] INFO  backtype.storm.zookeeper - Zookeeper state update: :connected:none
8634 [ProcessThread(sid:0 cport:-1):] INFO  org.apache.storm.zookeeper.server.PrepRequestProcessor - Processed session termination for sessionid: 0x1565c6752710008
8636 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxn - Closed socket connection for client /127.0.0.1:55739 which had sessionid 0x1565c6752710008
8637 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Session: 0x1565c6752710008 closed
8637 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
8637 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
8638 [main-EventThread] INFO  org.apache.storm.zookeeper.ClientCnxn - EventThread shut down
8638 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000/storm sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@58bd92cd
8639 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
8639 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55740
8640 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
8641 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55740
8657 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c6752710009, negotiated timeout = 20000
8658 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
8658 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c6752710009 with negotiated timeout 20000 for client /127.0.0.1:55740
8675 [main] INFO  backtype.storm.daemon.supervisor - Starting supervisor with id 9d099d53-9d13-4aab-b8b2-ca18904274dc at host ip-172-31-4-51.ec2.internal
8790 [main] INFO  backtype.storm.daemon.nimbus - Received topology submission for tweetcount with conf {"storm.id" "tweetcount-1-1470429093", "topology.acker.executors" 2, "streamparse.log.path" "/root/tweetcount/logs", "topology.kryo.decorators" (), "topology.name" "tweetcount", "topology.max.spout.pending" 5000, "topology.debug" true, "topology.kryo.register" nil, "topology.message.timeout.secs" 60, "topology.workers" 2, "topology.max.task.parallelism" nil, "streamparse.log.level" "debug"}
8857 [main] INFO  backtype.storm.daemon.nimbus - Activating tweetcount: tweetcount-1-1470429093
9145 [main] INFO  backtype.storm.scheduler.EvenScheduler - Available slots: (["9d099d53-9d13-4aab-b8b2-ca18904274dc" 1027] ["9d099d53-9d13-4aab-b8b2-ca18904274dc" 1028] ["9d099d53-9d13-4aab-b8b2-ca18904274dc" 1029] ["ba0eed9a-f418-4b06-9bb5-47397052d7d3" 1024] ["ba0eed9a-f418-4b06-9bb5-47397052d7d3" 1025] ["ba0eed9a-f418-4b06-9bb5-47397052d7d3" 1026])
9296 [main] INFO  backtype.storm.daemon.nimbus - Setting new assignment for topology id tweetcount-1-1470429093: #backtype.storm.daemon.common.Assignment{:master-code-dir "/tmp/937314f4-7c19-486b-8f28-81c7c6de5a7e/nimbus/stormdist/tweetcount-1-1470429093", :node->host {"ba0eed9a-f418-4b06-9bb5-47397052d7d3" "ip-172-31-4-51.ec2.internal", "9d099d53-9d13-4aab-b8b2-ca18904274dc" "ip-172-31-4-51.ec2.internal"}, :executor->node+port {[3 3] ["9d099d53-9d13-4aab-b8b2-ca18904274dc" 1027], [6 6] ["ba0eed9a-f418-4b06-9bb5-47397052d7d3" 1024], [5 5] ["9d099d53-9d13-4aab-b8b2-ca18904274dc" 1027], [4 4] ["ba0eed9a-f418-4b06-9bb5-47397052d7d3" 1024], [7 7] ["9d099d53-9d13-4aab-b8b2-ca18904274dc" 1027], [2 2] ["ba0eed9a-f418-4b06-9bb5-47397052d7d3" 1024], [1 1] ["9d099d53-9d13-4aab-b8b2-ca18904274dc" 1027]}, :executor->start-time-secs {[7 7] 1470429094, [5 5] 1470429094, [3 3] 1470429094, [1 1] 1470429094, [6 6] 1470429094, [4 4] 1470429094, [2 2] 1470429094}}
11116 [Thread-5] INFO  backtype.storm.daemon.supervisor - Copying resources at file:/root/tweetcount/_resources/resources to /tmp/96d5a0cf-cb8f-426a-9fba-0c72e8756952/supervisor/stormdist/tweetcount-1-1470429093/resources
11200 [Thread-3] INFO  backtype.storm.daemon.supervisor - Copying resources at file:/root/tweetcount/_resources/resources to /tmp/f71eda67-1617-4056-82c4-5820a56fc606/supervisor/stormdist/tweetcount-1-1470429093/resources
11279 [Thread-4] INFO  backtype.storm.daemon.supervisor - Launching worker with assignment #backtype.storm.daemon.supervisor.LocalAssignment{:storm-id "tweetcount-1-1470429093", :executors ([6 6] [4 4] [2 2])} for this supervisor ba0eed9a-f418-4b06-9bb5-47397052d7d3 on port 1024 with id c4e95046-ae0b-485c-9d78-8b74a84e2417
11315 [Thread-4] INFO  backtype.storm.daemon.worker - Launching worker for tweetcount-1-1470429093 on ba0eed9a-f418-4b06-9bb5-47397052d7d3:1024 with id c4e95046-ae0b-485c-9d78-8b74a84e2417 and conf {"dev.zookeeper.path" "/tmp/dev-storm-zookeeper", "topology.tick.tuple.freq.secs" nil, "topology.builtin.metrics.bucket.size.secs" 60, "topology.fall.back.on.java.serialization" true, "topology.max.error.report.per.interval" 5, "zmq.linger.millis" 0, "topology.skip.missing.kryo.registrations" true, "storm.messaging.netty.client_worker_threads" 1, "ui.childopts" "-Xmx768m", "storm.zookeeper.session.timeout" 20000, "nimbus.reassign" true, "topology.trident.batch.emit.interval.millis" 50, "storm.messaging.netty.flush.check.interval.ms" 10, "nimbus.monitor.freq.secs" 10, "logviewer.childopts" "-Xmx128m", "java.library.path" "/usr/local/lib:/opt/local/lib:/usr/lib", "topology.executor.send.buffer.size" 1024, "storm.local.dir" "/tmp/f71eda67-1617-4056-82c4-5820a56fc606", "storm.messaging.netty.buffer_size" 5242880, "supervisor.worker.start.timeout.secs" 120, "topology.enable.message.timeouts" true, "nimbus.cleanup.inbox.freq.secs" 600, "nimbus.inbox.jar.expiration.secs" 3600, "drpc.worker.threads" 64, "storm.meta.serialization.delegate" "backtype.storm.serialization.DefaultSerializationDelegate", "topology.worker.shared.thread.pool.size" 4, "nimbus.host" "localhost", "storm.messaging.netty.min_wait_ms" 100, "storm.zookeeper.port" 2000, "transactional.zookeeper.port" nil, "topology.executor.receive.buffer.size" 1024, "transactional.zookeeper.servers" nil, "storm.zookeeper.root" "/storm", "storm.zookeeper.retry.intervalceiling.millis" 30000, "supervisor.enable" true, "storm.messaging.netty.server_worker_threads" 1, "storm.zookeeper.servers" ["localhost"], "transactional.zookeeper.root" "/transactional", "topology.acker.executors" nil, "topology.transfer.buffer.size" 1024, "topology.worker.childopts" nil, "drpc.queue.size" 128, "worker.childopts" "-Xmx768m", "supervisor.heartbeat.frequency.secs" 5, "topology.error.throttle.interval.secs" 10, "zmq.hwm" 0, "drpc.port" 3772, "supervisor.monitor.frequency.secs" 3, "drpc.childopts" "-Xmx768m", "topology.receiver.buffer.size" 8, "task.heartbeat.frequency.secs" 3, "topology.tasks" nil, "storm.messaging.netty.max_retries" 300, "topology.spout.wait.strategy" "backtype.storm.spout.SleepSpoutWaitStrategy", "nimbus.thrift.max_buffer_size" 1048576, "topology.max.spout.pending" nil, "storm.zookeeper.retry.interval" 1000, "topology.sleep.spout.wait.strategy.time.ms" 1, "nimbus.topology.validator" "backtype.storm.nimbus.DefaultTopologyValidator", "supervisor.slots.ports" (1024 1025 1026), "topology.environment" nil, "topology.debug" false, "nimbus.task.launch.secs" 120, "nimbus.supervisor.timeout.secs" 60, "topology.message.timeout.secs" 30, "task.refresh.poll.secs" 10, "topology.workers" 1, "supervisor.childopts" "-Xmx256m", "nimbus.thrift.port" 6627, "topology.stats.sample.rate" 0.05, "worker.heartbeat.frequency.secs" 1, "topology.tuple.serializer" "backtype.storm.serialization.types.ListDelegateSerializer", "topology.disruptor.wait.strategy" "com.lmax.disruptor.BlockingWaitStrategy", "topology.multilang.serializer" "backtype.storm.multilang.JsonSerializer", "nimbus.task.timeout.secs" 30, "storm.zookeeper.connection.timeout" 15000, "topology.kryo.factory" "backtype.storm.serialization.DefaultKryoFactory", "drpc.invocations.port" 3773, "logviewer.port" 8000, "zmq.threads" 1, "storm.zookeeper.retry.times" 5, "topology.worker.receiver.thread.count" 1, "storm.thrift.transport" "backtype.storm.security.auth.SimpleTransportPlugin", "topology.state.synchronization.timeout.secs" 60, "supervisor.worker.timeout.secs" 30, "nimbus.file.copy.expiration.secs" 600, "storm.messaging.transport" "backtype.storm.messaging.netty.Context", "logviewer.appender.name" "A1", "storm.messaging.netty.max_wait_ms" 1000, "drpc.request.timeout.secs" 600, "storm.local.mode.zmq" false, "ui.port" 8080, "nimbus.childopts" "-Xmx1024m", "storm.cluster.mode" "local", "topology.max.task.parallelism" nil, "storm.messaging.netty.transfer.batch.size" 262144, "topology.classpath" nil}
11316 [Thread-4] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
11317 [Thread-4] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
11317 [Thread-4] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000 sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@4fa2e041
11318 [Thread-4-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
11318 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55742
11319 [Thread-4-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
11319 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55742
11320 [Thread-6] INFO  backtype.storm.daemon.supervisor - Launching worker with assignment #backtype.storm.daemon.supervisor.LocalAssignment{:storm-id "tweetcount-1-1470429093", :executors ([3 3] [5 5] [7 7] [1 1])} for this supervisor 9d099d53-9d13-4aab-b8b2-ca18904274dc on port 1027 with id 3861ebfe-777d-4389-ad42-4896a52091cf
11325 [Thread-6] INFO  backtype.storm.daemon.worker - Launching worker for tweetcount-1-1470429093 on 9d099d53-9d13-4aab-b8b2-ca18904274dc:1027 with id 3861ebfe-777d-4389-ad42-4896a52091cf and conf {"dev.zookeeper.path" "/tmp/dev-storm-zookeeper", "topology.tick.tuple.freq.secs" nil, "topology.builtin.metrics.bucket.size.secs" 60, "topology.fall.back.on.java.serialization" true, "topology.max.error.report.per.interval" 5, "zmq.linger.millis" 0, "topology.skip.missing.kryo.registrations" true, "storm.messaging.netty.client_worker_threads" 1, "ui.childopts" "-Xmx768m", "storm.zookeeper.session.timeout" 20000, "nimbus.reassign" true, "topology.trident.batch.emit.interval.millis" 50, "storm.messaging.netty.flush.check.interval.ms" 10, "nimbus.monitor.freq.secs" 10, "logviewer.childopts" "-Xmx128m", "java.library.path" "/usr/local/lib:/opt/local/lib:/usr/lib", "topology.executor.send.buffer.size" 1024, "storm.local.dir" "/tmp/96d5a0cf-cb8f-426a-9fba-0c72e8756952", "storm.messaging.netty.buffer_size" 5242880, "supervisor.worker.start.timeout.secs" 120, "topology.enable.message.timeouts" true, "nimbus.cleanup.inbox.freq.secs" 600, "nimbus.inbox.jar.expiration.secs" 3600, "drpc.worker.threads" 64, "storm.meta.serialization.delegate" "backtype.storm.serialization.DefaultSerializationDelegate", "topology.worker.shared.thread.pool.size" 4, "nimbus.host" "localhost", "storm.messaging.netty.min_wait_ms" 100, "storm.zookeeper.port" 2000, "transactional.zookeeper.port" nil, "topology.executor.receive.buffer.size" 1024, "transactional.zookeeper.servers" nil, "storm.zookeeper.root" "/storm", "storm.zookeeper.retry.intervalceiling.millis" 30000, "supervisor.enable" true, "storm.messaging.netty.server_worker_threads" 1, "storm.zookeeper.servers" ["localhost"], "transactional.zookeeper.root" "/transactional", "topology.acker.executors" nil, "topology.transfer.buffer.size" 1024, "topology.worker.childopts" nil, "drpc.queue.size" 128, "worker.childopts" "-Xmx768m", "supervisor.heartbeat.frequency.secs" 5, "topology.error.throttle.interval.secs" 10, "zmq.hwm" 0, "drpc.port" 3772, "supervisor.monitor.frequency.secs" 3, "drpc.childopts" "-Xmx768m", "topology.receiver.buffer.size" 8, "task.heartbeat.frequency.secs" 3, "topology.tasks" nil, "storm.messaging.netty.max_retries" 300, "topology.spout.wait.strategy" "backtype.storm.spout.SleepSpoutWaitStrategy", "nimbus.thrift.max_buffer_size" 1048576, "topology.max.spout.pending" nil, "storm.zookeeper.retry.interval" 1000, "topology.sleep.spout.wait.strategy.time.ms" 1, "nimbus.topology.validator" "backtype.storm.nimbus.DefaultTopologyValidator", "supervisor.slots.ports" (1027 1028 1029), "topology.environment" nil, "topology.debug" false, "nimbus.task.launch.secs" 120, "nimbus.supervisor.timeout.secs" 60, "topology.message.timeout.secs" 30, "task.refresh.poll.secs" 10, "topology.workers" 1, "supervisor.childopts" "-Xmx256m", "nimbus.thrift.port" 6627, "topology.stats.sample.rate" 0.05, "worker.heartbeat.frequency.secs" 1, "topology.tuple.serializer" "backtype.storm.serialization.types.ListDelegateSerializer", "topology.disruptor.wait.strategy" "com.lmax.disruptor.BlockingWaitStrategy", "topology.multilang.serializer" "backtype.storm.multilang.JsonSerializer", "nimbus.task.timeout.secs" 30, "storm.zookeeper.connection.timeout" 15000, "topology.kryo.factory" "backtype.storm.serialization.DefaultKryoFactory", "drpc.invocations.port" 3773, "logviewer.port" 8000, "zmq.threads" 1, "storm.zookeeper.retry.times" 5, "topology.worker.receiver.thread.count" 1, "storm.thrift.transport" "backtype.storm.security.auth.SimpleTransportPlugin", "topology.state.synchronization.timeout.secs" 60, "supervisor.worker.timeout.secs" 30, "nimbus.file.copy.expiration.secs" 600, "storm.messaging.transport" "backtype.storm.messaging.netty.Context", "logviewer.appender.name" "A1", "storm.messaging.netty.max_wait_ms" 1000, "drpc.request.timeout.secs" 600, "storm.local.mode.zmq" false, "ui.port" 8080, "nimbus.childopts" "-Xmx1024m", "storm.cluster.mode" "local", "topology.max.task.parallelism" nil, "storm.messaging.netty.transfer.batch.size" 262144, "topology.classpath" nil}
11325 [Thread-6] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
11326 [Thread-6] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
11326 [Thread-6] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000 sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@655a5675
11340 [Thread-6-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
11340 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55743
11341 [Thread-6-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
11341 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55743
11360 [Thread-4-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c675271000a, negotiated timeout = 20000
11361 [Thread-4-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
11361 [Thread-4-EventThread] INFO  backtype.storm.zookeeper - Zookeeper state update: :connected:none
11362 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c675271000a with negotiated timeout 20000 for client /127.0.0.1:55742
11372 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c675271000b with negotiated timeout 20000 for client /127.0.0.1:55743
11392 [ProcessThread(sid:0 cport:-1):] INFO  org.apache.storm.zookeeper.server.PrepRequestProcessor - Processed session termination for sessionid: 0x1565c675271000a
11394 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxn - Closed socket connection for client /127.0.0.1:55742 which had sessionid 0x1565c675271000a
11394 [Thread-4] INFO  org.apache.storm.zookeeper.ZooKeeper - Session: 0x1565c675271000a closed
11395 [Thread-4] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
11395 [Thread-4] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
11395 [Thread-4-EventThread] INFO  org.apache.storm.zookeeper.ClientCnxn - EventThread shut down
11396 [Thread-6-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c675271000b, negotiated timeout = 20000
11396 [Thread-4] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000/storm sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@46e73024
11397 [Thread-4-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
11397 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55744
11397 [Thread-4-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
11398 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55744
11437 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c675271000c with negotiated timeout 20000 for client /127.0.0.1:55744
11437 [Thread-6-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
11437 [Thread-6-EventThread] INFO  backtype.storm.zookeeper - Zookeeper state update: :connected:none
11438 [Thread-4-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c675271000c, negotiated timeout = 20000
11438 [Thread-4-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
11440 [ProcessThread(sid:0 cport:-1):] INFO  org.apache.storm.zookeeper.server.PrepRequestProcessor - Processed session termination for sessionid: 0x1565c675271000b
11442 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxn - Closed socket connection for client /127.0.0.1:55743 which had sessionid 0x1565c675271000b
11442 [Thread-6] INFO  org.apache.storm.zookeeper.ZooKeeper - Session: 0x1565c675271000b closed
11443 [Thread-6] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
11443 [Thread-6] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
11453 [Thread-6-EventThread] INFO  org.apache.storm.zookeeper.ClientCnxn - EventThread shut down
11457 [Thread-4] INFO  backtype.storm.daemon.worker - Reading Assignments.
11462 [Thread-6] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000/storm sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@4c8f1195
11479 [Thread-6-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
11480 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55745
11480 [Thread-6-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
11503 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55745
11505 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c675271000d with negotiated timeout 20000 for client /127.0.0.1:55745
11505 [Thread-6-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c675271000d, negotiated timeout = 20000
11505 [Thread-6-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
11533 [Thread-6] INFO  backtype.storm.daemon.worker - Reading Assignments.
11731 [Thread-6] INFO  backtype.storm.daemon.worker - Launching receive-thread for 9d099d53-9d13-4aab-b8b2-ca18904274dc:1027
11744 [Thread-4] INFO  backtype.storm.daemon.worker - Launching receive-thread for ba0eed9a-f418-4b06-9bb5-47397052d7d3:1024
11748 [Thread-7-worker-receiver-thread-0] INFO  backtype.storm.messaging.loader - Starting receive-thread: [stormId: tweetcount-1-1470429093, port: 1024, thread-id: 0 ]
11764 [Thread-8-worker-receiver-thread-0] INFO  backtype.storm.messaging.loader - Starting receive-thread: [stormId: tweetcount-1-1470429093, port: 1027, thread-id: 0 ]
12619 [refresh-active-timer] INFO  backtype.storm.daemon.worker - All connections are ready for worker 9d099d53-9d13-4aab-b8b2-ca18904274dc:1027 with id 3861ebfe-777d-4389-ad42-4896a52091cf
12666 [refresh-active-timer] INFO  backtype.storm.daemon.worker - All connections are ready for worker ba0eed9a-f418-4b06-9bb5-47397052d7d3:1024 with id c4e95046-ae0b-485c-9d78-8b74a84e2417
12873 [Thread-6] INFO  backtype.storm.daemon.executor - Loading executor counter-bolt:[3 3]
12874 [Thread-4] INFO  backtype.storm.daemon.executor - Loading executor __acker:[2 2]
12941 [Thread-4] INFO  backtype.storm.daemon.task - Emitting: __acker __system ["startup"]
12946 [Thread-4] INFO  backtype.storm.daemon.executor - Loaded executor tasks __acker:[2 2]
12948 [Thread-6] INFO  backtype.storm.daemon.task - Emitting: counter-bolt __system ["startup"]
12948 [Thread-6] INFO  backtype.storm.daemon.executor - Loaded executor tasks counter-bolt:[3 3]
12983 [Thread-4] INFO  backtype.storm.daemon.executor - Timeouts disabled for executor __acker:[2 2]
12983 [Thread-4] INFO  backtype.storm.daemon.executor - Finished loading executor __acker:[2 2]
13015 [Thread-6] INFO  backtype.storm.daemon.executor - Finished loading executor counter-bolt:[3 3]
13028 [Thread-4] INFO  backtype.storm.daemon.executor - Loading executor counter-bolt:[4 4]
13044 [Thread-6] INFO  backtype.storm.daemon.executor - Loading executor parse-bolt:[5 5]
13049 [Thread-4] INFO  backtype.storm.daemon.task - Emitting: counter-bolt __system ["startup"]
13058 [Thread-4] INFO  backtype.storm.daemon.executor - Loaded executor tasks counter-bolt:[4 4]
13058 [Thread-6] INFO  backtype.storm.daemon.task - Emitting: parse-bolt __system ["startup"]
13064 [Thread-4] INFO  backtype.storm.daemon.executor - Finished loading executor counter-bolt:[4 4]
13095 [Thread-6] INFO  backtype.storm.daemon.executor - Loaded executor tasks parse-bolt:[5 5]
13111 [Thread-6] INFO  backtype.storm.daemon.executor - Finished loading executor parse-bolt:[5 5]
13127 [Thread-4] INFO  backtype.storm.daemon.executor - Loading executor parse-bolt:[6 6]
13130 [Thread-4] INFO  backtype.storm.daemon.task - Emitting: parse-bolt __system ["startup"]
13131 [Thread-4] INFO  backtype.storm.daemon.executor - Loaded executor tasks parse-bolt:[6 6]
13151 [Thread-4] INFO  backtype.storm.daemon.executor - Finished loading executor parse-bolt:[6 6]
13158 [Thread-6] INFO  backtype.storm.daemon.executor - Loading executor tweet-spout:[7 7]
13168 [Thread-4] INFO  backtype.storm.daemon.executor - Loading executor __system:[-1 -1]
13168 [Thread-4] INFO  backtype.storm.daemon.task - Emitting: __system __system ["startup"]
13169 [Thread-4] INFO  backtype.storm.daemon.executor - Loaded executor tasks __system:[-1 -1]
13183 [Thread-4] INFO  backtype.storm.daemon.executor - Finished loading executor __system:[-1 -1]
13189 [Thread-4] INFO  backtype.storm.daemon.worker - Worker has topology config {"storm.id" "tweetcount-1-1470429093", "dev.zookeeper.path" "/tmp/dev-storm-zookeeper", "topology.tick.tuple.freq.secs" nil, "topology.builtin.metrics.bucket.size.secs" 60, "topology.fall.back.on.java.serialization" true, "topology.max.error.report.per.interval" 5, "zmq.linger.millis" 0, "topology.skip.missing.kryo.registrations" true, "storm.messaging.netty.client_worker_threads" 1, "ui.childopts" "-Xmx768m", "storm.zookeeper.session.timeout" 20000, "nimbus.reassign" true, "topology.trident.batch.emit.interval.millis" 50, "storm.messaging.netty.flush.check.interval.ms" 10, "nimbus.monitor.freq.secs" 10, "logviewer.childopts" "-Xmx128m", "java.library.path" "/usr/local/lib:/opt/local/lib:/usr/lib", "topology.executor.send.buffer.size" 1024, "storm.local.dir" "/tmp/f71eda67-1617-4056-82c4-5820a56fc606", "storm.messaging.netty.buffer_size" 5242880, "supervisor.worker.start.timeout.secs" 120, "topology.enable.message.timeouts" true, "nimbus.cleanup.inbox.freq.secs" 600, "nimbus.inbox.jar.expiration.secs" 3600, "drpc.worker.threads" 64, "storm.meta.serialization.delegate" "backtype.storm.serialization.DefaultSerializationDelegate", "topology.worker.shared.thread.pool.size" 4, "nimbus.host" "localhost", "storm.messaging.netty.min_wait_ms" 100, "storm.zookeeper.port" 2000, "transactional.zookeeper.port" nil, "topology.executor.receive.buffer.size" 1024, "transactional.zookeeper.servers" nil, "storm.zookeeper.root" "/storm", "storm.zookeeper.retry.intervalceiling.millis" 30000, "supervisor.enable" true, "storm.messaging.netty.server_worker_threads" 1, "storm.zookeeper.servers" ["localhost"], "transactional.zookeeper.root" "/transactional", "topology.acker.executors" 2, "streamparse.log.path" "/root/tweetcount/logs", "topology.kryo.decorators" (), "topology.name" "tweetcount", "topology.transfer.buffer.size" 1024, "topology.worker.childopts" nil, "drpc.queue.size" 128, "worker.childopts" "-Xmx768m", "supervisor.heartbeat.frequency.secs" 5, "topology.error.throttle.interval.secs" 10, "zmq.hwm" 0, "drpc.port" 3772, "supervisor.monitor.frequency.secs" 3, "drpc.childopts" "-Xmx768m", "topology.receiver.buffer.size" 8, "task.heartbeat.frequency.secs" 3, "topology.tasks" nil, "storm.messaging.netty.max_retries" 300, "topology.spout.wait.strategy" "backtype.storm.spout.SleepSpoutWaitStrategy", "nimbus.thrift.max_buffer_size" 1048576, "topology.max.spout.pending" 5000, "storm.zookeeper.retry.interval" 1000, "topology.sleep.spout.wait.strategy.time.ms" 1, "nimbus.topology.validator" "backtype.storm.nimbus.DefaultTopologyValidator", "supervisor.slots.ports" (1024 1025 1026), "topology.environment" nil, "topology.debug" true, "nimbus.task.launch.secs" 120, "nimbus.supervisor.timeout.secs" 60, "topology.kryo.register" nil, "topology.message.timeout.secs" 60, "task.refresh.poll.secs" 10, "topology.workers" 2, "supervisor.childopts" "-Xmx256m", "nimbus.thrift.port" 6627, "topology.stats.sample.rate" 0.05, "worker.heartbeat.frequency.secs" 1, "topology.tuple.serializer" "backtype.storm.serialization.types.ListDelegateSerializer", "topology.disruptor.wait.strategy" "com.lmax.disruptor.BlockingWaitStrategy", "topology.multilang.serializer" "backtype.storm.multilang.JsonSerializer", "nimbus.task.timeout.secs" 30, "storm.zookeeper.connection.timeout" 15000, "topology.kryo.factory" "backtype.storm.serialization.DefaultKryoFactory", "drpc.invocations.port" 3773, "logviewer.port" 8000, "zmq.threads" 1, "storm.zookeeper.retry.times" 5, "topology.worker.receiver.thread.count" 1, "storm.thrift.transport" "backtype.storm.security.auth.SimpleTransportPlugin", "topology.state.synchronization.timeout.secs" 60, "supervisor.worker.timeout.secs" 30, "nimbus.file.copy.expiration.secs" 600, "storm.messaging.transport" "backtype.storm.messaging.netty.Context", "logviewer.appender.name" "A1", "storm.messaging.netty.max_wait_ms" 1000, "drpc.request.timeout.secs" 600, "storm.local.mode.zmq" false, "ui.port" 8080, "nimbus.childopts" "-Xmx1024m", "storm.cluster.mode" "local", "topology.max.task.parallelism" nil, "storm.messaging.netty.transfer.batch.size" 262144, "topology.classpath" nil, "streamparse.log.level" "debug"}
13199 [Thread-4] INFO  backtype.storm.daemon.worker - Worker c4e95046-ae0b-485c-9d78-8b74a84e2417 for storm tweetcount-1-1470429093 on ba0eed9a-f418-4b06-9bb5-47397052d7d3:1024 has finished loading
13217 [Thread-6] INFO  backtype.storm.daemon.task - Emitting: tweet-spout __system ["startup"]
13218 [Thread-6] INFO  backtype.storm.daemon.executor - Loaded executor tasks tweet-spout:[7 7]
13253 [Thread-6] INFO  backtype.storm.daemon.executor - Finished loading executor tweet-spout:[7 7]
13284 [Thread-6] INFO  backtype.storm.daemon.executor - Loading executor __system:[-1 -1]
13285 [Thread-6] INFO  backtype.storm.daemon.task - Emitting: __system __system ["startup"]
13285 [Thread-6] INFO  backtype.storm.daemon.executor - Loaded executor tasks __system:[-1 -1]
13298 [Thread-6] INFO  backtype.storm.daemon.executor - Finished loading executor __system:[-1 -1]
13304 [Thread-6] INFO  backtype.storm.daemon.executor - Loading executor __acker:[1 1]
13313 [Thread-6] INFO  backtype.storm.daemon.task - Emitting: __acker __system ["startup"]
13313 [Thread-6] INFO  backtype.storm.daemon.executor - Loaded executor tasks __acker:[1 1]
13315 [Thread-6] INFO  backtype.storm.daemon.executor - Timeouts disabled for executor __acker:[1 1]
13315 [Thread-6] INFO  backtype.storm.daemon.executor - Finished loading executor __acker:[1 1]
13319 [Thread-6] INFO  backtype.storm.daemon.worker - Worker has topology config {"storm.id" "tweetcount-1-1470429093", "dev.zookeeper.path" "/tmp/dev-storm-zookeeper", "topology.tick.tuple.freq.secs" nil, "topology.builtin.metrics.bucket.size.secs" 60, "topology.fall.back.on.java.serialization" true, "topology.max.error.report.per.interval" 5, "zmq.linger.millis" 0, "topology.skip.missing.kryo.registrations" true, "storm.messaging.netty.client_worker_threads" 1, "ui.childopts" "-Xmx768m", "storm.zookeeper.session.timeout" 20000, "nimbus.reassign" true, "topology.trident.batch.emit.interval.millis" 50, "storm.messaging.netty.flush.check.interval.ms" 10, "nimbus.monitor.freq.secs" 10, "logviewer.childopts" "-Xmx128m", "java.library.path" "/usr/local/lib:/opt/local/lib:/usr/lib", "topology.executor.send.buffer.size" 1024, "storm.local.dir" "/tmp/96d5a0cf-cb8f-426a-9fba-0c72e8756952", "storm.messaging.netty.buffer_size" 5242880, "supervisor.worker.start.timeout.secs" 120, "topology.enable.message.timeouts" true, "nimbus.cleanup.inbox.freq.secs" 600, "nimbus.inbox.jar.expiration.secs" 3600, "drpc.worker.threads" 64, "storm.meta.serialization.delegate" "backtype.storm.serialization.DefaultSerializationDelegate", "topology.worker.shared.thread.pool.size" 4, "nimbus.host" "localhost", "storm.messaging.netty.min_wait_ms" 100, "storm.zookeeper.port" 2000, "transactional.zookeeper.port" nil, "topology.executor.receive.buffer.size" 1024, "transactional.zookeeper.servers" nil, "storm.zookeeper.root" "/storm", "storm.zookeeper.retry.intervalceiling.millis" 30000, "supervisor.enable" true, "storm.messaging.netty.server_worker_threads" 1, "storm.zookeeper.servers" ["localhost"], "transactional.zookeeper.root" "/transactional", "topology.acker.executors" 2, "streamparse.log.path" "/root/tweetcount/logs", "topology.kryo.decorators" (), "topology.name" "tweetcount", "topology.transfer.buffer.size" 1024, "topology.worker.childopts" nil, "drpc.queue.size" 128, "worker.childopts" "-Xmx768m", "supervisor.heartbeat.frequency.secs" 5, "topology.error.throttle.interval.secs" 10, "zmq.hwm" 0, "drpc.port" 3772, "supervisor.monitor.frequency.secs" 3, "drpc.childopts" "-Xmx768m", "topology.receiver.buffer.size" 8, "task.heartbeat.frequency.secs" 3, "topology.tasks" nil, "storm.messaging.netty.max_retries" 300, "topology.spout.wait.strategy" "backtype.storm.spout.SleepSpoutWaitStrategy", "nimbus.thrift.max_buffer_size" 1048576, "topology.max.spout.pending" 5000, "storm.zookeeper.retry.interval" 1000, "topology.sleep.spout.wait.strategy.time.ms" 1, "nimbus.topology.validator" "backtype.storm.nimbus.DefaultTopologyValidator", "supervisor.slots.ports" (1027 1028 1029), "topology.environment" nil, "topology.debug" true, "nimbus.task.launch.secs" 120, "nimbus.supervisor.timeout.secs" 60, "topology.kryo.register" nil, "topology.message.timeout.secs" 60, "task.refresh.poll.secs" 10, "topology.workers" 2, "supervisor.childopts" "-Xmx256m", "nimbus.thrift.port" 6627, "topology.stats.sample.rate" 0.05, "worker.heartbeat.frequency.secs" 1, "topology.tuple.serializer" "backtype.storm.serialization.types.ListDelegateSerializer", "topology.disruptor.wait.strategy" "com.lmax.disruptor.BlockingWaitStrategy", "topology.multilang.serializer" "backtype.storm.multilang.JsonSerializer", "nimbus.task.timeout.secs" 30, "storm.zookeeper.connection.timeout" 15000, "topology.kryo.factory" "backtype.storm.serialization.DefaultKryoFactory", "drpc.invocations.port" 3773, "logviewer.port" 8000, "zmq.threads" 1, "storm.zookeeper.retry.times" 5, "topology.worker.receiver.thread.count" 1, "storm.thrift.transport" "backtype.storm.security.auth.SimpleTransportPlugin", "topology.state.synchronization.timeout.secs" 60, "supervisor.worker.timeout.secs" 30, "nimbus.file.copy.expiration.secs" 600, "storm.messaging.transport" "backtype.storm.messaging.netty.Context", "logviewer.appender.name" "A1", "storm.messaging.netty.max_wait_ms" 1000, "drpc.request.timeout.secs" 600, "storm.local.mode.zmq" false, "ui.port" 8080, "nimbus.childopts" "-Xmx1024m", "storm.cluster.mode" "local", "topology.max.task.parallelism" nil, "storm.messaging.netty.transfer.batch.size" 262144, "topology.classpath" nil, "streamparse.log.level" "debug"}
13320 [Thread-6] INFO  backtype.storm.daemon.worker - Worker 3861ebfe-777d-4389-ad42-4896a52091cf for storm tweetcount-1-1470429093 on 9d099d53-9d13-4aab-b8b2-ca18904274dc:1027 has finished loading
13654 [Thread-12-counter-bolt] INFO  backtype.storm.daemon.executor - Preparing bolt counter-bolt:(3)
13656 [Thread-23-tweet-spout] INFO  backtype.storm.daemon.executor - Opening spout tweet-spout:(7)
13706 [Thread-23-tweet-spout] INFO  backtype.storm.utils.ShellProcess - Storm multilang serializer: backtype.storm.multilang.JsonSerializer
13708 [Thread-25-__system] INFO  backtype.storm.daemon.executor - Preparing bolt __system:(-1)
13718 [Thread-11-__acker] INFO  backtype.storm.daemon.executor - Preparing bolt __acker:(2)
13719 [Thread-27-__acker] INFO  backtype.storm.daemon.executor - Preparing bolt __acker:(1)
13720 [Thread-27-__acker] INFO  backtype.storm.daemon.executor - Prepared bolt __acker:(1)
13721 [Thread-16-parse-bolt] INFO  backtype.storm.daemon.executor - Preparing bolt parse-bolt:(5)
13734 [Thread-11-__acker] INFO  backtype.storm.daemon.executor - Prepared bolt __acker:(2)
13768 [Thread-25-__system] INFO  backtype.storm.daemon.executor - Prepared bolt __system:(-1)
13770 [Thread-16-parse-bolt] INFO  backtype.storm.utils.ShellProcess - Storm multilang serializer: backtype.storm.multilang.JsonSerializer
13770 [Thread-12-counter-bolt] INFO  backtype.storm.utils.ShellProcess - Storm multilang serializer: backtype.storm.multilang.JsonSerializer
13771 [Thread-18-parse-bolt] INFO  backtype.storm.daemon.executor - Preparing bolt parse-bolt:(6)
13772 [Thread-18-parse-bolt] INFO  backtype.storm.utils.ShellProcess - Storm multilang serializer: backtype.storm.multilang.JsonSerializer
13787 [Thread-14-counter-bolt] INFO  backtype.storm.daemon.executor - Preparing bolt counter-bolt:(4)
13787 [Thread-14-counter-bolt] INFO  backtype.storm.utils.ShellProcess - Storm multilang serializer: backtype.storm.multilang.JsonSerializer
13788 [Thread-20-__system] INFO  backtype.storm.daemon.executor - Preparing bolt __system:(-1)
13790 [Thread-20-__system] INFO  backtype.storm.daemon.executor - Prepared bolt __system:(-1)
14586 [Thread-14-counter-bolt] INFO  backtype.storm.task.ShellBolt - Launched subprocess with pid 4194
14623 [Thread-18-parse-bolt] INFO  backtype.storm.task.ShellBolt - Launched subprocess with pid 4193
14639 [Thread-18-parse-bolt] INFO  backtype.storm.task.ShellBolt - Start checking heartbeat...
14639 [Thread-18-parse-bolt] INFO  backtype.storm.daemon.executor - Prepared bolt parse-bolt:(6)
14641 [Thread-14-counter-bolt] INFO  backtype.storm.task.ShellBolt - Start checking heartbeat...
14642 [Thread-14-counter-bolt] INFO  backtype.storm.daemon.executor - Prepared bolt counter-bolt:(4)
14709 [Thread-12-counter-bolt] INFO  backtype.storm.task.ShellBolt - Launched subprocess with pid 4192
14710 [Thread-12-counter-bolt] INFO  backtype.storm.task.ShellBolt - Start checking heartbeat...
14711 [Thread-12-counter-bolt] INFO  backtype.storm.daemon.executor - Prepared bolt counter-bolt:(3)
14724 [Thread-16-parse-bolt] INFO  backtype.storm.task.ShellBolt - Launched subprocess with pid 4191
14725 [Thread-16-parse-bolt] INFO  backtype.storm.task.ShellBolt - Start checking heartbeat...
14725 [Thread-16-parse-bolt] INFO  backtype.storm.daemon.executor - Prepared bolt parse-bolt:(5)
14948 [Thread-23-tweet-spout] INFO  backtype.storm.spout.ShellSpout - Launched subprocess with pid 4190
14948 [Thread-23-tweet-spout] INFO  backtype.storm.daemon.executor - Opened spout tweet-spout:(7)
14959 [Thread-23-tweet-spout] INFO  backtype.storm.daemon.executor - Activating spout tweet-spout:(7)
14960 [Thread-23-tweet-spout] INFO  backtype.storm.spout.ShellSpout - Start checking heartbeat...
15065 [Thread-23-tweet-spout] INFO  backtype.storm.spout.ShellSpout - ShellLog pid:4190, name:tweet-spout Empty queue exception 
15066 [Thread-23-tweet-spout] ERROR backtype.storm.daemon.executor - 
java.lang.Exception: Shell Process Exception: Python NameError raised
Traceback (most recent call last):
  File "/usr/lib/python2.7/site-packages/streamparse/storm/component.py", line 489, in run
    self._run()
  File "/usr/lib/python2.7/site-packages/streamparse/storm/spout.py", line 150, in _run
    self.next_tuple()
  File "spouts/tweets.py", line 76, in next_tuple
    time.sleep(0.1)
NameError: global name 'time' is not defined

	at backtype.storm.spout.ShellSpout.handleError(ShellSpout.java:212) [storm-core-0.9.5.jar:0.9.5]
	at backtype.storm.spout.ShellSpout.querySubprocess(ShellSpout.java:158) [storm-core-0.9.5.jar:0.9.5]
	at backtype.storm.spout.ShellSpout.nextTuple(ShellSpout.java:91) [storm-core-0.9.5.jar:0.9.5]
	at backtype.storm.daemon.executor$fn__3371$fn__3386$fn__3415.invoke(executor.clj:565) [storm-core-0.9.5.jar:0.9.5]
	at backtype.storm.util$async_loop$fn__460.invoke(util.clj:463) [storm-core-0.9.5.jar:0.9.5]
	at clojure.lang.AFn.run(AFn.java:24) [clojure-1.5.1.jar:na]
	at java.lang.Thread.run(Thread.java:745) [na:1.7.0_79]
15093 [Thread-23-tweet-spout] INFO  counter-bolt - /usr/lib/python2.7/site-packages/requests/packages/urllib3/util/ssl_.py:318: SNIMissingWarning: An HTTPS request has been made, but the SNI (Subject Name Indication) extension to TLS is not available on this platform. This may cause the server to present an incorrect TLS certificate, which can cause validation failures. You can upgrade to a newer version of Python to solve this. For more information, see https://urllib3.readthedocs.org/en/latest/security.html#snimissingwarning.
  SNIMissingWarning
/usr/lib/python2.7/site-packages/requests/packages/urllib3/util/ssl_.py:122: InsecurePlatformWarning: A true SSLContext object is not available. This prevents urllib3 from configuring SSL appropriately and may cause certain SSL connections to fail. You can upgrade to a newer version of Python to solve this. For more information, see https://urllib3.readthedocs.org/en/latest/security.html#insecureplatformwarning.
  InsecurePlatformWarning

16744 [Thread-23-tweet-spout] ERROR backtype.storm.util - Async loop died!
java.lang.RuntimeException: pid:4190, name:tweet-spout exitCode:-1, errorString: 
	at backtype.storm.spout.ShellSpout.querySubprocess(ShellSpout.java:180) ~[storm-core-0.9.5.jar:0.9.5]
	at backtype.storm.spout.ShellSpout.nextTuple(ShellSpout.java:91) ~[storm-core-0.9.5.jar:0.9.5]
	at backtype.storm.daemon.executor$fn__3371$fn__3386$fn__3415.invoke(executor.clj:565) ~[storm-core-0.9.5.jar:0.9.5]
	at backtype.storm.util$async_loop$fn__460.invoke(util.clj:463) ~[storm-core-0.9.5.jar:0.9.5]
	at clojure.lang.AFn.run(AFn.java:24) [clojure-1.5.1.jar:na]
	at java.lang.Thread.run(Thread.java:745) [na:1.7.0_79]
Caused by: java.lang.RuntimeException: backtype.storm.multilang.NoOutputException: Pipe to subprocess seems to be broken! No output read.
Serializer Exception:
Exception in thread Thread-1:
Traceback (most recent call last):
  File "/usr/lib64/python2.7/threading.py", line 551, in __bootstrap_inner
    self.run()
  File "/usr/lib64/python2.7/threading.py", line 504, in run
    self.__target(*self.__args, **self.__kwargs)
  File "/usr/lib/python2.7/site-packages/tweepy/streaming.py", line 294, in _run
    raise exception
Full



	at backtype.storm.utils.ShellProcess.readShellMsg(ShellProcess.java:101) ~[storm-core-0.9.5.jar:0.9.5]
	at backtype.storm.spout.ShellSpout.querySubprocess(ShellSpout.java:145) ~[storm-core-0.9.5.jar:0.9.5]
	... 5 common frames omitted
16745 [Thread-23-tweet-spout] ERROR backtype.storm.daemon.executor - 
java.lang.RuntimeException: pid:4190, name:tweet-spout exitCode:-1, errorString: 
	at backtype.storm.spout.ShellSpout.querySubprocess(ShellSpout.java:180) ~[storm-core-0.9.5.jar:0.9.5]
	at backtype.storm.spout.ShellSpout.nextTuple(ShellSpout.java:91) ~[storm-core-0.9.5.jar:0.9.5]
	at backtype.storm.daemon.executor$fn__3371$fn__3386$fn__3415.invoke(executor.clj:565) ~[storm-core-0.9.5.jar:0.9.5]
	at backtype.storm.util$async_loop$fn__460.invoke(util.clj:463) ~[storm-core-0.9.5.jar:0.9.5]
	at clojure.lang.AFn.run(AFn.java:24) [clojure-1.5.1.jar:na]
	at java.lang.Thread.run(Thread.java:745) [na:1.7.0_79]
Caused by: java.lang.RuntimeException: backtype.storm.multilang.NoOutputException: Pipe to subprocess seems to be broken! No output read.
Serializer Exception:
Exception in thread Thread-1:
Traceback (most recent call last):
  File "/usr/lib64/python2.7/threading.py", line 551, in __bootstrap_inner
    self.run()
  File "/usr/lib64/python2.7/threading.py", line 504, in run
    self.__target(*self.__args, **self.__kwargs)
  File "/usr/lib/python2.7/site-packages/tweepy/streaming.py", line 294, in _run
    raise exception
Full



	at backtype.storm.utils.ShellProcess.readShellMsg(ShellProcess.java:101) ~[storm-core-0.9.5.jar:0.9.5]
	at backtype.storm.spout.ShellSpout.querySubprocess(ShellSpout.java:145) ~[storm-core-0.9.5.jar:0.9.5]
	... 5 common frames omitted
16785 [Thread-23-tweet-spout] ERROR backtype.storm.util - Halting process: ("Worker died")
java.lang.RuntimeException: ("Worker died")
	at backtype.storm.util$exit_process_BANG_.doInvoke(util.clj:325) [storm-core-0.9.5.jar:0.9.5]
	at clojure.lang.RestFn.invoke(RestFn.java:423) [clojure-1.5.1.jar:na]
	at backtype.storm.daemon.worker$fn__4694$fn__4695.invoke(worker.clj:493) [storm-core-0.9.5.jar:0.9.5]
	at backtype.storm.daemon.executor$mk_executor_data$fn__3272$fn__3273.invoke(executor.clj:240) [storm-core-0.9.5.jar:0.9.5]
	at backtype.storm.util$async_loop$fn__460.invoke(util.clj:473) [storm-core-0.9.5.jar:0.9.5]
	at clojure.lang.AFn.run(AFn.java:24) [clojure-1.5.1.jar:na]
	at java.lang.Thread.run(Thread.java:745) [na:1.7.0_79]
Traceback (most recent call last):
  File "/usr/bin/sparse", line 9, in <module>
    load_entry_point('streamparse==2.1.4', 'console_scripts', 'sparse')()
  File "/usr/lib/python2.7/site-packages/streamparse/cli/sparse.py", line 57, in main
    args.func(args)
  File "/usr/lib/python2.7/site-packages/streamparse/cli/run.py", line 81, in main
    debug=args.debug)
  File "/usr/lib/python2.7/site-packages/streamparse/cli/run.py", line 52, in run_local_topology
    run(full_cmd)
  File "/usr/lib/python2.7/site-packages/invoke/__init__.py", line 32, in run
    return Context().run(command, **kwargs)
  File "/usr/lib/python2.7/site-packages/invoke/context.py", line 53, in run
    return runner_class(context=self).run(command, **kwargs)
  File "/usr/lib/python2.7/site-packages/invoke/runners.py", line 363, in run
    raise Failure(result)
invoke.exceptions.Failure: Command execution failure!

Exit code: 1

Stderr:




[root@ip-172-31-4-51 tweetcount]# cd ..
[root@ip-172-31-4-51 ~]# ls -l
total 724
-rw-------  1 root root    287 Sep 22  2015 dans_bash_history.txt
drwxr-xr-x  4 root root   4096 Aug  5 20:01 exercise_2
-rw-r--r--  1 root root  12402 Jul 11 18:07 ez_setup.py
-rw-r--r--  1 root root    763 Aug  5 17:04 finalresults.py
-rw-r--r--  1 root root    446 Aug  5 16:38 histogram.py
drwxr-xr-x 11 root root   4096 May  4  2015 ipython
drwxr-xr-x  5 root root   4096 May  4  2015 pgxl-deployment-tools
-rw-r--r--  1 root root 655364 Jul 11 18:07 setuptools-24.0.2.zip
-rwxr-xr-x  1 root root    221 Sep 22  2015 start-hadoop.sh
-rwxr-xr-x  1 root root    252 Sep 22  2015 start-hadoop.sh~
-rwxr-xr-x  1 root root    209 Sep 22  2015 stop-hadoop.sh
-rwxr-xr-x  1 root root    222 Sep 22  2015 stop-hadoop.sh~
drwxr-xr-x 11 root root   4096 May  4  2015 streamparse
drwxr-xr-x  8 root root   4096 Jul 11 19:33 tweetcount
-rw-r--r--  1 root root   2307 Aug  5 20:17 tweets.py
drwxr-xr-x  8 root root   4096 Aug  5 20:04 tweetwordcount
-rw-r--r--  1 root root    765 Jul 29 01:42 Twittercredentials.py
[root@ip-172-31-4-51 ~]# exercise_2/
-bash: exercise_2/: is a directory
[root@ip-172-31-4-51 ~]# ls -l
total 724
-rw-------  1 root root    287 Sep 22  2015 dans_bash_history.txt
drwxr-xr-x  4 root root   4096 Aug  5 20:01 exercise_2
-rw-r--r--  1 root root  12402 Jul 11 18:07 ez_setup.py
-rw-r--r--  1 root root    763 Aug  5 17:04 finalresults.py
-rw-r--r--  1 root root    446 Aug  5 16:38 histogram.py
drwxr-xr-x 11 root root   4096 May  4  2015 ipython
drwxr-xr-x  5 root root   4096 May  4  2015 pgxl-deployment-tools
-rw-r--r--  1 root root 655364 Jul 11 18:07 setuptools-24.0.2.zip
-rwxr-xr-x  1 root root    221 Sep 22  2015 start-hadoop.sh
-rwxr-xr-x  1 root root    252 Sep 22  2015 start-hadoop.sh~
-rwxr-xr-x  1 root root    209 Sep 22  2015 stop-hadoop.sh
-rwxr-xr-x  1 root root    222 Sep 22  2015 stop-hadoop.sh~
drwxr-xr-x 11 root root   4096 May  4  2015 streamparse
drwxr-xr-x  8 root root   4096 Jul 11 19:33 tweetcount
-rw-r--r--  1 root root   2307 Aug  5 20:17 tweets.py
drwxr-xr-x  8 root root   4096 Aug  5 20:04 tweetwordcount
-rw-r--r--  1 root root    765 Jul 29 01:42 Twittercredentials.py
[root@ip-172-31-4-51 ~]# cd exercise_2/
[root@ip-172-31-4-51 exercise_2]# ls -l
total 20
-rw-r--r-- 1 root root  812 Aug  5 20:01 db_setup.py
-rw-r--r-- 1 root root 1384 Aug  5 20:01 finalresults.py
-rw-r--r-- 1 root root  826 Aug  5 20:01 histogram.py
-rw-r--r-- 1 root root 1145 Aug  5 20:01 README.md
drwxr-xr-x 8 root root 4096 Aug  5 20:01 tweetwordcount
[root@ip-172-31-4-51 exercise_2]# cd ..
[root@ip-172-31-4-51 ~]# sparse tweetcount
usage: sparse [-h] [--version]
              
              {jar,kill,list,quickstart,remove_logs,run,slot_usage,stats,submit,tail,update_virtualenv,visualize,worker_uptime}
              ...
sparse: error: invalid choice: 'tweetcount' (choose from u'jar', 'kill', 'list', 'quickstart', 'remove_logs', 'run', 'slot_usage', 'stats', u'submit', 'tail', u'update_virtualenv', 'visualize', 'worker_uptime')
[root@ip-172-31-4-51 ~]# cd tweetsount
-bash: cd: tweetsount: No such file or directory
[root@ip-172-31-4-51 ~]# cd tweetcount
[root@ip-172-31-4-51 tweetcount]# sparse run
Running tweetcount topology...
Routing Python logging to /root/tweetcount/logs.
Running lein command to run local cluster:
lein run -m streamparse.commands.run/-main topologies/tweetcount.clj -t 0 --option 'topology.workers=2' --option 'topology.acker.executors=2' --option 'streamparse.log.path="/root/tweetcount/logs"' --option 'streamparse.log.level="debug"'
WARNING: You're currently running as root; probably by accident.
Press control-C to abort or Enter to continue as root.
Set LEIN_ROOT to disable this warning.

3940 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:zookeeper.version=3.4.6-1569965, built on 02/20/2014 09:09 GMT
3973 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:host.name=ip-172-31-4-51.ec2.internal
3973 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:java.version=1.7.0_79
3973 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:java.vendor=Oracle Corporation
3973 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:java.home=/opt/jdk1.7.0_79/jre
3973 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:java.class.path=/root/tweetcount/test:/root/tweetcount/topologies:/root/tweetcount/dev-resources:/root/tweetcount/_resources:/root/tweetcount/_build/classes:/root/.m2/repository/ch/qos/logback/logback-classic/1.0.13/logback-classic-1.0.13.jar:/root/.m2/repository/org/clojure/tools.macro/0.1.0/tools.macro-0.1.0.jar:/root/.m2/repository/ring/ring-core/1.1.5/ring-core-1.1.5.jar:/root/.m2/repository/hiccup/hiccup/0.3.6/hiccup-0.3.6.jar:/root/.m2/repository/ring/ring-servlet/0.3.11/ring-servlet-0.3.11.jar:/root/.m2/repository/com/googlecode/json-simple/json-simple/1.1/json-simple-1.1.jar:/root/.m2/repository/org/clojure/math.numeric-tower/0.0.1/math.numeric-tower-0.0.1.jar:/root/.m2/repository/clj-time/clj-time/0.4.1/clj-time-0.4.1.jar:/root/.m2/repository/org/objenesis/objenesis/1.2/objenesis-1.2.jar:/root/.m2/repository/com/twitter/chill-java/0.3.5/chill-java-0.3.5.jar:/root/.m2/repository/com/parsely/streamparse/0.0.4-SNAPSHOT/streamparse-0.0.4-SNAPSHOT.jar:/root/.m2/repository/ring/ring-jetty-adapter/0.3.11/ring-jetty-adapter-0.3.11.jar:/root/.m2/repository/jline/jline/2.11/jline-2.11.jar:/root/.m2/repository/clj-stacktrace/clj-stacktrace/0.2.2/clj-stacktrace-0.2.2.jar:/root/.m2/repository/org/clojure/tools.nrepl/0.2.12/tools.nrepl-0.2.12.jar:/root/.m2/repository/org/slf4j/slf4j-api/1.7.5/slf4j-api-1.7.5.jar:/root/.m2/repository/ring/ring-devel/0.3.11/ring-devel-0.3.11.jar:/root/.m2/repository/org/mortbay/jetty/jetty-util/6.1.26/jetty-util-6.1.26.jar:/root/.m2/repository/javax/servlet/servlet-api/2.5/servlet-api-2.5.jar:/root/.m2/repository/clojure-complete/clojure-complete/0.2.4/clojure-complete-0.2.4.jar:/root/.m2/repository/org/yaml/snakeyaml/1.11/snakeyaml-1.11.jar:/root/.m2/repository/ch/qos/logback/logback-core/1.0.13/logback-core-1.0.13.jar:/root/.m2/repository/commons-lang/commons-lang/2.5/commons-lang-2.5.jar:/root/.m2/repository/org/mortbay/jetty/jetty/6.1.26/jetty-6.1.26.jar:/root/.m2/repository/joda-time/joda-time/2.0/joda-time-2.0.jar:/root/.m2/repository/commons-io/commons-io/2.4/commons-io-2.4.jar:/root/.m2/repository/commons-logging/commons-logging/1.1.3/commons-logging-1.1.3.jar:/root/.m2/repository/com/esotericsoftware/kryo/kryo/2.21/kryo-2.21.jar:/root/.m2/repository/com/esotericsoftware/minlog/minlog/1.2/minlog-1.2.jar:/root/.m2/repository/org/apache/storm/storm-core/0.9.5/storm-core-0.9.5.jar:/root/.m2/repository/compojure/compojure/1.1.3/compojure-1.1.3.jar:/root/.m2/repository/com/esotericsoftware/reflectasm/reflectasm/1.07/reflectasm-1.07-shaded.jar:/root/.m2/repository/com/twitter/carbonite/1.4.0/carbonite-1.4.0.jar:/root/.m2/repository/commons-codec/commons-codec/1.6/commons-codec-1.6.jar:/root/.m2/repository/commons-fileupload/commons-fileupload/1.2.1/commons-fileupload-1.2.1.jar:/root/.m2/repository/org/clojure/data.json/0.2.6/data.json-0.2.6.jar:/root/.m2/repository/org/slf4j/log4j-over-slf4j/1.6.6/log4j-over-slf4j-1.6.6.jar:/root/.m2/repository/org/jgrapht/jgrapht-core/0.9.0/jgrapht-core-0.9.0.jar:/root/.m2/repository/org/clojure/clojure/1.5.1/clojure-1.5.1.jar:/root/.m2/repository/org/clojure/tools.logging/0.2.3/tools.logging-0.2.3.jar:/root/.m2/repository/org/ow2/asm/asm/4.0/asm-4.0.jar:/root/.m2/repository/clout/clout/1.0.1/clout-1.0.1.jar:/root/.m2/repository/org/apache/commons/commons-exec/1.1/commons-exec-1.1.jar:/root/.m2/repository/com/googlecode/disruptor/disruptor/2.10.1/disruptor-2.10.1.jar:/root/.m2/repository/org/clojure/core.incubator/0.1.0/core.incubator-0.1.0.jar:/root/.m2/repository/org/clojure/tools.cli/0.2.4/tools.cli-0.2.4.jar
3974 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:java.library.path=/usr/java/packages/lib/amd64:/usr/lib64:/lib64:/lib:/usr/lib
3974 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:java.io.tmpdir=/tmp
3974 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:java.compiler=<NA>
3974 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:os.name=Linux
3974 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:os.arch=amd64
3974 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:os.version=2.6.32-504.12.2.el6.centos.plus.x86_64
3975 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:user.name=root
3975 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:user.home=/root
3975 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:user.dir=/root/tweetcount
4021 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:zookeeper.version=3.4.6-1569965, built on 02/20/2014 09:09 GMT
4021 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:host.name=ip-172-31-4-51.ec2.internal
4021 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:java.version=1.7.0_79
4021 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:java.vendor=Oracle Corporation
4021 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:java.home=/opt/jdk1.7.0_79/jre
4021 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:java.class.path=/root/tweetcount/test:/root/tweetcount/topologies:/root/tweetcount/dev-resources:/root/tweetcount/_resources:/root/tweetcount/_build/classes:/root/.m2/repository/ch/qos/logback/logback-classic/1.0.13/logback-classic-1.0.13.jar:/root/.m2/repository/org/clojure/tools.macro/0.1.0/tools.macro-0.1.0.jar:/root/.m2/repository/ring/ring-core/1.1.5/ring-core-1.1.5.jar:/root/.m2/repository/hiccup/hiccup/0.3.6/hiccup-0.3.6.jar:/root/.m2/repository/ring/ring-servlet/0.3.11/ring-servlet-0.3.11.jar:/root/.m2/repository/com/googlecode/json-simple/json-simple/1.1/json-simple-1.1.jar:/root/.m2/repository/org/clojure/math.numeric-tower/0.0.1/math.numeric-tower-0.0.1.jar:/root/.m2/repository/clj-time/clj-time/0.4.1/clj-time-0.4.1.jar:/root/.m2/repository/org/objenesis/objenesis/1.2/objenesis-1.2.jar:/root/.m2/repository/com/twitter/chill-java/0.3.5/chill-java-0.3.5.jar:/root/.m2/repository/com/parsely/streamparse/0.0.4-SNAPSHOT/streamparse-0.0.4-SNAPSHOT.jar:/root/.m2/repository/ring/ring-jetty-adapter/0.3.11/ring-jetty-adapter-0.3.11.jar:/root/.m2/repository/jline/jline/2.11/jline-2.11.jar:/root/.m2/repository/clj-stacktrace/clj-stacktrace/0.2.2/clj-stacktrace-0.2.2.jar:/root/.m2/repository/org/clojure/tools.nrepl/0.2.12/tools.nrepl-0.2.12.jar:/root/.m2/repository/org/slf4j/slf4j-api/1.7.5/slf4j-api-1.7.5.jar:/root/.m2/repository/ring/ring-devel/0.3.11/ring-devel-0.3.11.jar:/root/.m2/repository/org/mortbay/jetty/jetty-util/6.1.26/jetty-util-6.1.26.jar:/root/.m2/repository/javax/servlet/servlet-api/2.5/servlet-api-2.5.jar:/root/.m2/repository/clojure-complete/clojure-complete/0.2.4/clojure-complete-0.2.4.jar:/root/.m2/repository/org/yaml/snakeyaml/1.11/snakeyaml-1.11.jar:/root/.m2/repository/ch/qos/logback/logback-core/1.0.13/logback-core-1.0.13.jar:/root/.m2/repository/commons-lang/commons-lang/2.5/commons-lang-2.5.jar:/root/.m2/repository/org/mortbay/jetty/jetty/6.1.26/jetty-6.1.26.jar:/root/.m2/repository/joda-time/joda-time/2.0/joda-time-2.0.jar:/root/.m2/repository/commons-io/commons-io/2.4/commons-io-2.4.jar:/root/.m2/repository/commons-logging/commons-logging/1.1.3/commons-logging-1.1.3.jar:/root/.m2/repository/com/esotericsoftware/kryo/kryo/2.21/kryo-2.21.jar:/root/.m2/repository/com/esotericsoftware/minlog/minlog/1.2/minlog-1.2.jar:/root/.m2/repository/org/apache/storm/storm-core/0.9.5/storm-core-0.9.5.jar:/root/.m2/repository/compojure/compojure/1.1.3/compojure-1.1.3.jar:/root/.m2/repository/com/esotericsoftware/reflectasm/reflectasm/1.07/reflectasm-1.07-shaded.jar:/root/.m2/repository/com/twitter/carbonite/1.4.0/carbonite-1.4.0.jar:/root/.m2/repository/commons-codec/commons-codec/1.6/commons-codec-1.6.jar:/root/.m2/repository/commons-fileupload/commons-fileupload/1.2.1/commons-fileupload-1.2.1.jar:/root/.m2/repository/org/clojure/data.json/0.2.6/data.json-0.2.6.jar:/root/.m2/repository/org/slf4j/log4j-over-slf4j/1.6.6/log4j-over-slf4j-1.6.6.jar:/root/.m2/repository/org/jgrapht/jgrapht-core/0.9.0/jgrapht-core-0.9.0.jar:/root/.m2/repository/org/clojure/clojure/1.5.1/clojure-1.5.1.jar:/root/.m2/repository/org/clojure/tools.logging/0.2.3/tools.logging-0.2.3.jar:/root/.m2/repository/org/ow2/asm/asm/4.0/asm-4.0.jar:/root/.m2/repository/clout/clout/1.0.1/clout-1.0.1.jar:/root/.m2/repository/org/apache/commons/commons-exec/1.1/commons-exec-1.1.jar:/root/.m2/repository/com/googlecode/disruptor/disruptor/2.10.1/disruptor-2.10.1.jar:/root/.m2/repository/org/clojure/core.incubator/0.1.0/core.incubator-0.1.0.jar:/root/.m2/repository/org/clojure/tools.cli/0.2.4/tools.cli-0.2.4.jar
4021 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:java.library.path=/usr/java/packages/lib/amd64:/usr/lib64:/lib64:/lib:/usr/lib
4021 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:java.io.tmpdir=/tmp
4021 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:java.compiler=<NA>
4021 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:os.name=Linux
4021 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:os.arch=amd64
4021 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:os.version=2.6.32-504.12.2.el6.centos.plus.x86_64
4021 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:user.name=root
4021 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:user.home=/root
4021 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:user.dir=/root/tweetcount
5918 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Created server with tickTime 2000 minSessionTimeout 4000 maxSessionTimeout 40000 datadir /tmp/270338b7-7c08-4d0d-a59f-60e72c50f580/version-2 snapdir /tmp/270338b7-7c08-4d0d-a59f-60e72c50f580/version-2
5951 [main] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - binding to port 0.0.0.0/0.0.0.0:2000
5993 [main] INFO  backtype.storm.zookeeper - Starting inprocess zookeeper at port 2000 and dir /tmp/270338b7-7c08-4d0d-a59f-60e72c50f580
6514 [main] INFO  backtype.storm.daemon.nimbus - Starting Nimbus with conf {"dev.zookeeper.path" "/tmp/dev-storm-zookeeper", "topology.tick.tuple.freq.secs" nil, "topology.builtin.metrics.bucket.size.secs" 60, "topology.fall.back.on.java.serialization" true, "topology.max.error.report.per.interval" 5, "zmq.linger.millis" 0, "topology.skip.missing.kryo.registrations" true, "storm.messaging.netty.client_worker_threads" 1, "ui.childopts" "-Xmx768m", "storm.zookeeper.session.timeout" 20000, "nimbus.reassign" true, "topology.trident.batch.emit.interval.millis" 50, "storm.messaging.netty.flush.check.interval.ms" 10, "nimbus.monitor.freq.secs" 10, "logviewer.childopts" "-Xmx128m", "java.library.path" "/usr/local/lib:/opt/local/lib:/usr/lib", "topology.executor.send.buffer.size" 1024, "storm.local.dir" "/tmp/836fd586-7ebd-49c8-a5b1-db7e0a26f10c", "storm.messaging.netty.buffer_size" 5242880, "supervisor.worker.start.timeout.secs" 120, "topology.enable.message.timeouts" true, "nimbus.cleanup.inbox.freq.secs" 600, "nimbus.inbox.jar.expiration.secs" 3600, "drpc.worker.threads" 64, "storm.meta.serialization.delegate" "backtype.storm.serialization.DefaultSerializationDelegate", "topology.worker.shared.thread.pool.size" 4, "nimbus.host" "localhost", "storm.messaging.netty.min_wait_ms" 100, "storm.zookeeper.port" 2000, "transactional.zookeeper.port" nil, "topology.executor.receive.buffer.size" 1024, "transactional.zookeeper.servers" nil, "storm.zookeeper.root" "/storm", "storm.zookeeper.retry.intervalceiling.millis" 30000, "supervisor.enable" true, "storm.messaging.netty.server_worker_threads" 1, "storm.zookeeper.servers" ["localhost"], "transactional.zookeeper.root" "/transactional", "topology.acker.executors" nil, "topology.transfer.buffer.size" 1024, "topology.worker.childopts" nil, "drpc.queue.size" 128, "worker.childopts" "-Xmx768m", "supervisor.heartbeat.frequency.secs" 5, "topology.error.throttle.interval.secs" 10, "zmq.hwm" 0, "drpc.port" 3772, "supervisor.monitor.frequency.secs" 3, "drpc.childopts" "-Xmx768m", "topology.receiver.buffer.size" 8, "task.heartbeat.frequency.secs" 3, "topology.tasks" nil, "storm.messaging.netty.max_retries" 300, "topology.spout.wait.strategy" "backtype.storm.spout.SleepSpoutWaitStrategy", "nimbus.thrift.max_buffer_size" 1048576, "topology.max.spout.pending" nil, "storm.zookeeper.retry.interval" 1000, "topology.sleep.spout.wait.strategy.time.ms" 1, "nimbus.topology.validator" "backtype.storm.nimbus.DefaultTopologyValidator", "supervisor.slots.ports" [6700 6701 6702 6703], "topology.environment" nil, "topology.debug" false, "nimbus.task.launch.secs" 120, "nimbus.supervisor.timeout.secs" 60, "topology.message.timeout.secs" 30, "task.refresh.poll.secs" 10, "topology.workers" 1, "supervisor.childopts" "-Xmx256m", "nimbus.thrift.port" 6627, "topology.stats.sample.rate" 0.05, "worker.heartbeat.frequency.secs" 1, "topology.tuple.serializer" "backtype.storm.serialization.types.ListDelegateSerializer", "topology.disruptor.wait.strategy" "com.lmax.disruptor.BlockingWaitStrategy", "topology.multilang.serializer" "backtype.storm.multilang.JsonSerializer", "nimbus.task.timeout.secs" 30, "storm.zookeeper.connection.timeout" 15000, "topology.kryo.factory" "backtype.storm.serialization.DefaultKryoFactory", "drpc.invocations.port" 3773, "logviewer.port" 8000, "zmq.threads" 1, "storm.zookeeper.retry.times" 5, "topology.worker.receiver.thread.count" 1, "storm.thrift.transport" "backtype.storm.security.auth.SimpleTransportPlugin", "topology.state.synchronization.timeout.secs" 60, "supervisor.worker.timeout.secs" 30, "nimbus.file.copy.expiration.secs" 600, "storm.messaging.transport" "backtype.storm.messaging.netty.Context", "logviewer.appender.name" "A1", "storm.messaging.netty.max_wait_ms" 1000, "drpc.request.timeout.secs" 600, "storm.local.mode.zmq" false, "ui.port" 8080, "nimbus.childopts" "-Xmx1024m", "storm.cluster.mode" "local", "topology.max.task.parallelism" nil, "storm.messaging.netty.transfer.batch.size" 262144, "topology.classpath" nil}
6528 [main] INFO  backtype.storm.daemon.nimbus - Using default scheduler
6568 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
6821 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
6824 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000 sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@4b94b3b3
6856 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
6875 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55764
6886 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
6890 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55764
6902 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.persistence.FileTxnLog - Creating new log file: log.1
6914 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c6a03020000, negotiated timeout = 20000
6924 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c6a03020000 with negotiated timeout 20000 for client /127.0.0.1:55764
6925 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
6927 [main-EventThread] INFO  backtype.storm.zookeeper - Zookeeper state update: :connected:none
7972 [ProcessThread(sid:0 cport:-1):] INFO  org.apache.storm.zookeeper.server.PrepRequestProcessor - Processed session termination for sessionid: 0x1565c6a03020000
7982 [main-EventThread] INFO  org.apache.storm.zookeeper.ClientCnxn - EventThread shut down
7982 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Session: 0x1565c6a03020000 closed
7984 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
7984 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
7986 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000/storm sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@355dddf2
7998 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
7999 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
7999 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxn - Closed socket connection for client /127.0.0.1:55764 which had sessionid 0x1565c6a03020000
8000 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55765
8000 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55765
8002 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c6a03020001 with negotiated timeout 20000 for client /127.0.0.1:55765
8002 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c6a03020001, negotiated timeout = 20000
8002 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
8071 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
8071 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
8072 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000 sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@a632536
8073 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
8073 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55766
8073 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
8074 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55766
8077 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c6a03020002 with negotiated timeout 20000 for client /127.0.0.1:55766
8077 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c6a03020002, negotiated timeout = 20000
8078 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
8078 [main-EventThread] INFO  backtype.storm.zookeeper - Zookeeper state update: :connected:none
9081 [ProcessThread(sid:0 cport:-1):] INFO  org.apache.storm.zookeeper.server.PrepRequestProcessor - Processed session termination for sessionid: 0x1565c6a03020002
9083 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxn - Closed socket connection for client /127.0.0.1:55766 which had sessionid 0x1565c6a03020002
9084 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Session: 0x1565c6a03020002 closed
9084 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
9084 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
9085 [main-EventThread] INFO  org.apache.storm.zookeeper.ClientCnxn - EventThread shut down
9085 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000/storm sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@677d089c
9100 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
9100 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55767
9101 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
9101 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55767
9102 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
9103 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
9103 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000 sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@71a67848
9104 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
9105 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55768
9105 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
9105 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55768
9116 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c6a03020003 with negotiated timeout 20000 for client /127.0.0.1:55767
9117 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c6a03020003, negotiated timeout = 20000
9117 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
9118 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c6a03020004 with negotiated timeout 20000 for client /127.0.0.1:55768
9118 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c6a03020004, negotiated timeout = 20000
9118 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
9118 [main-EventThread] INFO  backtype.storm.zookeeper - Zookeeper state update: :connected:none
9120 [ProcessThread(sid:0 cport:-1):] INFO  org.apache.storm.zookeeper.server.PrepRequestProcessor - Processed session termination for sessionid: 0x1565c6a03020004
9121 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Session: 0x1565c6a03020004 closed
9122 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
9122 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
9122 [main-EventThread] INFO  org.apache.storm.zookeeper.ClientCnxn - EventThread shut down
9122 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000/storm sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@63854b3a
9123 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
9123 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
9126 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxn - Closed socket connection for client /127.0.0.1:55768 which had sessionid 0x1565c6a03020004
9127 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55769
9127 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55769
9137 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c6a03020005 with negotiated timeout 20000 for client /127.0.0.1:55769
9137 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c6a03020005, negotiated timeout = 20000
9137 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
10186 [main] INFO  backtype.storm.daemon.supervisor - Starting Supervisor with conf {"dev.zookeeper.path" "/tmp/dev-storm-zookeeper", "topology.tick.tuple.freq.secs" nil, "topology.builtin.metrics.bucket.size.secs" 60, "topology.fall.back.on.java.serialization" true, "topology.max.error.report.per.interval" 5, "zmq.linger.millis" 0, "topology.skip.missing.kryo.registrations" true, "storm.messaging.netty.client_worker_threads" 1, "ui.childopts" "-Xmx768m", "storm.zookeeper.session.timeout" 20000, "nimbus.reassign" true, "topology.trident.batch.emit.interval.millis" 50, "storm.messaging.netty.flush.check.interval.ms" 10, "nimbus.monitor.freq.secs" 10, "logviewer.childopts" "-Xmx128m", "java.library.path" "/usr/local/lib:/opt/local/lib:/usr/lib", "topology.executor.send.buffer.size" 1024, "storm.local.dir" "/tmp/02bcc8b4-16b4-4c79-ba17-23480f39535b", "storm.messaging.netty.buffer_size" 5242880, "supervisor.worker.start.timeout.secs" 120, "topology.enable.message.timeouts" true, "nimbus.cleanup.inbox.freq.secs" 600, "nimbus.inbox.jar.expiration.secs" 3600, "drpc.worker.threads" 64, "storm.meta.serialization.delegate" "backtype.storm.serialization.DefaultSerializationDelegate", "topology.worker.shared.thread.pool.size" 4, "nimbus.host" "localhost", "storm.messaging.netty.min_wait_ms" 100, "storm.zookeeper.port" 2000, "transactional.zookeeper.port" nil, "topology.executor.receive.buffer.size" 1024, "transactional.zookeeper.servers" nil, "storm.zookeeper.root" "/storm", "storm.zookeeper.retry.intervalceiling.millis" 30000, "supervisor.enable" true, "storm.messaging.netty.server_worker_threads" 1, "storm.zookeeper.servers" ["localhost"], "transactional.zookeeper.root" "/transactional", "topology.acker.executors" nil, "topology.transfer.buffer.size" 1024, "topology.worker.childopts" nil, "drpc.queue.size" 128, "worker.childopts" "-Xmx768m", "supervisor.heartbeat.frequency.secs" 5, "topology.error.throttle.interval.secs" 10, "zmq.hwm" 0, "drpc.port" 3772, "supervisor.monitor.frequency.secs" 3, "drpc.childopts" "-Xmx768m", "topology.receiver.buffer.size" 8, "task.heartbeat.frequency.secs" 3, "topology.tasks" nil, "storm.messaging.netty.max_retries" 300, "topology.spout.wait.strategy" "backtype.storm.spout.SleepSpoutWaitStrategy", "nimbus.thrift.max_buffer_size" 1048576, "topology.max.spout.pending" nil, "storm.zookeeper.retry.interval" 1000, "topology.sleep.spout.wait.strategy.time.ms" 1, "nimbus.topology.validator" "backtype.storm.nimbus.DefaultTopologyValidator", "supervisor.slots.ports" (1024 1025 1026), "topology.environment" nil, "topology.debug" false, "nimbus.task.launch.secs" 120, "nimbus.supervisor.timeout.secs" 60, "topology.message.timeout.secs" 30, "task.refresh.poll.secs" 10, "topology.workers" 1, "supervisor.childopts" "-Xmx256m", "nimbus.thrift.port" 6627, "topology.stats.sample.rate" 0.05, "worker.heartbeat.frequency.secs" 1, "topology.tuple.serializer" "backtype.storm.serialization.types.ListDelegateSerializer", "topology.disruptor.wait.strategy" "com.lmax.disruptor.BlockingWaitStrategy", "topology.multilang.serializer" "backtype.storm.multilang.JsonSerializer", "nimbus.task.timeout.secs" 30, "storm.zookeeper.connection.timeout" 15000, "topology.kryo.factory" "backtype.storm.serialization.DefaultKryoFactory", "drpc.invocations.port" 3773, "logviewer.port" 8000, "zmq.threads" 1, "storm.zookeeper.retry.times" 5, "topology.worker.receiver.thread.count" 1, "storm.thrift.transport" "backtype.storm.security.auth.SimpleTransportPlugin", "topology.state.synchronization.timeout.secs" 60, "supervisor.worker.timeout.secs" 30, "nimbus.file.copy.expiration.secs" 600, "storm.messaging.transport" "backtype.storm.messaging.netty.Context", "logviewer.appender.name" "A1", "storm.messaging.netty.max_wait_ms" 1000, "drpc.request.timeout.secs" 600, "storm.local.mode.zmq" false, "ui.port" 8080, "nimbus.childopts" "-Xmx1024m", "storm.cluster.mode" "local", "topology.max.task.parallelism" nil, "storm.messaging.netty.transfer.batch.size" 262144, "topology.classpath" nil}
10205 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
10214 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
10214 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000 sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@6d4d9023
10215 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
10215 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55770
10216 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
10216 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55770
10218 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c6a03020006 with negotiated timeout 20000 for client /127.0.0.1:55770
10218 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c6a03020006, negotiated timeout = 20000
10219 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
10219 [main-EventThread] INFO  backtype.storm.zookeeper - Zookeeper state update: :connected:none
11221 [ProcessThread(sid:0 cport:-1):] INFO  org.apache.storm.zookeeper.server.PrepRequestProcessor - Processed session termination for sessionid: 0x1565c6a03020006
11223 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxn - Closed socket connection for client /127.0.0.1:55770 which had sessionid 0x1565c6a03020006
11223 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Session: 0x1565c6a03020006 closed
11224 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
11224 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
11224 [main-EventThread] INFO  org.apache.storm.zookeeper.ClientCnxn - EventThread shut down
11227 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000/storm sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@7d15a969
11228 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
11229 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55771
11229 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
11229 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55771
11240 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c6a03020007 with negotiated timeout 20000 for client /127.0.0.1:55771
11241 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c6a03020007, negotiated timeout = 20000
11243 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
12293 [main] INFO  backtype.storm.daemon.supervisor - Starting supervisor with id e2fdc280-587d-4e71-98df-833f1ca75dc0 at host ip-172-31-4-51.ec2.internal
12316 [main] INFO  backtype.storm.daemon.supervisor - Starting Supervisor with conf {"dev.zookeeper.path" "/tmp/dev-storm-zookeeper", "topology.tick.tuple.freq.secs" nil, "topology.builtin.metrics.bucket.size.secs" 60, "topology.fall.back.on.java.serialization" true, "topology.max.error.report.per.interval" 5, "zmq.linger.millis" 0, "topology.skip.missing.kryo.registrations" true, "storm.messaging.netty.client_worker_threads" 1, "ui.childopts" "-Xmx768m", "storm.zookeeper.session.timeout" 20000, "nimbus.reassign" true, "topology.trident.batch.emit.interval.millis" 50, "storm.messaging.netty.flush.check.interval.ms" 10, "nimbus.monitor.freq.secs" 10, "logviewer.childopts" "-Xmx128m", "java.library.path" "/usr/local/lib:/opt/local/lib:/usr/lib", "topology.executor.send.buffer.size" 1024, "storm.local.dir" "/tmp/c138ef3b-ec9c-4248-a94c-3472cdca60b4", "storm.messaging.netty.buffer_size" 5242880, "supervisor.worker.start.timeout.secs" 120, "topology.enable.message.timeouts" true, "nimbus.cleanup.inbox.freq.secs" 600, "nimbus.inbox.jar.expiration.secs" 3600, "drpc.worker.threads" 64, "storm.meta.serialization.delegate" "backtype.storm.serialization.DefaultSerializationDelegate", "topology.worker.shared.thread.pool.size" 4, "nimbus.host" "localhost", "storm.messaging.netty.min_wait_ms" 100, "storm.zookeeper.port" 2000, "transactional.zookeeper.port" nil, "topology.executor.receive.buffer.size" 1024, "transactional.zookeeper.servers" nil, "storm.zookeeper.root" "/storm", "storm.zookeeper.retry.intervalceiling.millis" 30000, "supervisor.enable" true, "storm.messaging.netty.server_worker_threads" 1, "storm.zookeeper.servers" ["localhost"], "transactional.zookeeper.root" "/transactional", "topology.acker.executors" nil, "topology.transfer.buffer.size" 1024, "topology.worker.childopts" nil, "drpc.queue.size" 128, "worker.childopts" "-Xmx768m", "supervisor.heartbeat.frequency.secs" 5, "topology.error.throttle.interval.secs" 10, "zmq.hwm" 0, "drpc.port" 3772, "supervisor.monitor.frequency.secs" 3, "drpc.childopts" "-Xmx768m", "topology.receiver.buffer.size" 8, "task.heartbeat.frequency.secs" 3, "topology.tasks" nil, "storm.messaging.netty.max_retries" 300, "topology.spout.wait.strategy" "backtype.storm.spout.SleepSpoutWaitStrategy", "nimbus.thrift.max_buffer_size" 1048576, "topology.max.spout.pending" nil, "storm.zookeeper.retry.interval" 1000, "topology.sleep.spout.wait.strategy.time.ms" 1, "nimbus.topology.validator" "backtype.storm.nimbus.DefaultTopologyValidator", "supervisor.slots.ports" (1027 1028 1029), "topology.environment" nil, "topology.debug" false, "nimbus.task.launch.secs" 120, "nimbus.supervisor.timeout.secs" 60, "topology.message.timeout.secs" 30, "task.refresh.poll.secs" 10, "topology.workers" 1, "supervisor.childopts" "-Xmx256m", "nimbus.thrift.port" 6627, "topology.stats.sample.rate" 0.05, "worker.heartbeat.frequency.secs" 1, "topology.tuple.serializer" "backtype.storm.serialization.types.ListDelegateSerializer", "topology.disruptor.wait.strategy" "com.lmax.disruptor.BlockingWaitStrategy", "topology.multilang.serializer" "backtype.storm.multilang.JsonSerializer", "nimbus.task.timeout.secs" 30, "storm.zookeeper.connection.timeout" 15000, "topology.kryo.factory" "backtype.storm.serialization.DefaultKryoFactory", "drpc.invocations.port" 3773, "logviewer.port" 8000, "zmq.threads" 1, "storm.zookeeper.retry.times" 5, "topology.worker.receiver.thread.count" 1, "storm.thrift.transport" "backtype.storm.security.auth.SimpleTransportPlugin", "topology.state.synchronization.timeout.secs" 60, "supervisor.worker.timeout.secs" 30, "nimbus.file.copy.expiration.secs" 600, "storm.messaging.transport" "backtype.storm.messaging.netty.Context", "logviewer.appender.name" "A1", "storm.messaging.netty.max_wait_ms" 1000, "drpc.request.timeout.secs" 600, "storm.local.mode.zmq" false, "ui.port" 8080, "nimbus.childopts" "-Xmx1024m", "storm.cluster.mode" "local", "topology.max.task.parallelism" nil, "storm.messaging.netty.transfer.batch.size" 262144, "topology.classpath" nil}
12321 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
12322 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
12323 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000 sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@1c094d3c
12333 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
12334 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55772
12335 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
12335 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55772
12337 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c6a03020008 with negotiated timeout 20000 for client /127.0.0.1:55772
12338 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c6a03020008, negotiated timeout = 20000
12338 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
12357 [main-EventThread] INFO  backtype.storm.zookeeper - Zookeeper state update: :connected:none
12360 [ProcessThread(sid:0 cport:-1):] INFO  org.apache.storm.zookeeper.server.PrepRequestProcessor - Processed session termination for sessionid: 0x1565c6a03020008
12363 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxn - Closed socket connection for client /127.0.0.1:55772 which had sessionid 0x1565c6a03020008
12363 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Session: 0x1565c6a03020008 closed
12363 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
12364 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
12364 [main-EventThread] INFO  org.apache.storm.zookeeper.ClientCnxn - EventThread shut down
12364 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000/storm sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@40819d8c
12365 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
12365 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55773
12366 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
12366 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55773
12377 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c6a03020009 with negotiated timeout 20000 for client /127.0.0.1:55773
12377 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c6a03020009, negotiated timeout = 20000
12378 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
12395 [main] INFO  backtype.storm.daemon.supervisor - Starting supervisor with id aff4953e-8b07-401a-a269-440087a4032f at host ip-172-31-4-51.ec2.internal
12535 [main] INFO  backtype.storm.daemon.nimbus - Received topology submission for tweetcount with conf {"storm.id" "tweetcount-1-1470429273", "topology.acker.executors" 2, "streamparse.log.path" "/root/tweetcount/logs", "topology.kryo.decorators" (), "topology.name" "tweetcount", "topology.max.spout.pending" 5000, "topology.debug" false, "topology.kryo.register" nil, "topology.message.timeout.secs" 60, "topology.workers" 2, "topology.max.task.parallelism" nil, "streamparse.log.level" "debug"}
12618 [main] INFO  backtype.storm.daemon.nimbus - Activating tweetcount: tweetcount-1-1470429273
12829 [main] INFO  backtype.storm.scheduler.EvenScheduler - Available slots: (["e2fdc280-587d-4e71-98df-833f1ca75dc0" 1024] ["e2fdc280-587d-4e71-98df-833f1ca75dc0" 1025] ["e2fdc280-587d-4e71-98df-833f1ca75dc0" 1026] ["aff4953e-8b07-401a-a269-440087a4032f" 1027] ["aff4953e-8b07-401a-a269-440087a4032f" 1028] ["aff4953e-8b07-401a-a269-440087a4032f" 1029])
12971 [main] INFO  backtype.storm.daemon.nimbus - Setting new assignment for topology id tweetcount-1-1470429273: #backtype.storm.daemon.common.Assignment{:master-code-dir "/tmp/836fd586-7ebd-49c8-a5b1-db7e0a26f10c/nimbus/stormdist/tweetcount-1-1470429273", :node->host {"e2fdc280-587d-4e71-98df-833f1ca75dc0" "ip-172-31-4-51.ec2.internal", "aff4953e-8b07-401a-a269-440087a4032f" "ip-172-31-4-51.ec2.internal"}, :executor->node+port {[3 3] ["e2fdc280-587d-4e71-98df-833f1ca75dc0" 1024], [6 6] ["aff4953e-8b07-401a-a269-440087a4032f" 1027], [5 5] ["e2fdc280-587d-4e71-98df-833f1ca75dc0" 1024], [4 4] ["aff4953e-8b07-401a-a269-440087a4032f" 1027], [7 7] ["e2fdc280-587d-4e71-98df-833f1ca75dc0" 1024], [2 2] ["aff4953e-8b07-401a-a269-440087a4032f" 1027], [1 1] ["e2fdc280-587d-4e71-98df-833f1ca75dc0" 1024]}, :executor->start-time-secs {[7 7] 1470429273, [5 5] 1470429273, [3 3] 1470429273, [1 1] 1470429273, [6 6] 1470429273, [4 4] 1470429273, [2 2] 1470429273}}
14521 [Thread-5] INFO  backtype.storm.daemon.supervisor - Copying resources at file:/root/tweetcount/_resources/resources to /tmp/c138ef3b-ec9c-4248-a94c-3472cdca60b4/supervisor/stormdist/tweetcount-1-1470429273/resources
14561 [Thread-3] INFO  backtype.storm.daemon.supervisor - Copying resources at file:/root/tweetcount/_resources/resources to /tmp/02bcc8b4-16b4-4c79-ba17-23480f39535b/supervisor/stormdist/tweetcount-1-1470429273/resources
14647 [Thread-6] INFO  backtype.storm.daemon.supervisor - Launching worker with assignment #backtype.storm.daemon.supervisor.LocalAssignment{:storm-id "tweetcount-1-1470429273", :executors ([6 6] [4 4] [2 2])} for this supervisor aff4953e-8b07-401a-a269-440087a4032f on port 1027 with id 6e20024c-2093-48ae-bcd0-29f09eaf5741
14650 [Thread-4] INFO  backtype.storm.daemon.supervisor - Launching worker with assignment #backtype.storm.daemon.supervisor.LocalAssignment{:storm-id "tweetcount-1-1470429273", :executors ([3 3] [5 5] [7 7] [1 1])} for this supervisor e2fdc280-587d-4e71-98df-833f1ca75dc0 on port 1024 with id 745f7d9d-a5d7-4e7c-94b1-a7c90b4c9372
14655 [Thread-6] INFO  backtype.storm.daemon.worker - Launching worker for tweetcount-1-1470429273 on aff4953e-8b07-401a-a269-440087a4032f:1027 with id 6e20024c-2093-48ae-bcd0-29f09eaf5741 and conf {"dev.zookeeper.path" "/tmp/dev-storm-zookeeper", "topology.tick.tuple.freq.secs" nil, "topology.builtin.metrics.bucket.size.secs" 60, "topology.fall.back.on.java.serialization" true, "topology.max.error.report.per.interval" 5, "zmq.linger.millis" 0, "topology.skip.missing.kryo.registrations" true, "storm.messaging.netty.client_worker_threads" 1, "ui.childopts" "-Xmx768m", "storm.zookeeper.session.timeout" 20000, "nimbus.reassign" true, "topology.trident.batch.emit.interval.millis" 50, "storm.messaging.netty.flush.check.interval.ms" 10, "nimbus.monitor.freq.secs" 10, "logviewer.childopts" "-Xmx128m", "java.library.path" "/usr/local/lib:/opt/local/lib:/usr/lib", "topology.executor.send.buffer.size" 1024, "storm.local.dir" "/tmp/c138ef3b-ec9c-4248-a94c-3472cdca60b4", "storm.messaging.netty.buffer_size" 5242880, "supervisor.worker.start.timeout.secs" 120, "topology.enable.message.timeouts" true, "nimbus.cleanup.inbox.freq.secs" 600, "nimbus.inbox.jar.expiration.secs" 3600, "drpc.worker.threads" 64, "storm.meta.serialization.delegate" "backtype.storm.serialization.DefaultSerializationDelegate", "topology.worker.shared.thread.pool.size" 4, "nimbus.host" "localhost", "storm.messaging.netty.min_wait_ms" 100, "storm.zookeeper.port" 2000, "transactional.zookeeper.port" nil, "topology.executor.receive.buffer.size" 1024, "transactional.zookeeper.servers" nil, "storm.zookeeper.root" "/storm", "storm.zookeeper.retry.intervalceiling.millis" 30000, "supervisor.enable" true, "storm.messaging.netty.server_worker_threads" 1, "storm.zookeeper.servers" ["localhost"], "transactional.zookeeper.root" "/transactional", "topology.acker.executors" nil, "topology.transfer.buffer.size" 1024, "topology.worker.childopts" nil, "drpc.queue.size" 128, "worker.childopts" "-Xmx768m", "supervisor.heartbeat.frequency.secs" 5, "topology.error.throttle.interval.secs" 10, "zmq.hwm" 0, "drpc.port" 3772, "supervisor.monitor.frequency.secs" 3, "drpc.childopts" "-Xmx768m", "topology.receiver.buffer.size" 8, "task.heartbeat.frequency.secs" 3, "topology.tasks" nil, "storm.messaging.netty.max_retries" 300, "topology.spout.wait.strategy" "backtype.storm.spout.SleepSpoutWaitStrategy", "nimbus.thrift.max_buffer_size" 1048576, "topology.max.spout.pending" nil, "storm.zookeeper.retry.interval" 1000, "topology.sleep.spout.wait.strategy.time.ms" 1, "nimbus.topology.validator" "backtype.storm.nimbus.DefaultTopologyValidator", "supervisor.slots.ports" (1027 1028 1029), "topology.environment" nil, "topology.debug" false, "nimbus.task.launch.secs" 120, "nimbus.supervisor.timeout.secs" 60, "topology.message.timeout.secs" 30, "task.refresh.poll.secs" 10, "topology.workers" 1, "supervisor.childopts" "-Xmx256m", "nimbus.thrift.port" 6627, "topology.stats.sample.rate" 0.05, "worker.heartbeat.frequency.secs" 1, "topology.tuple.serializer" "backtype.storm.serialization.types.ListDelegateSerializer", "topology.disruptor.wait.strategy" "com.lmax.disruptor.BlockingWaitStrategy", "topology.multilang.serializer" "backtype.storm.multilang.JsonSerializer", "nimbus.task.timeout.secs" 30, "storm.zookeeper.connection.timeout" 15000, "topology.kryo.factory" "backtype.storm.serialization.DefaultKryoFactory", "drpc.invocations.port" 3773, "logviewer.port" 8000, "zmq.threads" 1, "storm.zookeeper.retry.times" 5, "topology.worker.receiver.thread.count" 1, "storm.thrift.transport" "backtype.storm.security.auth.SimpleTransportPlugin", "topology.state.synchronization.timeout.secs" 60, "supervisor.worker.timeout.secs" 30, "nimbus.file.copy.expiration.secs" 600, "storm.messaging.transport" "backtype.storm.messaging.netty.Context", "logviewer.appender.name" "A1", "storm.messaging.netty.max_wait_ms" 1000, "drpc.request.timeout.secs" 600, "storm.local.mode.zmq" false, "ui.port" 8080, "nimbus.childopts" "-Xmx1024m", "storm.cluster.mode" "local", "topology.max.task.parallelism" nil, "storm.messaging.netty.transfer.batch.size" 262144, "topology.classpath" nil}
14655 [Thread-6] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
14656 [Thread-6] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
14656 [Thread-6] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000 sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@636ccda7
14669 [Thread-6-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
14670 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55774
14670 [Thread-6-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
14670 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55774
14702 [Thread-4] INFO  backtype.storm.daemon.worker - Launching worker for tweetcount-1-1470429273 on e2fdc280-587d-4e71-98df-833f1ca75dc0:1024 with id 745f7d9d-a5d7-4e7c-94b1-a7c90b4c9372 and conf {"dev.zookeeper.path" "/tmp/dev-storm-zookeeper", "topology.tick.tuple.freq.secs" nil, "topology.builtin.metrics.bucket.size.secs" 60, "topology.fall.back.on.java.serialization" true, "topology.max.error.report.per.interval" 5, "zmq.linger.millis" 0, "topology.skip.missing.kryo.registrations" true, "storm.messaging.netty.client_worker_threads" 1, "ui.childopts" "-Xmx768m", "storm.zookeeper.session.timeout" 20000, "nimbus.reassign" true, "topology.trident.batch.emit.interval.millis" 50, "storm.messaging.netty.flush.check.interval.ms" 10, "nimbus.monitor.freq.secs" 10, "logviewer.childopts" "-Xmx128m", "java.library.path" "/usr/local/lib:/opt/local/lib:/usr/lib", "topology.executor.send.buffer.size" 1024, "storm.local.dir" "/tmp/02bcc8b4-16b4-4c79-ba17-23480f39535b", "storm.messaging.netty.buffer_size" 5242880, "supervisor.worker.start.timeout.secs" 120, "topology.enable.message.timeouts" true, "nimbus.cleanup.inbox.freq.secs" 600, "nimbus.inbox.jar.expiration.secs" 3600, "drpc.worker.threads" 64, "storm.meta.serialization.delegate" "backtype.storm.serialization.DefaultSerializationDelegate", "topology.worker.shared.thread.pool.size" 4, "nimbus.host" "localhost", "storm.messaging.netty.min_wait_ms" 100, "storm.zookeeper.port" 2000, "transactional.zookeeper.port" nil, "topology.executor.receive.buffer.size" 1024, "transactional.zookeeper.servers" nil, "storm.zookeeper.root" "/storm", "storm.zookeeper.retry.intervalceiling.millis" 30000, "supervisor.enable" true, "storm.messaging.netty.server_worker_threads" 1, "storm.zookeeper.servers" ["localhost"], "transactional.zookeeper.root" "/transactional", "topology.acker.executors" nil, "topology.transfer.buffer.size" 1024, "topology.worker.childopts" nil, "drpc.queue.size" 128, "worker.childopts" "-Xmx768m", "supervisor.heartbeat.frequency.secs" 5, "topology.error.throttle.interval.secs" 10, "zmq.hwm" 0, "drpc.port" 3772, "supervisor.monitor.frequency.secs" 3, "drpc.childopts" "-Xmx768m", "topology.receiver.buffer.size" 8, "task.heartbeat.frequency.secs" 3, "topology.tasks" nil, "storm.messaging.netty.max_retries" 300, "topology.spout.wait.strategy" "backtype.storm.spout.SleepSpoutWaitStrategy", "nimbus.thrift.max_buffer_size" 1048576, "topology.max.spout.pending" nil, "storm.zookeeper.retry.interval" 1000, "topology.sleep.spout.wait.strategy.time.ms" 1, "nimbus.topology.validator" "backtype.storm.nimbus.DefaultTopologyValidator", "supervisor.slots.ports" (1024 1025 1026), "topology.environment" nil, "topology.debug" false, "nimbus.task.launch.secs" 120, "nimbus.supervisor.timeout.secs" 60, "topology.message.timeout.secs" 30, "task.refresh.poll.secs" 10, "topology.workers" 1, "supervisor.childopts" "-Xmx256m", "nimbus.thrift.port" 6627, "topology.stats.sample.rate" 0.05, "worker.heartbeat.frequency.secs" 1, "topology.tuple.serializer" "backtype.storm.serialization.types.ListDelegateSerializer", "topology.disruptor.wait.strategy" "com.lmax.disruptor.BlockingWaitStrategy", "topology.multilang.serializer" "backtype.storm.multilang.JsonSerializer", "nimbus.task.timeout.secs" 30, "storm.zookeeper.connection.timeout" 15000, "topology.kryo.factory" "backtype.storm.serialization.DefaultKryoFactory", "drpc.invocations.port" 3773, "logviewer.port" 8000, "zmq.threads" 1, "storm.zookeeper.retry.times" 5, "topology.worker.receiver.thread.count" 1, "storm.thrift.transport" "backtype.storm.security.auth.SimpleTransportPlugin", "topology.state.synchronization.timeout.secs" 60, "supervisor.worker.timeout.secs" 30, "nimbus.file.copy.expiration.secs" 600, "storm.messaging.transport" "backtype.storm.messaging.netty.Context", "logviewer.appender.name" "A1", "storm.messaging.netty.max_wait_ms" 1000, "drpc.request.timeout.secs" 600, "storm.local.mode.zmq" false, "ui.port" 8080, "nimbus.childopts" "-Xmx1024m", "storm.cluster.mode" "local", "topology.max.task.parallelism" nil, "storm.messaging.netty.transfer.batch.size" 262144, "topology.classpath" nil}
14703 [Thread-4] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
14703 [Thread-4] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
14707 [Thread-6-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c6a0302000a, negotiated timeout = 20000
14707 [Thread-6-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
14707 [Thread-6-EventThread] INFO  backtype.storm.zookeeper - Zookeeper state update: :connected:none
14707 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c6a0302000a with negotiated timeout 20000 for client /127.0.0.1:55774
14709 [ProcessThread(sid:0 cport:-1):] INFO  org.apache.storm.zookeeper.server.PrepRequestProcessor - Processed session termination for sessionid: 0x1565c6a0302000a
14718 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxn - Closed socket connection for client /127.0.0.1:55774 which had sessionid 0x1565c6a0302000a
14718 [Thread-6] INFO  org.apache.storm.zookeeper.ZooKeeper - Session: 0x1565c6a0302000a closed
14718 [Thread-6] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
14719 [Thread-6] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
14719 [Thread-6-EventThread] INFO  org.apache.storm.zookeeper.ClientCnxn - EventThread shut down
14721 [Thread-6] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000/storm sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@49c450f6
14722 [Thread-6-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
14722 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55775
14723 [Thread-6-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
14723 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55775
14734 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c6a0302000b with negotiated timeout 20000 for client /127.0.0.1:55775
14735 [Thread-6-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c6a0302000b, negotiated timeout = 20000
14735 [Thread-6-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
14751 [Thread-4] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000 sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@e854e0
14752 [Thread-4-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
14752 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55776
14753 [Thread-4-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
14753 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55776
14754 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c6a0302000c with negotiated timeout 20000 for client /127.0.0.1:55776
14755 [Thread-4-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c6a0302000c, negotiated timeout = 20000
14755 [Thread-4-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
14755 [Thread-4-EventThread] INFO  backtype.storm.zookeeper - Zookeeper state update: :connected:none
14767 [Thread-6] INFO  backtype.storm.daemon.worker - Reading Assignments.
14785 [ProcessThread(sid:0 cport:-1):] INFO  org.apache.storm.zookeeper.server.PrepRequestProcessor - Processed session termination for sessionid: 0x1565c6a0302000c
14787 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxn - Closed socket connection for client /127.0.0.1:55776 which had sessionid 0x1565c6a0302000c
14787 [Thread-4] INFO  org.apache.storm.zookeeper.ZooKeeper - Session: 0x1565c6a0302000c closed
14787 [Thread-4] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
14788 [Thread-4] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
14788 [Thread-4-EventThread] INFO  org.apache.storm.zookeeper.ClientCnxn - EventThread shut down
14799 [Thread-4] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000/storm sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@21869105
14800 [Thread-4-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
14800 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55777
14800 [Thread-4-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
14801 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55777
14815 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c6a0302000d with negotiated timeout 20000 for client /127.0.0.1:55777
14815 [Thread-4-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c6a0302000d, negotiated timeout = 20000
14816 [Thread-4-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
14937 [Thread-6] INFO  backtype.storm.daemon.worker - Launching receive-thread for aff4953e-8b07-401a-a269-440087a4032f:1027
14959 [Thread-7-worker-receiver-thread-0] INFO  backtype.storm.messaging.loader - Starting receive-thread: [stormId: tweetcount-1-1470429273, port: 1027, thread-id: 0 ]
15721 [Thread-6] INFO  backtype.storm.daemon.executor - Loading executor __acker:[2 2]
15736 [Thread-6] INFO  backtype.storm.daemon.executor - Loaded executor tasks __acker:[2 2]
15752 [Thread-6] INFO  backtype.storm.daemon.executor - Timeouts disabled for executor __acker:[2 2]
15752 [Thread-6] INFO  backtype.storm.daemon.executor - Finished loading executor __acker:[2 2]
15779 [Thread-6] INFO  backtype.storm.daemon.executor - Loading executor counter-bolt:[4 4]
15783 [Thread-6] INFO  backtype.storm.daemon.executor - Loaded executor tasks counter-bolt:[4 4]
15785 [Thread-6] INFO  backtype.storm.daemon.executor - Finished loading executor counter-bolt:[4 4]
15794 [Thread-6] INFO  backtype.storm.daemon.executor - Loading executor parse-bolt:[6 6]
15809 [Thread-6] INFO  backtype.storm.daemon.executor - Loaded executor tasks parse-bolt:[6 6]
15828 [Thread-6] INFO  backtype.storm.daemon.executor - Finished loading executor parse-bolt:[6 6]
15847 [Thread-4] INFO  backtype.storm.daemon.worker - Reading Assignments.
15859 [Thread-6] INFO  backtype.storm.daemon.executor - Loading executor __system:[-1 -1]
15859 [Thread-6] INFO  backtype.storm.daemon.executor - Loaded executor tasks __system:[-1 -1]
15874 [Thread-6] INFO  backtype.storm.daemon.executor - Finished loading executor __system:[-1 -1]
15889 [refresh-active-timer] INFO  backtype.storm.daemon.worker - All connections are ready for worker aff4953e-8b07-401a-a269-440087a4032f:1027 with id 6e20024c-2093-48ae-bcd0-29f09eaf5741
15905 [Thread-6] INFO  backtype.storm.daemon.worker - Worker has topology config {"storm.id" "tweetcount-1-1470429273", "dev.zookeeper.path" "/tmp/dev-storm-zookeeper", "topology.tick.tuple.freq.secs" nil, "topology.builtin.metrics.bucket.size.secs" 60, "topology.fall.back.on.java.serialization" true, "topology.max.error.report.per.interval" 5, "zmq.linger.millis" 0, "topology.skip.missing.kryo.registrations" true, "storm.messaging.netty.client_worker_threads" 1, "ui.childopts" "-Xmx768m", "storm.zookeeper.session.timeout" 20000, "nimbus.reassign" true, "topology.trident.batch.emit.interval.millis" 50, "storm.messaging.netty.flush.check.interval.ms" 10, "nimbus.monitor.freq.secs" 10, "logviewer.childopts" "-Xmx128m", "java.library.path" "/usr/local/lib:/opt/local/lib:/usr/lib", "topology.executor.send.buffer.size" 1024, "storm.local.dir" "/tmp/c138ef3b-ec9c-4248-a94c-3472cdca60b4", "storm.messaging.netty.buffer_size" 5242880, "supervisor.worker.start.timeout.secs" 120, "topology.enable.message.timeouts" true, "nimbus.cleanup.inbox.freq.secs" 600, "nimbus.inbox.jar.expiration.secs" 3600, "drpc.worker.threads" 64, "storm.meta.serialization.delegate" "backtype.storm.serialization.DefaultSerializationDelegate", "topology.worker.shared.thread.pool.size" 4, "nimbus.host" "localhost", "storm.messaging.netty.min_wait_ms" 100, "storm.zookeeper.port" 2000, "transactional.zookeeper.port" nil, "topology.executor.receive.buffer.size" 1024, "transactional.zookeeper.servers" nil, "storm.zookeeper.root" "/storm", "storm.zookeeper.retry.intervalceiling.millis" 30000, "supervisor.enable" true, "storm.messaging.netty.server_worker_threads" 1, "storm.zookeeper.servers" ["localhost"], "transactional.zookeeper.root" "/transactional", "topology.acker.executors" 2, "streamparse.log.path" "/root/tweetcount/logs", "topology.kryo.decorators" (), "topology.name" "tweetcount", "topology.transfer.buffer.size" 1024, "topology.worker.childopts" nil, "drpc.queue.size" 128, "worker.childopts" "-Xmx768m", "supervisor.heartbeat.frequency.secs" 5, "topology.error.throttle.interval.secs" 10, "zmq.hwm" 0, "drpc.port" 3772, "supervisor.monitor.frequency.secs" 3, "drpc.childopts" "-Xmx768m", "topology.receiver.buffer.size" 8, "task.heartbeat.frequency.secs" 3, "topology.tasks" nil, "storm.messaging.netty.max_retries" 300, "topology.spout.wait.strategy" "backtype.storm.spout.SleepSpoutWaitStrategy", "nimbus.thrift.max_buffer_size" 1048576, "topology.max.spout.pending" 5000, "storm.zookeeper.retry.interval" 1000, "topology.sleep.spout.wait.strategy.time.ms" 1, "nimbus.topology.validator" "backtype.storm.nimbus.DefaultTopologyValidator", "supervisor.slots.ports" (1027 1028 1029), "topology.environment" nil, "topology.debug" false, "nimbus.task.launch.secs" 120, "nimbus.supervisor.timeout.secs" 60, "topology.kryo.register" nil, "topology.message.timeout.secs" 60, "task.refresh.poll.secs" 10, "topology.workers" 2, "supervisor.childopts" "-Xmx256m", "nimbus.thrift.port" 6627, "topology.stats.sample.rate" 0.05, "worker.heartbeat.frequency.secs" 1, "topology.tuple.serializer" "backtype.storm.serialization.types.ListDelegateSerializer", "topology.disruptor.wait.strategy" "com.lmax.disruptor.BlockingWaitStrategy", "topology.multilang.serializer" "backtype.storm.multilang.JsonSerializer", "nimbus.task.timeout.secs" 30, "storm.zookeeper.connection.timeout" 15000, "topology.kryo.factory" "backtype.storm.serialization.DefaultKryoFactory", "drpc.invocations.port" 3773, "logviewer.port" 8000, "zmq.threads" 1, "storm.zookeeper.retry.times" 5, "topology.worker.receiver.thread.count" 1, "storm.thrift.transport" "backtype.storm.security.auth.SimpleTransportPlugin", "topology.state.synchronization.timeout.secs" 60, "supervisor.worker.timeout.secs" 30, "nimbus.file.copy.expiration.secs" 600, "storm.messaging.transport" "backtype.storm.messaging.netty.Context", "logviewer.appender.name" "A1", "storm.messaging.netty.max_wait_ms" 1000, "drpc.request.timeout.secs" 600, "storm.local.mode.zmq" false, "ui.port" 8080, "nimbus.childopts" "-Xmx1024m", "storm.cluster.mode" "local", "topology.max.task.parallelism" nil, "storm.messaging.netty.transfer.batch.size" 262144, "topology.classpath" nil, "streamparse.log.level" "debug"}
15905 [Thread-6] INFO  backtype.storm.daemon.worker - Worker 6e20024c-2093-48ae-bcd0-29f09eaf5741 for storm tweetcount-1-1470429273 on aff4953e-8b07-401a-a269-440087a4032f:1027 has finished loading
15971 [Thread-13-parse-bolt] INFO  backtype.storm.daemon.executor - Preparing bolt parse-bolt:(6)
15975 [Thread-9-__acker] INFO  backtype.storm.daemon.executor - Preparing bolt __acker:(2)
15992 [Thread-11-counter-bolt] INFO  backtype.storm.daemon.executor - Preparing bolt counter-bolt:(4)
15975 [Thread-15-__system] INFO  backtype.storm.daemon.executor - Preparing bolt __system:(-1)
16023 [Thread-15-__system] INFO  backtype.storm.daemon.executor - Prepared bolt __system:(-1)
16051 [Thread-13-parse-bolt] INFO  backtype.storm.utils.ShellProcess - Storm multilang serializer: backtype.storm.multilang.JsonSerializer
16112 [Thread-9-__acker] INFO  backtype.storm.daemon.executor - Prepared bolt __acker:(2)
16116 [Thread-11-counter-bolt] INFO  backtype.storm.utils.ShellProcess - Storm multilang serializer: backtype.storm.multilang.JsonSerializer
16138 [Thread-4] INFO  backtype.storm.daemon.worker - Launching receive-thread for e2fdc280-587d-4e71-98df-833f1ca75dc0:1024
16159 [Thread-17-worker-receiver-thread-0] INFO  backtype.storm.messaging.loader - Starting receive-thread: [stormId: tweetcount-1-1470429273, port: 1024, thread-id: 0 ]
16265 [Thread-4] INFO  backtype.storm.daemon.executor - Loading executor counter-bolt:[3 3]
16280 [Thread-4] INFO  backtype.storm.daemon.executor - Loaded executor tasks counter-bolt:[3 3]
16296 [Thread-4] INFO  backtype.storm.daemon.executor - Finished loading executor counter-bolt:[3 3]
16331 [Thread-4] INFO  backtype.storm.daemon.executor - Loading executor parse-bolt:[5 5]
16351 [Thread-4] INFO  backtype.storm.daemon.executor - Loaded executor tasks parse-bolt:[5 5]
16381 [Thread-4] INFO  backtype.storm.daemon.executor - Finished loading executor parse-bolt:[5 5]
16449 [Thread-4] INFO  backtype.storm.daemon.executor - Loading executor tweet-spout:[7 7]
16451 [Thread-4] INFO  backtype.storm.daemon.executor - Loaded executor tasks tweet-spout:[7 7]
16498 [Thread-4] INFO  backtype.storm.daemon.executor - Finished loading executor tweet-spout:[7 7]
16528 [Thread-4] INFO  backtype.storm.daemon.executor - Loading executor __system:[-1 -1]
16529 [Thread-4] INFO  backtype.storm.daemon.executor - Loaded executor tasks __system:[-1 -1]
16550 [Thread-4] INFO  backtype.storm.daemon.executor - Finished loading executor __system:[-1 -1]
16583 [Thread-4] INFO  backtype.storm.daemon.executor - Loading executor __acker:[1 1]
16584 [Thread-4] INFO  backtype.storm.daemon.executor - Loaded executor tasks __acker:[1 1]
16595 [Thread-4] INFO  backtype.storm.daemon.executor - Timeouts disabled for executor __acker:[1 1]
16595 [Thread-4] INFO  backtype.storm.daemon.executor - Finished loading executor __acker:[1 1]
16598 [Thread-4] INFO  backtype.storm.daemon.worker - Worker has topology config {"storm.id" "tweetcount-1-1470429273", "dev.zookeeper.path" "/tmp/dev-storm-zookeeper", "topology.tick.tuple.freq.secs" nil, "topology.builtin.metrics.bucket.size.secs" 60, "topology.fall.back.on.java.serialization" true, "topology.max.error.report.per.interval" 5, "zmq.linger.millis" 0, "topology.skip.missing.kryo.registrations" true, "storm.messaging.netty.client_worker_threads" 1, "ui.childopts" "-Xmx768m", "storm.zookeeper.session.timeout" 20000, "nimbus.reassign" true, "topology.trident.batch.emit.interval.millis" 50, "storm.messaging.netty.flush.check.interval.ms" 10, "nimbus.monitor.freq.secs" 10, "logviewer.childopts" "-Xmx128m", "java.library.path" "/usr/local/lib:/opt/local/lib:/usr/lib", "topology.executor.send.buffer.size" 1024, "storm.local.dir" "/tmp/02bcc8b4-16b4-4c79-ba17-23480f39535b", "storm.messaging.netty.buffer_size" 5242880, "supervisor.worker.start.timeout.secs" 120, "topology.enable.message.timeouts" true, "nimbus.cleanup.inbox.freq.secs" 600, "nimbus.inbox.jar.expiration.secs" 3600, "drpc.worker.threads" 64, "storm.meta.serialization.delegate" "backtype.storm.serialization.DefaultSerializationDelegate", "topology.worker.shared.thread.pool.size" 4, "nimbus.host" "localhost", "storm.messaging.netty.min_wait_ms" 100, "storm.zookeeper.port" 2000, "transactional.zookeeper.port" nil, "topology.executor.receive.buffer.size" 1024, "transactional.zookeeper.servers" nil, "storm.zookeeper.root" "/storm", "storm.zookeeper.retry.intervalceiling.millis" 30000, "supervisor.enable" true, "storm.messaging.netty.server_worker_threads" 1, "storm.zookeeper.servers" ["localhost"], "transactional.zookeeper.root" "/transactional", "topology.acker.executors" 2, "streamparse.log.path" "/root/tweetcount/logs", "topology.kryo.decorators" (), "topology.name" "tweetcount", "topology.transfer.buffer.size" 1024, "topology.worker.childopts" nil, "drpc.queue.size" 128, "worker.childopts" "-Xmx768m", "supervisor.heartbeat.frequency.secs" 5, "topology.error.throttle.interval.secs" 10, "zmq.hwm" 0, "drpc.port" 3772, "supervisor.monitor.frequency.secs" 3, "drpc.childopts" "-Xmx768m", "topology.receiver.buffer.size" 8, "task.heartbeat.frequency.secs" 3, "topology.tasks" nil, "storm.messaging.netty.max_retries" 300, "topology.spout.wait.strategy" "backtype.storm.spout.SleepSpoutWaitStrategy", "nimbus.thrift.max_buffer_size" 1048576, "topology.max.spout.pending" 5000, "storm.zookeeper.retry.interval" 1000, "topology.sleep.spout.wait.strategy.time.ms" 1, "nimbus.topology.validator" "backtype.storm.nimbus.DefaultTopologyValidator", "supervisor.slots.ports" (1024 1025 1026), "topology.environment" nil, "topology.debug" false, "nimbus.task.launch.secs" 120, "nimbus.supervisor.timeout.secs" 60, "topology.kryo.register" nil, "topology.message.timeout.secs" 60, "task.refresh.poll.secs" 10, "topology.workers" 2, "supervisor.childopts" "-Xmx256m", "nimbus.thrift.port" 6627, "topology.stats.sample.rate" 0.05, "worker.heartbeat.frequency.secs" 1, "topology.tuple.serializer" "backtype.storm.serialization.types.ListDelegateSerializer", "topology.disruptor.wait.strategy" "com.lmax.disruptor.BlockingWaitStrategy", "topology.multilang.serializer" "backtype.storm.multilang.JsonSerializer", "nimbus.task.timeout.secs" 30, "storm.zookeeper.connection.timeout" 15000, "topology.kryo.factory" "backtype.storm.serialization.DefaultKryoFactory", "drpc.invocations.port" 3773, "logviewer.port" 8000, "zmq.threads" 1, "storm.zookeeper.retry.times" 5, "topology.worker.receiver.thread.count" 1, "storm.thrift.transport" "backtype.storm.security.auth.SimpleTransportPlugin", "topology.state.synchronization.timeout.secs" 60, "supervisor.worker.timeout.secs" 30, "nimbus.file.copy.expiration.secs" 600, "storm.messaging.transport" "backtype.storm.messaging.netty.Context", "logviewer.appender.name" "A1", "storm.messaging.netty.max_wait_ms" 1000, "drpc.request.timeout.secs" 600, "storm.local.mode.zmq" false, "ui.port" 8080, "nimbus.childopts" "-Xmx1024m", "storm.cluster.mode" "local", "topology.max.task.parallelism" nil, "storm.messaging.netty.transfer.batch.size" 262144, "topology.classpath" nil, "streamparse.log.level" "debug"}
16599 [Thread-4] INFO  backtype.storm.daemon.worker - Worker 745f7d9d-a5d7-4e7c-94b1-a7c90b4c9372 for storm tweetcount-1-1470429273 on e2fdc280-587d-4e71-98df-833f1ca75dc0:1024 has finished loading
16932 [Thread-11-counter-bolt] INFO  backtype.storm.task.ShellBolt - Launched subprocess with pid 4389
16947 [Thread-13-parse-bolt] INFO  backtype.storm.task.ShellBolt - Launched subprocess with pid 4387
16965 [Thread-11-counter-bolt] INFO  backtype.storm.task.ShellBolt - Start checking heartbeat...
16965 [Thread-11-counter-bolt] INFO  backtype.storm.daemon.executor - Prepared bolt counter-bolt:(4)
16979 [Thread-13-parse-bolt] INFO  backtype.storm.task.ShellBolt - Start checking heartbeat...
16979 [Thread-13-parse-bolt] INFO  backtype.storm.daemon.executor - Prepared bolt parse-bolt:(6)
17040 [refresh-active-timer] INFO  backtype.storm.daemon.worker - All connections are ready for worker e2fdc280-587d-4e71-98df-833f1ca75dc0:1024 with id 745f7d9d-a5d7-4e7c-94b1-a7c90b4c9372
17084 [Thread-25-__system] INFO  backtype.storm.daemon.executor - Preparing bolt __system:(-1)
17088 [Thread-25-__system] INFO  backtype.storm.daemon.executor - Prepared bolt __system:(-1)
17120 [Thread-23-tweet-spout] INFO  backtype.storm.daemon.executor - Opening spout tweet-spout:(7)
17121 [Thread-21-parse-bolt] INFO  backtype.storm.daemon.executor - Preparing bolt parse-bolt:(5)
17121 [Thread-21-parse-bolt] INFO  backtype.storm.utils.ShellProcess - Storm multilang serializer: backtype.storm.multilang.JsonSerializer
17122 [Thread-27-__acker] INFO  backtype.storm.daemon.executor - Preparing bolt __acker:(1)
17122 [Thread-27-__acker] INFO  backtype.storm.daemon.executor - Prepared bolt __acker:(1)
17133 [Thread-19-counter-bolt] INFO  backtype.storm.daemon.executor - Preparing bolt counter-bolt:(3)
17133 [Thread-19-counter-bolt] INFO  backtype.storm.utils.ShellProcess - Storm multilang serializer: backtype.storm.multilang.JsonSerializer
17135 [Thread-23-tweet-spout] INFO  backtype.storm.utils.ShellProcess - Storm multilang serializer: backtype.storm.multilang.JsonSerializer
17634 [Thread-21-parse-bolt] INFO  backtype.storm.task.ShellBolt - Launched subprocess with pid 4409
17649 [Thread-21-parse-bolt] INFO  backtype.storm.task.ShellBolt - Start checking heartbeat...
17649 [Thread-21-parse-bolt] INFO  backtype.storm.daemon.executor - Prepared bolt parse-bolt:(5)
17790 [Thread-19-counter-bolt] INFO  backtype.storm.task.ShellBolt - Launched subprocess with pid 4410
17791 [Thread-19-counter-bolt] INFO  backtype.storm.task.ShellBolt - Start checking heartbeat...
17791 [Thread-19-counter-bolt] INFO  backtype.storm.daemon.executor - Prepared bolt counter-bolt:(3)
17938 [Thread-23-tweet-spout] INFO  backtype.storm.spout.ShellSpout - Launched subprocess with pid 4411
17938 [Thread-23-tweet-spout] INFO  backtype.storm.daemon.executor - Opened spout tweet-spout:(7)
17941 [Thread-23-tweet-spout] INFO  backtype.storm.daemon.executor - Activating spout tweet-spout:(7)
17941 [Thread-23-tweet-spout] INFO  backtype.storm.spout.ShellSpout - Start checking heartbeat...
18064 [Thread-23-tweet-spout] INFO  backtype.storm.spout.ShellSpout - ShellLog pid:4411, name:tweet-spout Empty queue exception 
18069 [Thread-23-tweet-spout] ERROR backtype.storm.daemon.executor - 
java.lang.Exception: Shell Process Exception: Python NameError raised
Traceback (most recent call last):
  File "/usr/lib/python2.7/site-packages/streamparse/storm/component.py", line 489, in run
    self._run()
  File "/usr/lib/python2.7/site-packages/streamparse/storm/spout.py", line 150, in _run
    self.next_tuple()
  File "spouts/tweets.py", line 76, in next_tuple
    time.sleep(0.1)
NameError: global name 'time' is not defined

	at backtype.storm.spout.ShellSpout.handleError(ShellSpout.java:212) [storm-core-0.9.5.jar:0.9.5]
	at backtype.storm.spout.ShellSpout.querySubprocess(ShellSpout.java:158) [storm-core-0.9.5.jar:0.9.5]
	at backtype.storm.spout.ShellSpout.nextTuple(ShellSpout.java:91) [storm-core-0.9.5.jar:0.9.5]
	at backtype.storm.daemon.executor$fn__3371$fn__3386$fn__3415.invoke(executor.clj:565) [storm-core-0.9.5.jar:0.9.5]
	at backtype.storm.util$async_loop$fn__460.invoke(util.clj:463) [storm-core-0.9.5.jar:0.9.5]
	at clojure.lang.AFn.run(AFn.java:24) [clojure-1.5.1.jar:na]
	at java.lang.Thread.run(Thread.java:745) [na:1.7.0_79]
18097 [Thread-23-tweet-spout] INFO  tweet-spout - /usr/lib/python2.7/site-packages/requests/packages/urllib3/util/ssl_.py:318: SNIMissingWarning: An HTTPS request has been made, but the SNI (Subject Name Indication) extension to TLS is not available on this platform. This may cause the server to present an incorrect TLS certificate, which can cause validation failures. You can upgrade to a newer version of Python to solve this. For more information, see https://urllib3.readthedocs.org/en/latest/security.html#snimissingwarning.
  SNIMissingWarning
/usr/lib/python2.7/site-packages/requests/packages/urllib3/util/ssl_.py:122: InsecurePlatformWarning: A true SSLContext object is not available. This prevents urllib3 from configuring SSL appropriately and may cause certain SSL connections to fail. You can upgrade to a newer version of Python to solve this. For more information, see https://urllib3.readthedocs.org/en/latest/security.html#insecureplatformwarning.
  InsecurePlatformWarning

20227 [Thread-23-tweet-spout] ERROR backtype.storm.util - Async loop died!
java.lang.RuntimeException: pid:4411, name:tweet-spout exitCode:-1, errorString: 
	at backtype.storm.spout.ShellSpout.querySubprocess(ShellSpout.java:180) ~[storm-core-0.9.5.jar:0.9.5]
	at backtype.storm.spout.ShellSpout.nextTuple(ShellSpout.java:91) ~[storm-core-0.9.5.jar:0.9.5]
	at backtype.storm.daemon.executor$fn__3371$fn__3386$fn__3415.invoke(executor.clj:565) ~[storm-core-0.9.5.jar:0.9.5]
	at backtype.storm.util$async_loop$fn__460.invoke(util.clj:463) ~[storm-core-0.9.5.jar:0.9.5]
	at clojure.lang.AFn.run(AFn.java:24) [clojure-1.5.1.jar:na]
	at java.lang.Thread.run(Thread.java:745) [na:1.7.0_79]
Caused by: java.lang.RuntimeException: backtype.storm.multilang.NoOutputException: Pipe to subprocess seems to be broken! No output read.
Serializer Exception:
Exception in thread Thread-1:
Traceback (most recent call last):
  File "/usr/lib64/python2.7/threading.py", line 551, in __bootstrap_inner
    self.run()
  File "/usr/lib64/python2.7/threading.py", line 504, in run
    self.__target(*self.__args, **self.__kwargs)
  File "/usr/lib/python2.7/site-packages/tweepy/streaming.py", line 294, in _run
    raise exception
Full



	at backtype.storm.utils.ShellProcess.readShellMsg(ShellProcess.java:101) ~[storm-core-0.9.5.jar:0.9.5]
	at backtype.storm.spout.ShellSpout.querySubprocess(ShellSpout.java:145) ~[storm-core-0.9.5.jar:0.9.5]
	... 5 common frames omitted
20227 [Thread-23-tweet-spout] ERROR backtype.storm.daemon.executor - 
java.lang.RuntimeException: pid:4411, name:tweet-spout exitCode:-1, errorString: 
	at backtype.storm.spout.ShellSpout.querySubprocess(ShellSpout.java:180) ~[storm-core-0.9.5.jar:0.9.5]
	at backtype.storm.spout.ShellSpout.nextTuple(ShellSpout.java:91) ~[storm-core-0.9.5.jar:0.9.5]
	at backtype.storm.daemon.executor$fn__3371$fn__3386$fn__3415.invoke(executor.clj:565) ~[storm-core-0.9.5.jar:0.9.5]
	at backtype.storm.util$async_loop$fn__460.invoke(util.clj:463) ~[storm-core-0.9.5.jar:0.9.5]
	at clojure.lang.AFn.run(AFn.java:24) [clojure-1.5.1.jar:na]
	at java.lang.Thread.run(Thread.java:745) [na:1.7.0_79]
Caused by: java.lang.RuntimeException: backtype.storm.multilang.NoOutputException: Pipe to subprocess seems to be broken! No output read.
Serializer Exception:
Exception in thread Thread-1:
Traceback (most recent call last):
  File "/usr/lib64/python2.7/threading.py", line 551, in __bootstrap_inner
    self.run()
  File "/usr/lib64/python2.7/threading.py", line 504, in run
    self.__target(*self.__args, **self.__kwargs)
  File "/usr/lib/python2.7/site-packages/tweepy/streaming.py", line 294, in _run
    raise exception
Full



	at backtype.storm.utils.ShellProcess.readShellMsg(ShellProcess.java:101) ~[storm-core-0.9.5.jar:0.9.5]
	at backtype.storm.spout.ShellSpout.querySubprocess(ShellSpout.java:145) ~[storm-core-0.9.5.jar:0.9.5]
	... 5 common frames omitted
20276 [Thread-23-tweet-spout] ERROR backtype.storm.util - Halting process: ("Worker died")
java.lang.RuntimeException: ("Worker died")
	at backtype.storm.util$exit_process_BANG_.doInvoke(util.clj:325) [storm-core-0.9.5.jar:0.9.5]
	at clojure.lang.RestFn.invoke(RestFn.java:423) [clojure-1.5.1.jar:na]
	at backtype.storm.daemon.worker$fn__4694$fn__4695.invoke(worker.clj:493) [storm-core-0.9.5.jar:0.9.5]
	at backtype.storm.daemon.executor$mk_executor_data$fn__3272$fn__3273.invoke(executor.clj:240) [storm-core-0.9.5.jar:0.9.5]
	at backtype.storm.util$async_loop$fn__460.invoke(util.clj:473) [storm-core-0.9.5.jar:0.9.5]
	at clojure.lang.AFn.run(AFn.java:24) [clojure-1.5.1.jar:na]
	at java.lang.Thread.run(Thread.java:745) [na:1.7.0_79]
Traceback (most recent call last):
  File "/usr/bin/sparse", line 9, in <module>
    load_entry_point('streamparse==2.1.4', 'console_scripts', 'sparse')()
  File "/usr/lib/python2.7/site-packages/streamparse/cli/sparse.py", line 57, in main
    args.func(args)
  File "/usr/lib/python2.7/site-packages/streamparse/cli/run.py", line 81, in main
    debug=args.debug)
  File "/usr/lib/python2.7/site-packages/streamparse/cli/run.py", line 52, in run_local_topology
    run(full_cmd)
  File "/usr/lib/python2.7/site-packages/invoke/__init__.py", line 32, in run
    return Context().run(command, **kwargs)
  File "/usr/lib/python2.7/site-packages/invoke/context.py", line 53, in run
    return runner_class(context=self).run(command, **kwargs)
  File "/usr/lib/python2.7/site-packages/invoke/runners.py", line 363, in run
    raise Failure(result)
invoke.exceptions.Failure: Command execution failure!

Exit code: 1

Stderr:




[root@ip-172-31-4-51 tweetcount]# cd src
[root@ip-172-31-4-51 src]# cd spouts
[root@ip-172-31-4-51 spouts]# ls -
ls: cannot access -: No such file or directory
[root@ip-172-31-4-51 spouts]# ls -l
total 4
-rw-r--r-- 1 root root    0 Jul 11 18:27 __init__.py
-rw-r--r-- 1 root root 2307 Aug  5 20:18 tweets.py
[root@ip-172-31-4-51 spouts]# vi tweets.py 
[root@ip-172-31-4-51 spouts]# cd ..
[root@ip-172-31-4-51 src]# cd ..
[root@ip-172-31-4-51 tweetcount]# cd ..
[root@ip-172-31-4-51 ~]# git clone https://github.com/UC-Berkeley-I-School/w205-summer-16-labs-exercises/tree/master/exercise_2/tweetwordcount
fatal: destination path 'tweetwordcount' already exists and is not an empty directory.
[root@ip-172-31-4-51 ~]# ls -l
total 724
-rw-------  1 root root    287 Sep 22  2015 dans_bash_history.txt
drwxr-xr-x  4 root root   4096 Aug  5 20:01 exercise_2
-rw-r--r--  1 root root  12402 Jul 11 18:07 ez_setup.py
-rw-r--r--  1 root root    763 Aug  5 17:04 finalresults.py
-rw-r--r--  1 root root    446 Aug  5 16:38 histogram.py
drwxr-xr-x 11 root root   4096 May  4  2015 ipython
drwxr-xr-x  5 root root   4096 May  4  2015 pgxl-deployment-tools
-rw-r--r--  1 root root 655364 Jul 11 18:07 setuptools-24.0.2.zip
-rwxr-xr-x  1 root root    221 Sep 22  2015 start-hadoop.sh
-rwxr-xr-x  1 root root    252 Sep 22  2015 start-hadoop.sh~
-rwxr-xr-x  1 root root    209 Sep 22  2015 stop-hadoop.sh
-rwxr-xr-x  1 root root    222 Sep 22  2015 stop-hadoop.sh~
drwxr-xr-x 11 root root   4096 May  4  2015 streamparse
drwxr-xr-x  8 root root   4096 Jul 11 19:33 tweetcount
-rw-r--r--  1 root root   2307 Aug  5 20:17 tweets.py
drwxr-xr-x  8 root root   4096 Aug  5 20:04 tweetwordcount
-rw-r--r--  1 root root    765 Jul 29 01:42 Twittercredentials.py
[root@ip-172-31-4-51 ~]# cd tweetwordcount/
[root@ip-172-31-4-51 tweetwordcount]# ls -l
total 40
drwxr-xr-x 4 root root 4096 Aug  5 20:04 _build
-rw-r--r-- 1 root root  428 Aug  5 20:04 config.json
-rw-r--r-- 1 root root  456 Aug  5 20:04 fabfile.py
drwxr-xr-x 2 root root 4096 Aug  5 20:05 logs
-rw-r--r-- 1 root root  528 Aug  5 20:04 project.clj
-rw-r--r-- 1 root root    0 Aug  5 20:04 README.md
drwxr-xr-x 3 root root 4096 Aug  5 20:04 _resources
drwxr-xr-x 4 root root 4096 Aug  5 20:04 src
-rw-r--r-- 1 root root  456 Aug  5 20:04 tasks.py
drwxr-xr-x 2 root root 4096 Aug  5 20:14 topologies
drwxr-xr-x 2 root root 4096 Aug  5 20:04 virtualenvs
[root@ip-172-31-4-51 tweetwordcount]# cd ..
[root@ip-172-31-4-51 ~]# rm -rf tweetwordcount/
[root@ip-172-31-4-51 ~]# git clone https://github.com/UC-Berkeley-I-School/w205-summer-16-labs-exercises/tree/master/exercise_2/tweetwordcount
Initialized empty Git repository in /root/tweetwordcount/.git/
error: The requested URL returned error: 403 Forbidden while accessing https://github.com/UC-Berkeley-I-School/w205-summer-16-labs-exercises/tree/master/exercise_2/tweetwordcount/info/refs

fatal: HTTP request failed
[root@ip-172-31-4-51 ~]# git clone https://github.com/UC-Berkeley-I-School/w205-summer-16-labs-exercises/tree/master/exercise_2
fatal: destination path 'exercise_2' already exists and is not an empty directory.
[root@ip-172-31-4-51 ~]# rm -rf exercise_2/
[root@ip-172-31-4-51 ~]# git clone https://github.com/UC-Berkeley-I-School/w205-summer-16-labs-exercises/tree/master/exercise_2
Initialized empty Git repository in /root/exercise_2/.git/
error: The requested URL returned error: 403 Forbidden while accessing https://github.com/UC-Berkeley-I-School/w205-summer-16-labs-exercises/tree/master/exercise_2/info/refs

fatal: HTTP request failed
[root@ip-172-31-4-51 ~]# cd ..
[root@ip-172-31-4-51 /]# ls -l
total 112
dr-xr-xr-x   2 root root  4096 Sep 28  2015 bin
dr-xr-xr-x   4 root root  4096 Mar 17  2015 boot
drwxrwxrwx  10 root root  4096 Jul 28 00:02 data
drwxr-xr-x  15 root root  3200 Aug  5 19:51 dev
drwxr-xr-x  88 root root  4096 Aug  5 19:53 etc
drwxr-xr-x   7 root root  4096 Sep 22  2015 home
dr-xr-xr-x  11 root root  4096 May  4  2015 lib
dr-xr-xr-x   9 root root 12288 May  4  2015 lib64
drwx------   2 root root 16384 Mar 17  2015 lost+found
drwxr-xr-x   2 root root  4096 Sep 23  2011 media
drwxr-xr-x   2 root root  4096 Sep 23  2011 mnt
drwxr-xr-x   5 root root  4096 May  4  2015 opt
dr-xr-xr-x  81 root root     0 Aug  5 19:51 proc
dr-xr-x---  15 root root  4096 Aug  5 20:39 root
dr-xr-xr-x   2 root root 12288 Sep 28  2015 sbin
drwxr-xr-x   7 root root     0 Aug  5 19:51 selinux
-rw-r--r--   1 root root     0 Jul 11 19:05 sentences.py
drwxr-xr-x   2 root root  4096 Sep 23  2011 srv
drwxr-xr-x  13 root root     0 Aug  5 19:51 sys
drwxrwxrwt 201 root root 20480 Aug  5 20:34 tmp
drwxr-xr-x  15 root root  4096 May  4  2015 usr
drwxr-xr-x  19 root root  4096 Mar 17  2015 var
[root@ip-172-31-4-51 /]# cd root
[root@ip-172-31-4-51 ~]# ls -l
total 716
-rw-------  1 root root    287 Sep 22  2015 dans_bash_history.txt
-rw-r--r--  1 root root  12402 Jul 11 18:07 ez_setup.py
-rw-r--r--  1 root root    763 Aug  5 17:04 finalresults.py
-rw-r--r--  1 root root    446 Aug  5 16:38 histogram.py
drwxr-xr-x 11 root root   4096 May  4  2015 ipython
drwxr-xr-x  5 root root   4096 May  4  2015 pgxl-deployment-tools
-rw-r--r--  1 root root 655364 Jul 11 18:07 setuptools-24.0.2.zip
-rwxr-xr-x  1 root root    221 Sep 22  2015 start-hadoop.sh
-rwxr-xr-x  1 root root    252 Sep 22  2015 start-hadoop.sh~
-rwxr-xr-x  1 root root    209 Sep 22  2015 stop-hadoop.sh
-rwxr-xr-x  1 root root    222 Sep 22  2015 stop-hadoop.sh~
drwxr-xr-x 11 root root   4096 May  4  2015 streamparse
drwxr-xr-x  8 root root   4096 Jul 11 19:33 tweetcount
-rw-r--r--  1 root root   2307 Aug  5 20:17 tweets.py
-rw-r--r--  1 root root    765 Jul 29 01:42 Twittercredentials.py
[root@ip-172-31-4-51 ~]# git clone https://github.com/mpera/exercise_2/tree/master/tweetwordcount
Initialized empty Git repository in /root/tweetwordcount/.git/
error: The requested URL returned error: 403 Forbidden while accessing https://github.com/mpera/exercise_2/tree/master/tweetwordcount/info/refs

fatal: HTTP request failed
[root@ip-172-31-4-51 ~]# ls -l
total 716
-rw-------  1 root root    287 Sep 22  2015 dans_bash_history.txt
-rw-r--r--  1 root root  12402 Jul 11 18:07 ez_setup.py
-rw-r--r--  1 root root    763 Aug  5 17:04 finalresults.py
-rw-r--r--  1 root root    446 Aug  5 16:38 histogram.py
drwxr-xr-x 11 root root   4096 May  4  2015 ipython
drwxr-xr-x  5 root root   4096 May  4  2015 pgxl-deployment-tools
-rw-r--r--  1 root root 655364 Jul 11 18:07 setuptools-24.0.2.zip
-rwxr-xr-x  1 root root    221 Sep 22  2015 start-hadoop.sh
-rwxr-xr-x  1 root root    252 Sep 22  2015 start-hadoop.sh~
-rwxr-xr-x  1 root root    209 Sep 22  2015 stop-hadoop.sh
-rwxr-xr-x  1 root root    222 Sep 22  2015 stop-hadoop.sh~
drwxr-xr-x 11 root root   4096 May  4  2015 streamparse
drwxr-xr-x  8 root root   4096 Jul 11 19:33 tweetcount
-rw-r--r--  1 root root   2307 Aug  5 20:17 tweets.py
-rw-r--r--  1 root root    765 Jul 29 01:42 Twittercredentials.py
[root@ip-172-31-4-51 ~]# sparse quickstart tweetwordcount

Creating your tweetwordcount streamparse project...
    create    tweetwordcount
    create    tweetwordcount/.gitignore
    create    tweetwordcount/config.json
    create    tweetwordcount/fabfile.py
    create    tweetwordcount/project.clj
    create    tweetwordcount/README.md
    create    tweetwordcount/src
    create    tweetwordcount/src/bolts
    create    tweetwordcount/src/bolts/__init__.py
    create    tweetwordcount/src/bolts/wordcount.py
    create    tweetwordcount/src/spouts
    create    tweetwordcount/src/spouts/__init__.py
    create    tweetwordcount/src/spouts/words.py
    create    tweetwordcount/tasks.py
    create    tweetwordcount/topologies
    create    tweetwordcount/topologies/wordcount.clj
    create    tweetwordcount/virtualenvs
    create    tweetwordcount/virtualenvs/wordcount.txt
Done.

Try running your topology locally with:

	cd tweetwordcount
	sparse run
[root@ip-172-31-4-51 ~]# cd tweetwordcount/
[root@ip-172-31-4-51 tweetwordcount]# cd topologies/
[root@ip-172-31-4-51 topologies]# vi
[root@ip-172-31-4-51 topologies]# ls -l
total 4
-rw-r--r-- 1 root root 469 Aug  5 20:41 wordcount.clj
[root@ip-172-31-4-51 topologies]# touch tweetwordcount.clj
[root@ip-172-31-4-51 topologies]# vi tweetwordcount.clj 
[root@ip-172-31-4-51 topologies]# python -V
Python 2.7.3
[root@ip-172-31-4-51 topologies]# cd ..
[root@ip-172-31-4-51 tweetwordcount]# cd src
[root@ip-172-31-4-51 src]# cd bolts/
[root@ip-172-31-4-51 bolts]# ls -l
total 4
-rw-r--r-- 1 root root   0 Aug  5 20:41 __init__.py
-rw-r--r-- 1 root root 426 Aug  5 20:41 wordcount.py
[root@ip-172-31-4-51 bolts]# touch parse.py
[root@ip-172-31-4-51 bolts]# vi parse.py 
[root@ip-172-31-4-51 bolts]# vi wordcount.py 
[root@ip-172-31-4-51 bolts]# vi wordcount.py 
[root@ip-172-31-4-51 bolts]# cd ..
[root@ip-172-31-4-51 src]# cd spouts/
[root@ip-172-31-4-51 spouts]# ls -l
total 4
-rw-r--r-- 1 root root   0 Aug  5 20:41 __init__.py
-rw-r--r-- 1 root root 396 Aug  5 20:41 words.py
[root@ip-172-31-4-51 spouts]# touch tweets.py
[root@ip-172-31-4-51 spouts]# vi tweets.py 
[root@ip-172-31-4-51 spouts]# cd ..
[root@ip-172-31-4-51 src]# cd ..
[root@ip-172-31-4-51 tweetwordcount]# sparse run
error: Found more than one topology definition file in topologies/. When more than one topology definition file exists, you must explicitly specify the topology by name using the -n or --name flags.
[root@ip-172-31-4-51 tweetwordcount]# cd topologies/
[root@ip-172-31-4-51 topologies]# ls -l
total 8
-rw-r--r-- 1 root root 678 Aug  5 20:42 tweetwordcount.clj
-rw-r--r-- 1 root root 469 Aug  5 20:41 wordcount.clj
[root@ip-172-31-4-51 topologies]# rm wordcount.clj 
[root@ip-172-31-4-51 topologies]# ls -l
total 4
-rw-r--r-- 1 root root 678 Aug  5 20:42 tweetwordcount.clj
[root@ip-172-31-4-51 topologies]# cd ..
[root@ip-172-31-4-51 tweetwordcount]# cd src
[root@ip-172-31-4-51 src]# cd bolts/
[root@ip-172-31-4-51 bolts]# ls -l
total 8
-rw-r--r-- 1 root root    0 Aug  5 20:41 __init__.py
-rw-r--r-- 1 root root 1432 Aug  5 20:43 parse.py
-rw-r--r-- 1 root root  486 Aug  5 20:46 wordcount.py
[root@ip-172-31-4-51 bolts]# cd ..
[root@ip-172-31-4-51 src]# cd spouts/
[root@ip-172-31-4-51 spouts]# ls -l
total 8
-rw-r--r-- 1 root root    0 Aug  5 20:41 __init__.py
-rw-r--r-- 1 root root 2965 Aug  5 20:49 tweets.py
-rw-r--r-- 1 root root  396 Aug  5 20:41 words.py
[root@ip-172-31-4-51 spouts]# rm words.py 
[root@ip-172-31-4-51 spouts]# cd ..
[root@ip-172-31-4-51 src]# cd ..
[root@ip-172-31-4-51 tweetwordcount]# sparse run
Running tweetwordcount topology...
Routing Python logging to /root/tweetwordcount/logs.
Running lein command to run local cluster:
lein run -m streamparse.commands.run/-main topologies/tweetwordcount.clj -t 0 --option 'topology.workers=2' --option 'topology.acker.executors=2' --option 'streamparse.log.path="/root/tweetwordcount/logs"' --option 'streamparse.log.level="debug"'
WARNING: You're currently running as root; probably by accident.
Press control-C to abort or Enter to continue as root.
Set LEIN_ROOT to disable this warning.

3336 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:zookeeper.version=3.4.6-1569965, built on 02/20/2014 09:09 GMT
3380 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:host.name=ip-172-31-4-51.ec2.internal
3380 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:java.version=1.7.0_79
3380 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:java.vendor=Oracle Corporation
3380 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:java.home=/opt/jdk1.7.0_79/jre
3380 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:java.class.path=/root/tweetwordcount/test:/root/tweetwordcount/topologies:/root/tweetwordcount/dev-resources:/root/tweetwordcount/_resources:/root/tweetwordcount/_build/classes:/root/.m2/repository/ch/qos/logback/logback-classic/1.0.13/logback-classic-1.0.13.jar:/root/.m2/repository/org/clojure/tools.macro/0.1.0/tools.macro-0.1.0.jar:/root/.m2/repository/ring/ring-core/1.1.5/ring-core-1.1.5.jar:/root/.m2/repository/hiccup/hiccup/0.3.6/hiccup-0.3.6.jar:/root/.m2/repository/ring/ring-servlet/0.3.11/ring-servlet-0.3.11.jar:/root/.m2/repository/com/googlecode/json-simple/json-simple/1.1/json-simple-1.1.jar:/root/.m2/repository/org/clojure/math.numeric-tower/0.0.1/math.numeric-tower-0.0.1.jar:/root/.m2/repository/clj-time/clj-time/0.4.1/clj-time-0.4.1.jar:/root/.m2/repository/org/objenesis/objenesis/1.2/objenesis-1.2.jar:/root/.m2/repository/com/twitter/chill-java/0.3.5/chill-java-0.3.5.jar:/root/.m2/repository/com/parsely/streamparse/0.0.4-SNAPSHOT/streamparse-0.0.4-SNAPSHOT.jar:/root/.m2/repository/ring/ring-jetty-adapter/0.3.11/ring-jetty-adapter-0.3.11.jar:/root/.m2/repository/jline/jline/2.11/jline-2.11.jar:/root/.m2/repository/clj-stacktrace/clj-stacktrace/0.2.2/clj-stacktrace-0.2.2.jar:/root/.m2/repository/org/clojure/tools.nrepl/0.2.12/tools.nrepl-0.2.12.jar:/root/.m2/repository/org/slf4j/slf4j-api/1.7.5/slf4j-api-1.7.5.jar:/root/.m2/repository/ring/ring-devel/0.3.11/ring-devel-0.3.11.jar:/root/.m2/repository/org/mortbay/jetty/jetty-util/6.1.26/jetty-util-6.1.26.jar:/root/.m2/repository/javax/servlet/servlet-api/2.5/servlet-api-2.5.jar:/root/.m2/repository/clojure-complete/clojure-complete/0.2.4/clojure-complete-0.2.4.jar:/root/.m2/repository/org/yaml/snakeyaml/1.11/snakeyaml-1.11.jar:/root/.m2/repository/ch/qos/logback/logback-core/1.0.13/logback-core-1.0.13.jar:/root/.m2/repository/commons-lang/commons-lang/2.5/commons-lang-2.5.jar:/root/.m2/repository/org/mortbay/jetty/jetty/6.1.26/jetty-6.1.26.jar:/root/.m2/repository/joda-time/joda-time/2.0/joda-time-2.0.jar:/root/.m2/repository/commons-io/commons-io/2.4/commons-io-2.4.jar:/root/.m2/repository/commons-logging/commons-logging/1.1.3/commons-logging-1.1.3.jar:/root/.m2/repository/com/esotericsoftware/kryo/kryo/2.21/kryo-2.21.jar:/root/.m2/repository/com/esotericsoftware/minlog/minlog/1.2/minlog-1.2.jar:/root/.m2/repository/org/apache/storm/storm-core/0.9.5/storm-core-0.9.5.jar:/root/.m2/repository/compojure/compojure/1.1.3/compojure-1.1.3.jar:/root/.m2/repository/com/esotericsoftware/reflectasm/reflectasm/1.07/reflectasm-1.07-shaded.jar:/root/.m2/repository/com/twitter/carbonite/1.4.0/carbonite-1.4.0.jar:/root/.m2/repository/commons-codec/commons-codec/1.6/commons-codec-1.6.jar:/root/.m2/repository/commons-fileupload/commons-fileupload/1.2.1/commons-fileupload-1.2.1.jar:/root/.m2/repository/org/clojure/data.json/0.2.6/data.json-0.2.6.jar:/root/.m2/repository/org/slf4j/log4j-over-slf4j/1.6.6/log4j-over-slf4j-1.6.6.jar:/root/.m2/repository/org/jgrapht/jgrapht-core/0.9.0/jgrapht-core-0.9.0.jar:/root/.m2/repository/org/clojure/clojure/1.5.1/clojure-1.5.1.jar:/root/.m2/repository/org/clojure/tools.logging/0.2.3/tools.logging-0.2.3.jar:/root/.m2/repository/org/ow2/asm/asm/4.0/asm-4.0.jar:/root/.m2/repository/clout/clout/1.0.1/clout-1.0.1.jar:/root/.m2/repository/org/apache/commons/commons-exec/1.1/commons-exec-1.1.jar:/root/.m2/repository/com/googlecode/disruptor/disruptor/2.10.1/disruptor-2.10.1.jar:/root/.m2/repository/org/clojure/core.incubator/0.1.0/core.incubator-0.1.0.jar:/root/.m2/repository/org/clojure/tools.cli/0.2.4/tools.cli-0.2.4.jar
3381 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:java.library.path=/usr/java/packages/lib/amd64:/usr/lib64:/lib64:/lib:/usr/lib
3381 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:java.io.tmpdir=/tmp
3381 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:java.compiler=<NA>
3381 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:os.name=Linux
3381 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:os.arch=amd64
3381 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:os.version=2.6.32-504.12.2.el6.centos.plus.x86_64
3381 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:user.name=root
3382 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:user.home=/root
3382 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:user.dir=/root/tweetwordcount
3423 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:zookeeper.version=3.4.6-1569965, built on 02/20/2014 09:09 GMT
3423 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:host.name=ip-172-31-4-51.ec2.internal
3423 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:java.version=1.7.0_79
3423 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:java.vendor=Oracle Corporation
3423 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:java.home=/opt/jdk1.7.0_79/jre
3423 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:java.class.path=/root/tweetwordcount/test:/root/tweetwordcount/topologies:/root/tweetwordcount/dev-resources:/root/tweetwordcount/_resources:/root/tweetwordcount/_build/classes:/root/.m2/repository/ch/qos/logback/logback-classic/1.0.13/logback-classic-1.0.13.jar:/root/.m2/repository/org/clojure/tools.macro/0.1.0/tools.macro-0.1.0.jar:/root/.m2/repository/ring/ring-core/1.1.5/ring-core-1.1.5.jar:/root/.m2/repository/hiccup/hiccup/0.3.6/hiccup-0.3.6.jar:/root/.m2/repository/ring/ring-servlet/0.3.11/ring-servlet-0.3.11.jar:/root/.m2/repository/com/googlecode/json-simple/json-simple/1.1/json-simple-1.1.jar:/root/.m2/repository/org/clojure/math.numeric-tower/0.0.1/math.numeric-tower-0.0.1.jar:/root/.m2/repository/clj-time/clj-time/0.4.1/clj-time-0.4.1.jar:/root/.m2/repository/org/objenesis/objenesis/1.2/objenesis-1.2.jar:/root/.m2/repository/com/twitter/chill-java/0.3.5/chill-java-0.3.5.jar:/root/.m2/repository/com/parsely/streamparse/0.0.4-SNAPSHOT/streamparse-0.0.4-SNAPSHOT.jar:/root/.m2/repository/ring/ring-jetty-adapter/0.3.11/ring-jetty-adapter-0.3.11.jar:/root/.m2/repository/jline/jline/2.11/jline-2.11.jar:/root/.m2/repository/clj-stacktrace/clj-stacktrace/0.2.2/clj-stacktrace-0.2.2.jar:/root/.m2/repository/org/clojure/tools.nrepl/0.2.12/tools.nrepl-0.2.12.jar:/root/.m2/repository/org/slf4j/slf4j-api/1.7.5/slf4j-api-1.7.5.jar:/root/.m2/repository/ring/ring-devel/0.3.11/ring-devel-0.3.11.jar:/root/.m2/repository/org/mortbay/jetty/jetty-util/6.1.26/jetty-util-6.1.26.jar:/root/.m2/repository/javax/servlet/servlet-api/2.5/servlet-api-2.5.jar:/root/.m2/repository/clojure-complete/clojure-complete/0.2.4/clojure-complete-0.2.4.jar:/root/.m2/repository/org/yaml/snakeyaml/1.11/snakeyaml-1.11.jar:/root/.m2/repository/ch/qos/logback/logback-core/1.0.13/logback-core-1.0.13.jar:/root/.m2/repository/commons-lang/commons-lang/2.5/commons-lang-2.5.jar:/root/.m2/repository/org/mortbay/jetty/jetty/6.1.26/jetty-6.1.26.jar:/root/.m2/repository/joda-time/joda-time/2.0/joda-time-2.0.jar:/root/.m2/repository/commons-io/commons-io/2.4/commons-io-2.4.jar:/root/.m2/repository/commons-logging/commons-logging/1.1.3/commons-logging-1.1.3.jar:/root/.m2/repository/com/esotericsoftware/kryo/kryo/2.21/kryo-2.21.jar:/root/.m2/repository/com/esotericsoftware/minlog/minlog/1.2/minlog-1.2.jar:/root/.m2/repository/org/apache/storm/storm-core/0.9.5/storm-core-0.9.5.jar:/root/.m2/repository/compojure/compojure/1.1.3/compojure-1.1.3.jar:/root/.m2/repository/com/esotericsoftware/reflectasm/reflectasm/1.07/reflectasm-1.07-shaded.jar:/root/.m2/repository/com/twitter/carbonite/1.4.0/carbonite-1.4.0.jar:/root/.m2/repository/commons-codec/commons-codec/1.6/commons-codec-1.6.jar:/root/.m2/repository/commons-fileupload/commons-fileupload/1.2.1/commons-fileupload-1.2.1.jar:/root/.m2/repository/org/clojure/data.json/0.2.6/data.json-0.2.6.jar:/root/.m2/repository/org/slf4j/log4j-over-slf4j/1.6.6/log4j-over-slf4j-1.6.6.jar:/root/.m2/repository/org/jgrapht/jgrapht-core/0.9.0/jgrapht-core-0.9.0.jar:/root/.m2/repository/org/clojure/clojure/1.5.1/clojure-1.5.1.jar:/root/.m2/repository/org/clojure/tools.logging/0.2.3/tools.logging-0.2.3.jar:/root/.m2/repository/org/ow2/asm/asm/4.0/asm-4.0.jar:/root/.m2/repository/clout/clout/1.0.1/clout-1.0.1.jar:/root/.m2/repository/org/apache/commons/commons-exec/1.1/commons-exec-1.1.jar:/root/.m2/repository/com/googlecode/disruptor/disruptor/2.10.1/disruptor-2.10.1.jar:/root/.m2/repository/org/clojure/core.incubator/0.1.0/core.incubator-0.1.0.jar:/root/.m2/repository/org/clojure/tools.cli/0.2.4/tools.cli-0.2.4.jar
3423 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:java.library.path=/usr/java/packages/lib/amd64:/usr/lib64:/lib64:/lib:/usr/lib
3423 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:java.io.tmpdir=/tmp
3423 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:java.compiler=<NA>
3423 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:os.name=Linux
3423 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:os.arch=amd64
3423 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:os.version=2.6.32-504.12.2.el6.centos.plus.x86_64
3423 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:user.name=root
3424 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:user.home=/root
3424 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:user.dir=/root/tweetwordcount
5566 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Created server with tickTime 2000 minSessionTimeout 4000 maxSessionTimeout 40000 datadir /tmp/b9c9a4ae-ae78-4f02-ae8f-e4f4c052e1c5/version-2 snapdir /tmp/b9c9a4ae-ae78-4f02-ae8f-e4f4c052e1c5/version-2
5581 [main] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - binding to port 0.0.0.0/0.0.0.0:2000
5585 [main] INFO  backtype.storm.zookeeper - Starting inprocess zookeeper at port 2000 and dir /tmp/b9c9a4ae-ae78-4f02-ae8f-e4f4c052e1c5
6038 [main] INFO  backtype.storm.daemon.nimbus - Starting Nimbus with conf {"dev.zookeeper.path" "/tmp/dev-storm-zookeeper", "topology.tick.tuple.freq.secs" nil, "topology.builtin.metrics.bucket.size.secs" 60, "topology.fall.back.on.java.serialization" true, "topology.max.error.report.per.interval" 5, "zmq.linger.millis" 0, "topology.skip.missing.kryo.registrations" true, "storm.messaging.netty.client_worker_threads" 1, "ui.childopts" "-Xmx768m", "storm.zookeeper.session.timeout" 20000, "nimbus.reassign" true, "topology.trident.batch.emit.interval.millis" 50, "storm.messaging.netty.flush.check.interval.ms" 10, "nimbus.monitor.freq.secs" 10, "logviewer.childopts" "-Xmx128m", "java.library.path" "/usr/local/lib:/opt/local/lib:/usr/lib", "topology.executor.send.buffer.size" 1024, "storm.local.dir" "/tmp/bab9b120-6c75-49bf-b46d-04960ba73a7b", "storm.messaging.netty.buffer_size" 5242880, "supervisor.worker.start.timeout.secs" 120, "topology.enable.message.timeouts" true, "nimbus.cleanup.inbox.freq.secs" 600, "nimbus.inbox.jar.expiration.secs" 3600, "drpc.worker.threads" 64, "storm.meta.serialization.delegate" "backtype.storm.serialization.DefaultSerializationDelegate", "topology.worker.shared.thread.pool.size" 4, "nimbus.host" "localhost", "storm.messaging.netty.min_wait_ms" 100, "storm.zookeeper.port" 2000, "transactional.zookeeper.port" nil, "topology.executor.receive.buffer.size" 1024, "transactional.zookeeper.servers" nil, "storm.zookeeper.root" "/storm", "storm.zookeeper.retry.intervalceiling.millis" 30000, "supervisor.enable" true, "storm.messaging.netty.server_worker_threads" 1, "storm.zookeeper.servers" ["localhost"], "transactional.zookeeper.root" "/transactional", "topology.acker.executors" nil, "topology.transfer.buffer.size" 1024, "topology.worker.childopts" nil, "drpc.queue.size" 128, "worker.childopts" "-Xmx768m", "supervisor.heartbeat.frequency.secs" 5, "topology.error.throttle.interval.secs" 10, "zmq.hwm" 0, "drpc.port" 3772, "supervisor.monitor.frequency.secs" 3, "drpc.childopts" "-Xmx768m", "topology.receiver.buffer.size" 8, "task.heartbeat.frequency.secs" 3, "topology.tasks" nil, "storm.messaging.netty.max_retries" 300, "topology.spout.wait.strategy" "backtype.storm.spout.SleepSpoutWaitStrategy", "nimbus.thrift.max_buffer_size" 1048576, "topology.max.spout.pending" nil, "storm.zookeeper.retry.interval" 1000, "topology.sleep.spout.wait.strategy.time.ms" 1, "nimbus.topology.validator" "backtype.storm.nimbus.DefaultTopologyValidator", "supervisor.slots.ports" [6700 6701 6702 6703], "topology.environment" nil, "topology.debug" false, "nimbus.task.launch.secs" 120, "nimbus.supervisor.timeout.secs" 60, "topology.message.timeout.secs" 30, "task.refresh.poll.secs" 10, "topology.workers" 1, "supervisor.childopts" "-Xmx256m", "nimbus.thrift.port" 6627, "topology.stats.sample.rate" 0.05, "worker.heartbeat.frequency.secs" 1, "topology.tuple.serializer" "backtype.storm.serialization.types.ListDelegateSerializer", "topology.disruptor.wait.strategy" "com.lmax.disruptor.BlockingWaitStrategy", "topology.multilang.serializer" "backtype.storm.multilang.JsonSerializer", "nimbus.task.timeout.secs" 30, "storm.zookeeper.connection.timeout" 15000, "topology.kryo.factory" "backtype.storm.serialization.DefaultKryoFactory", "drpc.invocations.port" 3773, "logviewer.port" 8000, "zmq.threads" 1, "storm.zookeeper.retry.times" 5, "topology.worker.receiver.thread.count" 1, "storm.thrift.transport" "backtype.storm.security.auth.SimpleTransportPlugin", "topology.state.synchronization.timeout.secs" 60, "supervisor.worker.timeout.secs" 30, "nimbus.file.copy.expiration.secs" 600, "storm.messaging.transport" "backtype.storm.messaging.netty.Context", "logviewer.appender.name" "A1", "storm.messaging.netty.max_wait_ms" 1000, "drpc.request.timeout.secs" 600, "storm.local.mode.zmq" false, "ui.port" 8080, "nimbus.childopts" "-Xmx1024m", "storm.cluster.mode" "local", "topology.max.task.parallelism" nil, "storm.messaging.netty.transfer.batch.size" 262144, "topology.classpath" nil}
6066 [main] INFO  backtype.storm.daemon.nimbus - Using default scheduler
6100 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
6410 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
6414 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000 sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@5ae856b5
6463 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
6474 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55885
6476 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
6489 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55885
6492 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.persistence.FileTxnLog - Creating new log file: log.1
6514 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c7957460000, negotiated timeout = 20000
6516 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
6518 [main-EventThread] INFO  backtype.storm.zookeeper - Zookeeper state update: :connected:none
6518 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c7957460000 with negotiated timeout 20000 for client /127.0.0.1:55885
7559 [ProcessThread(sid:0 cport:-1):] INFO  org.apache.storm.zookeeper.server.PrepRequestProcessor - Processed session termination for sessionid: 0x1565c7957460000
7574 [main-EventThread] INFO  org.apache.storm.zookeeper.ClientCnxn - EventThread shut down
7575 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Session: 0x1565c7957460000 closed
7576 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
7577 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
7577 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000/storm sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@57b0dd3a
7580 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxn - Closed socket connection for client /127.0.0.1:55885 which had sessionid 0x1565c7957460000
7590 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
7590 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
7591 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55886
7591 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55886
7593 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c7957460001 with negotiated timeout 20000 for client /127.0.0.1:55886
7593 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c7957460001, negotiated timeout = 20000
7593 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
7658 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
7658 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
7659 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000 sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@2efd9584
7660 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
7660 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55887
7660 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
7661 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55887
7663 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c7957460002 with negotiated timeout 20000 for client /127.0.0.1:55887
7671 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c7957460002, negotiated timeout = 20000
7672 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
7672 [main-EventThread] INFO  backtype.storm.zookeeper - Zookeeper state update: :connected:none
7677 [ProcessThread(sid:0 cport:-1):] INFO  org.apache.storm.zookeeper.server.PrepRequestProcessor - Processed session termination for sessionid: 0x1565c7957460002
7679 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxn - Closed socket connection for client /127.0.0.1:55887 which had sessionid 0x1565c7957460002
7679 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Session: 0x1565c7957460002 closed
7679 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
7680 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
7680 [main-EventThread] INFO  org.apache.storm.zookeeper.ClientCnxn - EventThread shut down
7680 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000/storm sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@5332efbc
7681 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
7681 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55888
7682 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
7682 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55888
7704 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
7705 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
7705 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000 sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@1c3dd15c
7706 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
7706 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55889
7707 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
7707 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55889
7710 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c7957460003 with negotiated timeout 20000 for client /127.0.0.1:55888
7710 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c7957460003, negotiated timeout = 20000
7710 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
7711 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c7957460004 with negotiated timeout 20000 for client /127.0.0.1:55889
7712 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c7957460004, negotiated timeout = 20000
7712 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
7712 [main-EventThread] INFO  backtype.storm.zookeeper - Zookeeper state update: :connected:none
8715 [ProcessThread(sid:0 cport:-1):] INFO  org.apache.storm.zookeeper.server.PrepRequestProcessor - Processed session termination for sessionid: 0x1565c7957460004
8725 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Session: 0x1565c7957460004 closed
8725 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
8725 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
8725 [main-EventThread] INFO  org.apache.storm.zookeeper.ClientCnxn - EventThread shut down
8726 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000/storm sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@498f5e80
8727 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
8727 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
8729 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxn - Closed socket connection for client /127.0.0.1:55889 which had sessionid 0x1565c7957460004
8729 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55890
8729 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55890
8731 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c7957460005 with negotiated timeout 20000 for client /127.0.0.1:55890
8731 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c7957460005, negotiated timeout = 20000
8731 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
8810 [main] INFO  backtype.storm.daemon.supervisor - Starting Supervisor with conf {"dev.zookeeper.path" "/tmp/dev-storm-zookeeper", "topology.tick.tuple.freq.secs" nil, "topology.builtin.metrics.bucket.size.secs" 60, "topology.fall.back.on.java.serialization" true, "topology.max.error.report.per.interval" 5, "zmq.linger.millis" 0, "topology.skip.missing.kryo.registrations" true, "storm.messaging.netty.client_worker_threads" 1, "ui.childopts" "-Xmx768m", "storm.zookeeper.session.timeout" 20000, "nimbus.reassign" true, "topology.trident.batch.emit.interval.millis" 50, "storm.messaging.netty.flush.check.interval.ms" 10, "nimbus.monitor.freq.secs" 10, "logviewer.childopts" "-Xmx128m", "java.library.path" "/usr/local/lib:/opt/local/lib:/usr/lib", "topology.executor.send.buffer.size" 1024, "storm.local.dir" "/tmp/d7d5b030-64e7-40e0-8b25-e30c68efbed6", "storm.messaging.netty.buffer_size" 5242880, "supervisor.worker.start.timeout.secs" 120, "topology.enable.message.timeouts" true, "nimbus.cleanup.inbox.freq.secs" 600, "nimbus.inbox.jar.expiration.secs" 3600, "drpc.worker.threads" 64, "storm.meta.serialization.delegate" "backtype.storm.serialization.DefaultSerializationDelegate", "topology.worker.shared.thread.pool.size" 4, "nimbus.host" "localhost", "storm.messaging.netty.min_wait_ms" 100, "storm.zookeeper.port" 2000, "transactional.zookeeper.port" nil, "topology.executor.receive.buffer.size" 1024, "transactional.zookeeper.servers" nil, "storm.zookeeper.root" "/storm", "storm.zookeeper.retry.intervalceiling.millis" 30000, "supervisor.enable" true, "storm.messaging.netty.server_worker_threads" 1, "storm.zookeeper.servers" ["localhost"], "transactional.zookeeper.root" "/transactional", "topology.acker.executors" nil, "topology.transfer.buffer.size" 1024, "topology.worker.childopts" nil, "drpc.queue.size" 128, "worker.childopts" "-Xmx768m", "supervisor.heartbeat.frequency.secs" 5, "topology.error.throttle.interval.secs" 10, "zmq.hwm" 0, "drpc.port" 3772, "supervisor.monitor.frequency.secs" 3, "drpc.childopts" "-Xmx768m", "topology.receiver.buffer.size" 8, "task.heartbeat.frequency.secs" 3, "topology.tasks" nil, "storm.messaging.netty.max_retries" 300, "topology.spout.wait.strategy" "backtype.storm.spout.SleepSpoutWaitStrategy", "nimbus.thrift.max_buffer_size" 1048576, "topology.max.spout.pending" nil, "storm.zookeeper.retry.interval" 1000, "topology.sleep.spout.wait.strategy.time.ms" 1, "nimbus.topology.validator" "backtype.storm.nimbus.DefaultTopologyValidator", "supervisor.slots.ports" (1024 1025 1026), "topology.environment" nil, "topology.debug" false, "nimbus.task.launch.secs" 120, "nimbus.supervisor.timeout.secs" 60, "topology.message.timeout.secs" 30, "task.refresh.poll.secs" 10, "topology.workers" 1, "supervisor.childopts" "-Xmx256m", "nimbus.thrift.port" 6627, "topology.stats.sample.rate" 0.05, "worker.heartbeat.frequency.secs" 1, "topology.tuple.serializer" "backtype.storm.serialization.types.ListDelegateSerializer", "topology.disruptor.wait.strategy" "com.lmax.disruptor.BlockingWaitStrategy", "topology.multilang.serializer" "backtype.storm.multilang.JsonSerializer", "nimbus.task.timeout.secs" 30, "storm.zookeeper.connection.timeout" 15000, "topology.kryo.factory" "backtype.storm.serialization.DefaultKryoFactory", "drpc.invocations.port" 3773, "logviewer.port" 8000, "zmq.threads" 1, "storm.zookeeper.retry.times" 5, "topology.worker.receiver.thread.count" 1, "storm.thrift.transport" "backtype.storm.security.auth.SimpleTransportPlugin", "topology.state.synchronization.timeout.secs" 60, "supervisor.worker.timeout.secs" 30, "nimbus.file.copy.expiration.secs" 600, "storm.messaging.transport" "backtype.storm.messaging.netty.Context", "logviewer.appender.name" "A1", "storm.messaging.netty.max_wait_ms" 1000, "drpc.request.timeout.secs" 600, "storm.local.mode.zmq" false, "ui.port" 8080, "nimbus.childopts" "-Xmx1024m", "storm.cluster.mode" "local", "topology.max.task.parallelism" nil, "storm.messaging.netty.transfer.batch.size" 262144, "topology.classpath" nil}
8834 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
8834 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
8835 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000 sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@783b0edf
8837 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
8838 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55891
8838 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
8839 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55891
8840 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c7957460006 with negotiated timeout 20000 for client /127.0.0.1:55891
8841 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c7957460006, negotiated timeout = 20000
8841 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
8841 [main-EventThread] INFO  backtype.storm.zookeeper - Zookeeper state update: :connected:none
9852 [ProcessThread(sid:0 cport:-1):] INFO  org.apache.storm.zookeeper.server.PrepRequestProcessor - Processed session termination for sessionid: 0x1565c7957460006
9854 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxn - Closed socket connection for client /127.0.0.1:55891 which had sessionid 0x1565c7957460006
9855 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Session: 0x1565c7957460006 closed
9855 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
9855 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
9856 [main-EventThread] INFO  org.apache.storm.zookeeper.ClientCnxn - EventThread shut down
9856 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000/storm sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@e45a028
9857 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
9857 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55892
9858 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
9858 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55892
9861 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c7957460007 with negotiated timeout 20000 for client /127.0.0.1:55892
9862 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c7957460007, negotiated timeout = 20000
9862 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
10903 [main] INFO  backtype.storm.daemon.supervisor - Starting supervisor with id d2d121eb-b70e-48c0-a093-0afea2a31298 at host ip-172-31-4-51.ec2.internal
10921 [main] INFO  backtype.storm.daemon.supervisor - Starting Supervisor with conf {"dev.zookeeper.path" "/tmp/dev-storm-zookeeper", "topology.tick.tuple.freq.secs" nil, "topology.builtin.metrics.bucket.size.secs" 60, "topology.fall.back.on.java.serialization" true, "topology.max.error.report.per.interval" 5, "zmq.linger.millis" 0, "topology.skip.missing.kryo.registrations" true, "storm.messaging.netty.client_worker_threads" 1, "ui.childopts" "-Xmx768m", "storm.zookeeper.session.timeout" 20000, "nimbus.reassign" true, "topology.trident.batch.emit.interval.millis" 50, "storm.messaging.netty.flush.check.interval.ms" 10, "nimbus.monitor.freq.secs" 10, "logviewer.childopts" "-Xmx128m", "java.library.path" "/usr/local/lib:/opt/local/lib:/usr/lib", "topology.executor.send.buffer.size" 1024, "storm.local.dir" "/tmp/74c71777-9f78-4862-bac5-015a1be71f28", "storm.messaging.netty.buffer_size" 5242880, "supervisor.worker.start.timeout.secs" 120, "topology.enable.message.timeouts" true, "nimbus.cleanup.inbox.freq.secs" 600, "nimbus.inbox.jar.expiration.secs" 3600, "drpc.worker.threads" 64, "storm.meta.serialization.delegate" "backtype.storm.serialization.DefaultSerializationDelegate", "topology.worker.shared.thread.pool.size" 4, "nimbus.host" "localhost", "storm.messaging.netty.min_wait_ms" 100, "storm.zookeeper.port" 2000, "transactional.zookeeper.port" nil, "topology.executor.receive.buffer.size" 1024, "transactional.zookeeper.servers" nil, "storm.zookeeper.root" "/storm", "storm.zookeeper.retry.intervalceiling.millis" 30000, "supervisor.enable" true, "storm.messaging.netty.server_worker_threads" 1, "storm.zookeeper.servers" ["localhost"], "transactional.zookeeper.root" "/transactional", "topology.acker.executors" nil, "topology.transfer.buffer.size" 1024, "topology.worker.childopts" nil, "drpc.queue.size" 128, "worker.childopts" "-Xmx768m", "supervisor.heartbeat.frequency.secs" 5, "topology.error.throttle.interval.secs" 10, "zmq.hwm" 0, "drpc.port" 3772, "supervisor.monitor.frequency.secs" 3, "drpc.childopts" "-Xmx768m", "topology.receiver.buffer.size" 8, "task.heartbeat.frequency.secs" 3, "topology.tasks" nil, "storm.messaging.netty.max_retries" 300, "topology.spout.wait.strategy" "backtype.storm.spout.SleepSpoutWaitStrategy", "nimbus.thrift.max_buffer_size" 1048576, "topology.max.spout.pending" nil, "storm.zookeeper.retry.interval" 1000, "topology.sleep.spout.wait.strategy.time.ms" 1, "nimbus.topology.validator" "backtype.storm.nimbus.DefaultTopologyValidator", "supervisor.slots.ports" (1027 1028 1029), "topology.environment" nil, "topology.debug" false, "nimbus.task.launch.secs" 120, "nimbus.supervisor.timeout.secs" 60, "topology.message.timeout.secs" 30, "task.refresh.poll.secs" 10, "topology.workers" 1, "supervisor.childopts" "-Xmx256m", "nimbus.thrift.port" 6627, "topology.stats.sample.rate" 0.05, "worker.heartbeat.frequency.secs" 1, "topology.tuple.serializer" "backtype.storm.serialization.types.ListDelegateSerializer", "topology.disruptor.wait.strategy" "com.lmax.disruptor.BlockingWaitStrategy", "topology.multilang.serializer" "backtype.storm.multilang.JsonSerializer", "nimbus.task.timeout.secs" 30, "storm.zookeeper.connection.timeout" 15000, "topology.kryo.factory" "backtype.storm.serialization.DefaultKryoFactory", "drpc.invocations.port" 3773, "logviewer.port" 8000, "zmq.threads" 1, "storm.zookeeper.retry.times" 5, "topology.worker.receiver.thread.count" 1, "storm.thrift.transport" "backtype.storm.security.auth.SimpleTransportPlugin", "topology.state.synchronization.timeout.secs" 60, "supervisor.worker.timeout.secs" 30, "nimbus.file.copy.expiration.secs" 600, "storm.messaging.transport" "backtype.storm.messaging.netty.Context", "logviewer.appender.name" "A1", "storm.messaging.netty.max_wait_ms" 1000, "drpc.request.timeout.secs" 600, "storm.local.mode.zmq" false, "ui.port" 8080, "nimbus.childopts" "-Xmx1024m", "storm.cluster.mode" "local", "topology.max.task.parallelism" nil, "storm.messaging.netty.transfer.batch.size" 262144, "topology.classpath" nil}
10929 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
10930 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
10932 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000 sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@3e872ac6
10942 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
10942 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55893
10943 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
10943 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55893
10945 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c7957460008 with negotiated timeout 20000 for client /127.0.0.1:55893
10945 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c7957460008, negotiated timeout = 20000
10945 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
10946 [main-EventThread] INFO  backtype.storm.zookeeper - Zookeeper state update: :connected:none
11948 [ProcessThread(sid:0 cport:-1):] INFO  org.apache.storm.zookeeper.server.PrepRequestProcessor - Processed session termination for sessionid: 0x1565c7957460008
11949 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxn - Closed socket connection for client /127.0.0.1:55893 which had sessionid 0x1565c7957460008
11950 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Session: 0x1565c7957460008 closed
11950 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
11950 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
11951 [main-EventThread] INFO  org.apache.storm.zookeeper.ClientCnxn - EventThread shut down
11951 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000/storm sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@2db6b6ca
11952 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
11952 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55894
11954 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
11954 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55894
11957 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c7957460009 with negotiated timeout 20000 for client /127.0.0.1:55894
11958 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c7957460009, negotiated timeout = 20000
11958 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
12972 [main] INFO  backtype.storm.daemon.supervisor - Starting supervisor with id 13e19c64-b528-44ec-8d83-c3b6ab74cc09 at host ip-172-31-4-51.ec2.internal
13093 [main] INFO  backtype.storm.daemon.nimbus - Received topology submission for tweetwordcount with conf {"storm.id" "tweetwordcount-1-1470430278", "topology.acker.executors" 2, "streamparse.log.path" "/root/tweetwordcount/logs", "topology.kryo.decorators" (), "topology.name" "tweetwordcount", "topology.max.spout.pending" 5000, "topology.debug" false, "topology.kryo.register" nil, "topology.message.timeout.secs" 60, "topology.workers" 2, "topology.max.task.parallelism" nil, "streamparse.log.level" "debug"}
13161 [main] INFO  backtype.storm.daemon.nimbus - Activating tweetwordcount: tweetwordcount-1-1470430278
13391 [main] INFO  backtype.storm.scheduler.EvenScheduler - Available slots: (["d2d121eb-b70e-48c0-a093-0afea2a31298" 1024] ["d2d121eb-b70e-48c0-a093-0afea2a31298" 1025] ["d2d121eb-b70e-48c0-a093-0afea2a31298" 1026] ["13e19c64-b528-44ec-8d83-c3b6ab74cc09" 1027] ["13e19c64-b528-44ec-8d83-c3b6ab74cc09" 1028] ["13e19c64-b528-44ec-8d83-c3b6ab74cc09" 1029])
13539 [main] INFO  backtype.storm.daemon.nimbus - Setting new assignment for topology id tweetwordcount-1-1470430278: #backtype.storm.daemon.common.Assignment{:master-code-dir "/tmp/bab9b120-6c75-49bf-b46d-04960ba73a7b/nimbus/stormdist/tweetwordcount-1-1470430278", :node->host {"13e19c64-b528-44ec-8d83-c3b6ab74cc09" "ip-172-31-4-51.ec2.internal", "d2d121eb-b70e-48c0-a093-0afea2a31298" "ip-172-31-4-51.ec2.internal"}, :executor->node+port {[3 3] ["d2d121eb-b70e-48c0-a093-0afea2a31298" 1024], [6 6] ["13e19c64-b528-44ec-8d83-c3b6ab74cc09" 1027], [5 5] ["d2d121eb-b70e-48c0-a093-0afea2a31298" 1024], [4 4] ["13e19c64-b528-44ec-8d83-c3b6ab74cc09" 1027], [7 7] ["d2d121eb-b70e-48c0-a093-0afea2a31298" 1024], [2 2] ["13e19c64-b528-44ec-8d83-c3b6ab74cc09" 1027], [1 1] ["d2d121eb-b70e-48c0-a093-0afea2a31298" 1024]}, :executor->start-time-secs {[7 7] 1470430279, [5 5] 1470430279, [3 3] 1470430279, [1 1] 1470430279, [6 6] 1470430279, [4 4] 1470430279, [2 2] 1470430279}}
15286 [Thread-5] INFO  backtype.storm.daemon.supervisor - Copying resources at file:/root/tweetwordcount/_resources/resources to /tmp/74c71777-9f78-4862-bac5-015a1be71f28/supervisor/stormdist/tweetwordcount-1-1470430278/resources
15320 [Thread-3] INFO  backtype.storm.daemon.supervisor - Copying resources at file:/root/tweetwordcount/_resources/resources to /tmp/d7d5b030-64e7-40e0-8b25-e30c68efbed6/supervisor/stormdist/tweetwordcount-1-1470430278/resources
15432 [Thread-4] INFO  backtype.storm.daemon.supervisor - Launching worker with assignment #backtype.storm.daemon.supervisor.LocalAssignment{:storm-id "tweetwordcount-1-1470430278", :executors ([3 3] [5 5] [7 7] [1 1])} for this supervisor d2d121eb-b70e-48c0-a093-0afea2a31298 on port 1024 with id 734172ee-877c-4cb2-acc9-4a667273e90d
15449 [Thread-4] INFO  backtype.storm.daemon.worker - Launching worker for tweetwordcount-1-1470430278 on d2d121eb-b70e-48c0-a093-0afea2a31298:1024 with id 734172ee-877c-4cb2-acc9-4a667273e90d and conf {"dev.zookeeper.path" "/tmp/dev-storm-zookeeper", "topology.tick.tuple.freq.secs" nil, "topology.builtin.metrics.bucket.size.secs" 60, "topology.fall.back.on.java.serialization" true, "topology.max.error.report.per.interval" 5, "zmq.linger.millis" 0, "topology.skip.missing.kryo.registrations" true, "storm.messaging.netty.client_worker_threads" 1, "ui.childopts" "-Xmx768m", "storm.zookeeper.session.timeout" 20000, "nimbus.reassign" true, "topology.trident.batch.emit.interval.millis" 50, "storm.messaging.netty.flush.check.interval.ms" 10, "nimbus.monitor.freq.secs" 10, "logviewer.childopts" "-Xmx128m", "java.library.path" "/usr/local/lib:/opt/local/lib:/usr/lib", "topology.executor.send.buffer.size" 1024, "storm.local.dir" "/tmp/d7d5b030-64e7-40e0-8b25-e30c68efbed6", "storm.messaging.netty.buffer_size" 5242880, "supervisor.worker.start.timeout.secs" 120, "topology.enable.message.timeouts" true, "nimbus.cleanup.inbox.freq.secs" 600, "nimbus.inbox.jar.expiration.secs" 3600, "drpc.worker.threads" 64, "storm.meta.serialization.delegate" "backtype.storm.serialization.DefaultSerializationDelegate", "topology.worker.shared.thread.pool.size" 4, "nimbus.host" "localhost", "storm.messaging.netty.min_wait_ms" 100, "storm.zookeeper.port" 2000, "transactional.zookeeper.port" nil, "topology.executor.receive.buffer.size" 1024, "transactional.zookeeper.servers" nil, "storm.zookeeper.root" "/storm", "storm.zookeeper.retry.intervalceiling.millis" 30000, "supervisor.enable" true, "storm.messaging.netty.server_worker_threads" 1, "storm.zookeeper.servers" ["localhost"], "transactional.zookeeper.root" "/transactional", "topology.acker.executors" nil, "topology.transfer.buffer.size" 1024, "topology.worker.childopts" nil, "drpc.queue.size" 128, "worker.childopts" "-Xmx768m", "supervisor.heartbeat.frequency.secs" 5, "topology.error.throttle.interval.secs" 10, "zmq.hwm" 0, "drpc.port" 3772, "supervisor.monitor.frequency.secs" 3, "drpc.childopts" "-Xmx768m", "topology.receiver.buffer.size" 8, "task.heartbeat.frequency.secs" 3, "topology.tasks" nil, "storm.messaging.netty.max_retries" 300, "topology.spout.wait.strategy" "backtype.storm.spout.SleepSpoutWaitStrategy", "nimbus.thrift.max_buffer_size" 1048576, "topology.max.spout.pending" nil, "storm.zookeeper.retry.interval" 1000, "topology.sleep.spout.wait.strategy.time.ms" 1, "nimbus.topology.validator" "backtype.storm.nimbus.DefaultTopologyValidator", "supervisor.slots.ports" (1024 1025 1026), "topology.environment" nil, "topology.debug" false, "nimbus.task.launch.secs" 120, "nimbus.supervisor.timeout.secs" 60, "topology.message.timeout.secs" 30, "task.refresh.poll.secs" 10, "topology.workers" 1, "supervisor.childopts" "-Xmx256m", "nimbus.thrift.port" 6627, "topology.stats.sample.rate" 0.05, "worker.heartbeat.frequency.secs" 1, "topology.tuple.serializer" "backtype.storm.serialization.types.ListDelegateSerializer", "topology.disruptor.wait.strategy" "com.lmax.disruptor.BlockingWaitStrategy", "topology.multilang.serializer" "backtype.storm.multilang.JsonSerializer", "nimbus.task.timeout.secs" 30, "storm.zookeeper.connection.timeout" 15000, "topology.kryo.factory" "backtype.storm.serialization.DefaultKryoFactory", "drpc.invocations.port" 3773, "logviewer.port" 8000, "zmq.threads" 1, "storm.zookeeper.retry.times" 5, "topology.worker.receiver.thread.count" 1, "storm.thrift.transport" "backtype.storm.security.auth.SimpleTransportPlugin", "topology.state.synchronization.timeout.secs" 60, "supervisor.worker.timeout.secs" 30, "nimbus.file.copy.expiration.secs" 600, "storm.messaging.transport" "backtype.storm.messaging.netty.Context", "logviewer.appender.name" "A1", "storm.messaging.netty.max_wait_ms" 1000, "drpc.request.timeout.secs" 600, "storm.local.mode.zmq" false, "ui.port" 8080, "nimbus.childopts" "-Xmx1024m", "storm.cluster.mode" "local", "topology.max.task.parallelism" nil, "storm.messaging.netty.transfer.batch.size" 262144, "topology.classpath" nil}
15479 [Thread-6] INFO  backtype.storm.daemon.supervisor - Launching worker with assignment #backtype.storm.daemon.supervisor.LocalAssignment{:storm-id "tweetwordcount-1-1470430278", :executors ([6 6] [4 4] [2 2])} for this supervisor 13e19c64-b528-44ec-8d83-c3b6ab74cc09 on port 1027 with id d9ea2815-1279-4fc8-bbfe-cb97f5d46858
15491 [Thread-6] INFO  backtype.storm.daemon.worker - Launching worker for tweetwordcount-1-1470430278 on 13e19c64-b528-44ec-8d83-c3b6ab74cc09:1027 with id d9ea2815-1279-4fc8-bbfe-cb97f5d46858 and conf {"dev.zookeeper.path" "/tmp/dev-storm-zookeeper", "topology.tick.tuple.freq.secs" nil, "topology.builtin.metrics.bucket.size.secs" 60, "topology.fall.back.on.java.serialization" true, "topology.max.error.report.per.interval" 5, "zmq.linger.millis" 0, "topology.skip.missing.kryo.registrations" true, "storm.messaging.netty.client_worker_threads" 1, "ui.childopts" "-Xmx768m", "storm.zookeeper.session.timeout" 20000, "nimbus.reassign" true, "topology.trident.batch.emit.interval.millis" 50, "storm.messaging.netty.flush.check.interval.ms" 10, "nimbus.monitor.freq.secs" 10, "logviewer.childopts" "-Xmx128m", "java.library.path" "/usr/local/lib:/opt/local/lib:/usr/lib", "topology.executor.send.buffer.size" 1024, "storm.local.dir" "/tmp/74c71777-9f78-4862-bac5-015a1be71f28", "storm.messaging.netty.buffer_size" 5242880, "supervisor.worker.start.timeout.secs" 120, "topology.enable.message.timeouts" true, "nimbus.cleanup.inbox.freq.secs" 600, "nimbus.inbox.jar.expiration.secs" 3600, "drpc.worker.threads" 64, "storm.meta.serialization.delegate" "backtype.storm.serialization.DefaultSerializationDelegate", "topology.worker.shared.thread.pool.size" 4, "nimbus.host" "localhost", "storm.messaging.netty.min_wait_ms" 100, "storm.zookeeper.port" 2000, "transactional.zookeeper.port" nil, "topology.executor.receive.buffer.size" 1024, "transactional.zookeeper.servers" nil, "storm.zookeeper.root" "/storm", "storm.zookeeper.retry.intervalceiling.millis" 30000, "supervisor.enable" true, "storm.messaging.netty.server_worker_threads" 1, "storm.zookeeper.servers" ["localhost"], "transactional.zookeeper.root" "/transactional", "topology.acker.executors" nil, "topology.transfer.buffer.size" 1024, "topology.worker.childopts" nil, "drpc.queue.size" 128, "worker.childopts" "-Xmx768m", "supervisor.heartbeat.frequency.secs" 5, "topology.error.throttle.interval.secs" 10, "zmq.hwm" 0, "drpc.port" 3772, "supervisor.monitor.frequency.secs" 3, "drpc.childopts" "-Xmx768m", "topology.receiver.buffer.size" 8, "task.heartbeat.frequency.secs" 3, "topology.tasks" nil, "storm.messaging.netty.max_retries" 300, "topology.spout.wait.strategy" "backtype.storm.spout.SleepSpoutWaitStrategy", "nimbus.thrift.max_buffer_size" 1048576, "topology.max.spout.pending" nil, "storm.zookeeper.retry.interval" 1000, "topology.sleep.spout.wait.strategy.time.ms" 1, "nimbus.topology.validator" "backtype.storm.nimbus.DefaultTopologyValidator", "supervisor.slots.ports" (1027 1028 1029), "topology.environment" nil, "topology.debug" false, "nimbus.task.launch.secs" 120, "nimbus.supervisor.timeout.secs" 60, "topology.message.timeout.secs" 30, "task.refresh.poll.secs" 10, "topology.workers" 1, "supervisor.childopts" "-Xmx256m", "nimbus.thrift.port" 6627, "topology.stats.sample.rate" 0.05, "worker.heartbeat.frequency.secs" 1, "topology.tuple.serializer" "backtype.storm.serialization.types.ListDelegateSerializer", "topology.disruptor.wait.strategy" "com.lmax.disruptor.BlockingWaitStrategy", "topology.multilang.serializer" "backtype.storm.multilang.JsonSerializer", "nimbus.task.timeout.secs" 30, "storm.zookeeper.connection.timeout" 15000, "topology.kryo.factory" "backtype.storm.serialization.DefaultKryoFactory", "drpc.invocations.port" 3773, "logviewer.port" 8000, "zmq.threads" 1, "storm.zookeeper.retry.times" 5, "topology.worker.receiver.thread.count" 1, "storm.thrift.transport" "backtype.storm.security.auth.SimpleTransportPlugin", "topology.state.synchronization.timeout.secs" 60, "supervisor.worker.timeout.secs" 30, "nimbus.file.copy.expiration.secs" 600, "storm.messaging.transport" "backtype.storm.messaging.netty.Context", "logviewer.appender.name" "A1", "storm.messaging.netty.max_wait_ms" 1000, "drpc.request.timeout.secs" 600, "storm.local.mode.zmq" false, "ui.port" 8080, "nimbus.childopts" "-Xmx1024m", "storm.cluster.mode" "local", "topology.max.task.parallelism" nil, "storm.messaging.netty.transfer.batch.size" 262144, "topology.classpath" nil}
15491 [Thread-6] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
15491 [Thread-6] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
15492 [Thread-6] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000 sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@2c3ba12f
15493 [Thread-6-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
15493 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55896
15494 [Thread-6-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
15494 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55896
15496 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c795746000a with negotiated timeout 20000 for client /127.0.0.1:55896
15496 [Thread-6-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c795746000a, negotiated timeout = 20000
15496 [Thread-4] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
15497 [Thread-4] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
15499 [Thread-4] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000 sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@4ce2fbd3
15500 [Thread-4-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
15501 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55897
15501 [Thread-4-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
15501 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55897
15514 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c795746000b with negotiated timeout 20000 for client /127.0.0.1:55897
15515 [Thread-4-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c795746000b, negotiated timeout = 20000
15515 [Thread-4-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
15516 [Thread-6-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
15516 [Thread-6-EventThread] INFO  backtype.storm.zookeeper - Zookeeper state update: :connected:none
15519 [ProcessThread(sid:0 cport:-1):] INFO  org.apache.storm.zookeeper.server.PrepRequestProcessor - Processed session termination for sessionid: 0x1565c795746000a
15520 [Thread-4-EventThread] INFO  backtype.storm.zookeeper - Zookeeper state update: :connected:none
15521 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxn - Closed socket connection for client /127.0.0.1:55896 which had sessionid 0x1565c795746000a
15521 [Thread-6] INFO  org.apache.storm.zookeeper.ZooKeeper - Session: 0x1565c795746000a closed
15521 [Thread-6] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
15521 [Thread-6] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
15522 [Thread-6-EventThread] INFO  org.apache.storm.zookeeper.ClientCnxn - EventThread shut down
15532 [Thread-6] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000/storm sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@6c48d3e2
15535 [Thread-6-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
15536 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55898
15536 [Thread-6-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
15536 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55898
15538 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c795746000c with negotiated timeout 20000 for client /127.0.0.1:55898
15547 [Thread-6-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c795746000c, negotiated timeout = 20000
15549 [Thread-6-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
16521 [ProcessThread(sid:0 cport:-1):] INFO  org.apache.storm.zookeeper.server.PrepRequestProcessor - Processed session termination for sessionid: 0x1565c795746000b
16522 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxn - Closed socket connection for client /127.0.0.1:55897 which had sessionid 0x1565c795746000b
16523 [Thread-4] INFO  org.apache.storm.zookeeper.ZooKeeper - Session: 0x1565c795746000b closed
16523 [Thread-4] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
16523 [Thread-4] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
16524 [Thread-4-EventThread] INFO  org.apache.storm.zookeeper.ClientCnxn - EventThread shut down
16525 [Thread-4] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000/storm sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@69ed8d93
16526 [Thread-4-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
16539 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:55899
16540 [Thread-4-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
16540 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:55899
16543 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x1565c795746000d with negotiated timeout 20000 for client /127.0.0.1:55899
16543 [Thread-4-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x1565c795746000d, negotiated timeout = 20000
16544 [Thread-4-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
16557 [Thread-6] INFO  backtype.storm.daemon.worker - Reading Assignments.
16669 [Thread-6] INFO  backtype.storm.daemon.worker - Launching receive-thread for 13e19c64-b528-44ec-8d83-c3b6ab74cc09:1027
16690 [Thread-7-worker-receiver-thread-0] INFO  backtype.storm.messaging.loader - Starting receive-thread: [stormId: tweetwordcount-1-1470430278, port: 1027, thread-id: 0 ]
17343 [Thread-6] INFO  backtype.storm.daemon.executor - Loading executor __acker:[2 2]
17360 [Thread-6] INFO  backtype.storm.daemon.executor - Loaded executor tasks __acker:[2 2]
17412 [Thread-6] INFO  backtype.storm.daemon.executor - Timeouts disabled for executor __acker:[2 2]
17413 [Thread-6] INFO  backtype.storm.daemon.executor - Finished loading executor __acker:[2 2]
17445 [Thread-6] INFO  backtype.storm.daemon.executor - Loading executor count-bolt:[4 4]
17468 [Thread-6] INFO  backtype.storm.daemon.executor - Loaded executor tasks count-bolt:[4 4]
17470 [Thread-6] INFO  backtype.storm.daemon.executor - Finished loading executor count-bolt:[4 4]
17485 [Thread-6] INFO  backtype.storm.daemon.executor - Loading executor parse-bolt:[6 6]
17493 [Thread-6] INFO  backtype.storm.daemon.executor - Loaded executor tasks parse-bolt:[6 6]
17508 [Thread-6] INFO  backtype.storm.daemon.executor - Finished loading executor parse-bolt:[6 6]
17514 [Thread-6] INFO  backtype.storm.daemon.executor - Loading executor __system:[-1 -1]
17515 [Thread-6] INFO  backtype.storm.daemon.executor - Loaded executor tasks __system:[-1 -1]
17517 [Thread-6] INFO  backtype.storm.daemon.executor - Finished loading executor __system:[-1 -1]
17535 [Thread-6] INFO  backtype.storm.daemon.worker - Worker has topology config {"storm.id" "tweetwordcount-1-1470430278", "dev.zookeeper.path" "/tmp/dev-storm-zookeeper", "topology.tick.tuple.freq.secs" nil, "topology.builtin.metrics.bucket.size.secs" 60, "topology.fall.back.on.java.serialization" true, "topology.max.error.report.per.interval" 5, "zmq.linger.millis" 0, "topology.skip.missing.kryo.registrations" true, "storm.messaging.netty.client_worker_threads" 1, "ui.childopts" "-Xmx768m", "storm.zookeeper.session.timeout" 20000, "nimbus.reassign" true, "topology.trident.batch.emit.interval.millis" 50, "storm.messaging.netty.flush.check.interval.ms" 10, "nimbus.monitor.freq.secs" 10, "logviewer.childopts" "-Xmx128m", "java.library.path" "/usr/local/lib:/opt/local/lib:/usr/lib", "topology.executor.send.buffer.size" 1024, "storm.local.dir" "/tmp/74c71777-9f78-4862-bac5-015a1be71f28", "storm.messaging.netty.buffer_size" 5242880, "supervisor.worker.start.timeout.secs" 120, "topology.enable.message.timeouts" true, "nimbus.cleanup.inbox.freq.secs" 600, "nimbus.inbox.jar.expiration.secs" 3600, "drpc.worker.threads" 64, "storm.meta.serialization.delegate" "backtype.storm.serialization.DefaultSerializationDelegate", "topology.worker.shared.thread.pool.size" 4, "nimbus.host" "localhost", "storm.messaging.netty.min_wait_ms" 100, "storm.zookeeper.port" 2000, "transactional.zookeeper.port" nil, "topology.executor.receive.buffer.size" 1024, "transactional.zookeeper.servers" nil, "storm.zookeeper.root" "/storm", "storm.zookeeper.retry.intervalceiling.millis" 30000, "supervisor.enable" true, "storm.messaging.netty.server_worker_threads" 1, "storm.zookeeper.servers" ["localhost"], "transactional.zookeeper.root" "/transactional", "topology.acker.executors" 2, "streamparse.log.path" "/root/tweetwordcount/logs", "topology.kryo.decorators" (), "topology.name" "tweetwordcount", "topology.transfer.buffer.size" 1024, "topology.worker.childopts" nil, "drpc.queue.size" 128, "worker.childopts" "-Xmx768m", "supervisor.heartbeat.frequency.secs" 5, "topology.error.throttle.interval.secs" 10, "zmq.hwm" 0, "drpc.port" 3772, "supervisor.monitor.frequency.secs" 3, "drpc.childopts" "-Xmx768m", "topology.receiver.buffer.size" 8, "task.heartbeat.frequency.secs" 3, "topology.tasks" nil, "storm.messaging.netty.max_retries" 300, "topology.spout.wait.strategy" "backtype.storm.spout.SleepSpoutWaitStrategy", "nimbus.thrift.max_buffer_size" 1048576, "topology.max.spout.pending" 5000, "storm.zookeeper.retry.interval" 1000, "topology.sleep.spout.wait.strategy.time.ms" 1, "nimbus.topology.validator" "backtype.storm.nimbus.DefaultTopologyValidator", "supervisor.slots.ports" (1027 1028 1029), "topology.environment" nil, "topology.debug" false, "nimbus.task.launch.secs" 120, "nimbus.supervisor.timeout.secs" 60, "topology.kryo.register" nil, "topology.message.timeout.secs" 60, "task.refresh.poll.secs" 10, "topology.workers" 2, "supervisor.childopts" "-Xmx256m", "nimbus.thrift.port" 6627, "topology.stats.sample.rate" 0.05, "worker.heartbeat.frequency.secs" 1, "topology.tuple.serializer" "backtype.storm.serialization.types.ListDelegateSerializer", "topology.disruptor.wait.strategy" "com.lmax.disruptor.BlockingWaitStrategy", "topology.multilang.serializer" "backtype.storm.multilang.JsonSerializer", "nimbus.task.timeout.secs" 30, "storm.zookeeper.connection.timeout" 15000, "topology.kryo.factory" "backtype.storm.serialization.DefaultKryoFactory", "drpc.invocations.port" 3773, "logviewer.port" 8000, "zmq.threads" 1, "storm.zookeeper.retry.times" 5, "topology.worker.receiver.thread.count" 1, "storm.thrift.transport" "backtype.storm.security.auth.SimpleTransportPlugin", "topology.state.synchronization.timeout.secs" 60, "supervisor.worker.timeout.secs" 30, "nimbus.file.copy.expiration.secs" 600, "storm.messaging.transport" "backtype.storm.messaging.netty.Context", "logviewer.appender.name" "A1", "storm.messaging.netty.max_wait_ms" 1000, "drpc.request.timeout.secs" 600, "storm.local.mode.zmq" false, "ui.port" 8080, "nimbus.childopts" "-Xmx1024m", "storm.cluster.mode" "local", "topology.max.task.parallelism" nil, "storm.messaging.netty.transfer.batch.size" 262144, "topology.classpath" nil, "streamparse.log.level" "debug"}
17536 [Thread-6] INFO  backtype.storm.daemon.worker - Worker d9ea2815-1279-4fc8-bbfe-cb97f5d46858 for storm tweetwordcount-1-1470430278 on 13e19c64-b528-44ec-8d83-c3b6ab74cc09:1027 has finished loading
17554 [Thread-4] INFO  backtype.storm.daemon.worker - Reading Assignments.
17605 [Thread-4] INFO  backtype.storm.daemon.worker - Launching receive-thread for d2d121eb-b70e-48c0-a093-0afea2a31298:1024
17623 [refresh-active-timer] INFO  backtype.storm.daemon.worker - All connections are ready for worker 13e19c64-b528-44ec-8d83-c3b6ab74cc09:1027 with id d9ea2815-1279-4fc8-bbfe-cb97f5d46858
17646 [Thread-17-worker-receiver-thread-0] INFO  backtype.storm.messaging.loader - Starting receive-thread: [stormId: tweetwordcount-1-1470430278, port: 1024, thread-id: 0 ]
17743 [Thread-11-count-bolt] INFO  backtype.storm.daemon.executor - Preparing bolt count-bolt:(4)
17744 [Thread-9-__acker] INFO  backtype.storm.daemon.executor - Preparing bolt __acker:(2)
17765 [Thread-9-__acker] INFO  backtype.storm.daemon.executor - Prepared bolt __acker:(2)
17799 [Thread-13-parse-bolt] INFO  backtype.storm.daemon.executor - Preparing bolt parse-bolt:(6)
17766 [Thread-4] INFO  backtype.storm.daemon.executor - Loading executor count-bolt:[3 3]
17807 [Thread-15-__system] INFO  backtype.storm.daemon.executor - Preparing bolt __system:(-1)
17859 [Thread-11-count-bolt] INFO  backtype.storm.utils.ShellProcess - Storm multilang serializer: backtype.storm.multilang.JsonSerializer
17891 [Thread-15-__system] INFO  backtype.storm.daemon.executor - Prepared bolt __system:(-1)
17905 [Thread-4] INFO  backtype.storm.daemon.executor - Loaded executor tasks count-bolt:[3 3]
17907 [Thread-13-parse-bolt] INFO  backtype.storm.utils.ShellProcess - Storm multilang serializer: backtype.storm.multilang.JsonSerializer
17911 [Thread-4] INFO  backtype.storm.daemon.executor - Finished loading executor count-bolt:[3 3]
17927 [Thread-4] INFO  backtype.storm.daemon.executor - Loading executor parse-bolt:[5 5]
17987 [Thread-4] INFO  backtype.storm.daemon.executor - Loaded executor tasks parse-bolt:[5 5]
17991 [Thread-4] INFO  backtype.storm.daemon.executor - Finished loading executor parse-bolt:[5 5]
18066 [Thread-4] INFO  backtype.storm.daemon.executor - Loading executor tweet-spout:[7 7]
18099 [Thread-4] INFO  backtype.storm.daemon.executor - Loaded executor tasks tweet-spout:[7 7]
18122 [Thread-4] INFO  backtype.storm.daemon.executor - Finished loading executor tweet-spout:[7 7]
18271 [Thread-4] INFO  backtype.storm.daemon.executor - Loading executor __system:[-1 -1]
18281 [Thread-4] INFO  backtype.storm.daemon.executor - Loaded executor tasks __system:[-1 -1]
18289 [Thread-4] INFO  backtype.storm.daemon.executor - Finished loading executor __system:[-1 -1]
18346 [Thread-4] INFO  backtype.storm.daemon.executor - Loading executor __acker:[1 1]
18347 [Thread-4] INFO  backtype.storm.daemon.executor - Loaded executor tasks __acker:[1 1]
18352 [Thread-4] INFO  backtype.storm.daemon.executor - Timeouts disabled for executor __acker:[1 1]
18395 [Thread-4] INFO  backtype.storm.daemon.executor - Finished loading executor __acker:[1 1]
18402 [Thread-4] INFO  backtype.storm.daemon.worker - Worker has topology config {"storm.id" "tweetwordcount-1-1470430278", "dev.zookeeper.path" "/tmp/dev-storm-zookeeper", "topology.tick.tuple.freq.secs" nil, "topology.builtin.metrics.bucket.size.secs" 60, "topology.fall.back.on.java.serialization" true, "topology.max.error.report.per.interval" 5, "zmq.linger.millis" 0, "topology.skip.missing.kryo.registrations" true, "storm.messaging.netty.client_worker_threads" 1, "ui.childopts" "-Xmx768m", "storm.zookeeper.session.timeout" 20000, "nimbus.reassign" true, "topology.trident.batch.emit.interval.millis" 50, "storm.messaging.netty.flush.check.interval.ms" 10, "nimbus.monitor.freq.secs" 10, "logviewer.childopts" "-Xmx128m", "java.library.path" "/usr/local/lib:/opt/local/lib:/usr/lib", "topology.executor.send.buffer.size" 1024, "storm.local.dir" "/tmp/d7d5b030-64e7-40e0-8b25-e30c68efbed6", "storm.messaging.netty.buffer_size" 5242880, "supervisor.worker.start.timeout.secs" 120, "topology.enable.message.timeouts" true, "nimbus.cleanup.inbox.freq.secs" 600, "nimbus.inbox.jar.expiration.secs" 3600, "drpc.worker.threads" 64, "storm.meta.serialization.delegate" "backtype.storm.serialization.DefaultSerializationDelegate", "topology.worker.shared.thread.pool.size" 4, "nimbus.host" "localhost", "storm.messaging.netty.min_wait_ms" 100, "storm.zookeeper.port" 2000, "transactional.zookeeper.port" nil, "topology.executor.receive.buffer.size" 1024, "transactional.zookeeper.servers" nil, "storm.zookeeper.root" "/storm", "storm.zookeeper.retry.intervalceiling.millis" 30000, "supervisor.enable" true, "storm.messaging.netty.server_worker_threads" 1, "storm.zookeeper.servers" ["localhost"], "transactional.zookeeper.root" "/transactional", "topology.acker.executors" 2, "streamparse.log.path" "/root/tweetwordcount/logs", "topology.kryo.decorators" (), "topology.name" "tweetwordcount", "topology.transfer.buffer.size" 1024, "topology.worker.childopts" nil, "drpc.queue.size" 128, "worker.childopts" "-Xmx768m", "supervisor.heartbeat.frequency.secs" 5, "topology.error.throttle.interval.secs" 10, "zmq.hwm" 0, "drpc.port" 3772, "supervisor.monitor.frequency.secs" 3, "drpc.childopts" "-Xmx768m", "topology.receiver.buffer.size" 8, "task.heartbeat.frequency.secs" 3, "topology.tasks" nil, "storm.messaging.netty.max_retries" 300, "topology.spout.wait.strategy" "backtype.storm.spout.SleepSpoutWaitStrategy", "nimbus.thrift.max_buffer_size" 1048576, "topology.max.spout.pending" 5000, "storm.zookeeper.retry.interval" 1000, "topology.sleep.spout.wait.strategy.time.ms" 1, "nimbus.topology.validator" "backtype.storm.nimbus.DefaultTopologyValidator", "supervisor.slots.ports" (1024 1025 1026), "topology.environment" nil, "topology.debug" false, "nimbus.task.launch.secs" 120, "nimbus.supervisor.timeout.secs" 60, "topology.kryo.register" nil, "topology.message.timeout.secs" 60, "task.refresh.poll.secs" 10, "topology.workers" 2, "supervisor.childopts" "-Xmx256m", "nimbus.thrift.port" 6627, "topology.stats.sample.rate" 0.05, "worker.heartbeat.frequency.secs" 1, "topology.tuple.serializer" "backtype.storm.serialization.types.ListDelegateSerializer", "topology.disruptor.wait.strategy" "com.lmax.disruptor.BlockingWaitStrategy", "topology.multilang.serializer" "backtype.storm.multilang.JsonSerializer", "nimbus.task.timeout.secs" 30, "storm.zookeeper.connection.timeout" 15000, "topology.kryo.factory" "backtype.storm.serialization.DefaultKryoFactory", "drpc.invocations.port" 3773, "logviewer.port" 8000, "zmq.threads" 1, "storm.zookeeper.retry.times" 5, "topology.worker.receiver.thread.count" 1, "storm.thrift.transport" "backtype.storm.security.auth.SimpleTransportPlugin", "topology.state.synchronization.timeout.secs" 60, "supervisor.worker.timeout.secs" 30, "nimbus.file.copy.expiration.secs" 600, "storm.messaging.transport" "backtype.storm.messaging.netty.Context", "logviewer.appender.name" "A1", "storm.messaging.netty.max_wait_ms" 1000, "drpc.request.timeout.secs" 600, "storm.local.mode.zmq" false, "ui.port" 8080, "nimbus.childopts" "-Xmx1024m", "storm.cluster.mode" "local", "topology.max.task.parallelism" nil, "storm.messaging.netty.transfer.batch.size" 262144, "topology.classpath" nil, "streamparse.log.level" "debug"}
18411 [Thread-4] INFO  backtype.storm.daemon.worker - Worker 734172ee-877c-4cb2-acc9-4a667273e90d for storm tweetwordcount-1-1470430278 on d2d121eb-b70e-48c0-a093-0afea2a31298:1024 has finished loading
18466 [Thread-11-count-bolt] INFO  backtype.storm.task.ShellBolt - Launched subprocess with pid 4719
18505 [Thread-11-count-bolt] INFO  backtype.storm.task.ShellBolt - Start checking heartbeat...
18506 [Thread-11-count-bolt] INFO  backtype.storm.daemon.executor - Prepared bolt count-bolt:(4)
18580 [Thread-13-parse-bolt] INFO  backtype.storm.task.ShellBolt - Launched subprocess with pid 4720
18617 [Thread-13-parse-bolt] INFO  backtype.storm.task.ShellBolt - Start checking heartbeat...
18617 [Thread-13-parse-bolt] INFO  backtype.storm.daemon.executor - Prepared bolt parse-bolt:(6)
18646 [refresh-active-timer] INFO  backtype.storm.daemon.worker - All connections are ready for worker d2d121eb-b70e-48c0-a093-0afea2a31298:1024 with id 734172ee-877c-4cb2-acc9-4a667273e90d
18664 [Thread-27-__acker] INFO  backtype.storm.daemon.executor - Preparing bolt __acker:(1)
18665 [Thread-27-__acker] INFO  backtype.storm.daemon.executor - Prepared bolt __acker:(1)
18674 [Thread-23-tweet-spout] INFO  backtype.storm.daemon.executor - Opening spout tweet-spout:(7)
18675 [Thread-19-count-bolt] INFO  backtype.storm.daemon.executor - Preparing bolt count-bolt:(3)
18675 [Thread-19-count-bolt] INFO  backtype.storm.utils.ShellProcess - Storm multilang serializer: backtype.storm.multilang.JsonSerializer
18676 [Thread-21-parse-bolt] INFO  backtype.storm.daemon.executor - Preparing bolt parse-bolt:(5)
18676 [Thread-21-parse-bolt] INFO  backtype.storm.utils.ShellProcess - Storm multilang serializer: backtype.storm.multilang.JsonSerializer
18678 [Thread-23-tweet-spout] INFO  backtype.storm.utils.ShellProcess - Storm multilang serializer: backtype.storm.multilang.JsonSerializer
18710 [Thread-25-__system] INFO  backtype.storm.daemon.executor - Preparing bolt __system:(-1)
18743 [Thread-25-__system] INFO  backtype.storm.daemon.executor - Prepared bolt __system:(-1)
19249 [Thread-19-count-bolt] INFO  backtype.storm.task.ShellBolt - Launched subprocess with pid 4738
19250 [Thread-19-count-bolt] INFO  backtype.storm.task.ShellBolt - Start checking heartbeat...
19250 [Thread-19-count-bolt] INFO  backtype.storm.daemon.executor - Prepared bolt count-bolt:(3)
19400 [Thread-21-parse-bolt] INFO  backtype.storm.task.ShellBolt - Launched subprocess with pid 4739
19401 [Thread-21-parse-bolt] INFO  backtype.storm.task.ShellBolt - Start checking heartbeat...
19401 [Thread-21-parse-bolt] INFO  backtype.storm.daemon.executor - Prepared bolt parse-bolt:(5)
19510 [Thread-23-tweet-spout] INFO  backtype.storm.spout.ShellSpout - Launched subprocess with pid 4740
19511 [Thread-23-tweet-spout] INFO  backtype.storm.daemon.executor - Opened spout tweet-spout:(7)
19515 [Thread-23-tweet-spout] INFO  backtype.storm.daemon.executor - Activating spout tweet-spout:(7)
19516 [Thread-23-tweet-spout] INFO  backtype.storm.spout.ShellSpout - Start checking heartbeat...
19619 [Thread-23-tweet-spout] INFO  backtype.storm.spout.ShellSpout - ShellLog pid:4740, name:tweet-spout Empty queue exception 
19720 [Thread-23-tweet-spout] INFO  tweet-spout - /usr/lib/python2.7/site-packages/requests/packages/urllib3/util/ssl_.py:318: SNIMissingWarning: An HTTPS request has been made, but the SNI (Subject Name Indication) extension to TLS is not available on this platform. This may cause the server to present an incorrect TLS certificate, which can cause validation failures. You can upgrade to a newer version of Python to solve this. For more information, see https://urllib3.readthedocs.org/en/latest/security.html#snimissingwarning.
  SNIMissingWarning
/usr/lib/python2.7/site-packages/requests/packages/urllib3/util/ssl_.py:122: InsecurePlatformWarning: A true SSLContext object is not available. This prevents urllib3 from configuring SSL appropriately and may cause certain SSL connections to fail. You can upgrade to a newer version of Python to solve this. For more information, see https://urllib3.readthedocs.org/en/latest/security.html#insecureplatformwarning.
  InsecurePlatformWarning

19726 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt Taylor: 1
19732 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt The: 1
19734 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt Trex: 1
19746 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt You: 1
19746 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt Like: 1
19768 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt Old: 1
19830 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt C#$k: 1
19831 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt HUH: 1
19843 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt you: 1
19844 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt ask: 1
19846 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt a: 1
19848 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt like: 1
19906 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt got: 1
19981 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt into: 1
20002 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt Your: 1
20003 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt My: 1
20006 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt more: 1
20017 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt that: 1
20020 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt your: 1
20032 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt fucking: 1
20033 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt of: 1
20034 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt do: 1
20039 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt you: 2
20067 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt How: 1
20068 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt remember: 1
20069 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt Welsh: 1
20070 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt Rugby: 1
20071 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt was: 1
20100 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt can: 1
20102 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt even: 1
20103 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt question: 1
20116 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt this: 1
20216 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt like: 2
20217 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt back: 1
20249 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt moms: 1
20250 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt life: 1
20333 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt then: 1
20396 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt on: 1
20409 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt and: 1
20411 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt off: 1
20412 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt I: 1
20413 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt with: 1
20414 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt is: 1
20430 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt an: 1
20442 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt argument: 1
20446 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt I: 2
20447 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt the: 1
20448 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt I: 3
20461 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt could: 1
20462 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt for: 1
20481 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt the: 2
20490 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt of: 2
20556 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt members: 1
20561 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt about: 1
20572 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt important: 1
20578 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt present: 1
20669 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt racism: 1
20688 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt and: 2
20689 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt whatnot: 1
20690 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt Frustrating: 1
20711 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt While: 1
20805 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt that: 2
20806 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt may: 1
20807 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt be: 1
20826 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt fix: 1
20827 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt Team: 1
20828 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt Refugee: 1
20859 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt at: 1
20860 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt the: 3
20881 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt not: 1
20882 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt stupid: 1
20894 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt concept: 1
20895 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt honor: 1
20926 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt what: 1
20928 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt field: 1
20939 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt got: 2
20941 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt some: 1
20942 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt older: 1
20943 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt family: 1
20944 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt day: 1
20957 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt systematic: 1
20958 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt true: 1
20975 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt we're: 1
20976 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt enough: 1
20977 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt think: 1
20988 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt best: 1
20989 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt deal: 1
20990 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt Please: 1
21006 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt love: 1
21007 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt God: 1
21024 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt to: 1
21025 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt YOU'RE: 1
21043 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt that: 3
21039 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt this: 2
21055 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt a: 2
21056 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt joke: 1
21066 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt gonna: 1
21087 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt it: 1
21088 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt You're: 1
21089 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt a: 3
21153 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt giant: 1
21163 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt Olympics: 1
21169 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt Is: 1
21179 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt change: 1
21182 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt dope: 1
21183 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt think: 2
21236 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt Are: 1
21267 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt me: 1
21268 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt if: 1
21273 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt you: 3
21288 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt smile: 1
21291 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt day: 2
21292 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt 5-6: 1
21293 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt happy: 1
21311 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt out: 1
21314 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt there: 1
21315 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt me: 2
21358 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt that: 4
21379 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt even: 2
21391 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt mention: 1
21392 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt Tooth: 1
21392 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt picks: 1
21393 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt are: 1
21395 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt go: 1
21422 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt Make: 1
21423 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt call: 1
21423 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt b/c: 1
21438 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt You: 2
21440 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt Awesome: 1
21441 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt people: 1
21442 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt -D: 1
21442 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt Thanks: 1
21456 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt amp: 1
21457 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt chance: 1
21457 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt win: 1
21458 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt Vampire: 1
21459 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt Buffy: 1
21459 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt for: 2
21483 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt post: 1
21484 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt making: 1
21486 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt each: 1
21487 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt hours: 1
21487 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt Good: 1
21488 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt for: 3
21489 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt all: 1
21490 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt you: 4
21490 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt couples: 1
21508 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt snapchat: 1
21509 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt one: 1
21509 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt day: 3
21510 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt I: 4
21510 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt either: 1
21511 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt 47: 1
21512 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt stories: 1
21513 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt in: 1
21514 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt post: 2
21526 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt or: 1
21527 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt not: 2
21528 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt for: 4
21529 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt a: 4
21529 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt really: 1
21551 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt it's: 1
21552 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt hard: 1
21583 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt for: 5
21624 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt anything: 1
21626 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt month: 1
21627 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt there's: 1
21637 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt amp: 2
21641 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt between: 1
21642 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt 26: 1
21643 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt when: 1
21644 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt 2-pack: 1
21645 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt own: 1
21646 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt powers: 1
21661 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt almost: 1
21661 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt almost: 2
21677 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt cant: 1
21680 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt to: 2
21682 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt find: 1
21682 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt people: 2
21683 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt shit: 1
21726 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt talk: 1
21730 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt I: 5
21731 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt war: 1
21733 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt like: 3
21742 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt hero: 1
21745 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt Respect: 1
21748 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt One: 1
21823 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt Deuce: 1
21824 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt Nickle: 1
21825 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt who: 1
21826 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt retard: 1
21827 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt who: 2
21828 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt paid: 1
21839 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt $1500: 1
21839 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt new: 1
21840 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt has: 1
21841 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt changed: 1
21842 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt not: 3
21843 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt to: 3
21844 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt the: 4
21844 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt way: 1
21857 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt to: 4
21858 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt a: 5
21858 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt to: 5
21862 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt our: 1
21872 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt 2013: 1
21872 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt Optima: 1
21873 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt have: 1
21874 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt same: 1
21877 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt Yelp: 1
21878 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt Sometimes: 1
21876 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt your: 2
21915 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt what: 2
21916 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt after: 1
21916 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt abuse: 1
21935 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt she: 1
21936 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt suffered: 1
21937 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt hands: 1
21973 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt valack: 1
21973 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt What: 1
21974 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt have: 2
21975 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt get: 1
21994 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt is: 2
21995 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt so: 1
21996 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt with: 2
22047 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt congressional: 1
22062 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt rep: 1
22065 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt and: 3
22102 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt our: 2
22103 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt world: 1
22105 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt Only: 1
22144 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt when: 2
22144 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt they're: 1
22145 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt fresh: 1
22146 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt say: 1
22147 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt no: 1
22149 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt follow: 1
22151 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt come: 1
22152 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt me: 3
22153 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt night: 1
22154 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt for: 6
22172 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt the: 5
22253 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt to: 6
22299 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt ppl: 1
22309 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt a: 6
22313 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt no: 2
22326 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt legends: 1
22330 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt in: 2
22331 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt have: 3
22342 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt Angel: 1
22342 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt club: 1
22345 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt Pop: 1
22346 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt who: 3
22357 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt her: 1
22358 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt lgbt+: 1
22361 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt it's: 2
22362 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt Batigol: 1
22363 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt ugh: 1
22363 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt guys: 1
22392 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt together: 1
22374 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt like: 4
22392 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt you: 5
22393 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt the: 6
22394 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt grieving: 1
22395 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt hsjaysksusbd: 1
22396 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt handle: 1
22396 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt this: 3
22409 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt parents: 1
22409 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt of: 3
22410 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt a: 7
22411 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt are: 2
22411 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt ew: 1
22412 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt when: 3
22413 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt to: 7
22430 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt Reynard: 1
22431 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt for: 7
22432 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt ripping: 1
22432 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt killed: 1
22433 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt A: 1
22433 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt grace: 1
22451 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt But: 1
22452 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt the: 7
22452 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt thinks: 1
22453 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt he: 1
22454 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt for: 8
22606 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt a: 8
22608 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt YZ: 1
22611 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt her: 2
22621 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt The: 2
22624 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt dignity: 1
22634 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt I'll: 1
22639 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt drive: 1
22640 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt later: 1
22641 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt man: 1
22665 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt we're: 2
22682 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt here: 1
22682 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt we: 1
22683 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt are: 3
22684 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt going: 1
22684 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt nowhere: 1
22698 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt little: 1
22699 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt ship: 1
22699 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt Been: 1
22841 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt saving: 1
22842 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt price: 1
22846 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt this: 4
22847 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt on: 2
22861 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt boy: 1
22863 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt Kia: 1
22865 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt so: 2
22867 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt Take: 1
22871 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt glad: 1
22885 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt a: 9
23017 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt look: 1
23018 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt I: 6
23018 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt the: 8
23019 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt issue: 1
23020 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt I: 7
23020 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt wonder: 1
23021 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt the: 9
23030 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt hell: 1
23031 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt all: 2
23032 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt here: 2
23032 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt this: 5
23033 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt afternoon: 1
23034 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt believe: 1
23034 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt shit: 2
23035 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt of: 4
23036 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt the: 10
23036 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt at: 2
23037 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt the: 11
23049 [Thread-23-tweet-spout] INFO  backtype.storm.spout.ShellSpout - ShellLog pid:4740, name:tweet-spout Empty queue exception 
23049 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt vote: 1
23061 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt out: 2
23061 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt Orange: 1
23062 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt guys: 2
23062 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt So: 1
23063 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt lady: 1
23063 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt just: 1
23064 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt me: 4
23065 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt shake: 1
23079 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt out: 3
23080 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt us: 1
23081 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt requested: 1
23082 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt polipo0315: 1
23117 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt of: 5
23121 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt down: 1
23133 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt its: 1
23134 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt do: 2
23217 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt I: 8
23246 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt to: 8
23246 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt just: 2
23250 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt this: 6
23251 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt do: 3
23261 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt away: 1
23262 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt to: 9
23263 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt Yo: 1
23264 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt to: 10
23265 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt wrong: 1
23266 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt pay: 1
23268 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt Which: 1
23277 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt money: 1
23278 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt sing: 1
23279 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt shortcake: 1
23326 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt of: 6
23346 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt these: 1
23354 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt cream: 1
23354 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt cake: 1
23355 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt me: 5
23371 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt to: 11
23373 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt sleep: 1
23374 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt have: 4
23376 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt every: 1
23377 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt 2: 1
23386 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt Good: 2
23387 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt extra: 1
23388 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt laaaawd: 1
23388 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt gates: 1
23389 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt would: 1
23390 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt anybody: 1
23390 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt is: 3
23391 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt 8: 1
23392 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt is: 4
23392 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt you: 6
23393 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt preferred: 1
23393 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt at: 3
23406 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt Sunday: 1
23407 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt because: 1
23407 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt love: 2
23408 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt love: 3
23409 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt me: 6
23409 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt too: 1
23410 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt Chickens: 1
23428 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt is: 5
23429 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt resting: 1
23430 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt icing: 1
23430 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt my: 1
23431 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt with: 3
23432 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt don't: 1
23432 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt somebody: 1
23433 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt even: 3
23434 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt mind: 1
23443 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt Pretty: 1
23444 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt Funny: 1
23445 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt how: 1
23445 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt pic: 1
23446 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt can: 2
23446 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt change: 2
23461 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt your: 3
23462 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt guys: 3
23463 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt its: 2
23464 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt who's: 1
23464 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt with: 4
23464 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt for: 9
23476 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt Ronaldo: 1
23477 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt Fav: 1
23478 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt for: 10
23478 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt fetishist: 1
23479 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt m/m: 1
23480 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt damn: 1
23481 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt business: 1
23483 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt ships: 1
23486 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt and: 4
23515 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt preach: 1
23516 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt literally: 1
23519 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt abt: 1
23528 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt after: 2
23531 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt reading: 1
23531 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt this: 7
23532 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt When: 1
23533 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt go: 2
23533 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt scary: 1
23564 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt movie: 1
23564 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt when: 4
23565 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt who's: 2
23566 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt with: 5
23567 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt when: 5
23567 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt get: 2
23581 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt Business: 1
23582 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt Media: 1
23582 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt amp: 3
23583 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt Fitch: 1
23584 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt focusing: 1
23595 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt rep: 2
23597 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt but: 1
23598 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt Dhhskauskasiis: 1
23598 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt I: 9
23609 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt says: 1
23610 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt early-stage: 1
23611 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt information: 1
23611 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt so: 3
23612 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt wish: 1
23613 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt I: 10
23613 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt could: 2
23614 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt tell: 1
23615 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt u: 1
23616 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt everything: 1
23626 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt I'm: 1
23627 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt then: 2
23628 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt sweet: 1
23628 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt until: 1
23629 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt tried: 1
23641 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt like: 5
23642 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt it: 2
23643 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt happens: 1
23643 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt to: 12
23644 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt be: 2
23645 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt a: 10
23645 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt putting: 1
23646 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt kill: 1
23647 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt me: 7
23648 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt me: 8
23649 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt money: 2
23658 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt ever: 1
23658 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt just: 3
23697 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt Julie: 1
23710 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt you: 7
23745 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt don't: 2
23746 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt with: 6
23755 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt never: 1
23756 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt true: 2
23761 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt are: 4
23785 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt ever: 2
23788 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt bring: 1
23801 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt neighborhood: 1
23802 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt shirt: 1
23806 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt p: 1
23826 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt This: 1
23827 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt is: 6
23828 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt mistake: 1
23828 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt when: 6
23829 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt think: 3
23835 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt final: 1
23848 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt nail: 1
23849 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt is: 7
23850 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt amaze: 1
23850 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt think: 4
23851 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt again: 1
23852 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt us: 2
23855 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt Purposemaker: 1
23855 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt new: 2
23866 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt w/much: 1
23868 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt favorite: 1
23872 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt From: 1
23873 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt Citiez: 1
23873 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt and: 5
23890 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt =: 1
23891 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt Look: 1
23892 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt to: 13
23892 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt stay: 1
23893 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt you: 8
23894 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt scifi: 1
23894 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt Snappppp: 1
23895 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt explains: 1
23896 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt Got: 1
23905 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt and: 6
23907 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt your: 4
23908 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt f/f: 1
23908 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt bad: 1
23909 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt for: 11
23910 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt One: 2
23911 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt From: 2
23911 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt Jump: 1
23912 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt why: 1
23921 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt a: 11
23922 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt writes: 1
23922 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt WRITES: 1
23923 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt CHRISTIANCOMMUNITY: 1
23924 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt Fyi: 1
23924 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt My: 2
23925 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt from: 1
23937 [Thread-23-tweet-spout] INFO  backtype.storm.spout.ShellSpout - ShellLog pid:4740, name:tweet-spout Empty queue exception 
23976 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt springs: 1
23977 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt Poppin: 1
24022 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt why: 2
24023 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt don't: 3
24023 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt have: 5
24040 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt any: 1
24041 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt Harmony: 1
24041 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt science: 1
24069 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt special: 1
24132 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt fiction: 1
24150 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt Read: 1
24166 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt post: 3
24184 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt Chaser: 1
24337 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt occasion: 1
24340 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt you're: 1
24358 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt rainy: 1
24359 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt I: 11
24364 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt cannot: 1
24385 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt the: 12
24386 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt that: 5
24430 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt only: 1
24511 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt is: 8
24512 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt is: 9
24512 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt same: 2
24513 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt what: 3
24514 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt is: 10
24514 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt going: 2
24515 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt are: 5
24516 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt wonderful: 1
24517 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt comes: 1
24518 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt of: 7
24519 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt the: 13
24519 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt matt: 1
24534 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt We: 1
24535 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt is: 11
24536 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt imagination: 1
24554 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt mouth: 1
24555 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt won't: 1
24555 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt a: 12
24556 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt stop: 1
24583 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt cussed: 1
24598 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt ha: 1
24599 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt o: 1
24676 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt taking: 1
24703 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt amp: 4
24706 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt Just: 1
24708 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt inspire: 1
24710 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt some: 2
24727 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt Bullsnot: 1
24728 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt a: 13
24730 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt song: 1
24875 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt for: 12
24876 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt fun: 1
24877 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt And: 1
24878 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt said: 1
24878 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt calm: 1
24879 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt sepe: 1
24906 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt to: 14
24906 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt a: 14
24907 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt song: 2
24922 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt If: 1
24923 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt u: 2
24923 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt meet: 1
24926 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt creature: 1
24927 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt FakeUniform: 1
24927 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt stay: 2
24928 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt Part: 1
24929 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt 3: 1
25002 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt miss: 1
25018 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt I'll: 2
25039 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt I: 12
25040 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt would: 2
25041 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt ABSURD: 1
25042 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt miss: 2
25043 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt my: 2
25043 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt Yessss: 1
25044 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt braces: 1
25044 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt them: 1
25045 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt stream: 1
25056 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt join: 1
25056 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt streaming: 1
25057 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt Collection: 1
25058 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt love: 4
25058 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt Who's: 1
25059 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt favorite: 2
25059 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt amounts: 1
25061 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt Just: 2
25061 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt of: 8
25077 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt Join: 1
25078 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt for: 13
25091 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt a: 15
25091 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt now: 1
25105 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt Harmony: 2
25106 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt strawberry: 1
25107 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt too: 2
25109 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt ice: 1
25110 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt automaticlly: 1
25111 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt say: 2
25157 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt times: 1
25160 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt hi: 1
25169 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt out: 4
25170 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt When: 2
25170 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt case: 1
25171 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt don't: 4
25176 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt have: 6
25185 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt me: 9
25186 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt snapchat: 2
25223 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt This: 2
25234 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt Maybe: 1
25235 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt one: 2
25236 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt day: 4
25238 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt dreams: 1
25241 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt will: 1
25250 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt come: 2
25287 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt to: 15
25298 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt the: 14
25299 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt i: 1
25317 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt tickets: 1
25318 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt to: 16
25318 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt kevin: 1
25321 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt at: 4
25322 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt cobblestones: 1
25464 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt for: 14
25473 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt tonight: 1
25473 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt if: 2
25492 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt true: 3
25493 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt Because: 1
25511 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt very: 1
25512 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt point: 1
25512 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt very: 2
25527 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt important: 2
25527 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt love: 5
25529 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt Pink: 1
25530 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt Floyd: 1
25530 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt Dark: 1
25531 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt with: 7
25552 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt need: 1
25562 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt TENTSILE: 1
25566 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt TREE: 1
25579 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt TENTS: 1
25580 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt Live: 1
25580 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt friggin: 1
25581 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt axe: 1
25584 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt axe: 2
25588 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt damn: 2
25629 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt interested: 1
25648 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt THE: 1
25649 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt CRAZY: 1
25659 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt Crazy: 1
25662 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt stuff: 1
25664 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt is: 12
25665 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt yours: 1
25667 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt now: 2
25669 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt When: 3
25670 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt me: 10
25680 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt have: 7
25680 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt boyfriend: 1
25681 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt man: 2
25682 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt gon: 1
25682 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt funny: 1
25749 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt for: 15
25751 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt Hillary: 1
25769 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt that: 6
25770 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt all: 3
25786 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt money: 3
25787 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt I'm: 2
25929 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt doing: 1
26013 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt I: 13
26027 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt Rollin: 1
26029 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt this: 8
26188 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt campaign: 1
26191 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt don't: 5
26192 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt throw: 1
26202 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt babies: 1
26223 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt do: 4
26224 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt you: 9
26239 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt and: 7
26312 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt out: 5
26317 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt this: 9
26317 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt worth: 1
26318 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt Harmony: 3
26385 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt legs: 1
26466 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt rn: 1
26466 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt amp: 5
26467 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt there: 2
26468 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt have: 8
26468 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt been: 1
26469 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt some: 3
26469 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt high: 1
26470 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt bids: 1
26471 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt amp: 6
26485 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt got: 3
26485 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt him: 1
26486 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt low: 1
26487 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt rest: 1
26487 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt Milano: 1
26501 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt Unfortunately: 1
26502 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt boyfriend: 2
26503 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt money: 4
26503 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt Are: 2
26504 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt joining: 1
26504 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt Industry: 1
26505 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt conference: 1
26532 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt and: 8
26534 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt Learn: 1
26535 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt here: 3
26536 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt So: 2
26536 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt potential: 1
26537 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt Bring: 1
26546 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt bring: 2
26547 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt something: 1
26547 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt inspired: 1
26549 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt watching: 1
26567 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt Shop: 1
26567 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt from: 2
26568 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt movies: 1
26582 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt The: 3
26582 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt thought: 1
26583 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt of: 9
26583 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt you: 10
26584 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt fly: 1
26584 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt your: 5
26585 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt else: 1
26585 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt I: 14
26586 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt dont: 1
26595 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt Sonic: 1
26595 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt Mania: 1
26596 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt this: 10
26647 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt like: 6
26683 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt snuck: 1
26692 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt that: 7
26762 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt U: 1
26763 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt I: 15
26764 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt cried: 1
26777 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt a: 16
26778 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt at: 5
26778 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt booty: 1
26779 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt work: 1
26780 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt a: 17
26781 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt us: 3
26781 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt so: 4
26782 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt We're: 1
26783 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt I: 16
26784 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt wanna: 1
26795 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt mood: 1
26799 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt calendar: 1
26799 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt so: 5
26800 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt we: 2
26862 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt be: 3
26863 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt a: 18
26863 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt not: 4
26864 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt taco: 1
26887 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt about: 2
26889 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt you: 11
26890 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt see: 1
26891 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt you: 12
26892 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt can: 3
26893 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt set: 1
26894 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt fire: 1
26913 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt a: 19
27023 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt you're: 2
27024 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt up: 1
27025 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt it's: 3
27025 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt about: 3
27050 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt you: 13
27051 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt things: 1
27052 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt tough: 1
27061 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt Hearst: 1
27061 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt Group: 1
27062 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt formed: 1
27062 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt a: 20
27063 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt fund: 1
27064 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt investing: 1
27065 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt in: 3
27066 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt down: 2
27067 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt my: 3
27132 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt me: 11
27144 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt even: 4
27146 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt tried: 2
27148 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt am: 1
27160 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt too: 3
27209 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt and: 9
27211 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt it: 3
27211 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt Based: 1
27223 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt stop: 2
27224 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt tracks: 1
27225 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt is: 13
27226 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt Sunday: 2
27226 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt How: 2
27227 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt now: 3
27255 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt works: 1
27256 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt on: 3
27257 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt mobile: 1
27262 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt too: 4
27275 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt How: 3
27276 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt am: 2
27277 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt Facebook: 1
27278 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt how: 2
27278 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt am: 3
27279 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt Come: 1
27280 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt shop: 1
27282 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt my: 4
27283 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt closet: 1
27283 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt resale: 1
27284 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt shopping: 1
27284 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt family: 2
27285 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt are: 6
27286 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt best: 2
27300 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt 24: 1
27300 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt soul/: 1
27301 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt nigga: 1
27302 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt fn: 1
27304 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt skater: 1
27306 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt a: 21
27307 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt story: 1
27307 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt hi: 2
27308 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt u: 3
27308 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt gonna: 2
27309 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt back: 2
27310 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt serious: 1
27311 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt young: 1
27324 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt the: 15
27325 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt watch: 1
27325 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt no: 3
27326 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt no: 4
27326 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt accident: 1
27327 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt you: 14
27328 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt financial: 1
27328 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt service: 1
27331 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt and: 10
27331 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt Everything: 1
27332 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt was: 2
27333 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt u: 4
27333 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt R.I.P: 1
27348 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt the: 16
27349 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt original: 1
27358 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt video: 1
27371 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt If: 2
27372 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt you: 15
27374 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt owe: 1
27385 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt and: 11
27385 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt I: 17
27386 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt tell: 2
27387 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt you: 16
27389 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt to: 17
27390 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt keep: 1
27390 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt it: 4
27391 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt know: 1
27391 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt I: 18
27392 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt fuck: 1
27443 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt blackface: 1
27444 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt holy: 1
27454 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt you: 17
27456 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt the: 17
27456 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt in: 4
27457 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt no: 5
27458 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt more: 2
27471 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt He: 1
27472 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt fails: 1
27472 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt to: 18
27473 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt A: 2
27474 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt The: 4
27474 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt Mr: 1
27475 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt Jeff: 1
27488 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt Mills: 1
27488 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt Prince: 1
27551 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt shit: 3
27556 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt panel: 1
27571 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt with: 8
27574 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt since: 1
27576 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt is: 14
27579 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt iTunes: 1
27596 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt of: 10
27597 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt Detroit: 1
27597 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt The: 5
27598 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt A: 3
27599 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt by: 1
27679 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt over: 1
27680 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt 20: 1
27681 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt countries: 1
27681 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt Can: 1
27682 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt spot: 1
27683 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt country: 1
27683 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt me: 12
27692 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt knows: 1
27729 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt on: 4
27730 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt author: 1
27731 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt Oh: 1
27751 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt Ladiessss: 1
27752 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt I: 19
27753 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt The: 6
27754 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt 100: 1
27766 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt Retweets: 1
27767 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt And: 2
27769 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt I'm: 3
27770 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt he: 2
27771 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt Dropping: 1
27772 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt LORDALTON: 1
27772 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt ABOUTSECURING: 1
27783 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt A: 4
27784 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt THRIVING: 1
27784 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt IN: 1
27793 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt niggas: 1
27863 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt exactly: 1
27865 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt what: 4
27868 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt im: 1
27869 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt me: 13
27869 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt *stutters: 1
27870 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt fucks: 1
27920 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt the: 18
27920 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt made: 1
27921 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt greeley: 1
27922 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt that's: 1
27936 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt I: 20
27936 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt Fifth: 1
27937 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt it: 5
27938 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt the: 19
27938 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt by: 2
27939 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt Steve: 1
27942 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt Sea: 1
27942 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt The: 7
27952 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt mine: 1
27953 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt the: 20
27953 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt on: 5
27954 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt /: 1
27954 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt you: 18
27957 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt 4: 1
27958 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt word: 1
27959 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt women: 1
27959 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt are: 7
27968 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt something: 2
27969 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt need: 2
27969 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt women: 2
28070 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt amp: 7
28070 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt only: 2
28071 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt man: 3
28072 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt change: 3
28072 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt invested: 1
28075 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt 3,881,002: 1
28076 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt this: 11
28077 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt lady: 2
28176 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt a: 22
28177 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt person: 1
28177 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt should: 1
28178 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt limit: 1
28179 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt your: 6
28179 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt the: 21
28180 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt TTC: 1
28180 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt scrap: 1
28194 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt invested: 2
28195 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt Get: 1
28196 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt what: 5
28197 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt sometimes: 1
28197 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt trustees: 1
28198 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt might: 1
28199 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt smart: 1
28199 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt strategy: 1
28200 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt I'm: 4
28200 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt a: 23
28201 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt sucker: 1
28215 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt have: 9
28225 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt for: 16
28226 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt the: 22
28226 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt focus: 1
28240 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt I: 21
28241 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt you: 19
28241 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt message: 1
28242 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt forever: 1
28243 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt Thanks: 2
28243 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt for: 17
28264 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt coming: 1
28265 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt to: 19
28265 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt the: 23
28266 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt everyone: 1
28280 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt Goodnight: 1
28281 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt Invite: 1
28281 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt you: 20
28282 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt to: 20
28283 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt YF|ALFIN: 1
28287 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt on: 6
28288 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt The: 8
28289 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt Roseanne: 1
28289 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt Gotta: 1
28290 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt that: 8
28290 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt show: 1
28291 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt your: 7
28343 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt going: 3
28344 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt make: 1
28439 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt character: 1
28441 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt happy: 2
28451 [Thread-23-tweet-spout] INFO  backtype.storm.spout.ShellSpout - ShellLog pid:4740, name:tweet-spout Empty queue exception 
28453 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt reading: 2
28454 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt Fifth: 2
28456 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt feed: 1
28456 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt if: 3
28458 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt you: 21
28467 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt think: 5
28471 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt check: 1
28472 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt own: 2
28473 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt health: 1
28485 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt don't: 6
28594 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt join: 2
28596 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt Freedom: 1
28601 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt network: 1
28603 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt ever: 3
28603 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt with: 9
28618 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt communication: 1
28620 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt spam: 1
28621 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt much: 1
28623 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt with: 10
28623 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt creator: 1
28633 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt just: 4
28633 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt it: 6
28638 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt you: 22
28639 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt for: 18
28640 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt 30: 1
28649 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt sec: 1
28684 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt in: 5
28685 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt you: 23
28685 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt I: 22
28686 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt ate: 1
28687 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt so: 6
28687 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt tea: 1
28688 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt DJ: 1
28688 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt Sha: 1
28701 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt dream: 1
28702 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt I: 23
28703 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt on: 7
28703 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt dream: 2
28714 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt of: 11
28714 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt you: 24
28715 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt was: 3
28730 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt to: 21
28731 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt the: 24
28731 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt but: 2
28732 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt I: 24
28733 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt really: 2
28734 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt you: 25
28734 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt /: 2
28736 [Thread-23-tweet-spout] INFO  backtype.storm.spout.ShellSpout - ShellLog pid:4740, name:tweet-spout Empty queue exception 
28740 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt The: 9
28757 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt Side: 1
28773 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt of: 12
28777 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt the: 25
28793 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt breaker: 1
28793 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt im: 2
28794 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt getting: 1
28841 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt Moon: 1
28841 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt Bruh: 1
28842 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt I: 25
28842 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt the: 26
28903 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt full: 1
28905 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt story: 2
28907 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt Like: 2
28921 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt a: 24
28921 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt a: 25
28923 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt dull: 1
28924 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt that: 9
28925 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt butt-ugly: 1
28927 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt pissed: 1
28927 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt gtg: 1
28928 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt Fea: 1
28928 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt dark: 1
28929 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt fear: 1
28929 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt dark: 2
28944 [Thread-23-tweet-spout] INFO  backtype.storm.spout.ShellSpout - ShellLog pid:4740, name:tweet-spout Empty queue exception 
28949 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt have: 10
28950 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt constant: 1
28951 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt fear: 2
28961 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt something: 3
28962 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt lol: 1
28963 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt need: 3
28964 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt you: 26
28977 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt 2's: 1
28978 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt slow: 1
28979 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt out: 6
28980 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt Niggas: 1
28982 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt Pioggia: 1
28983 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt life: 2
28984 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt A: 5
28985 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt BOSS: 1
28986 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt will: 2
28987 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt secure: 1
28997 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt at: 6
29000 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt people: 3
29002 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt keep: 2
29003 [Thread-33] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4738, name:count-bolt ask: 2
29136 [Thread-29] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4719, name:count-bolt Version: 1
29137 [Thread-30] INFO  tweet-spout - Traceback (most recent call last):
  File "/usr/lib64/python2.7/runpy.py", line 162, in _run_module_as_main
    "__main__", fname, loader, pkg_name)
  File "/usr/lib64/python2.7/runpy.py", line 72, in _run_code
    exec code in run_globals
  File "/usr/lib/python2.7/site-packages/streamparse/run.py", line 25, in <module>
    main()
  File "/usr/lib/python2.7/site-packages/streamparse/run.py", line 21, in main
    cls().run()
  File "/usr/lib/python2.7/site-packages/streamparse/storm/component.py", line 489, in run
    self._run()
  File "/usr/lib/python2.7/site-packages/streamparse/storm/bolt.py", line 219, in _run
    self.process(tup)
  File "bolts/wordcount.py", line 16, in process
    self.emit([word, self.counts[word]])
  File "/usr/lib/python2.7/site-packages/streamparse/storm/bolt.py", line 145, in emit
    need_task_ids=need_task_ids)
  File "/usr/lib/python2.7/site-packages/streamparse/storm/component.py", line 467, in emit
    else self.read_task_ids()
  File "/usr/lib/python2.7/site-packages/streamparse/storm/component.py", line 324, in read_task_ids
    msg = self.read_message()
  File "/usr/lib/python2.7/site-packages/streamparse/storm/component.py", line 297, in read_message
    line = self.input_stream.readline()
KeyboardInterrupt

Traceback (most recent call last):
  File "/usr/bin/sparse", line 9, in <module>
    load_entry_point('streamparse==2.1.4', 'console_scripts', 'sparse')()
  File "/usr/lib/python2.7/site-packages/streamparse/cli/sparse.py", line 57, in main
    args.func(args)
  File "/usr/lib/python2.7/site-packages/streamparse/cli/run.py", line 81, in main
    debug=args.debug)
  File "/usr/lib/python2.7/site-packages/streamparse/cli/run.py", line 52, in run_local_topology
    run(full_cmd)
  File "/usr/lib/python2.7/site-packages/invoke/__init__.py", line 32, in run
    return Context().run(command, **kwargs)
  File "/usr/lib/python2.7/site-packages/invoke/context.py", line 53, in run
    return runner_class(context=self).run(command, **kwargs)
  File "/usr/lib/python2.7/site-packages/invoke/runners.py", line 335, in run
    raise exception
KeyboardInterrupt
[root@ip-172-31-4-51 tweetwordcount]# cd ..
[root@ip-172-31-4-51 ~]# ls -l
total 720
-rw-------  1 root root    287 Sep 22  2015 dans_bash_history.txt
-rw-r--r--  1 root root  12402 Jul 11 18:07 ez_setup.py
-rw-r--r--  1 root root    763 Aug  5 17:04 finalresults.py
-rw-r--r--  1 root root    446 Aug  5 16:38 histogram.py
drwxr-xr-x 11 root root   4096 May  4  2015 ipython
drwxr-xr-x  5 root root   4096 May  4  2015 pgxl-deployment-tools
-rw-r--r--  1 root root 655364 Jul 11 18:07 setuptools-24.0.2.zip
-rwxr-xr-x  1 root root    221 Sep 22  2015 start-hadoop.sh
-rwxr-xr-x  1 root root    252 Sep 22  2015 start-hadoop.sh~
-rwxr-xr-x  1 root root    209 Sep 22  2015 stop-hadoop.sh
-rwxr-xr-x  1 root root    222 Sep 22  2015 stop-hadoop.sh~
drwxr-xr-x 11 root root   4096 May  4  2015 streamparse
drwxr-xr-x  8 root root   4096 Jul 11 19:33 tweetcount
-rw-r--r--  1 root root   2307 Aug  5 20:17 tweets.py
drwxr-xr-x  8 root root   4096 Aug  5 20:50 tweetwordcount
-rw-r--r--  1 root root    765 Jul 29 01:42 Twittercredentials.py
[root@ip-172-31-4-51 ~]# cd tweet
-bash: cd: tweet: No such file or directory
[root@ip-172-31-4-51 ~]# cd tweetwordcount/
[root@ip-172-31-4-51 tweetwordcount]# cd src
[root@ip-172-31-4-51 src]# cd bolts
[root@ip-172-31-4-51 bolts]# ls -l
total 8
-rw-r--r-- 1 root root    0 Aug  5 20:41 __init__.py
-rw-r--r-- 1 root root 1432 Aug  5 20:43 parse.py
-rw-r--r-- 1 root root  486 Aug  5 20:46 wordcount.py
[root@ip-172-31-4-51 bolts]# vi parse.py

        valid_words = []
        for word in words:

            # Filter the hash tags
            if word.startswith("#"): continue

            # Filter the user mentions
            if word.startswith("@"): continue

            # Filter out retweet tags
            if word.startswith("RT"): continue

            # Filter out the urls
            if word.startswith("http"): continue

            # Strip leading and lagging punctuations
            aword = word.strip("\"?><,'.:;!&)")

            # now check if the word contains only ascii
            if len(aword) > 0 and ascii_string(word):
                valid_words.append([aword])

        if not valid_words: return

        # Emit all the words
        self.emit_many(valid_words)

        # tuple acknowledgement is handled automatically


