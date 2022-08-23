#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from requests_oauthlib import OAuth1Session
import json
from jq import jq

#import logging
#log = logging.getLogger('requests_oauthlib')
#log.addHandler(logging.StreamHandler(sys.stdout))
#log.setLevel(logging.DEBUG)

class foremanApi:
  def __init__(self):
    self.parameters = {}
    self.resultJson = {}
 
  def createSession(self):
    key = self.parameters['Key'] 
    secret = self.parameters['Secret'] 
    user = self.parameters['User']
    session=OAuth1Session(key, secret)
    session.headers.update({'FOREMAN-USER': self.parameters['User'],'User-Agent': 'python-requests/2.6.0 CPython/2.7.5 Linux/3.10.0-1160.36.2.el7.x86_64', 'Content-Type': 'application/json'})
    self.session = session
   
  def sendGet(self):
    request=self.session.get(self.parameters['url'], verify=False)
    if not request.ok:
      self.httpsStatus = request.raise_for_status()
    else:
      self.content = request.content
  
  def sendPut(self):
    request=self.session.put(self.parameters['url'], data=self.paramters['postData'])
    if not request.ok:
      self.httpsStatus = request.raise_for_status()
    else:
      self.content = request.content

  def parseJson(self):
    resultJson = self.content
    results = json.loads(self.content)
    self.resultJson = results
