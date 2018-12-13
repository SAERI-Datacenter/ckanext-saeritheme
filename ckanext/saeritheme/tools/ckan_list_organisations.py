#!/usr/bin/env python2

# Configuration:
ip = "172.16.92.142"
api_key = "0317c21c-7d04-48df-8f1b-9989edbd6165"

user_agent = 'ckanapiexample/1.0 (+http://example.com/my/website)'

from ckanapi import RemoteCKAN
from pprint import pprint

ckan = RemoteCKAN('http://%s' % ip, apikey=api_key, user_agent=user_agent)

result = ckan.action.organization_list(all_fields=True)
pprint(result)

RemoteCKAN.close(ckan)
exit(0)
