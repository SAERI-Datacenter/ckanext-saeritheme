# 1.02 arb Thu Jan 17 16:23:06 GMT 2019 - added search filter facets
# XXX arb commented out toolkit.add_resource

import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class SaerithemePlugin(plugins.SingletonPlugin):
    ''' SAERI theme plugin
    '''
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IFacets) # to add a search filter facet

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
#        toolkit.add_resource('fanstatic', 'saeritheme')

    def dataset_facets(self, facets_dict, package_type):
        '''Add new search facet (filter) for datasets.
        This must be a field in the dataset (or organization or
        group if you're modifying those search facets, just change the function).
        '''
        # This keeps the existing facet order.
        # Just add whichever fields you want to filter by:
        facets_dict['saeri_region'] = plugins.toolkit._('Region')
        facets_dict['saeri_topic_category'] = plugins.toolkit._('Topic')

        # Return the updated facet dict.
        return facets_dict
