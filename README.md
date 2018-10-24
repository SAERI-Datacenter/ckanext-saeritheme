# ckanext-saeritheme

## Requirements

This plugin now requires the spatial extension
https://docs.ckan.org/projects/ckanext-spatial/en/latest/
because it adds a map widget to the search filter column.

## Installation

first activate your virtual environment
```
cd /usr/lib/ckan/default/src
git clone https://github.com/SAERI-Datacenter/ckanext-saeritheme.git
cd ckanext-saeritheme
python setup.py develop
```
then add `saeritheme` to the `ckan.plugins` line in your ckan config file and restart the web server with sudo service apache2 restart

## Updating

cd /usr/lib/ckan/default/src/ckanext-saeritheme
git pull
sudo service apache2 restart
