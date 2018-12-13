# Organisations

List of organisations to be created inside CKAN.

Master list was grouped_organisations_ready_2018-12-07.csv

Modified by arb grouped_organisations_ready_arb.csv (for changes see below)

Note that it is spelled with a z inside CKAN as organizations.

# File format

organisation,organisation_name,organisation_logo,records_count

# Installation

First edit all scripts to change the IP address of the CKAN server
and the API key of the system administrator
(the one given in the script will not work).

After entering your virtual environment you should `pip install ckanapi`

# List organisations already in CKAN

Run `ckan_list_organisations.py`

# Add organisations from CSV into CKAN

Run `ckan_add_organisations.py`

# Update the organisations

There are some organisations which do not have a logo image.

Do NOT change the organisation code because it will have been
embedded into dataset records in the database.

# Changes by arb

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
