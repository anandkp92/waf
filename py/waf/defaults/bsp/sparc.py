from py.config import Default, Config

class Base(Config):
	arch = name = "sparc"
	conflicts=("clang",)

	def build(self, c):
		c.LINK_START	= ['${RTEMS}/start.o', 'crti.o', 'crtbegin.o']
		c.LINK_END		= ['crtend.o', 'crtn.o']



class erc32_shared(Base):
	def build(self, c):
		c.CFLAGS		= ['-mcpu=cypress']
		c.LINKCMDS		= ['src/lib/libbsp/sparc/erc32/startup/linkcmds',
					   'src/lib/libbsp/sparc/shared/startup/linkcmds.base']

	def header(self, c):
		c.CONSOLE_USE_INTERRUPTS	= False
		c.ENABLE_SIS_QUIRKS			= Default
		c.SIMSPARC_FAST_IDLE		= Default



class erc32(erc32_shared):
	name = "sparc/erc32"


class sis(erc32_shared):
	name = "sparc/sis"

	def header(self, c):
		c.ENABLE_SIS_QUIRKS			= True



class leon2(Base):
	name = "sparc/leon2"

	def build(self, c):
		c.CFLAGS		= ['-mcpu=cypress']
		c.LINKCMDS		= ['src/lib/libbsp/sparc/leon2/startup/linkcmds',
					   'src/lib/libbsp/sparc/shared/startup/linkcmds.base']

	def header(self, c):
		c.CONSOLE_USE_INTERRUPTS	= False
		c.SIMSPARC_FAST_IDLE		= Default


class leon3(Base):
	name = "sparc/leon3"

	def build(self, c):
		c.CFLAGS		= ['-mcpu=cypress']
		c.LINKCMDS		= ['src/lib/libbsp/sparc/leon3/startup/linkcmds.leon3',
					   'src/lib/libbsp/sparc/shared/startup/linkcmds.base']

	def header(self, c):
		c.BSP_LEON3_SMP				= Default
		c.CONSOLE_USE_INTERRUPTS	= False
		c.SIMSPARC_FAST_IDLE		= Default
