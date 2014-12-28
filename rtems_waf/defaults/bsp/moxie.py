from rtems_waf.config import Default, Config

class Base(Config):
	arch = name = "moxie"
	conflicts=("clang",)

	def build(self, c):
		c.LINK_START		= ['${RTEMS}/start.o', '-e', '_start']


class moxiesim(Base):
	name = "moxie/moxiesim"

	def build(self, c):
		c.LDFLAGS		= ['-Wl,--gc-sections']
		c.LINKCMDS		= ['src/lib/libbsp/moxie/moxiesim/startup/linkcmds']

