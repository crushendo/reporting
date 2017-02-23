# wsgi.py

activate_this = '/home/lbadmin/projects18/scoutingEnv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import os, sys
# Calculate the path based on the location of the WSGI script
apache_configuration= os.path.dirname(__file__)
project = os.path.dirname(apache_configuration)
workspace = os.path.dirname(project)
sys.path.append(workspace)
sys.path.append(project)

# Add the path to 3rd party django application and to django itself.
sys.path.append('/home/lbadmin/projects18')
os.environ['DJANGO_SETTINGS_MODULE'] = 'reporting.apache.override'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
