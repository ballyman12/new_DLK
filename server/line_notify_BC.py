#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import requests
import urllib.parse 	#for python3
#import urlparse, urllib	#for Python2.7


#token = "z2WsddL9iRFLmy4BAQhJTHjIwvqZVuYLpDwwGHU8ef5"

#token_user = "66n9Dod5EorHuVu9zF9RTH9bmMKzIEsaYpie4OXkqQo"


def line_notify(token, msg):
    LINE_ACCESS_TOKEN = token
    message = msg
    url = "https://notify-api.line.me/api/notify"
    msg = urllib.parse.urlencode({"message":message}) 	#for Python3
    #msg = urllib.urlencode({"message":message})		#for Python2.7
    LINE_HEADERS = {'Content-Type':'application/x-www-form-urlencoded',"Authorization":"Bearer "+LINE_ACCESS_TOKEN}
    session = requests.Session()
    a=session.post(url, headers=LINE_HEADERS, data=msg)
    return a.text

#msg = "Hello"
#result = line_notify(token, msg)
#print (result)
