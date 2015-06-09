from rtems_waf.config import Default, Config

class Base(Config):
	arch = name = "v850"
	conflicts=("clang",)



class v850_shared(Base):
	def build(self, c):
		c.CFLAGS		= ['-mtune=i386']
#		c.LDFLAGS		= ['-Wl,-Ttext,0x00100000']
		c.LINKCMDS		= ['src/lib/libbsp/v850/gdbv850sim/startup/linkcmds']
		c.LINK_START	= ['${RTEMS}/start.o', '-e', 'start']
#		c.LINK_END		= ['crtend.o', 'crtn.o']
#		c.ENABLE_NETWORKING	= True

#	def header(self, c):
#		c.BSP_HAS_SMP		= Default
#		c.BSP_VIDEO_80x50		= Default
#		c.CLOCK_DRIVER_USE_8254		= Default
#		c.CLOCK_DRIVER_USE_TSC		= Default
#		c.IDE_USE_PRIMARY_INTERFACE		= Default
#		c.IDE_USE_SECONDARY_INTERFACE		= Default
#		c.USE_COM1_AS_CONSOLE		= Default
#		c.BSP_PRESS_KEY_FOR_RESET	= True


class v850e1sim(v850_shared):
	name = "v850/v850e1sim"

	def build(self, c):
		c.CFLAGS		= ["-mv850e1",]


class v850e2sim(v850_shared):
	name = "v850/v850e2sim"

	def build(self, c):
		c.CFLAGS		= ["-mv850e2",]


class v850e2v3sim(v850_shared):
	name = "v850/v850e2v3sim"

	def build(self, c):
		c.CFLAGS		= ["-mv850e2v3",]


class v850esim(v850_shared):
	name = "v850/v850esim"

	def build(self, c):
		c.CFLAGS		= ["-mv850e",]


class v850essim(v850_shared):
	name = "v850/v850essim"

	def build(self, c):
		c.CFLAGS		= ["-mv850es",]


class v850sim(v850_shared):
	name = "v850/v850sim"

	def build(self, c):
		c.CFLAGS		= ["-mv850",]


