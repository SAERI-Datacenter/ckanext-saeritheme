#!/usr/bin/env python2

# Read the configuration
ckan_ip = open("ckan_ip.txt").read().replace('\n','')
api_key = open("ckan_api_key.txt").read().replace('\n','')
user_agent = 'ckanapiexample/1.0 (+http://example.com/my/website)'

from ckanapi import RemoteCKAN
from pprint import pprint

ckan = RemoteCKAN('http://%s' % ip, apikey=api_key, user_agent=user_agent)

result = ckan.action.organization_list(all_fields=True)
pprint(result)

RemoteCKAN.close(ckan)
exit(0)
