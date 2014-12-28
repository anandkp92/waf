from rtems_waf.config import Default, Config

class Base(Config):
	arch = name = "m32c"
	conflicts=("clang",)



class m32csim(Base):
	name = "m32c/m32csim"

	def build(self, c):
		c.CFLAGS		= ["-mcpu=m32cm"]
		c.LINKCMDS		= ['src/lib/libbsp/m32c/m32cbsp/startup/linkcmds']
		c.LINK_START	= ['${RTEMS}/start.o', 'crtbegin.o', '-e', '_start']
		c.LINK_END		= ['crtend.o']
		c.LINK_LINK		= ['-dc', '-dp', '-N']
