from rtems_waf.config import Default, Config

class Base(Config):
	arch = name = "i386"
	conflicts=("clang",)



class pc386_shared(Base):
	def build(self, c):
		c.CFLAGS		= ['-mtune=i386']
		c.LDFLAGS		= ['-Wl,-Ttext,0x00100000']
		c.LINKCMDS		= ['src/lib/libbsp/i386/pc386/startup/linkcmds']
		c.LINK_START		= ['${RTEMS}/start.o', 'crti.o', 'crtbegin.o', '-e', 'start']
		c.LINK_END		= ['crtend.o', 'crtn.o']
		c.ENABLE_NETWORKING	= True

	def header(self, c):
		c.BSP_HAS_SMP		= Default
		c.BSP_VIDEO_80x50		= Default
		c.CLOCK_DRIVER_USE_8254		= Default
		c.CLOCK_DRIVER_USE_TSC		= Default
		c.IDE_USE_PRIMARY_INTERFACE		= Default
		c.IDE_USE_SECONDARY_INTERFACE		= Default
		c.USE_COM1_AS_CONSOLE		= Default
		c.BSP_PRESS_KEY_FOR_RESET	= True


class pc486(pc386_shared):
	name = "i386/pc486"

	def build(self, c):
		c.CFLAGS		= ['-mtune=i486']
		c.LINKCMDS		= ['src/lib/libbsp/i386/pc386/startup/linkcmds']


class pc386(pc386_shared):
	name = "i386/pc386"

	def build(self, c):
		c.CFLAGS		= ['-mtune=i386']
		c.LINKCMDS		= ['src/lib/libbsp/i386/pc386/startup/linkcmds']



class pc686(pc386_shared):
	name = "i386/pc686"

	def build(self, c):
		c.CFLAGS		= ['-mtune=pentiumpro']
		c.LINKCMDS		= ['src/lib/libbsp/i386/pc386/startup/linkcmds']


class pc586_sse(pc386_shared):
	name = "i386/pc586-sse"

	def build(self, c):
		c.CFLAGS		= ['-mtune=i386']
		c.LINKCMDS		= ['src/lib/libbsp/i386/pc386/startup/linkcmds']


class pc586(pc386_shared):
	name = "i386/pc586"

	def build(self, c):
		c.CFLAGS		= ['-mtune=pentium']
		c.LINKCMDS		= ['src/lib/libbsp/i386/pc386/startup/linkcmds']


class pcp4(pc386_shared):
	name = "i386/pcp4"

	def build(self, c):
		c.CFLAGS		= ['-mtune=pentium4', '-march=pentium4', '-msse3']
