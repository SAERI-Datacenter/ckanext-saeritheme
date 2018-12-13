#!/usr/bin/env python2
# Create all organisations from a CSV file

import urllib2
import urllib
import json
from pprint import pprint
import csv
from ckanapi import RemoteCKAN

# Configuration
csv_filename="grouped_organisations_ready_arb.csv"
ckan_ip = "172.16.92.142"
api_key = "0317c21c-7d04-48df-8f1b-9989edbd6165"
user_agent = 'ckanapiexample/1.0 (+http://example.com/my/website)'

# CSV fields are:
# organisation,organisation_name,organisation_logo,records_count

# -----------------------------------------------------------------------
# field names which can be set:
# name (lowercase, no spaces)
# id / title / description
# image_url
# eg.
#'description': u'Can be deleted',
#'image_url': u'',
#'name': u'testorg',
#'title': u'Test Organization',

# ---------------------------------------------------------------------
# Return a list of organisation names, eg. ['BAS', 'FIG']
def get_existing_organisations():
	organisations_data = ckan.action.organization_list(all_fields=True)
	#pprint(organisations_data)
	organisations_list = [x['name'] for x in organisations_data]
	return(organisations_list)


# ---------------------------------------------------------------------
# Add one organisation to CKAN from the CSV data given in row
# i.e. row['organisation'] and organisation_name and organisation_logo.
def add_organisation(row):
	# Sanitise the input
	name_lowercase = row['organisation'].lower()
	if row['organisation_logo'] == '':
		image_with_path = ''
	else:
		image_with_path = "/logo/%s" % row['organisation_logo']
	fullname = row['organisation_name']
	print("Add %s %s = %s" % (name_lowercase, image_with_path, fullname))

	# First check that the organisation doesn't already exist
	if name_lowercase in organisations:
		#print("%s already in %s" % (name_lowercase, organisations))
		print("WARNING %s already in use, not added" % name_lowercase)
		return

	# Create a dictionary with the info we need to add to CKAN
	org_dict = {
		'name' : name_lowercase,
		'title': row['organisation_name'],
		'image_url': image_with_path }
	print("Adding %s" % org_dict)

	result = ckan.call_action('organization_create', org_dict)
	#pprint(result)
	if result['approval_status'] == 'approved':
		print("Added %s" % name_lowercase)
	else:
		print("ERROR adding %s :" % name_lowercase)
		pprint(result)
		exit(1)
	return


# -----------------------------------------------------------------------
# MAIN

# Read in the CSV file
fp = open(csv_filename)
reader = csv.DictReader(fp)

# Open the connection to the CKAN server
ckan = RemoteCKAN('http://%s' % ckan_ip, apikey=api_key, user_agent=user_agent)

organisations = get_existing_organisations()

# Process each row
for row in reader:
	add_organisation(row)

# Close
RemoteCKAN.close(ckan)
fp.close()

exit(0)
