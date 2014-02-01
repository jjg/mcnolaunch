#!/usr/bin/python

import yggdrasil

mcauth = yggdrasil.YggAuth()

# get credentials
email = raw_input('email: ')
password = raw_input('password: ')

# test authenticate
auth_result = mcauth.authenticate(username=email,password=password)

print 'username: %s' % auth_result['selectedProfile']['name']
print 'sessionID: %s' % auth_result['accessToken']

