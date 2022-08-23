#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
class ahActionsForman:
  def __init__(self,data):
    self.parameters = {}
    self.parameters['data'] = data
  def listUser(self):
    data = self.parameters['data']
    users = []
    for user in data :
       if re.match(self.parameters['regexFiltre'],user['mail']):
         users.append(user['login'])
    self.parameters['users'] = users
  def delUser(self,user,filtre):
    self.parameters['usr2del'] = filtre
    
