#!/usr/bin/python
# run time test for arowana indexing
# Copyright (C) 2013 by Voxsup Inc.
# python testArowana.py 100000
import sys
import os
import MySQLdb
import string
import time
import datetime
import urllib2
import urllib
import json
from random import randrange

iterations = int(sys.argv[1])



start = time.time()
i=0
while i < iterations:
    i += 1
    fid = randrange(200000000)+1
    data = {"user_id":fid }
    req=urllib2.Request("http://localhost:8087/sw_query_reverse_index_by_id", 
                      json.dumps(data), 
                      {'Content-Type': 'application/json'} )
    f = urllib2.urlopen(req)
elapsed = (time.time() - start)
print "arowana time: "
print elapsed


db = MySQLdb.connect(host="xxxxx", port=3306, user="xxx", passwd="xxxxx")
cursor = db.cursor()

i=0
start = time.time()
while i < iterations:
    i += 1
    fid = randrange(200000000)+1
    query = "SELECT * from fb_fe.fb_comment_like_access WHERE uid=\'" + str(fid) +"\'"
    try:
        cursor.execute(query)
    except:
        print "error executing " + query    
    for j in xrange(cursor.rowcount):
        row = cursor.fetchone()
elapsed = (time.time() - start)
print "btree time: "
print elapsed

db = MySQLdb.connect(host="xxxx", port=3306, user="xxxx", passwd="xxxx")
cursor = db.cursor()
start = time.time()
i=0
while i < iterations:
    i += 1
    fid = randrange(200000000)+1
    query = "SELECT * from fb_fe.fb_comment_like_access WHERE user_id=\'" + str(fid) +"\'"
    try:
        cursor.execute(query)
    except:
        print "error executing " + query    
    for j in xrange(cursor.rowcount):
        row = cursor.fetchone()
elapsed = (time.time() - start)
print "btree partitioned time: "
print elapsed



