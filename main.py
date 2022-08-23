#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import sys
from pkgFormanApi import foremanApi
from pkgFormanApi import ahActionsForman

if __name__ == "__main__": 
  parser = argparse.ArgumentParser()
  parser.set_defaults(regexFiltre='.*',per_page='9999')
  parser.add_argument("-p","--per-page",help="Nombre de page traité par la requête", dest="per_page", required=False, type=str )
  parser.add_argument("-f","--filtre",help="filtre générique regexp pour toute requête",dest="regexFiltre", required=False, type=str )
  args = parser.parse_args()
  if args.per_page :
    per_page = parser.get_default('per_page')
  if args.regexFiltre :
    regexFiltre = parser.get_default('regexFiltre')
  
  instance = foremanApi.foremanApi()
  instance.parameters['Key'] = 'blablabla...key'
  instance.parameters['Secret'] = 'blablabla...secret'
  instance.parameters['User'] = 'blablabla...user'
  instance.parameters['per_page'] = per_page
  instance.parameters['url'] = "https://blablabla...url...api
  instance.createSession()
  instance.sendGet()
  instance.parseJson()

  data = []
  for tmp in instance.resultJson['results']:
    data.append(tmp)

  actions = ahActionsForman.ahActionsForman(data)
  actions.parameters['regexFiltre'] = regexFiltre
  actions.listUser()

  users = actions.parameters['users']
  print(users)

