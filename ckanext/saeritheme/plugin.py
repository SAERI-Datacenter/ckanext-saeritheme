# XXX arb commented out toolkit.add_public_directory and toolkit.add_resource
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class SaerithemePlugin(plugins.SingletonPlugin):
    ''' SAERI theme plugin
    '''
    plugins.implements(plugins.IConfigurer)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
#        toolkit.add_public_directory(config_, 'public')
#        toolkit.add_resource('fanstatic', 'saeritheme')
