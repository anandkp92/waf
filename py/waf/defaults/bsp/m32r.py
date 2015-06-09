from rtems_waf.config import Default, Config

class Base(Config):
	arch = name = "m32r"
	conflicts=("clang",)



class m32rsim(Base):
	name = "m32r/m32rsim"

	def build(self, c):
		c.LINKCMDS		= ['src/lib/libbsp/m32r/m32rsim/startup/linkcmds']
		c.LINK_START	= ['${RTEMS}/start.o', 'crtinit.o', '-e', '_start']

