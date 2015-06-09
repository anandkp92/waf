from py.config import Default, Config

class Base(Config):
	arch = name = "sparc64"
	conflicts=("clang",)

	def build(self, c):
		c.LINKCMDS		= ['src/lib/libbsp/sparc64/shared/startup/linkcmds']
		c.LINK_START	= ['${RTEMS}/start.o', 'crtbegin.o', '-e', '_start']
		c.LINK_END		= ['crtend.o']


class niagara(Base):
	name = "sparc64/niagara"

	def build(self, c):
		c.CFLAGS		= ['-mcpu=niagara', '-DSUN4V']


class usiii(Base):
	name = "sparc64/usiii"

	def build(self, c):
		c.CFLAGS		= ['-mcpu=ultrasparc3', '-DUS3', '-DSUN4U']

	def header(self, c):
		c.SIMSPARC_FAST_IDLE		= Default
