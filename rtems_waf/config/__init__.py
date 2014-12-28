from .base import BuildConfig, Config, Default, Feature, Disable
from .feature import *
from .options import *

from rtems_waf import defaults

#XXX: Fix
# Test to make sure options are sane.
#for option in options_map:
#	a = options_map[option]()

