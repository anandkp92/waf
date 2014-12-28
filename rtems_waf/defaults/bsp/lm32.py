from rtems_waf.config import Default, Config

class Base(Config):
	arch = name = "lm32"
	conflicts=("clang",)

	def build(self, c):
		c.LINK_START	= ['${RTEMS}/start.o', 'crti.o', 'crtbegin.o', '-e', 'start']
		c.LINK_END      = ['crtend.o', 'crtn.o']
		c.LINK_LINK		= ['-dc', '-dp', '-N']



class lm32_evr(Base):
	name = "lm32/lm32_evr"

	def build(self, c):
		c.LINKCMDS		= ['src/lib/libbsp/lm32/lm32_evr/startup/linkcmds']

	def header(self, c):
		c.ON_SIMULATOR		= Default



class milkymist(Base):
	name = "lm32/milkymist"

	def build(self, c):
		c.CFLAGS		= ['-mbarrel-shift-enabled', '-mmultiply-enabled', '-mdivide-enabled', '-msign-extend-enabled']
		c.LINKCMDS		= ['src/lib/libbsp/lm32/milkymist/startup/linkcmds']

	def header(self, c):
		c.ON_SIMULATOR		= Default



