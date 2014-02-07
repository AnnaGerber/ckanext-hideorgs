This is a CKAN extension that removes CKAN's organizations
feature from CKAN's web interface.

It is based on http://github.com/okfn/ckanext-hidegroups

To install, activate your CKAN virtualenv then run:

    pip install -e 'git+git://github.com/AnnaGerber/ckanext-hideorgs.git#egg=ckanext-hideorgs'

Then add the plugin to your CKAN config file (e.g. `development.ini` or
`production.ini`), for example:

  ckan.plugins = stats text_preview recline_preview hideorgs
