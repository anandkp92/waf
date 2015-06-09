from rtems_waf.config import Default, Config

class Base(Config):
	arch = name = "h8300"
	conflicts=("clang",)



class h8sim_shared(Base):
	def build(self, c):
		c.LINKCMDS		= ['src/lib/libbsp/h8300/h8sim/startup/linkcmds']
		c.LINK_START	= ['${RTEMS}/start.o', '-e', '_start']

class h8sxsim(h8sim_shared):
	name = "h8300/h8sxsim"

	def build(self, c):
		c.LINKCMDS		= ['src/lib/libbsp/h8300/h8sim/startup/linkcmds']


class h8sim(h8sim_shared):
	name = "h8300/h8sim"

	def build(self, c):
		c.LINKCMDS		= ['src/lib/libbsp/h8300/h8sim/startup/linkcmds']


