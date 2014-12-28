from rtems_waf.config import Default, Config

class Base(Config):
	arch = name = "bfin"
	conflicts=("clang",)



class bf537stamp(Base):
	name = "bfin/bf537stamp"

	def build(self, c):
		c.LINKCMDS		= ['src/lib/libbsp/bfin/bf537Stamp/startup/linkcmds']
		c.LINK_START	= ['${RTEMS}/start.o', '-e', '__start']

	def header(self, c):
		c.BFIN_ON_SKYEYE				= Default
		c.CONSOLE_USE_INTERRUPTS		= Default



class ezkit533(Base):
	name = "bfin/ezkit533"

	def build(self, c):
		c.LINKCMDS		= ['src/lib/libbsp/bfin/eZKit533/startup/linkcmds']
		c.LINK_START	= ['${RTEMS}/start.o', '-e', '__start']

	def header(self, c):
		c.BFIN_ON_SKYEYE				= Default
		c.CONSOLE_USE_INTERRUPTS		= Default



class tll6527m(Base):
	name = "bfin/tll6527m"

	def build(self, c):
		c.CFLAGS		= ['-mcpu=bf527']
		c.LINKCMDS		= ['src/lib/libbsp/bfin/TLL6527M/startup/linkcmds']
		c.LINK_START	= ['${RTEMS}/start.o', '-e', '__start']

	def header(self, c):
		c.BFIN_ON_SKYEYE			= Default
		c.CONSOLE_BAUDRATE			= 9600
		c.CONSOLE_USE_INTERRUPTS	= False
		c.INTERRUPT_USE_TABLE		= Default
		c.UART_USE_DMA				= Default
