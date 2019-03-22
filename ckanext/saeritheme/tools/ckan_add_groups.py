#!/usr/bin/env python2
# 1.00 arb 

# Create all groups/themes/topic categories from a CSV file.
# See https://docs.ckan.org/en/2.8/api/index.html#ckan.logic.action.patch.group_patch
# See https://github.com/ckan/ckan/issues/3853

import urllib2
import urllib
import json
from pprint import pprint
import csv
import os # for os.path.isfile
from ckanapi import RemoteCKAN

# Configuration
#csv_filename="topic_categories.csv"
csv_filename="group_list.csv"
user_agent = 'ckanapiexample/1.0 (+http://example.com/my/website)'
logo_dir = "../public/logo"

# CSV fields are:
# csvname,group,description,logo
# eg.
# inland waters,inlandwaters,Inland Waters,,inland_waters.png

# -----------------------------------------------------------------------
# field names which can be set in a group:
# name (lowercase, no spaces)
# id / title / description
# image_url
# packages - a list of dictionaries each having name: and maybe title:
# users - ditto (name and capacity being their role)

# ---------------------------------------------------------------------
# Return a list of group names, eg. ['biota', 'etc']
def get_existing_groups_dict():
	groups_data = ckan.action.group_list(all_fields=True)
	print("Existing groups:")
	pprint(groups_data)
	return groups_data

# ---------------------------------------------------------------------
# Return a list of organisation names, eg. ['BAS', 'FIG']
def get_existing_groups_names(groups_data):
	groups_list = [x['name'] for x in groups_data]
	print("Existing group names:")
	pprint(groups_list)
	return(groups_list)


# ---------------------------------------------------------------------
# Add one group to CKAN from the CSV data given in row
def add_group(row):
	group_name = row['group']
	group_title = row['title']
	group_desc = row['description']

	# Find the logo image
	if row['logo'] == '':
		image_with_path = ''
	else:
		if os.path.isfile("%s/%s" % (logo_dir, row['logo'])):
			image_with_path = "/logo/%s" % row['logo']
		else:
			print("WARNING: %s logo %s file not found" % (group_name, row['logo']))
			image_with_path = ''

	print("Add %s %s = %s" % (group_name, image_with_path, group_title))

	# Group to be added/updated
	group_dict = {}

	# First check that the group doesn't already exist
	create_or_update_action = 'group_create'
	if group_name in groups_names:
		print("NOTE: %s already exists, will update" % group_name)
		create_or_update_action = 'group_patch' # not group_update which cleans it all first
		# Find the id of the given group to update this exact one
		group_dict['id'] = [i for i in groups_data if i['name']==group_name][0]['id']
		#group_dict['clear_upload'] = True # so that a change to image_url is forced

	# Create a dictionary with the info we need to add to CKAN
	group_dict['name'] = group_name
	group_dict['title'] = group_title
	group_dict['image_url'] = image_with_path
	if group_desc:
		group_dict['description'] = group_desc
	print("Running %s with %s" % (create_or_update_action, group_dict))

	result = ckan.call_action(create_or_update_action, group_dict)
	if result['approval_status'] == 'approved':
		print("Added (approved) group: %s" % group_name)
		#pprint(result)
	else:
		print("ERROR adding %s :" % group_name)
		pprint(result)
		exit(1)
	return


# -----------------------------------------------------------------------
# MAIN

# CSV filename is first parameter
if len(sys.argv) > 1:
	csv_filename = sys.argv[1]

# Read the configuration
ckan_ip = open("ckan_ip.txt").read().replace('\n','')
api_key = open("ckan_api_key.txt").read().replace('\n','')

# Read in the CSV file
fp = open(csv_filename)
reader = csv.DictReader(fp)

# Open the connection to the CKAN server
ckan = RemoteCKAN('http://%s' % ckan_ip, apikey=api_key, user_agent=user_agent)

groups_data = get_existing_groups_dict()
groups_names = get_existing_groups_names(groups_data)

# Process each row
for row in reader:
	#print("Add group: %s" % row['group'])
	add_group(row)

# Close
RemoteCKAN.close(ckan)
fp.close()

exit(0)
