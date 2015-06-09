from rtems_waf.config import Default, Config

class Base(Config):
	arch = name = "sh"
	conflicts=("clang",)

	def build(self, c):
		c.LINK_START		= ['${RTEMS}/start.o', '-e', '_start']


class gensh1(Base):
	name = "sh/gensh1"

	def build(self, c):
		c.CFLAGS		= ['-m1']
		c.LINKCMDS		= ['src/lib/libbsp/sh/gensh1/startup/linkcmds']

	def header(self, c):
		c.CPU_CLOCK_RATE_HZ		= Default
		c.START_HW_INIT		= Default



class gensh2(Base):
	name = "sh/gensh2"

	def build(self, c):
		c.CFLAGS		= ['-m2']
		c.LINKCMDS		= ['src/lib/libbsp/sh/gensh2/startup/linkcmds',
					   'src/lib/libbsp/sh/gensh2/startup/linkcmds.ram',
					   'src/lib/libbsp/sh/gensh2/startup/linkcmds.rom']

	def header(self, c):
		c.CPU_CLOCK_RATE_HZ		= 29491200
		c.STANDALONE_EVB		= Default
		c.START_HW_INIT		= Default



class gensh4(Base):
	name = "sh/gensh4"

	def build(self, c):
		c.CFLAGS		= ['-m4', '-ml']
		c.LDFLAGS		= ['-m4', '-ml']
		c.LINKCMDS		= ['src/lib/libbsp/sh/gensh4/startup/linkcmds',
					   'src/lib/libbsp/sh/gensh4/startup/linkcmds.rom',
					   'src/lib/libbsp/sh/gensh4/startup/linkcmds.rom2ram']
		c.LINK_LINK		= ['-EL']

	def header(self, c):
		c.CPU_CLOCK_RATE_HZ		= 29491200
		c.START_HW_INIT		= Default


class shsim_shared(Base):
	def header(self, c):
		c.CPU_CLOCK_RATE_HZ		= Default
		c.START_HW_INIT		= Default

	def build(self, c):
		c.CFLAGS		= ['-m1']
		c.LINKCMDS		= ['src/lib/libbsp/sh/shsim/startup/linkcmds',
					   'src/lib/libbsp/sh/shsim/startup/linkcmds.sim']


class simsh1(shsim_shared):
	name = "sh/simsh1"

	def build(self, c):
		c.CFLAGS		= ['-m1']


class simsh2(shsim_shared):
	name = "sh/simsh2"

	def build(self, c):
		c.CFLAGS		= ['-m2']


class simsh4(shsim_shared):
	name = "sh/simsh4"



class simsh2e(shsim_shared):
	name = "sh/simsh2e"
