import os
import importlib
import sys

env = os.environ.get("DJANGO_ENV", 'dev')

django_setting = importlib.import_module(
    f'.{env}', 'config')


# https://stackoverflow.com/questions/21221358/python-how-to-import-all-methods-and-attributes-from-a-module-dynamically#answer-21221452
# dinamically loading settings based on DJANGO_ENV variable
# all the code below simulate the statement 'from .module import *'
module_dict = django_setting.__dict__
try:
    to_import = django_setting.__all__
except AttributeError:
    to_import = [name for name in module_dict if not name.startswith('_')]
globals().update({name: module_dict[name] for name in to_import})


# if os.environ['DJANGO_ENV'] == 'prod':
#     from .prod import *
# elif os.environ['DJANGO_ENV'] == 'staging':
#     from .staging import *
# elif os.environ['DJANGO_ENV'] == 'dev':
#     from .dev import *
# else:
#     raise Exception('DJANGO_ENV env variable must be dev, staging or prod')
