from rtems_waf.config import Default, Config

class Base(Config):
	arch = name = "avr"
	conflicts=("clang",)



class avrtest(Base):
	name = "avr/avrtest"

	def build(self, c):
		c.LINKCMDS		= ['src/lib/libbsp/avr/avrtest/startup/linkcmds']
		c.LINK_START	= ['${RTEMS}/start.o', '-e', '__init']

