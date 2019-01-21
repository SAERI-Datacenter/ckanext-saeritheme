# 1.02 arb Thu Jan 17 16:23:06 GMT 2019 - added search filter facets

# This plugin defines the theme for CKAN.  All it does is
# adds 'templates' and 'public' directories to the search path so that
# any files you place in them will override or supplement the built-in ones.
# It also add search filters to the left-hand column of search results
# so that search results can be filtered by any of our custom fields,
# which must have been defined in our schema plugin.

# Theme plugins are documented here:
# https://docs.ckan.org/en/latest/theming/templates.html
# Search filter facets are documented here:
# https://docs.ckan.org/en/latest/extensions/plugin-interfaces.html?highlight=ifacet#ckan.plugins.interfaces.IFacets
# https://stackoverflow.com/questions/32175329/how-to-add-a-search-filter-facet-option-for-a-custom-field-in-ckan
# https://jira.ucar.edu/browse/DSET-168 (solve AttributeError: 'SaerithemePlugin' object has no attribute 'organization_facets')


import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class SaerithemePlugin(plugins.SingletonPlugin):
    ''' SAERI theme plugin
    '''
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IFacets, inherit=True) # to add a search filter facet (need to inherit to get the organization_facets attribute)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        #toolkit.add_resource('fanstatic', 'saeritheme') # not needed

    def dataset_facets(self, facets_dict, package_type):
        '''Add new search facet (filter) for datasets.
        This must be a field in the dataset (or organization or
        group if you're modifying those search facets, just change the function).
        '''
        # Doing it this way keeps the existing facet order.
        # Just add whichever fields you want to filter by:
        facets_dict['saeri_region'] = plugins.toolkit._('Region')
        facets_dict['saeri_topic_category'] = plugins.toolkit._('Topic')

        # Return the updated facet dict.
        return facets_dict
