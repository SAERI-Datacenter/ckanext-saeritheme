# ckanext-saeritheme

This CKAN plugin implements the changes required to customise a CKAN installation specifically for SAERI.

The main things done in this plugin are: display the SAERI logo, and display a map in the dataset create/update and dataset search pages. Note that the map display has other requirements (all the spatial plugin configured correctly and the saerischema plugin).

This plugin also contains all of the logo images required for the organisations and groups (themes) which will be created within CKAN.

## Requirements

This plugin now requires the spatial extension
https://docs.ckan.org/projects/ckanext-spatial/en/latest/
because it adds a map widget to the search filter column.

## Installation

first activate your virtual environment, then
```
cd /usr/lib/ckan/default/src
git clone https://github.com/SAERI-Datacenter/ckanext-saeritheme.git
cd ckanext-saeritheme
python setup.py develop
```

Add `saeritheme` to the `ckan.plugins` line in your ckan config file (typically `/etc/ckan/default/production.ini`).

Make the logo images accessible
using `sudo ln -s /usr/lib/ckan/default/src/ckanext-saeritheme/ckanext/saeritheme/public/logo /var/lib/ckan/default/storage/uploads/group/logo`
(this is because CKAN expects them to be in the uploads folder, 
it is hard-coded in here: `/usr/lib/ckan/default/src/ckan/ckan/lib/dictization/model_dictize.py`)

Restart the web server with `sudo service apache2 restart`

## Customising

The ckanext/saeritheme/tools directory contains some tools for creating organisations.

## Updating

```
cd /usr/lib/ckan/default/src/ckanext-saeritheme
git pull
sudo service apache2 restart
```

## Customising

Remember that some useful customisations can be made simply by editing the config file (`/etc/ckan/default/production.ini`) for example the About page text and the logo. The About text is written in Markdown and can span multiple lines (indent subsequent lines). See https://docs.ckan.org/en/2.8/sysadmin-guide.html#customizing-look-and-feel

The CSS can be edited in `ckanext/saeritheme/public/saeritheme.css` (this file is called from `ckanext/saeritheme/templates/base.html` - see https://docs.ckan.org/en/2.8/theming/css.html)

The background image on the home page is defined in the CSS file.

The home page is index.html but that simply include layoutN.html where N is the theme number. In our case this is layout1.html.
The home page is constructed from blocks so we extend or replace the default layout by editing `ckanext/saeritheme/templates/home/layout1.html`

Images (and other resources) which are required by the HTML files can be placed in the directory: `ckanext/saeritheme/public`.  The logo images in there are referenced directly by the symbolic link created earlier so can be updated live.

Home page logo - we display the SAERI logo instead of the "promoted" field by editing: `ckanext/saeritheme/templates/home/snippets/promoted.html`. The logo image is stored in the public directory (see above).

Home page showing recent activity (new/updated datasets) - this could be enabled by uncommenting the line in `ckanext/saeritheme/templates/home/layout1.html` but last time I tried it only raw HTML was displayed.

Map display - there are two places to edit. One is when searching for datasets which cover a specific area, the map needs to be displayed on the search page; done by `ckanext/saeritheme/templates/package/search.html`. The other is when creating/updating a dataset, the map showing the spatial extent is displayed at the bottom of the page by `ckanext/saeritheme/templates/package/read.html`. If you want the map displayed in the left-hand column (sidebar) the use `ckanext/saeritheme/templates/package/read_base.html` instead by commenting/uncommenting the line in both files as appropriate.

## To do

Use the map to _enter_ the spatial extent when creating (and updating?) a dataset. At the moment the extent is taken from the N,S,E,W fields (assumed to be in degrees WGS84). It would be good if it could be entered visually by dragging on the map. (This is possible, but not implemented yet).
