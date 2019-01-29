# Installation

You MUST create two files: `ckan_ip.txt` contains the IP address of your CKAN server, or it may be the name `localhost`, and `ckan_api_key.txt` contains the API key of your sysadmin
 account (or an account which has sufficient permissions). The API key can be found once logged into CKAN on your profile page (it's at the bottom of the left-hand column).
These values were hard-coded into the scripts which caused problems so they are now read from config files.

After entering your virtual environment you should `pip install ckanapi`

Remember to make the symbolic link as described in this plugin's README.

# Groups

List of groups (themes or topic categories) to be created inside CKAN.

Master list is `topic_categories.csv`

## File format

csvname,group,title,description,logo

The csvname is the name used in the topic_category column of the metadata_FK CSV file
so that we can map from the topic_category field to a group name.
The group field is the short group name which is used in the URL.
The title is a one line description and the description can be longer.
The logo file is the image filename which will have /logo/ prepended
and will be found via the symbolic link as described above.

## Add groups from CSV into CKAN

Run `./ckan_add_groups.py`

If a group already exists then it will be updated.

## Rename Groups to Themes

Run `rename_groups_to_themes.sh` to change the wording of Groups in the interface to use Themes instead. Does not replace all occurrences, only the main ones. This modifies your ckan installation outside this plugin.

# Organisations

List of organisations to be created inside CKAN.

Master list was grouped_organisations_ready_2018-12-07.csv

Modified by arb grouped_organisations_ready_arb.csv (for changes see below)

Note that it is spelled with a z inside CKAN as organizations.

## File format

organisation,organisation_name,organisation_logo,records_count

## List organisations already in CKAN

Run `./ckan_list_organisations.py`

## Add organisations from CSV into CKAN

Run `./ckan_add_organisations.py`

If an organisation already exists then it will be updated.

## Update the organisations

There are some organisations which do not have a logo image.
They will show the CKAN default image.
This could be modified to show the nologo_cube.png file if required.

Do NOT change the organisation code because it will have been
embedded into dataset records in the database.

## Changes by arb

Modified the list of organisations to correct some errors such as spaces, duplicated entry, capitalisation, etc. Also renamed .jpeg to .jpg and made all logo filenames lowercase (they were already lowercase in the CSV but not as files).
```
mv UNIGIESSEN.png unigiessen.png
mv UCPH.png ucph.png
mv ESRG.jpg esrg.jpg
mv UKHO.jpg ukho.jpg
mv WCS.png wcs.png
mv NMW.gif nmw.gif
mv FOGL.jpg fogl.jpg
mv aad.jpeg aad.jpg
mv fitb.jpeg fitb.jpg
mv smsg.jpeg smsg.jpg
```

Differences:
```
2c2
< AAD,Australian Antarctic Division,aad.jpeg,1
---
> AAD,Australian Antarctic Division,aad.jpg,1
11c11
< BRIGGS,Briggs Marine ,briggs.png,4
---
> BRIGGS,Briggs Marine,briggs.png,4
13c13
< Bhabitat,,,1
---
> Bhabitat,BHabitat,,1
18c18
< CU,Penguin International Ltd,pein.png,1
---
> PEIN,Penguin International Ltd,pein.png,1
31,32c31,32
< FITB,Falkland Islands Tourist Board,fitb.jpeg,2
< FMEBD,fundacion Migres,fmebd.jpg,1
---
> FITB,Falkland Islands Tourist Board,fitb.jpg,2
> FMEBD,Fundacion Migres,fmebd.jpg,1
41,42c41,42
< MNHN,museum national d'histoire naturelle,mnhn.jpg,1
< MOD,ministry of defence,mod.jpg,4
---
> MNHN,Museum National d'Histoire Naturelle,mnhn.jpg,1
> MOD,Ministry of Defence,mod.jpg,4
54,55c54,55
< SMSG,Shallow Marine Surveys Group,smsg.jpeg,4
< UCHILE,universidad de chile,uchile.jpg,2
---
> SMSG,Shallow Marine Surveys Group,smsg.jpg,4
> UCHILE,Universidad de Chile,uchile.jpg,2
60,62c60,61
< UKFIT,UK Falkland Island Trust,ukfit.png,3
< UKHO,UK Hydrographic Office,ukho.jpg,3
< UKHO,UK Hydrographic Office ,ukho.jpg,1
---
> UKFIT,UK Falkland Islands Trust,ukfit.png,3
> UKHO,UK Hydrographic Office,ukho.jpg,4
69c68
< UNIMSU,Michigan State University ,unimsu.png,1
---
> UNIMSU,Michigan State University,unimsu.png,1
```

Also on 21 Jan 2019 updated some logo files and a couple of other changes, see the commit for details.
