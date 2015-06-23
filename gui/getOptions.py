from py.waf import defaults
from py.config.tool import get_option_class, get_config_class
from py.config import RTEMSConfig

'''get dictionary of options from py/waf/defaults/options.py'''
option = get_option_class(defaults)
print option

'''get list of classes from each file in py/waf/defaults/bsp'''
config = get_config_class(defaults.bsp)
	
r = RTEMSConfig(option, config)
print "Name\tType\tGroup"
for a in r.options_get():
	print a.__name__,"\t", a.__base__.__name__, "\t", a.tag

