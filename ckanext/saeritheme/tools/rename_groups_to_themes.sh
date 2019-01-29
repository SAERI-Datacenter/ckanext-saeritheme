#!/bin/bash

# This program modifies CKAN to use a 'translation' (British English)
# which is then changed to use the word Theme instead of Group.
# Not all occurrences are replaced but the main ones are.
# This program can safely be run multiple times.
# Requires 'crudini' to be installed.
# For a more comprehensive replacement
# see https://github.com/smallmedia/iod-ckan/issues/19


# Change the path to your CKAN config file:
ini="/etc/ckan/default/production.ini"

# The locale which we will modify:
locale="en_GB"
message_source="/usr/lib/ckan/default/src/ckan/ckan/i18n/${locale}/LC_MESSAGES/ckan.po"

# Enter the virtual environment
cd /usr/lib/ckan/default/src/ckan
. /usr/lib/ckan/default/bin/activate

# Update the translation from the master source
python setup.py update_catalog --locale ${locale}

# Make the modifications to the translation
sed -e 's/^msgstr "Groups"/msgstr "Themes"/'  $message_source
sed -e 's/^msgstr "Group"/msgstr "Theme"/'  $message_source
sed -e 's/^msgstr "Add Group"/msgstr "Add Theme"/'  $message_source
sed -e 's/^msgstr "Edit Group"/msgstr "Edit Theme"/'  $message_source
sed -e 's/^msgstr "Create Group"/msgstr "Create Theme"/'  $message_source
sed -e 's/^msgstr "Update Group"/msgstr "Update Theme"/'  $message_source
sed -e 's/^msgstr "What are Groups?"/msgstr "What are Themes?"/'  $message_source
sed -e 's/^"You can use CKAN Groups to create and manage collections of datasets. "/"You can use CKAN Themes to create and manage collections of datasets. "/'  $message_source

# Compile the new translation
python setup.py compile_catalog --use-fuzzy --locale ${locale}

# Update the CKAN config file to use the new translation
crudini --set --inplace $ini app:main ckan.locale_default en_GB
crudini --set --inplace $ini app:main ckan.locales_offered en_GB
crudini --set --inplace $ini app:main ckan.locales_filtered_out '' # was en_GB!!
crudini --set --inplace $ini app:main ckan.locale_order "en_GB en pt_BR ja it cs_CZ ca es fr el sv sr sr@latin no sk fi ru de pl nl bg ko_KR hu sa sl lv"

exit 0

# ---------------------------------------------------------------------

Also could edit:
msgstr "This group has no description"
msgstr "Group"
msgstr "No groups"
msgstr "Group not found"
msgstr "Incorrect group type"
msgstr "Unauthorised to create a group"
msgstr "Unauthorised to delete group %s"
msgstr "Group has been deleted."
msgid "Unauthorized to create group %s members"
msgstr "CKAN Group Revision History"
msgstr "Recent changes to CKAN Group: "
msgstr "{actor} updated the group {group}"
msgstr "{actor} deleted the group {group}"
msgstr "{actor} created the group {group}"
msgstr "group"
msgstr "That group name or ID does not exist."
msgstr "Group name already exists in database"
msgstr "Trying to create an organisation as a group"
msgstr "You must be logged in to follow a group."
msgstr "User %s not authorised to create groups"
msgstr "Group was not found."
msgstr "User %s not authorised to edit group %s"
msgstr "User %s not authorised to delete groups"
msgstr "User %s not authorised to delete group %s"
msgstr "User %s not authorised to read group %s"
msgstr "User %s not authorised to change state of group %s"
msgstr "User %s not authorised to edit permissions of group %s"
msgstr "Add a Group"
msgstr "Group Form"
msgstr "Are you sure you want to delete group - {name}?"
msgstr "Edit Group"
msgstr "Add Group"
msgstr "Create a Group"
msgstr "Update Group"
msgstr "Create Group"
msgstr "Datasets in group: {group}"
msgstr "My Group"
msgstr "my-group"
msgstr "A little information about my group..."
msgstr "Are you sure you want to delete this Group?"
msgid "Save Group"
msgstr "Save Group"
msgstr "Remove dataset from this group"
msgstr "What are Groups?"
"You can use CKAN Groups to create and manage collections of datasets. "
msgstr "groups"
msgstr "Associate this group with this dataset"
msgstr "Add to group"
msgstr "There are no groups associated with this dataset"
msgstr "My Groups"
msgstr "You are not a member of any groups."
msgstr "Create datasets, groups and other exciting things"
msgstr[0] "{number} group found for \"{query}\""
msgstr[1] "{number} groups found for \"{query}\""
msgstr "No groups found for \"{query}\""
msgstr[0] "{number} group found"
msgstr[1] "{number} groups found"
msgstr "No groups found"

