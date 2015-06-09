from .base import BuildConfig, Config, Default, Feature, Disable
from .feature import *
from .options import *

from py.waf import defaults # XXX: This needs to be removed as no dependencies from config -> waf are allowed.


#XXX: Fix
# Test to make sure options are sane.
#for option in options_map:
#	a = options_map[option]()

