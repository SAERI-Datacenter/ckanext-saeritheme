# ckanext-saeritheme

## Installation

first activate your virtual environment
```
cd /usr/lib/ckan/default/src
git clone https://github.com/SAERI-Datacenter/ckanext-saeritheme.git
cd ckanext-saeritheme
python setup.py develop
```
then add `saeritheme` to the `ckan.plugins` line in your ckan config file and restart the web server with sudo service apache2 restart
