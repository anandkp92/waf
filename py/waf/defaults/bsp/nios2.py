from py.config import Default, Config

class Base(Config):
	arch = name = "nios2"
	conflicts=("clang",)

	def build(self, c):
		c.LINKCMDS			= ['src/lib/libbsp/nios2/nios2_iss/startup/linkcmds']
		c.LINK_START		= ['${RTEMS}/start.o', 'crti.o', 'crtbegin.o', '-e', 'start']
		c.LINK_END			= ['crtend.o', '${RTEMS}/crtnn.o']

class nios2_iss(Base):
	name = "nios2/nios2_iss"

	def build(self, c):
		c.CFLAGS = ["-mno-hw-mul", "-mno-hw-div"]
