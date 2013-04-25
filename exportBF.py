#!/usr/bin/env python
"""export compressed bf string from storage"""

import sys
import os
import MySQLdb
import string
import time
import BFPIconfiguration
import random
import pymongo
import cPickle as pickle
from pymongo import MongoClient
from bson.objectid import ObjectId

def readBFFromMongo(fbid , return_field = 'base64_str'):
  record = mongo_collection.find_one({ "fb_id":str(fbid) , 
                                               "start_date_unix":config.start_date_unix , 
                                               "end_date_unix":config.end_date_unix 
                                              })
  try:
    return record[return_field]
  except:
    return ''

def returnListOfFBIDs():
  src = config.src
  listOfID = {}
  if src == 'FB':
    query = "SELECT fb_id, fb_name , category FROM voxsup_facebook_backend_utf8.priority WHERE priority >=0 ORDER BY priority DESC"
    try:
      cursor_s.execute(query)
    except:
      print "error reading fb_id from table" 

    for i in xrange(cursor_s.rowcount):
      row = cursor_s.fetchone()
      try:
        fb_name = unicode(row[1], errors='ignore')
      except:
        fb_name = u""
      try:
        category = unicode(row[2], errors='ignore')
      except:
        category = u""
      listOfID[str(row[0])] =  {"fb_name":fb_name , "category":category}
  elif src == 'TW':
    query = "SELECT twitter_id,twitter_screen_name FROM company.twitter ORDER BY priority DESC"
    try:
      cursor_s.execute(query)
    except:
      print "error reading twitter_id from table" 

    for i in xrange(cursor_s.rowcount):
      row = cursor_s.fetchone()
      try:
        fb_name = unicode(row[1], errors='ignore')
      except:
        fb_name = u""
      listOfID[str(row[0])] =  {"fb_name":fb_name , "category":""}

  return listOfID

# making db connection
config = BFPIconfiguration.config("2012-10-01", "2012-12-31", "FB")
src = config.src
exc = Exception('Unspecified Mongo initialization error')
for i in range(10):
    host = random.choice(config.MONGO_CONNECTIONS['default']['hosts'])
    try:
        mongo_client = MongoClient(host, config.MONGO_CONNECTIONS['default']['port'])
        break
    except pymongo.errors.ConnectionFailure as e:
        print "mongo connection error"
        exc = e
        time.sleep(1)  # if we hit a db connection error, retry
else:
    print "mongo connection FAIL"
    raise exc
mongo_db = mongo_client[config.MONGO_CONNECTIONS['default']['name'][src]]
mongo_db.authenticate(config.MONGO_CONNECTIONS['default']['username'], config.MONGO_CONNECTIONS['default']['password'])
mongo_collection = mongo_db[config.mongo_collection[src]]
mongo_interest_collection = mongo_db[config.mongo_interest_collection[src]]
mongo_general_interest_collection = mongo_db[config.mongo_general_interest_collection[src]]
mongo_index_collection = mongo_db[config.mongo_index_collection[src]]
while True:
    try:
        db3 = MySQLdb.connect(host=config.db_host_s[src], port=config.db_port_s[src], user=config.db_user_s[src], passwd=config.db_passwd_s[src])
        cursor_s = db3.cursor()
        break
    except:
        print "cannot connect the frontend db! "+ str(config.db_host_s[src])
        time.sleep(1)  


if (sys.argv[1] == "export"):
	ListOfFBIDs = returnListOfFBIDs()
	keys = ListOfFBIDs.keys()
	for key in keys[:10]:
		str_to_file = readBFFromMongo(str(key))
		pickle.dump( {"fbid": str(key), "bf":str_to_file} , open( "%s%s"%(str(key),".bloompickle"), "wb" ) )