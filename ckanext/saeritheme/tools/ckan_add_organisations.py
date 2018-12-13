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
	print("Add %s %s = %s" % (row['organisation'], row['organisation_logo'], row['organisation_name']))
	name_lowercase = row['organisation'].lower()
	# First check that the organisation doesn't already exist
	if name_lowercase in organisations:
		#print("%s already in %s" % (name_lowercase, organisations))
		print("WARNING %s already in use, not added" % name_lowercase)
		return
	# Create a dictionary with the info we need to add to CKAN
	org_dict = {
		'name' : name_lowercase,
		'title': row['organisation_name'],
		'image_url': "/logo/%s" % row['organisation_logo'] }
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

# ---------------------

# Put the details of the dataset we're going to create into a dict.
dataset_dict = {
    'name': 'test_dataset',
    'notes': 'A long description of my test dataset',
    'owner_org': 'saeri'
}

# Use the json module to dump the dictionary to a string for posting.
data_string = urllib.quote(json.dumps(dataset_dict))

# We'll use the package_create function to create a new dataset.
request = urllib2.Request('http://publicamundi/api/action/package_create')


# Use the json module to load CKAN's response into a dictionary.
response_dict = json.loads(response.read())
assert response_dict['success'] is True

# package_create returns the created package as its result.
created_package = response_dict['result']
pprint.pprint(created_package)

#!/usr/bin/env python2




# Two ways to call an action:
datasets = ckan.action.package_search(include_private=True, include_drafts=True, q='"test-dataset-3"')
#datasets = ckan.call_action('package_search', {'include_private':True, 'include_drafts':True} )
#print(datasets['count'])
#pprint(datasets)

for result in datasets['results']:
	print("%s = %s" % ( result['id'], result['name']))
	for resource in result['resources']:
		print("  resource %s" % resource['url'])

