from rtems_waf.config import Default, Config

class Base(Config):
	arch = name = "arm"
	conflicts=("clang",)

	def build(self, c):
		c.LINK_START	= ['${RTEMS}/start.o', 'crti.o', 'crtbegin.o', '-e', '_start']
		c.LINK_END	= ['crtend.o', 'crtn.o']


class csb336(Base):
	name = "arm/csb336"

	def build(self, c):
		c.CFLAGS		= ['-mcpu=arm920', '-mfloat-abi=soft', '-mfpu=vfp', '-mstructure-size-boundary=8']
		c.LINKCMDS		= ['src/lib/libbsp/arm/csb336/startup/linkcmds', 'src/lib/libbsp/arm/shared/startup/linkcmds.base', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv4', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv7m']


class csb337_shared(Base):
	def build(self, c):
		c.CFLAGS		= ['-mcpu=arm920', '-mfloat-abi=soft', '-mfpu=vfp', '-mstructure-size-boundary=8']
		c.LINKCMDS		= ['src/lib/libbsp/arm/csb337/startup/linkcmds.csb337', 'src/lib/libbsp/arm/shared/startup/linkcmds.base', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv4', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv7m']
		c.ENABLE_LCD		= Default
		c.ENABLE_UMON		= True
		c.ENABLE_UMON_CONSOLE		= True

	def header(self, c):
		c.ENABLE_USART0		= True
		c.ENABLE_USART1		= True
		c.ENABLE_USART2		= True
		c.ENABLE_USART3		= True
		c.csb637		= Default



class csb637(csb337_shared):
	name = "arm/csb637"

	def build(self, c):
		c.CFLAGS		= ['-mcpu=arm920', '-mfloat-abi=soft', '-mfpu=vfp', '-mstructure-size-boundary=8']
		c.LINKCMDS		= ['src/lib/libbsp/arm/csb337/startup/linkcmds.csb637', 'src/lib/libbsp/arm/shared/startup/linkcmds.base', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv4', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv7m']

	def header(self, c):
		c.csb637		= True



class csb337(csb337_shared):
	name = "arm/csb337"

	def build(self, c):
		c.CFLAGS		= ['-mcpu=arm920', '-mfloat-abi=soft', '-mfpu=vfp', '-mstructure-size-boundary=8']
		c.LINKCMDS		= ['src/lib/libbsp/arm/csb337/startup/linkcmds.csb337', 'src/lib/libbsp/arm/shared/startup/linkcmds.base', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv4', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv7m']



class kit637_v6(csb337_shared):
	name = "arm/kit637_v6"

	def build(self, c):
		c.CFLAGS		= ['-mcpu=arm920', '-mfloat-abi=soft', '-mfpu=vfp', '-mstructure-size-boundary=8']
		c.LINKCMDS		= ['src/lib/libbsp/arm/csb337/startup/linkcmds.csb337', 'src/lib/libbsp/arm/shared/startup/linkcmds.base', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv4', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv7m']

	def header(self, c):
		c.csb637		= True




class lm3s_shared(Base):
	def build(self, c):
		c.CFLAGS		= ['-march=armv7-m', '-mthumb']

	def header(self, c):
		c.BSP_SMALL_MEMORY			= True
		c.LM3S69XX_ENABLE_UART_0	= Default
		c.LM3S69XX_ENABLE_UART_1	= Default
		c.LM3S69XX_ENABLE_UART_2	= Default
		c.LM3S69XX_HAS_UDMA			= Default
		c.LM3S69XX_MCU_LM3S3749		= Default
		c.LM3S69XX_MCU_LM3S6965		= Default
		c.LM3S69XX_SSI_CLOCK		= Default
		c.LM3S69XX_SYSTEM_CLOCK		= Default
		c.LM3S69XX_UART_BAUD		= Default
		c.LM3S69XX_USE_AHB_FOR_GPIO	= Default


class lm3s3749(lm3s_shared):
	name = "arm/lm3s3749"

	def build(self, c):
		c.LINKCMDS		= ['src/lib/libbsp/arm/lm3s69xx/startup/linkcmds.lm3s3749', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv7m', 'src/lib/libbsp/arm/shared/startup/linkcmds.base']

	def header(self, c):
		c.LM3S69XX_HAS_UDMA			= True
		c.LM3S69XX_XTAL_CONFIG		= Default
		c.LM3S69XX_MCU_LM3S3749		= True
		c.LM3S69XX_NUM_GPIO_BLOCKS	= 8
		c.LM3S69XX_NUM_SSI_BLOCKS	= 2
		c.LM3S69XX_USE_AHB_FOR_GPIO	= True

class lm3s6965(lm3s_shared):
	name = "arm/lm3s6965"

	def build(self, c):
		c.LINKCMDS		= ['src/lib/libbsp/arm/lm3s69xx/startup/linkcmds.lm3s6965', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv7m', 'src/lib/libbsp/arm/shared/startup/linkcmds.base']

	def header(self, c):
		c.LM3S69XX_XTAL_CONFIG		= "0xE"
		c.LM3S69XX_MCU_LM3S6965		= True
		c.LM3S69XX_NUM_GPIO_BLOCKS	= 7
	

class lm3s6965_qemu(lm3s_shared):
	name = "arm/lm3s6965_qemu"

	def build(self, c):
		c.LINKCMDS		= ['src/lib/libbsp/arm/lm3s69xx/startup/linkcmds.lm3s6965_qemu', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv7m', 'src/lib/libbsp/arm/shared/startup/linkcmds.base']

	def header(self, c):
		c.LM3S69XX_XTAL_CONFIG		= "0xE"
		c.LM3S69XX_MCU_LM3S6965		= True
		c.LM3S69XX_NUM_GPIO_BLOCKS	= 7


class lpc17xx_shared(Base):
	def build(self, c):
		c.CFLAGS		= ['-march=armv7-m', '-mthumb']

	def header(self, c):
		c.BSP_SMALL_MEMORY					= Default
		c.LPC24XX_CCLK						= Default
		c.LPC24XX_CONFIG_CONSOLE			= Default
		c.LPC24XX_CONFIG_I2C_2				= Default
		c.LPC24XX_CONFIG_UART_1				= Default
		c.LPC24XX_EMC_TEST					= Default
		c.LPC24XX_ETHERNET_RMII				= Default
		c.LPC24XX_OSCILLATOR_MAIN			= Default
		c.LPC24XX_OSCILLATOR_RTC			= Default
		c.LPC24XX_STOP_ETHERNET				= Default
		c.LPC24XX_STOP_GPDMA				= Default
		c.LPC24XX_STOP_USB					= Default
		c.LPC24XX_UART_BAUD					= Default
		c.LPC24XX_PCLKDIV					= Default
		c.LPC24XX_EMCCLKDIV					= Default
		c.LPC24XX_EMC_MT48LC4M16A2			= Default
		c.LPC24XX_EMC_W9825G2JB75I			= Default
		c.LPC24XX_EMC_IS42S32800D7			= Default
		c.LPC24XX_EMC_IS42S32800B			= Default
		c.LPC24XX_EMC_M29W160E				= Default
		c.LPC24XX_EMC_M29W320E70			= Default
		c.LPC24XX_EMC_SST39VF3201			= Default
		c.LPC24XX_CONFIG_UART_2				= Default
		c.LPC24XX_CONFIG_UART_3				= Default
		c.LPC24XX_CONFIG_I2C_0				= Default
		c.LPC24XX_CONFIG_I2C_1				= Default
		c.LPC_DMA_CHANNEL_COUNT				= 8
		c.BSP_START_RESET_VECTOR			= Default
		c.BSP_USB_OTG_TRANSCEIVER_I2C_ADDR	= "(0x2f << 1)"



class lpc17xx_ea_ram(lpc17xx_shared):
	name = "arm/lpc17xx_ea_ram"

	def build(self, c):
		c.LINKCMDS		= ['src/lib/libbsp/arm/lpc24xx/startup/linkcmds.lpc17xx_ea_ram', 'src/lib/libbsp/arm/shared/startup/linkcmds.base', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv4', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv7m']

	def header(self, c):
		c.LPC24XX_CCLK						= "96000000U"
		c.LPC24XX_PCLKDIV					= "2U"
		c.LPC24XX_EMCCLKDIV					= "2U"


class lpc17xx_ea_rom_int(lpc17xx_shared):
	name = "arm/lpc17xx_ea_rom_int"

	def build(self, c):
		c.LINKCMDS		= ['src/lib/libbsp/arm/lpc24xx/startup/linkcmds.lpc17xx_ea_rom_int', 'src/lib/libbsp/arm/shared/startup/linkcmds.base', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv4', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv7m']

	def header(self, c):
		c.LPC24XX_CCLK						= "96000000U"
		c.LPC24XX_PCLKDIV					= "2U"
		c.LPC24XX_EMC_IS42S32800B			= True

class lpc17xx_plx800_ram(lpc17xx_shared):
	name = "arm/lpc17xx_plx800_ram"

	def build(self, c):
		c.LINKCMDS		= ['src/lib/libbsp/arm/lpc24xx/startup/linkcmds.lpc17xx_plx800_ram', 'src/lib/libbsp/arm/shared/startup/linkcmds.base', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv4', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv7m']

	def header(self, c):
		pass

class lpc17xx_plx800_rom_int(lpc17xx_shared):
	name = "arm/lpc17xx_plx800_rom_int"

	def build(self, c):
		c.LINKCMDS		= ['src/lib/libbsp/arm/lpc24xx/startup/linkcmds.lpc17xx_plx800_rom_int', 'src/lib/libbsp/arm/shared/startup/linkcmds.base', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv4', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv7m']

	def header(self, c):
		c.LPC24XX_EMC_M29W320E70		= True


class edb7312(Base):
	name = "arm/edb7312"

	def build(self, c):
		c.CFLAGS		= ['-mcpu=arm7tdmi', '-mfloat-abi=soft', '-mfpu=vfp', '-mstructure-size-boundary=8']
		c.LINKCMDS		= ['src/lib/libbsp/arm/edb7312/startup/linkcmds', 'src/lib/libbsp/arm/shared/startup/linkcmds.base', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv4', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv7m']

	def header(self, c):
		c.ON_SKYEYE		= Default



class gba(Base):
	name = "arm/gba"

	def build(self, c):
		c.CFLAGS		= ['-mcpu=arm7tdmi', '-mfloat-abi=soft', '-mfpu=vfp', '-mstructure-size-boundary=8']
		c.LINKCMDS		= ['src/lib/libbsp/arm/gba/startup/linkcmds', 'src/lib/libbsp/arm/shared/startup/linkcmds.base', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv4', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv7m']


class gdbarmsim_shared(Base):
	def build(self, c):
		pass


class arm1136jfs(gdbarmsim_shared):
	name = "arm/arm1136jfs"

	def build(self, c):
		c.CFLAGS		= ['-mcpu=arm1136jf-s']
		c.LINKCMDS		= ['src/lib/libbsp/arm/gdbarmsim/startup/linkcmds', 'src/lib/libbsp/arm/shared/startup/linkcmds.base', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv4', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv7m']


class arm1136js(gdbarmsim_shared):
	name = "arm/arm1136js"

	def build(self, c):
		c.CFLAGS		= ['-mcpu=arm1136j-s']
		c.LINKCMDS		= ['src/lib/libbsp/arm/gdbarmsim/startup/linkcmds', 'src/lib/libbsp/arm/shared/startup/linkcmds.base', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv4', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv7m']


class armcortexa9(gdbarmsim_shared):
	name = "arm/armcortexa9"

	def build(self, c):
		c.CFLAGS		= ['-mcpu=cortex-a9']
		c.LINKCMDS		= ['src/lib/libbsp/arm/gdbarmsim/startup/linkcmds', 'src/lib/libbsp/arm/shared/startup/linkcmds.base', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv4', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv7m']


class arm7tdmi(gdbarmsim_shared):
	name = "arm/arm7tdmi"

	def build(self, c):
		c.CFLAGS		= ['-mcpu=arm7tdmi']
		c.LINKCMDS		= ['src/lib/libbsp/arm/gdbarmsim/startup/linkcmds', 'src/lib/libbsp/arm/shared/startup/linkcmds.base', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv4', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv7m']


class arm920(gdbarmsim_shared):
	name = "arm/arm920"

	def build(self, c):
		c.CFLAGS		= ['-mcpu=arm920', '-mfloat-abi=soft', '-mfpu=vfp']
		c.LINKCMDS		= ['src/lib/libbsp/arm/gdbarmsim/startup/linkcmds', 'src/lib/libbsp/arm/shared/startup/linkcmds.base', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv4', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv7m']


class gp32(Base):
	name = "arm/gp32"

	def build(self, c):
		c.CFLAGS		= ['-DCPU_S3C2400', '-mcpu=arm920t', '-mfloat-abi=soft', '-mfpu=vfp', '-mstructure-size-boundary=32']
		c.LINKCMDS		= ['src/lib/libbsp/arm/gp32/startup/linkcmds', 'src/lib/libbsp/arm/shared/startup/linkcmds.base', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv4', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv7m']


class gumstix(Base):
	name = "arm/gumstix"

	def build(self, c):
		c.CFLAGS		= ['-mcpu=xscale', '-mfloat-abi=soft', '-mfpu=vfp', '-mstructure-size-boundary=8']
		c.LINKCMDS		= ['src/lib/libbsp/arm/gumstix/startup/linkcmds', 'src/lib/libbsp/arm/shared/startup/linkcmds.base', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv4', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv7m']
		c.ON_SKYEYE		= Default

	def header(self, c):
		c.ON_SKYEYE		= Default



class lpc24xx_shared(Base):

	def build(self, c):
		c.CFLAGS		= ['-mcpu=arm7tdmi-s', '-mthumb', '-mfloat-abi=soft', '-mfpu=vfp', '-mstructure-size-boundary=8', '-Os']


	def header(self, c):
		c.BSP_SMALL_MEMORY					= Default
		c.LPC24XX_CCLK						= Default
		c.LPC24XX_CONFIG_CONSOLE			= Default
		c.LPC24XX_CONFIG_I2C_2				= Default
		c.LPC24XX_CONFIG_UART_1				= Default
		c.LPC24XX_EMC_TEST					= Default
		c.LPC24XX_ETHERNET_RMII				= Default
		c.LPC24XX_OSCILLATOR_MAIN			= Default
		c.LPC24XX_OSCILLATOR_RTC			= Default
		c.LPC24XX_STOP_ETHERNET				= Default
		c.LPC24XX_STOP_GPDMA				= Default
		c.LPC24XX_STOP_USB					= Default
		c.LPC24XX_UART_BAUD					= Default
		c.LPC24XX_PCLKDIV					= Default
		c.LPC24XX_EMCCLKDIV					= Default
		c.LPC24XX_EMC_MT48LC4M16A2			= Default
		c.LPC24XX_EMC_W9825G2JB75I			= Default
		c.LPC24XX_EMC_IS42S32800D7			= Default
		c.LPC24XX_EMC_IS42S32800B			= Default
		c.LPC24XX_EMC_M29W160E				= Default
		c.LPC24XX_EMC_M29W320E70			= Default
		c.LPC24XX_EMC_SST39VF3201			= Default
		c.LPC24XX_CONFIG_UART_2				= Default
		c.LPC24XX_CONFIG_UART_3				= Default
		c.LPC24XX_CONFIG_I2C_0				= Default
		c.LPC24XX_CONFIG_I2C_1				= Default
		c.LPC_DMA_CHANNEL_COUNT				= Default
		c.BSP_START_RESET_VECTOR			= Default
		c.BSP_USB_OTG_TRANSCEIVER_I2C_ADDR	= Default


class lpc24xx_ncs_rom_ext(lpc24xx_shared):
	name = "arm/lpc24xx_ncs_rom_ext"

	def build(self, c):
		c.LINKCMDS		= ['src/lib/libbsp/arm/lpc24xx/startup/linkcmds.lpc24xx_ncs_rom_ext', 'src/lib/libbsp/arm/shared/startup/linkcmds.base', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv4', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv7m']

	def header(self, c):
		c.BSP_START_RESET_VECTOR		= "0x80000040"
		c.LPC24XX_EMC_MT48LC4M16A2 		= True
		c.BSP_START_RESET_VECTOR		= "0x80000040"

class lpc24xx_ncs_rom_int(lpc24xx_shared):
	name = "arm/lpc24xx_ncs_rom_int"

	def build(self, c):
		c.LINKCMDS		= ['src/lib/libbsp/arm/lpc24xx/startup/linkcmds.lpc24xx_ncs_rom_int', 'src/lib/libbsp/arm/shared/startup/linkcmds.base', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv4', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv7m']

	def header(self, c):
		c.LPC24XX_EMC_M29W320E70		= True
		c.BSP_START_RESET_VECTOR		= "0x80000040"


class lpc24xx_plx800_ram(lpc24xx_shared):
	name = "arm/lpc24xx_plx800_ram"

	def build(self, c):
		c.LINKCMDS		= ['src/lib/libbsp/arm/lpc24xx/startup/linkcmds.lpc24xx_plx800_ram', 'src/lib/libbsp/arm/shared/startup/linkcmds.base', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv4', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv7m']

	def header(self, c):
		c.LPC24XX_CCLK						= "51612800U"
		c.LPC24XX_CONFIG_UART_1				= False
		c.LPC24XX_CONFIG_UART_2				= Default


class lpc24xx_plx800_rom_int(lpc24xx_shared):
	name = "arm/lpc24xx_plx800_rom_int"

	def build(self, c):
		c.LINKCMDS		= ['src/lib/libbsp/arm/lpc24xx/startup/linkcmds.lpc24xx_plx800_rom_int', 'src/lib/libbsp/arm/shared/startup/linkcmds.base', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv4', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv7m']

	def header(self, c):
		c.LPC24XX_CCLK						= "51612800U"
		c.LPC24XX_CONFIG_UART_1				= False
		c.LPC24XX_CONFIG_UART_2				= Default


class lpc24xx_ea(lpc24xx_shared):
	name = "arm/lpc24xx_ea"

	def build(self, c):
		c.LINKCMDS		= ['src/lib/libbsp/arm/lpc24xx/startup/linkcmds.lpc24xx_ea', 'src/lib/libbsp/arm/shared/startup/linkcmds.base', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv4', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv7m']

	def header(self, c):
		c.LPC24XX_ETHERNET_RMII		= True
		c.BSP_START_RESET_VECTOR		= "0x80000040"


class lpc23xx_tli800(lpc24xx_shared):
	name = "arm/lpc23xx_tli800"

	def build(self, c):
		c.CFLAGS		= ['-mcpu=arm7tdmi-s', '-mthumb', '-mfloat-abi=soft', '-mfpu=vfp', '-mstructure-size-boundary=8', '-Os']
		c.LINKCMDS		= ['src/lib/libbsp/arm/lpc24xx/startup/linkcmds.lpc23xx_tli800', 'src/lib/libbsp/arm/shared/startup/linkcmds.base', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv4', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv7m']

	def header(self, c):
		c.LPC24XX_OSCILLATOR_MAIN = "3686400U"
		c.LPC24XX_CCLK				= "58982400U"
		c.LPC24XX_HEAP_EXTEND		= True

class lpc2362(lpc24xx_shared):
	name = "arm/lpc2362"

	def build(self, c):
		c.CFLAGS		= ['-mcpu=arm7tdmi-s', '-mthumb', '-mfloat-abi=soft', '-mfpu=vfp', '-mstructure-size-boundary=8', '-Os']
		c.LINKCMDS		= ['src/lib/libbsp/arm/lpc24xx/startup/linkcmds.lpc2362', 'src/lib/libbsp/arm/shared/startup/linkcmds.base', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv4', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv7m']

	def header(self, c):
		c.LPC24XX_OSCILLATOR_MAIN = "3686400U"
		c.LPC24XX_CCLK				= "58982400U"
		c.LPC24XX_HEAP_EXTEND		= True


#XXX: Some of the armv4 linkcmds are unnessicary (when armv7 is used)
class lpc24xx_ncs_ram(lpc24xx_shared):
	name = "arm/lpc24xx_ncs_ram"

	def build(self, c):
		c.CFLAGS		= ['-mcpu=arm7tdmi-s', '-mthumb', '-mfloat-abi=soft', '-mfpu=vfp', '-mstructure-size-boundary=8', '-Os']
		c.LINKCMDS		= ['src/lib/libbsp/arm/lpc24xx/startup/linkcmds.lpc24xx_ncs_ram', 'src/lib/libbsp/arm/shared/startup/linkcmds.base', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv4', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv7m']

	def header(self, c):
		c.LPC24XX_CONFIG_I2C_1 = 1


class lpc32xx_shared(Base):

	def header(self, c):
		c.BSP_SMALL_MEMORY		= Default
		c.BSP_START_RESET_VECTOR		= ""
		c.LPC32XX_ARM_CLK		= Default
		c.LPC32XX_CONFIG_U3CLK		= Default
		c.LPC32XX_CONFIG_U4CLK		= Default
		c.LPC32XX_CONFIG_U5CLK		= Default
		c.LPC32XX_CONFIG_U6CLK		= Default
		c.LPC32XX_CONFIG_UART_CLKMODE		= Default
		c.LPC32XX_DISABLE_MMU		= Default
		c.LPC32XX_DISABLE_READ_ONLY_PROTECTION		= Default
		c.LPC32XX_DISABLE_READ_WRITE_DATA_CACHE		= Default
		c.LPC32XX_ENABLE_WATCHDOG_RESET		= Default
		c.LPC32XX_ETHERNET_RMII		= Default
		c.LPC32XX_HCLK		= Default
		c.LPC32XX_OSCILLATOR_MAIN		= Default
		c.LPC32XX_OSCILLATOR_RTC		= Default
		c.LPC32XX_PERIPH_CLK		= Default
		c.LPC32XX_STOP_ETHERNET		= Default
		c.LPC32XX_STOP_GPDMA		= Default
		c.LPC32XX_STOP_USB		= Default
		c.LPC32XX_UART_1_BAUD		= Default
		c.LPC32XX_UART_2_BAUD		= Default
		c.LPC32XX_UART_7_BAUD		= Default
		c.TESTS_USE_PRINTK		= True



class lpc32xx_mzx_stage_1(lpc32xx_shared):
	name = "arm/lpc32xx_mzx_stage_1"

	def build(self, c):
		# XXX: -Os was added as a hack to fix test builds (results were too huge resulting in an error)
		c.CFLAGS		= ['-fno-schedule-insns2', '-mcpu=arm926ej-s', '-mfloat-abi=soft', '-mfpu=vfp', '-mstructure-size-boundary=8', '-mthumb', '-Os']
		c.LINKCMDS		= ['src/lib/libbsp/arm/lpc32xx/startup/linkcmds.lpc32xx_mzx_stage_1', 'src/lib/libbsp/arm/shared/startup/linkcmds.base', 'src/lib/libbsp/arm/lpc32xx/startup/linkcmds.lpc32xx', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv4', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv7m']

	def header(self, c):
		c.BSP_SMALL_MEMORY		= True
		c.LPC_DMA_CHANNEL_COUNT = Default


class lpc32xx_mzx_stage_2(lpc32xx_shared):
	name = "arm/lpc32xx_mzx_stage_2"

	def build(self, c):
		c.CFLAGS		= ['-fno-schedule-insns2', '-mcpu=arm926ej-s', '-mfloat-abi=soft', '-mfpu=vfp', '-mstructure-size-boundary=8', '-mthumb']
		c.LINKCMDS		= ['src/lib/libbsp/arm/lpc32xx/startup/linkcmds.lpc32xx_mzx_stage_2', 'src/lib/libbsp/arm/shared/startup/linkcmds.base', 'src/lib/libbsp/arm/lpc32xx/startup/linkcmds.lpc32xx', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv4', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv7m']

	def header(self, c):
		c.LPC_DMA_CHANNEL_COUNT	= 8


class lpc32xx_phycore(lpc32xx_shared):
	name = "arm/lpc32xx_phycore"

	def build(self, c):
		c.CFLAGS		= ['-fno-schedule-insns2', '-mcpu=arm926ej-s', '-mfloat-abi=soft', '-mfpu=vfp', '-mstructure-size-boundary=8', '-mthumb']
		c.LINKCMDS		= ['src/lib/libbsp/arm/lpc32xx/startup/linkcmds.lpc32xx_phycore', 'src/lib/libbsp/arm/shared/startup/linkcmds.base', 'src/lib/libbsp/arm/lpc32xx/startup/linkcmds.lpc32xx', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv4', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv7m']

	def header(self, c):
		c.LPC_DMA_CHANNEL_COUNT	= 8


class lpc32xx_mzx(lpc32xx_shared):
	name = "arm/lpc32xx_mzx"

	def build(self, c):
		c.CFLAGS		= ['-fno-schedule-insns2', '-mcpu=arm926ej-s', '-mfloat-abi=soft', '-mfpu=vfp', '-mstructure-size-boundary=8', '-mthumb']
		c.LINKCMDS		= ['src/lib/libbsp/arm/lpc32xx/startup/linkcmds.lpc32xx_mzx', 'src/lib/libbsp/arm/shared/startup/linkcmds.base', 'src/lib/libbsp/arm/lpc32xx/startup/linkcmds.lpc32xx', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv4', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv7m']

	def header(self, c):
		c.LPC_DMA_CHANNEL_COUNT	= 8


class nds(Base):
	name = "arm/nds"

	def build(self, c):
		c.CFLAGS		= ['-mcpu=arm9tdmi', '-mfloat-abi=soft', '-mfpu=vfp', '-mstructure-size-boundary=8', '-mthumb-interwork']
		c.LINKCMDS		= ['src/lib/libbsp/arm/nds/startup/linkcmds', 'src/lib/libbsp/arm/shared/startup/linkcmds.base', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv4', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv7m']


class rtl22xx_shared(Base):
	def build(self, c):
		c.CFLAGS		= ['-mapcs-frame', '-mcpu=arm7tdmi', '-mfloat-abi=soft', '-mfpu=vfp', '-mstructure-size-boundary=8']
		c.LINKCMDS		= ['src/lib/libbsp/arm/rtl22xx/startup/linkcmds', 'src/lib/libbsp/arm/shared/startup/linkcmds.base', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv4', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv7m']
		c.ON_SKYEYE		= Default

	def header(self, c):
		c.ON_SKYEYE		= Default


class raspberrypi(Base):
	name = "arm/raspberrypi"
	def build(self, c):
		c.CFLAGS		= ['-mcpu=arm1176jzf-s']
		c.LINKCMDS		= ['src/lib/libbsp/arm/raspberrypi/startup/linkcmds', 'src/lib/libbsp/arm/shared/startup/linkcmds.base', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv4']

	def header(self, c):
		c.BSP_START_RESET_VECTOR = ""


class realview_pbx_a9_qemu(Base):
	name = "arm/realview_pbx_a9_qemu"

	def build(self, c):
		c.CFLAGS		= ['-march=armv7-a', '-mthumb', '-mfpu=neon', '-mfloat-abi=hard', '-mtune=cortex-a9']
		c.LINKCMDS		= ['src/lib/libbsp/arm/realview-pbx-a9/startup/linkcmds', 'src/lib/libbsp/arm/shared/startup/linkcmds.base', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv4']

	def header(self, c):
		c.BSP_START_RESET_VECTOR = ""
		c.BSP_ARM_A9MPCORE_PERIPHCLK = "100000000U"


class rtl22xx(rtl22xx_shared):
	name = "arm/rtl22xx"

	def build(self, c):
		c.CFLAGS		= ['-mapcs-frame', '-mcpu=arm7tdmi', '-mfloat-abi=soft', '-mfpu=vfp', '-mstructure-size-boundary=8']
		c.LINKCMDS		= ['src/lib/libbsp/arm/rtl22xx/startup/linkcmds', 'src/lib/libbsp/arm/shared/startup/linkcmds.base', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv4', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv7m']


class rtl22xx_t(rtl22xx_shared):
	name = "arm/rtl22xx_t"

	def build(self, c):
		c.CFLAGS		= ['-mapcs-frame', '-mcpu=arm7tdmi', '-mfloat-abi=soft', '-mfpu=vfp', '-mstructure-size-boundary=8', '-mthumb', '-fno-schedule-insns2']
		c.LINKCMDS		= ['src/lib/libbsp/arm/rtl22xx/startup/linkcmds', 'src/lib/libbsp/arm/shared/startup/linkcmds.base', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv4', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv7m']


class smdk2410(Base):
	name = "arm/smdk2410"

	def build(self, c):
		c.CFLAGS		= ['-DCPU_S3C2410', '-mcpu=arm920t', '-mfloat-abi=soft', '-mfpu=vfp', '-mstructure-size-boundary=32']
		c.LINKCMDS		= ['src/lib/libbsp/arm/smdk2410/startup/linkcmds', 'src/lib/libbsp/arm/shared/startup/linkcmds.base', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv4', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv7m']

	def header(self, c):
		c.ON_SKYEYE		= Default


class stm32f4(Base):
	name = "arm/stm32f4"

	def build(self, c):
		c.CFLAGS		= ['-march=armv7-m', '-mthumb']
		c.LINKCMDS		= ['src/lib/libbsp/arm/stm32f4/startup/linkcmds.stm32f4', 'src/lib/libbsp/arm/shared/startup/linkcmds.base', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv4', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv7m']

	def header(self, c):
		c.STM32F4_HSE_OSCILLATOR		= Default
		c.STM32F4_SYSCLK				= Default
		c.STM32F4_HCLK					= Default
		c.STM32F4_PCLK1					= Default
		c.STM32F4_PCLK2					= Default
		c.STM32F4_USART_BAUD			= Default
		c.STM32F4_ENABLE_USART_1		= Default
		c.STM32F4_ENABLE_USART_2		= Default
		c.STM32F4_ENABLE_USART_3		= Default
		c.STM32F4_ENABLE_UART_4			= Default
		c.STM32F4_ENABLE_UART_5			= Default
		c.STM32F4_ENABLE_USART_6		= Default


class xilinx_zynq_a9_qemu(Base):
	name = "arm/xilinx_zynq_a9_qemu"

	def build(self, c):
		c.CFLAGS		= ['-march=armv7-a', '-mthumb', '-mfpu=neon', '-mfloat-abi=hard', '-mtune=cortex-a9']
		c.LINKCMDS		= ['src/lib/libbsp/arm/xilinx-zynq/startup/linkcmds', 'src/lib/libbsp/arm/shared/startup/linkcmds.base', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv4', 'src/lib/libbsp/arm/shared/startup/linkcmds.armv7m']

	def header(self, c):
		c.BSP_START_RESET_VECTOR		= ""
		c.BSP_ARM_A9MPCORE_PERIPHCLK	= "100000000U"
