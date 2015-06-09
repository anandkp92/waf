from rtems_waf.config import Default, Config

class Base(Config):
	arch = name = "mips"
	conflicts=("clang",)

	def build(self, c):
		c.LINK_START	= ['${RTEMS}/start.o', 'crti.o', 'crtbegin.o', '-e', 'start']
		c.LINK_END	= ['crtend.o', 'crtn.o']


class csb350(Base):
	name = "mips/csb350"

	def build(self, c):
		c.CFLAGS		= ['-mips32', '-G0', '-msoft-float']
		c.LDFLAGS		= ['-msoft-float']
		c.LINKCMDS		= ['src/lib/libbsp/mips/csb350/startup/linkcmds']
		c.LINK_START	= ['${RTEMS}/start.o', 'crti.o', 'crtbegin.o', '-e', '_start']


class genmongoosev(Base):
	name = "mips/genmongoosev"

	def build(self, c):
		c.CFLAGS		= ['-mips1', '-G0']
		c.LINKCMDS		= ['src/lib/libbsp/mips/genmongoosev/startup/linkcmds']


class hurricane(Base):
	name = "mips/hurricane"

	def build(self, c):
		c.CFLAGS		= ['-mips3', '-G0', '-EL']
		c.LINKCMDS		= ['src/lib/libbsp/mips/hurricane/startup/linkcmds']
		c.LINK_LINK		= ['-EL'] # work around gcc driver bug

	def header(self, c):
		c.BSP_HAS_RM52xx		= Default
		c.BSP_HAS_USC320		= Default



class jmr3904(Base):
	name = "mips/jmr3904"

	def build(self, c):
		c.CFLAGS		= ['-march=r3900', '-Wa,-xgot', '-G0']
		c.LINKCMDS		= ['src/lib/libbsp/mips/jmr3904/startup/linkcmds']



class malta(Base):
	name = "mips/malta"

	def build(self, c):
		c.CFLAGS		= ['-march=24kf1_1', '-Wa,-xgot', '-G0']
		c.LINKCMDS		= ['src/lib/libbsp/mips/malta/startup/linkcmds']


class rbtx4925(Base):
	name = "mips/rbtx4925"

	def build(self, c):
		c.CFLAGS		= ['-mips3', '-G0', '-EL']
		c.LINKCMDS		= ['src/lib/libbsp/mips/rbtx4925/startup/linkcmds']
		c.LINK_LINK		= ['-EL'] # work around gcc driver bug

	def header(self, c):
		c.BSP_HAS_TX49xx		= Default



class rbtx4938(Base):
	name = "mips/rbtx4938"

	def build(self, c):
		c.CFLAGS		= ['-mips3', '-G0', '-EL']
		c.LINKCMDS		= ['src/lib/libbsp/mips/rbtx4938/startup/linkcmds']
		c.LINK_LINK		= ['-EL'] # work around gcc driver bug
