from rtems_waf.config import Default, Config

class Base(Config):
	arch = name = "m68k"
	conflicts=("clang",)

	def build(self, c):
		c.LINK_START	= ['${RTEMS}/start.o', 'crti.o', 'crtbegin.o', '-e', 'start']
		c.LINK_END	= ['crtend.o', 'crtn.o']


class av5282(Base):
	name = "m68k/av5282"

	def build(self, c):
		c.CFLAGS		= ['-mcpu=528x']
		c.LINKCMDS		= ['src/lib/libbsp/m68k/av5282/startup/linkcmds']

class csb360(Base):
	name = "m68k/csb360"

	def build(self, c):
		c.CFLAGS		= ['-mcpu=5272']
		c.LINKCMDS		= ['src/lib/libbsp/m68k/csb360/startup/linkcmds']


class gen68302(Base):
	name = "m68k/gen68302"

	def build(self, c):
		c.CFLAGS		= ['-mcpu=68302']
		c.LINKCMDS		= ['src/lib/libbsp/m68k/gen68302/startup/linkcmds']


class gen68340(Base):
	name = "m68k/gen68340"

	def build(self, c):
		c.CFLAGS		= ['-mcpu=cpu32']
		c.LINKCMDS		= ['src/lib/libbsp/m68k/gen68340/startup/linkcmds']


class gen68360_shared(Base):
	def build(self, c):
		c.CFLAGS		= ['-mcpu=cpu32']
		c.LINKCMDS		= ['src/lib/libbsp/m68k/gen68360/startup/linkcmds', 'src/lib/libbsp/m68k/gen68360/startup/linkcmds.bootp', 'src/lib/libbsp/m68k/gen68360/startup/linkcmds.prom']

	def header(self, c):
		c.GEN68360		= True



class gen68360_040(gen68360_shared):
	name = "m68k/gen68360_040"

	def build(self, c):
		c.CFLAGS		= ['-mcpu=68040']
		c.LINKCMDS		= ['src/lib/libbsp/m68k/gen68360/startup/linkcmds', 'src/lib/libbsp/m68k/gen68360/startup/linkcmds.bootp', 'src/lib/libbsp/m68k/gen68360/startup/linkcmds.prom']

	def header(self, c):
		c.GEN68360_040		= True



class pgh360(gen68360_shared):
	name = "m68k/pgh360"

	def build(self, c):
		c.CFLAGS		= ['-mcpu=cpu32']
		c.LINKCMDS		= ['src/lib/libbsp/m68k/gen68360/startup/linkcmds', 'src/lib/libbsp/m68k/gen68360/startup/linkcmds.bootp', 'src/lib/libbsp/m68k/gen68360/startup/linkcmds.prom']

	def header(self, c):
		c.PGH360		= True



class gen68360(gen68360_shared):
	name = "m68k/gen68360"

	def build(self, c):
		c.CFLAGS		= ['-mcpu=cpu32']
		c.LINKCMDS		= ['src/lib/libbsp/m68k/gen68360/startup/linkcmds', 'src/lib/libbsp/m68k/gen68360/startup/linkcmds.bootp', 'src/lib/libbsp/m68k/gen68360/startup/linkcmds.prom']



class genmcf548x_shared(Base):

	def header(self, c):
		c.BSP_CONSOLE_BAUD		= 9600
		c.BSP_CPU_CLOCK_SPEED		= 100000000
		c.HAS_DBUG		= Default
		c.HAS_LOW_LEVEL_INIT		= Default



class cobra5475(genmcf548x_shared):
	name = "m68k/cobra5475"

	def build(self, c):
		c.CFLAGS		= ['-mcfv4e', '-Wa,-memac']
		c.LINKCMDS		= ['src/lib/libbsp/m68k/genmcf548x/startup/linkcmds.COBRA5475']


class m5484fireengine(genmcf548x_shared):
	name = "m68k/m5484fireengine"

	def build(self, c):
		c.CFLAGS		= ['-mcfv4e', '-Wa,-memac']
		c.LINKCMDS		= ['src/lib/libbsp/m68k/genmcf548x/startup/linkcmds.m5484FireEngine', 'src/lib/libbsp/m68k/genmcf548x/startup/linkcmds.m5484FireEngine.flash']


class idp(Base):
	name = "m68k/idp"

	def build(self, c):
		c.CFLAGS		= ['-mcpu=68040', '-msoft-float']
		c.LINKCMDS		= ['src/lib/libbsp/m68k/idp/startup/linkcmds']


class mcf5206elite(Base):
	name = "m68k/mcf5206elite"

	def build(self, c):
		c.CFLAGS		= ['-mcpu=5206e']
		c.LINKCMDS		= ['src/lib/libbsp/m68k/mcf5206elite/startup/linkcmds', 'src/lib/libbsp/m68k/mcf5206elite/startup/linkcmds.flash']


class mcf52235(Base):
	name = "m68k/mcf52235"

	def build(self, c):
		c.CFLAGS		= ['-mcpu=52235']
		c.LINKCMDS		= ['src/lib/libbsp/m68k/mcf52235/startup/linkcmds']


class mcf5225x(Base):
	name = "m68k/mcf5225x"

	def build(self, c):
		c.CFLAGS		= ['-mcpu=52235']
		c.LINKCMDS		= ['src/lib/libbsp/m68k/mcf5225x/startup/linkcmds']


class mcf5235(Base):
	name = "m68k/mcf5235"

	def build(self, c):
		c.CFLAGS		= ['-mcpu=5235']
		c.LINKCMDS		= ['src/lib/libbsp/m68k/mcf5235/startup/linkcmds', 'src/lib/libbsp/m68k/mcf5235/startup/linkcmdsflash', 'src/lib/libbsp/m68k/mcf5235/startup/linkcmdsram']


class mcf5329(Base):
	name = "m68k/mcf5329"

	def build(self, c):
		c.CFLAGS		= ['-mcpu=5307']
		c.LINKCMDS		= ['src/lib/libbsp/m68k/mcf5329/startup/linkcmds', 'src/lib/libbsp/m68k/mcf5329/startup/linkcmdsflash']


class mrm332(Base):
	name = "m68k/mrm332"

	def build(self, c):
		c.CFLAGS		= ['-mcpu=cpu32']
		c.LINKCMDS		= ['src/lib/libbsp/m68k/mrm332/startup/linkcmds', 'src/lib/libbsp/m68k/mrm332/startup/linkcmds_ROM']


class mvme136(Base):
	name = "m68k/mvme136"

	def build(self, c):
		c.CFLAGS		= ['-mcpu=68020']
		c.LINKCMDS		= ['src/lib/libbsp/m68k/mvme136/startup/linkcmds']


class mvme147(Base):
	name = "m68k/mvme147"

	def build(self, c):
		c.CFLAGS		= ['-mcpu=68030']
		c.LINKCMDS		= ['src/lib/libbsp/m68k/mvme147/startup/linkcmds']


class mvme147s(Base):
	name = "m68k/mvme147s"

	def build(self, c):
		c.CFLAGS		= ['-mcpu=68030']
		c.LINKCMDS		= ['src/lib/libbsp/m68k/mvme147s/startup/linkcmds']


class mvme162_shared(Base):
	def build(self, c):
		c.CFLAGS		= ['-mcpu=68040']
		c.LINKCMDS		= ['src/lib/libbsp/m68k/mvme162/startup/linkcmds']


class mvme162lx(mvme162_shared):
	name = "m68k/mvme162lx"

	def build(self, c):
		c.CFLAGS		= ['-mcpu=68040']
		c.LINKCMDS		= ['src/lib/libbsp/m68k/mvme162/startup/linkcmds']


class mvme162(mvme162_shared):
	name = "m68k/mvme162"

	def build(self, c):
		c.CFLAGS		= ['-mcpu=68040']
		c.LINKCMDS		= ['src/lib/libbsp/m68k/mvme162/startup/linkcmds']


class mvme167(Base):
	name = "m68k/mvme167"

	def build(self, c):
		c.CFLAGS		= ['-mcpu=68040']
		c.LINKCMDS		= ['src/lib/libbsp/m68k/mvme167/startup/linkcmds']

	def header(self, c):
		c.mvme167			= True
		c.CD2401_INT_LEVEL		= Default
		c.CD2401_IO_MODE		= Default
		c.CD2401_USE_TERMIOS		= Default
		c.CONSOLE_MINOR		= Default
		c.PRINTK_MINOR		= Default


class ods68302(Base):
	name = "m68k/ods68302"

	def build(self, c):
		c.CFLAGS		= ['-mcpu=68302']
		c.LINKCMDS		= ['src/lib/libbsp/m68k/ods68302/startup/linkcmds']
		c.LINK_START		= ['${RTEMS}/reset.o', 'crti.o', 'crtbegin.o', '-e', 'start']


class sim68000_shared(Base):
	def build(self, c):
		c.CFLAGS		= ['-mcpu=68000']
		c.LINKCMDS		= ['src/lib/libbsp/m68k/sim68000/startup/linkcmds']

	def header(self, c):
		c.CONSOLE_USE_INTERRUPTS		= Default



class sim68000(sim68000_shared):
	name = "m68k/sim68000"

	def build(self, c):
		c.CFLAGS		= ['-mcpu=68000']
		c.LINKCMDS		= ['src/lib/libbsp/m68k/sim68000/startup/linkcmds']



class simcpu32(sim68000_shared):
	name = "m68k/simcpu32"

	def build(self, c):
		c.CFLAGS		= ['-mcpu=cpu32']
		c.LINKCMDS		= ['src/lib/libbsp/m68k/sim68000/startup/linkcmds']


class uc5282(Base):
	name = "m68k/uc5282"

	def build(self, c):
		c.CFLAGS		= ['-mcpu=5282']
		c.LINKCMDS		= ['src/lib/libbsp/m68k/uC5282/startup/linkcmds']
