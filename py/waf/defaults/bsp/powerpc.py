from py.config import Default, Config, Disable

class Base(Config):
	arch = name = "powerpc"
	conflicts=("clang",)



class beatnik(Base):
	name = "powerpc/beatnik"

	def build(self, c):
		c.CFLAGS		= ['-mcpu=7400', '-D__ppc_generic']
		c.LINKCMDS		= ['src/lib/libbsp/powerpc/shared/startup/linkcmds']
		c.LINK_START	= ['ecrti.o', '${RTEMS}/rtems_crti.o', 'crtbegin.o', '-e', '__rtems_entry_point', '-u', '__vectors', '${RTEMS}/vectors_entry.o', '${RTEMS}/preload.o', '${RTEMS}/start.o']
		c.LINK_END		= ['crtend.o', 'ecrtn.o']
		c.LINK_LINK		= ['-Bstatic']

	def header(self, c):
		c.CONFIGURE_MALLOC_BSP_SUPPORTS_SBRK		= Default



class ep1a(Base):
	name = "powerpc/ep1a"

	def build(self, c):
		c.CFLAGS		= ['-mcpu=603e', '-Dppc603e', '-mmultiple', '-mstring', '-mstrict-align']
		c.LINKCMDS		= ['src/lib/libbsp/powerpc/ep1a/startup/linkcmds']
		c.LINK_START	= ['ecrti.o', '${RTEMS}/rtems_crti.o', 'crtbegin.o', '${RTEMS}/start.o', '-e', '__rtems_entry_point', '-u', '__vectors']
		c.LINK_END		= ['crtend.o', 'ecrtn.o']
		c.LINK_LINK		= ['-Bstatic']

	def header(self, c):
		c.CONFIGURE_MALLOC_BSP_SUPPORTS_SBRK		= Default
		c.CONSOLE_USE_INTERRUPTS		= Default


class gen5200_shared(Base):
	def header(self, c):
		c.ALLOW_IRQ_NESTING		= True
		c.BENCHMARK_IRQ_PROCESSING		= False
		c.BSP_GPIOPCR_INITMASK		= Default
		c.BSP_GPIOPCR_INITVAL		= Default
		c.BSP_PRESS_KEY_FOR_RESET		= Default
		c.BSP_RESET_BOARD_AT_EXIT		= Default
		c.BSP_UART_AVAIL_MASK		= Default
		c.PRINTK_MINOR		= "0"
		c.SINGLE_CHAR_MODE		= Default
		c.UARTS_USE_TERMIOS_INT		= Default

	def build(self, c):
		c.CFLAGS		= ['-mcpu=603e', '-mstrict-align', '-meabi', '-msdata', '-fno-common']
		c.LINK_START		= ['ecrti.o', '${RTEMS}/rtems_crti.o', 'crtbegin.o', '${RTEMS}/start.o']
		c.LINK_END		= ['crtend.o', 'ecrtn.o']


class icecube(gen5200_shared):
	name = "powerpc/icecube"

	def build(self, c):
		c.LINKCMDS		= ['src/lib/libbsp/powerpc/gen5200/startup/linkcmds.icecube',
					   'src/lib/libbsp/powerpc/gen5200/startup/linkcmds.base']

	def header(self, c):
		c.ALLOW_IRQ_NESTING		= False
		c.BSP_PRESS_KEY_FOR_RESET		= True
		c.BSP_RESET_BOARD_AT_EXIT		= True
		c.HAS_UBOOT		= True
		c.MPC5200_BOARD_ICECUBE = True


class dp2(gen5200_shared):
	name = "powerpc/dp2"

	def build(self, c):
		c.LINKCMDS		= ['src/lib/libbsp/powerpc/gen5200/startup/linkcmds.dp2', 'src/lib/libbsp/powerpc/gen5200/startup/linkcmds.base']

	def header(self, c):
		c.BSP_GPIOPCR_INITMASK		= "0x337F3F77"
		c.BSP_GPIOPCR_INITVAL		= "0x03550040"
		c.BSP_TYPE_DP2		= True
		c.BSP_UART_AVAIL_MASK		= "0x22"
		c.HAS_UBOOT		= True
		c.MPC5200_BOARD_DP2			= True
		c.MPC5200_PSC_INDEX_FOR_GPS_MODULE		= 5
		c.PRINTK_MINOR		= "1"


class pm520_ze30(gen5200_shared):
	name = "powerpc/pm520_ze30"

	def build(self, c):
		c.LINKCMDS		= ['src/lib/libbsp/powerpc/gen5200/startup/linkcmds.pm520_ze30', 'src/lib/libbsp/powerpc/gen5200/startup/linkcmds.base']

	def header(self, c):
		c.BSP_GPIOPCR_INITMASK		= "0x037F3F07"
		c.BSP_GPIOPCR_INITVAL		= "0x01552104"
		c.BSP_UART_AVAIL_MASK		= "0x39"
		c.HAS_UBOOT					= True
		c.MPC5200_BOARD_PM520_ZE30	= True


class pm520_cr825(gen5200_shared):
	name = "powerpc/pm520_cr825"

	def build(self, c):
		c.LINKCMDS		= ['src/lib/libbsp/powerpc/gen5200/startup/linkcmds.pm520_cr825', 'src/lib/libbsp/powerpc/gen5200/startup/linkcmds.base']

	def header(self, c):
		c.BSP_RESET_BOARD_AT_EXIT		= True
		c.BSP_UART_AVAIL_MASK		= "0x07"
		c.HAS_UBOOT					= True
		c.MPC5200_BOARD_PM520_CR825	= True



class brs5l(gen5200_shared):
	name = "powerpc/brs5l"

	def build(self, c):
		c.LINKCMDS		= ['src/lib/libbsp/powerpc/gen5200/startup/linkcmds.brs5l', 'src/lib/libbsp/powerpc/gen5200/startup/linkcmds.base']

	def header(self, c):
		c.MPC5200_BOARD_BRS5L		= True
		c.BSP_GPIOPCR_INITMASK		= "0xb30F0F77"
		c.BSP_GPIOPCR_INITVAL		= "0x91050444"
		c.BSP_RESET_BOARD_AT_EXIT	= True
		c.BSP_UART_AVAIL_MASK		= "0x07"


class brs6l(gen5200_shared):
	name = "powerpc/brs6l"

	def build(self, c):
		c.LINKCMDS		= ['src/lib/libbsp/powerpc/gen5200/startup/linkcmds.brs6l', 'src/lib/libbsp/powerpc/gen5200/startup/linkcmds.base']

	def header(self, c):
		c.MPC5200_BOARD_BRS6L		= True


class gen83xx_shared(Base):
	def header(self, c):
		c.BSP_CONSOLE_BAUD		= 9600
		c.GEN83XX_ENABLE_INTERRUPT_NESTING		= Default

	def build(self, c):
		c.CFLAGS		= ['-mcpu=603e', '-meabi', '-msdata', '-fno-common', '-mstrict-align']
		# XXX: These extra linkcmds need to move below.
		c.LINKCMDS		= ['src/lib/libbsp/powerpc/gen83xx/startup/linkcmds.hsc_cm01',
						'src/lib/libbsp/powerpc/shared/startup/linkcmds.base',
						'src/lib/libbsp/powerpc/gen83xx/startup/linkcmds.mpc83xx',
						'src/lib/libbsp/powerpc/gen83xx/startup/linkcmds.mpc8349eamds',
						'src/lib/libbsp/powerpc/gen83xx/startup/linkcmds.mpc8313erdb']
		c.LINK_START		= ['ecrti.o', '${RTEMS}/rtems_crti.o', 'crtbegin.o', '${RTEMS}/start.o']
		c.LINK_END		= ['crtend.o', 'ecrtn.o']
		c.LINK_LINK		= ['-u', '__vectors']



class br_uid(gen83xx_shared):
	name = "powerpc/br_uid"

	def build(self, c):
		c.LINKCMDS		= ['src/lib/libbsp/powerpc/gen83xx/startup/linkcmds.br_uid', 'src/lib/libbsp/powerpc/gen83xx/startup/linkcmds.mpc83xx', 'src/lib/libbsp/powerpc/shared/startup/linkcmds.base']

	def header(self, c):
		c.MPC83XX_BOARD_BR_UID						= True
		c.MPC83XX_NETWORK_INTERFACE_0_PHY_ADDR		= "-1"
		c.MPC83XX_CHIP_TYPE							= 8309
		c.MPC83XX_HAS_NAND_LP_FLASH_ON_CS0			= True


class mpc8349eamds(gen83xx_shared):
	name = "powerpc/mpc8349eamds"

	def header(self, c):
		c.BSP_USE_UART2		= True
		c.HAS_UBOOT					= True
		c.MPC8349		= True
		c.MPC8349EAMDS		= True



class mpc8313erdb(gen83xx_shared):
	name = "powerpc/mpc8313erdb"

	def header(self, c):
		c.BSP_CONSOLE_BAUD		= 115200
		c.BSP_USE_UART2		= True
		c.BSP_USE_UART_INTERRUPTS		= Default
		c.HAS_UBOOT		= True
		c.MPC8313ERDB		= True
		c.MPC8349		= True



class hsc_cm01(gen83xx_shared):
	name = "powerpc/hsc_cm01"

	def header(self, c):
		c.BSP_USE_UART2		= True
		c.HSC_CM01		= True
		c.MPC8349		= True
		c.MPC83XX_BOARD_HSC_CM01 = Default


class mpc8309som(gen83xx_shared):
	name = "powerpc/mpc8309som"

	def build(self, c):
		c.LINKCMDS		= ['src/lib/libbsp/powerpc/gen83xx/startup/linkcmds.mpc8309som', 'src/lib/libbsp/powerpc/gen83xx/startup/linkcmds.mpc83xx', 'src/lib/libbsp/powerpc/shared/startup/linkcmds.base']

	def header(self, c):
		c.MPC83XX_BOARD_MPC8309SOM				= True
		c.MPC83XX_NETWORK_INTERFACE_0_PHY_ADDR	= "0x11"
		c.MPC83XX_CHIP_TYPE						= 8309
		c.HAS_UBOOT								= True



class haleakala(Base):
	name = "powerpc/haleakala"

	def build(self, c):
		c.CFLAGS		= ['-mcpu=405', '-Dppc405']
		c.LINKCMDS		= ['src/lib/libbsp/powerpc/haleakala/startup/linkcmds']
		c.LINK_START		= ['ecrti.o', '${RTEMS}/rtems_crti.o', 'crtbegin.o']
		c.LINK_END		= ['crtend.o', 'ecrtn.o']
		c.LINK_LINK		= ['-u', '__vectors', '-u', 'download_entry']

	def header(self, c):
		c.PPC_USE_SPRG		= Default
		c.PPC_VECTOR_FILE_BASE		= Default


class mbx8xx_shared(Base):
	def header(self, c):
		c.CONSOLE_MINOR		= "SMC2_MINOR"
		c.DISPATCH_HANDLER_STAT		= True
		c.EPPCBUG_SMC1		= Default
		c.EPPCBUG_VECTORS		= Default
		c.NVRAM_CONFIGURE		= Default
		c.PRINTK_IO_MODE		= Default
		c.PRINTK_MINOR		= "SMC2_MINOR"
		c.UARTS_IO_MODE		= Default
		c.UARTS_USE_TERMIOS		= Default

	def build(self, c):
		c.LINKCMDS		= ['src/lib/libbsp/powerpc/mbx8xx/startup/linkcmds']
		c.LINK_START		= ['ecrti.o', '-e', 'start']
		c.LINK_END		= ['ecrtn.o']
		c.LINK_LINK		= ['-u', '__vectors']


class mbx860_005b(mbx8xx_shared):
	name = "powerpc/mbx860_005b"

	def build(self, c):
		c.CFLAGS		= ['-mcpu=860', '-Dmpc860', '-Dmbx860_005b', '-meabi', '-msdata', '-fno-common']

	def header(self, c):
		c.CONSOLE_MINOR		= "SMC1_MINOR"
		c.EPPCBUG_SMC1		= Default
		c.EPPCBUG_VECTORS		= Default
		c.NVRAM_CONFIGURE		= False
		c.PRINTK_MINOR		= "SMC1_MINOR"
		c.UARTS_USE_TERMIOS		= True



class mbx821_002(mbx8xx_shared):
	name = "powerpc/mbx821_002"

	def build(self, c):
		c.CFLAGS		= ['-mcpu=821', '-Dmpc821', '-Dmbx821_002', '-meabi', '-msdata', '-fno-common']


class mbx821_001(mbx8xx_shared):
	name = "powerpc/mbx821_001"

	def build(self, c):
		c.CFLAGS		= ['-mcpu=821', '-Dmpc821', '-Dmbx821_001', '-meabi', '-msdata', '-fno-common']


class mbx860_1b(mbx8xx_shared):
	name = "powerpc/mbx860_1b"

	def build(self, c):
		c.CFLAGS		= ['-mcpu=860', '-Dmpc860', '-Dmbx860_001b', '-meabi', '-msdata', '-fno-common']


class mbx860_002(mbx8xx_shared):
	name = "powerpc/mbx860_002"

	def build(self, c):
		c.CFLAGS		= ['-mcpu=860', '-Dmpc860', '-Dmbx860_002', '-meabi', '-msdata', '-fno-common']


class mbx821_002b(mbx8xx_shared):
	name = "powerpc/mbx821_002b"

	def build(self, c):
		c.CFLAGS		= ['-mcpu=821', '-Dmpc821', '-Dmbx821_002b', '-meabi', '-msdata', '-fno-common']


class mbx860_001b(mbx8xx_shared):
	name = "powerpc/mbx860_001b"

	def build(self, c):
		c.CFLAGS		= ['-mcpu=860', '-Dmpc860', '-Dmbx860_001b', '-meabi', '-msdata', '-fno-common']


class motorola_powerpc_shared(Base):
	def header(self, c):
		c.CONFIGURE_MALLOC_BSP_SUPPORTS_SBRK		= Default

	def build(self, c):
		c.LINKCMDS		= ['src/lib/libbsp/powerpc/shared/startup/linkcmds']
		c.LINK_START		= ['ecrti.o', '${RTEMS}/rtems_crti.o', 'crtbegin.o', '${RTEMS}/vectors_entry.o', '${RTEMS}/start.o', '-e', '__rtems_entry_point', '-u', '__vectors']
		c.LINK_END		= ['crtend.o', 'ecrtn.o']
		c.LINK_LINK		= ['-Bstatic']


class mvme2307(motorola_powerpc_shared):
	name = "powerpc/mvme2307"

	def build(self, c):
		c.CFLAGS		= ['-mcpu=604', '-mmultiple', '-mstring', '-mstrict-align', '-meabi']

	def header(self, c):
		c.mpc8240		= True

class mvme2100(motorola_powerpc_shared):
	name = "powerpc/mvme2100"

	def build(self, c):
		c.CFLAGS		= ['-mcpu=603e', '-Dppc603e']

	def header(self, c):
		c.mvme2100		= True



class mtx603e(motorola_powerpc_shared):
	name = "powerpc/mtx603e"

	def build(self, c):
		c.CFLAGS		= ['-mcpu=603e', '-Dppc603e']


class mcp750(motorola_powerpc_shared):
	name = "powerpc/mcp750"

	def build(self, c):
		c.CFLAGS		= ['-mcpu=750', '-Dmpc750']


class qemuprep(motorola_powerpc_shared):
	name = "powerpc/qemuprep"

	def build(self, c):
		c.CFLAGS			= ['-mcpu=powerpc', '-mmultiple', '-mstring', '-mstrict-align', '-D__ppc_generic']

	def header(self, c):
		c.qemu				= True


class qemuprep_altivec(motorola_powerpc_shared):
	name = "powerpc/qemuprep-altivec"

	def build(self, c):
		c.CFLAGS			= ['-mcpu=7400', '-mmultiple', '-mstring', '-mstrict-align', '-D__ppc_generic']

	def header(self, c):
		c.qemu				= True


class mpc55xxevb_shared(Base):
	def header(self, c):
		c.MPC55XX_BOOTFLAGS		= Default
		c.MPC55XX_CHIP_TYPE		= 5554
		c.MPC55XX_CHIP_FAMILY	= Default
		c.MPC55XX_CLOCK_EMIOS_CHANNEL		= "(MPC55XX_EMIOS_CHANNEL_NUMBER-1)"
		c.MPC55XX_EMIOS_PRESCALER		= Default
		c.MPC55XX_ESCI_CONSOLE_MINOR		= Default
		c.MPC55XX_ESCI_USE_INTERRUPTS		= Default
		c.MPC55XX_FMPLL_CLK_OUT		= 128000000
		c.MPC55XX_FMPLL_MFD		= 12
		c.MPC55XX_FMPLL_PREDIV		= Default
		c.MPC55XX_FMPLL_REF_CLOCK		= 8000000
		c.SMSC9218I_EDMA_RX_CHANNEL		= Default
		c.SMSC9218I_EDMA_TX_CHANNEL		= Default
		c.SMSC9218I_BIG_ENDIAN_SUPPORT	= Default
		c.SMSC9218I_ENABLE_LED_OUTPUTS	= Default
		c.SMSC9218I_RESET_PIN			= Default
		c.SMSC9218I_IRQ_PIN				= Default
		c.MPC55XX_SYSTEM_CLOCK_DIVIDER	= Default
		c.MPC55XX_FMPLL_ESYNCR1_CLKCFG	= Default
		c.MPC55XX_CONSOLE_MINOR			= Default
		c.BSP_DEFAULT_BAUD_RATE			= Default
		c.MPC55XX_EARLY_STACK_SIZE		= Default
		c.MPC55XX_REFERENCE_CLOCK		= Default

	def build(self, c):
		c.CFLAGS		= ['-mcpu=8540', '-meabi', '-msdata', '-fno-common', '-msoft-float', '-D__ppc_generic', '-mstrict-align']
		c.LINK_START	= ['ecrti.o', '${RTEMS}/rtems_crti.o', 'crtbegin.o', '${RTEMS}/start.o']
		c.LINK_END		= ['crtend.o', 'ecrtn.o']


class gwlcfm(mpc55xxevb_shared):
	name = "powerpc/gwlcfm"

	def build(self, c):
		c.LINKCMDS		= ['src/lib/libbsp/powerpc/mpc55xxevb/startup/linkcmds.gwlcfm', 'src/lib/libbsp/powerpc/mpc55xxevb/startup/linkcmds.mpc55xx', 'src/lib/libbsp/powerpc/shared/startup/linkcmds.base']

	def header(self, c):
		c.MPC55XX_BOARD_GWLCFM		= True
		c.MPC55XX_CHIP_TYPE		= 5516
		c.MPC55XX_EMIOS_PRESCALER		= 66
		c.MPC55XX_FMPLL_CLK_OUT		= 66000000
		c.MPC55XX_FMPLL_MFD		= 99
		c.MPC55XX_FMPLL_PREDIV		= 10
		c.MPC55XX_FMPLL_REF_CLOCK		= 40000000
		c.RTEMS_BSP_I2C_EEPROM_DEVICE_NAME		= "'\"eeprom\"'"
		c.RTEMS_BSP_I2C_EEPROM_DEVICE_PATH		= "'\"/dev/i2c1.eeprom\"'"
		c.MPC55XX_REFERENCE_CLOCK		= 40000000
		c.MPC55XX_SYSTEM_CLOCK			= 66000000


class mpc5566evb(mpc55xxevb_shared):
	name = "powerpc/mpc5566evb"

	def build(self, c):
		c.LINKCMDS		= ['src/lib/libbsp/powerpc/mpc55xxevb/startup/linkcmds.mpc5566evb', 'src/lib/libbsp/powerpc/shared/startup/linkcmds.base', 'src/lib/libbsp/powerpc/mpc55xxevb/startup/linkcmds.mpc55xx']

	def header(self, c):
		c.MPC55XX_BOARD_MPC5566EVB			= True
		c.MPC55XX_CHIP_TYPE					= 5566
		c.MPC55XX_REFERENCE_CLOCK			= 40000000
		c.MPC55XX_SYSTEM_CLOCK				= Default
		c.MPC55XX_REFERENCE_CLOCK			= 40000000

class mpc5566evb_spe(mpc55xxevb_shared):
	name = "powerpc/mpc5566evb_spe"

	def build(self, c):
		c.LINKCMDS		= ['src/lib/libbsp/powerpc/mpc55xxevb/startup/linkcmds.mpc5566evb_spe', 'src/lib/libbsp/powerpc/mpc55xxevb/startup/linkcmds.mpc5566evb', 'src/lib/libbsp/powerpc/mpc55xxevb/startup/linkcmds.mpc5674fevb', 'src/lib/libbsp/powerpc/shared/startup/linkcmds.base', 'src/lib/libbsp/powerpc/mpc55xxevb/startup/linkcmds.mpc55xx']

	def header(self, c):
		c.BSP_INTERRUPT_HANDLER_TABLE_SIZE	= 127
		c.MPC55XX_NULL_POINTER_PROTECTION	= True
		c.MPC55XX_CHIP_TYPE					= 5566
		c.MPC55XX_BOARD_MPC5566EVB			= True
		c.MPC55XX_REFERENCE_CLOCK			= 40000000


class mpc5643l_dpu(mpc55xxevb_shared):
	name = "powerpc/mpc5643l_dpu"

	def build(self, c):
		c.LINKCMDS		= ['src/lib/libbsp/powerpc/mpc55xxevb/startup/linkcmds.mpc5643l_dpu', 'src/lib/libbsp/powerpc/mpc55xxevb/startup/linkcmds.mpc5643l_evb', 'src/lib/libbsp/powerpc/shared/startup/linkcmds.base', 'src/lib/libbsp/powerpc/mpc55xxevb/startup/linkcmds.mpc55xx']

	def header(self, c):
		c.BSP_INTERRUPT_HANDLER_TABLE_SIZE	= 127
		c.MPC55XX_REFERENCE_CLOCK			= 40000000
		c.MPC55XX_EMIOS_PRESCALER			= Disable
		c.MPC55XX_CLOCK_EMIOS_CHANNEL		= Disable
		c.MPC55XX_CLOCK_PIT_CHANNEL			= 3
		c.MPC55XX_CHIP_TYPE					= 5643
		c.BSP_DATA_CACHE_ENABLED			= False

class mpc5643l_evb(mpc55xxevb_shared):
	name = "powerpc/mpc5643l_evb"

	def build(self, c):
		c.LINKCMDS		= ['src/lib/libbsp/powerpc/mpc55xxevb/startup/linkcmds.mpc5643l_evb', 'src/lib/libbsp/powerpc/shared/startup/linkcmds.base', 'src/lib/libbsp/powerpc/mpc55xxevb/startup/linkcmds.mpc55xx']

	def header(self, c):
		c.BSP_INTERRUPT_HANDLER_TABLE_SIZE	= 127
		c.MPC55XX_REFERENCE_CLOCK			= 40000000
		c.MPC55XX_EMIOS_PRESCALER			= Disable
		c.MPC55XX_CLOCK_EMIOS_CHANNEL		= Disable
		c.MPC55XX_CLOCK_PIT_CHANNEL			= 3
		c.MPC55XX_CHIP_TYPE					= 5643
		c.BSP_DATA_CACHE_ENABLED			= False


class mpc5674f_ecu508_app(mpc55xxevb_shared):
	name = "powerpc/mpc5674f_ecu508_app"

	def build(self, c):
		c.LINKCMDS		= ['src/lib/libbsp/powerpc/mpc55xxevb/startup/linkcmds.mpc5674f_ecu508_app', 'src/lib/libbsp/powerpc/mpc55xxevb/startup/linkcmds.mpc5674f_ecu508', 'src/lib/libbsp/powerpc/shared/startup/linkcmds.base', 'src/lib/libbsp/powerpc/mpc55xxevb/startup/linkcmds.mpc55xx']

	def header(self, c):
		c.BSP_INTERRUPT_HANDLER_TABLE_SIZE	= 255
		c.MPC55XX_CHIP_TYPE					= 5674
		c.MPC55XX_CLOCK_EMIOS_CHANNEL		= "31"
		c.MPC55XX_FMPLL_MFD					= 66
		c.MPC55XX_FMPLL_PREDIV				= 5
		c.MPC55XX_NULL_POINTER_PROTECTION	= True
		c.MPC55XX_REFERENCE_CLOCK			= 40000000
		c.MPC55XX_SYSTEM_CLOCK				= 264000000
		c.MPC55XX_SYSTEM_CLOCK_DIVIDER		= 2
		c.MPC55XX_NEEDS_LOW_LEVEL_INIT		= Default
		c.BSP_DATA_CACHE_USE_WRITE_THROUGH	= True
		c.MPC55XX_BOARD_MPC5674F_ECU508		= True
		c.MPC55XX_CONSOLE_MINOR				= 2
		c.SMSC9218I_BIG_ENDIAN_SUPPORT		= True
		c.SMSC9218I_ENABLE_LED_OUTPUTS		= True
		c.SMSC9218I_IRQ_PIN					= 450
		c.SMSC9218I_RESET_PIN				= 433


class mpc5674f_ecu508_boot(mpc55xxevb_shared):
	name = "powerpc/mpc5674f_ecu508_boot"

	def build(self, c):
		c.LINKCMDS		= ['src/lib/libbsp/powerpc/mpc55xxevb/startup/linkcmds.mpc5674f_ecu508_boot', 'src/lib/libbsp/powerpc/mpc55xxevb/startup/linkcmds.mpc5674f_ecu508', 'src/lib/libbsp/powerpc/shared/startup/linkcmds.base', 'src/lib/libbsp/powerpc/mpc55xxevb/startup/linkcmds.mpc55xx']

	def header(self, c):
		c.BSP_INTERRUPT_HANDLER_TABLE_SIZE	= 255
		c.MPC55XX_CHIP_TYPE					= 5674
		c.MPC55XX_CLOCK_EMIOS_CHANNEL		= "31"
		c.MPC55XX_FMPLL_MFD					= 66
		c.MPC55XX_FMPLL_PREDIV				= 5
		c.MPC55XX_NULL_POINTER_PROTECTION	= True
		c.MPC55XX_REFERENCE_CLOCK			= 40000000
		c.MPC55XX_SYSTEM_CLOCK				= 264000000
		c.MPC55XX_SYSTEM_CLOCK_DIVIDER		= 2
		c.BSP_DATA_CACHE_USE_WRITE_THROUGH	= True
		c.MPC55XX_BOARD_MPC5674F_ECU508		= True
		c.MPC55XX_CONSOLE_MINOR				= 2
		c.SMSC9218I_BIG_ENDIAN_SUPPORT		= True
		c.SMSC9218I_ENABLE_LED_OUTPUTS		= True
		c.SMSC9218I_IRQ_PIN					= 450
		c.SMSC9218I_RESET_PIN				= 433



class mpc5674f_rsm6(mpc55xxevb_shared):
	name = "powerpc/mpc5674f_rsm6"

	def build(self, c):
		c.LINKCMDS		= ['src/lib/libbsp/powerpc/mpc55xxevb/startup/linkcmds.mpc5674f_rsm6', 'src/lib/libbsp/powerpc/mpc55xxevb/startup/linkcmds.mpc5674f_rsm6_base', 'src/lib/libbsp/powerpc/shared/startup/linkcmds.base', 'src/lib/libbsp/powerpc/mpc55xxevb/startup/linkcmds.mpc55xx']

	def header(self, c):
		c.BSP_INTERRUPT_HANDLER_TABLE_SIZE	= 255
		c.MPC55XX_CHIP_TYPE					= 5674
		c.MPC55XX_CLOCK_EMIOS_CHANNEL		= "31"
		c.MPC55XX_FMPLL_MFD					= 66
		c.MPC55XX_FMPLL_PREDIV				= 5
		c.MPC55XX_NULL_POINTER_PROTECTION	= True
		c.MPC55XX_REFERENCE_CLOCK			= 40000000
		c.MPC55XX_SYSTEM_CLOCK				= 264000000
		c.MPC55XX_SYSTEM_CLOCK_DIVIDER		= 2
		c.MPC55XX_BOARD_MPC5674F_RSM6		= True
		c.MPC55XX_ENABLE_START_PROLOGUE		= True
		c.MPC55XX_FMPLL_ESYNCR1_CLKCFG		= 6



class mpc5674fevb(mpc55xxevb_shared):
	name = "powerpc/mpc5674fevb"

	def build(self, c):
		c.LINKCMDS		= ['src/lib/libbsp/powerpc/mpc55xxevb/startup/linkcmds.mpc5674fevb', 'src/lib/libbsp/powerpc/shared/startup/linkcmds.base', 'src/lib/libbsp/powerpc/mpc55xxevb/startup/linkcmds.mpc55xx']

	def header(self, c):
		c.BSP_INTERRUPT_HANDLER_TABLE_SIZE	= 255
		c.MPC55XX_CHIP_TYPE					= 5674
		c.MPC55XX_CLOCK_EMIOS_CHANNEL		= "31"
		c.MPC55XX_FMPLL_MFD					= 66
		c.MPC55XX_FMPLL_PREDIV				= 5
		c.MPC55XX_NULL_POINTER_PROTECTION	= True
		c.MPC55XX_REFERENCE_CLOCK			= 40000000
		c.MPC55XX_SYSTEM_CLOCK				= 264000000
		c.MPC55XX_SYSTEM_CLOCK_DIVIDER		= 2
		c.MPC55XX_BOARD_MPC5674FEVB			= True


class mpc5674fevb_spe(mpc55xxevb_shared):
	name = "powerpc/mpc5674fevb_spe"

	def build(self, c):
		c.LINKCMDS		= ['src/lib/libbsp/powerpc/mpc55xxevb/startup/linkcmds.mpc5674fevb_spe', 'src/lib/libbsp/powerpc/mpc55xxevb/startup/linkcmds.mpc5674fevb', 'src/lib/libbsp/powerpc/shared/startup/linkcmds.base', 'src/lib/libbsp/powerpc/mpc55xxevb/startup/linkcmds.mpc55xx']

	def header(self, c):
		c.BSP_INTERRUPT_HANDLER_TABLE_SIZE	= 255
		c.MPC55XX_CHIP_TYPE					= 5674
		c.MPC55XX_CLOCK_EMIOS_CHANNEL		= "31"
		c.MPC55XX_FMPLL_MFD					= 66
		c.MPC55XX_FMPLL_PREDIV				= 5
		c.MPC55XX_NULL_POINTER_PROTECTION	= True
		c.MPC55XX_REFERENCE_CLOCK			= 40000000
		c.MPC55XX_SYSTEM_CLOCK				= 264000000
		c.MPC55XX_SYSTEM_CLOCK_DIVIDER		= 2
		c.MPC55XX_BOARD_MPC5674FEVB			= True



class phycore_mpc5554(mpc55xxevb_shared):
	name = "powerpc/phycore_mpc5554"

	def build(self, c):
		c.LINKCMDS		= ['src/lib/libbsp/powerpc/mpc55xxevb/startup/linkcmds.phycore_mpc5554', 'src/lib/libbsp/powerpc/shared/startup/linkcmds.base', 'src/lib/libbsp/powerpc/mpc55xxevb/startup/linkcmds.mpc55xx']

	def header(self, c):
		c.HAS_SMC91111						= True
		c.SMC91111_ENADDR_IS_SETUP			= True
		c.MPC55XX_BOARD_PHYCORE_MPC5554		= True



class mpc8260ads(Base):
	name = "powerpc/mpc8260ads"

	def build(self, c):
		c.CFLAGS		= ['-mcpu=603e', '-mstrict-align', '-Dmpc8260', '-meabi', '-msdata', '-fno-common']
		c.LINKCMDS		= ['src/lib/libbsp/powerpc/mpc8260ads/startup/linkcmds']
		c.LINK_START		= ['ecrti.o', '${RTEMS}/start.o', '-e', 'start', '-u', '__vectors']
		c.LINK_END		= ['ecrtn.o']

	def header(self, c):
		c.CONSOLE_MINOR		= "SCC2_MINOR"
		c.DISPATCH_HANDLER_STAT		= True
		c.PRINTK_MINOR		= "SMC2_MINOR"
		c.UARTS_IO_MODE		= Default
		c.UARTS_USE_TERMIOS		= Default



class mvme3100(Base):
	name = "powerpc/mvme3100"

	def build(self, c):
		c.CFLAGS		= ['-mcpu=powerpc', '-msoft-float', '-D__ppc_generic']
		c.LINKCMDS		= ['src/lib/libbsp/powerpc/shared/startup/linkcmds']
		c.LINK_START		= ['ecrti.o', '${RTEMS}/rtems_crti.o', 'crtbegin.o',
					   '-e', '__rtems_entry_point', '-u', '__vectors',
					   '${RTEMS}/preload.o', '${RTEMS}/vectors_entry.o', '${RTEMS}/start.o']
		c.LINK_END		= ['crtend.o', 'ecrtn.o']
		c.LINK_LINK		= ['-Bstatic']

	def header(self, c):
		c.CONFIGURE_MALLOC_BSP_SUPPORTS_SBRK		= Default



class mvme5500(Base):
	name = "powerpc/mvme5500"

	def build(self, c):
		c.CFLAGS		= ['-mcpu=7450', '-mtune=7450', '-Dmpc7455']
		c.LINKCMDS		= ['src/lib/libbsp/powerpc/shared/startup/linkcmds']
		c.LINK_START		= ['ecrti.o', '${RTEMS}/rtems_crti.o', 'crtbegin.o',
					   '-e', '__rtems_entry_point', '-u', '__vectors',
					   '${RTEMS}/preload.o', '${RTEMS}/start.o']
		c.LINK_END		= ['crtend.o', 'ecrtn.o']
		c.LINK_LINK		= ['-Bstatic']
		c.ENABLE_NETWORKING	= False # broken VPD.h header

	def header(self, c):
		c.CONFIGURE_MALLOC_BSP_SUPPORTS_SBRK		= Default



class psim(Base):
	name = "powerpc/psim"

	def build(self, c):
		c.CFLAGS		= ['-mcpu=603e', '-Dppc603e']
		c.LINKCMDS		= ['src/lib/libbsp/powerpc/psim/startup/linkcmds', 'src/lib/libbsp/powerpc/shared/startup/linkcmds.base']
		c.LINK_START		= ['ecrti.o', '${RTEMS}/rtems_crti.o', 'crtbegin.o',
					   '${RTEMS}/start.o', '-e', '_start', '-u', '__vectors']
		c.LINK_END		= ['crtend.o', 'ecrtn.o']
		c.LINK_LINK		= ['-Bstatic']

	def header(self, c):
		c.CLOCK_DRIVER_USE_FAST_IDLE		= True
		c.CONFIGURE_MALLOC_BSP_SUPPORTS_SBRK		= Default
		c.PPC_USE_SPRG		= False
		c.PPC_VECTOR_FILE_BASE		= "0xFFF00100"



class qemuppc(Base):
	name = "powerpc/qemuppc"

	def build(self, c):
		c.CFLAGS		= ['-mcpu=603e', '-Dppc603e']
		c.LINKCMDS		= ['src/lib/libbsp/powerpc/qemuppc/startup/linkcmds']
		c.LINK_START		= ['ecrti.o', '${RTEMS}/rtems_crti.o', 'crtbegin.o',
					   '${RTEMS}/start.o', '-e', '_start', '-u', '__vectors']
		c.LINK_END		= ['crtend.o', 'ecrtn.o']
		c.LINK_LINK		= ['-Bstatic']



class qoriq_shared(Base):
	name = "powerpc/qoriq"

	def build(self, c):
		c.CFLAGS		= ['-mcpu=8540', '-meabi', '-msdata', '-fno-common', '-mstrict-align', '-mspe', '-mabi=spe', '-mfloat-gprs=double', '-D__ppc_generic']
		c.LINK_START	= ['ecrti.o', '${RTEMS}/rtems_crti.o', 'crtbegin.o', '${RTEMS}/start.o']
		c.LINK_END		= ['crtend.o', 'ecrtn.o']
		c.LINK_LINK		= ['-u', '__vectors']

	def header(self, c):
		c.BSP_CONSOLE_BAUD							= 115200
		c.BSP_DISABLE_UBOOT_WORK_AREA_CONFIG		= Default
		c.BSP_INTERRUPT_STACK_AT_WORK_AREA_BEGIN	= Default
		c.BSP_USE_UART_INTERRUPTS					= Default
		c.HAS_UBOOT									= True
		c.QORIQ_CLOCK_TIMER							= Default
		c.QORIQ_ETSEC_1_PHY_ADDR					= -1
		c.QORIQ_ETSEC_2_PHY_ADDR					= Default
		c.QORIQ_ETSEC_3_PHY_ADDR					= Default
		c.QORIQ_INITIAL_MSR							= Default
		c.QORIQ_INITIAL_SPEFSCR						= Default
		c.QORIQ_INTERCOM_AREA_BEGIN					= Default
		c.QORIQ_INTERCOM_AREA_SIZE					= Default
		c.QORIQ_UART_0_ENABLE						= Default
		c.QORIQ_UART_1_ENABLE						= Default
		c.QORIQ_UART_BRIDGE_0_ENABLE				= Default
		c.QORIQ_UART_BRIDGE_1_ENABLE				= Default
		c.QORIQ_UART_BRIDGE_MASTER_CORE				= Default
		c.QORIQ_UART_BRIDGE_SLAVE_CORE				= Default
		c.QORIQ_UART_BRIDGE_TASK_PRIORITY			= 250


class qoriq_core_0(qoriq_shared):
	name = "powerpc/qoriq_core_0"

	def build(self, c):
		c.LINKCMDS		= ['src/lib/libbsp/powerpc/qoriq/startup/linkcmds.qoriq_core_0', 'src/lib/libbsp/powerpc/shared/startup/linkcmds.base']

	def header(self, c):
		c.QORIQ_UART_0_ENABLE			= True
		c.QORIQ_UART_1_ENABLE			= True
		c.QORIQ_UART_BRIDGE_1_ENABLE	= Default


class qoriq_core_1(qoriq_shared):
	name = "powerpc/qoriq_core_1"

	def build(self, c):
		c.LINKCMDS		= ['src/lib/libbsp/powerpc/qoriq/startup/linkcmds.qoriq_core_1', 'src/lib/libbsp/powerpc/shared/startup/linkcmds.base']

	def header(self, c):
		c.QORIQ_UART_BRIDGE_1_ENABLE	= True
		c.QORIQ_CLOCK_TIMER				= 4


class qoriq_p1020rdb(qoriq_shared):
	name = "powerpc/qoriq_p1020rdb"

	def build(self, c):
		c.LINKCMDS		= ['src/lib/libbsp/powerpc/qoriq/startup/linkcmds.qoriq_p1020rdb', 'src/lib/libbsp/powerpc/shared/startup/linkcmds.base']

	def header(self, c):
		c.QORIQ_UART_0_ENABLE			= True
		c.QORIQ_UART_1_ENABLE			= True


class score603e(Base):
	name = "powerpc/score603e"

	def build(self, c):
		c.CFLAGS		= ['-mcpu=603e', '-Dppc603e']
		c.LINKCMDS		= ['src/lib/libbsp/powerpc/score603e/startup/linkcmds']
		c.LINK_START		= ['ecrti.o', '${RTEMS}/start.o', '-e', '_start', '-u', '__vectors']
		c.LINK_END		= ['ecrtn.o']
		c.LINK_LINK		= ['-Bstatic']

	def header(self, c):
		c.CONFIGURE_MALLOC_BSP_SUPPORTS_SBRK		= Default
		c.CONSOLE_USE_INTERRUPTS		= Default
		c.HAS_PMC_PSC8		= True
		c.INITIALIZE_COM_PORTS		= False
		c.PPC_USE_SPRG		= False
		c.PPC_VECTOR_FILE_BASE		= Default
		c.SCORE603E_OPEN_FIRMWARE		= Default
		c.SCORE603E_USE_DINK		= True
		c.SCORE603E_USE_NONE		= Default
		c.SCORE603E_USE_SDS		= Default



class ss555(Base):
	name = "powerpc/ss555"

	def build(self, c):
		c.CFLAGS		= ['-mcpu=505', '-Dmpc555']
		c.LINKCMDS		= ['src/lib/libbsp/powerpc/ss555/startup/linkcmds']
		c.LINK_START		= ['ecrti.o', '-u', '__vectors', '-N', '-u', 'start', '-e', 'start']
		c.LINK_END		= ['ecrtn.o']

	def header(self, c):
		c.CONSOLE_MINOR		= "SCI2_MINOR"
		c.PRINTK_MINOR		= "SCI2_MINOR"
		c.UARTS_IO_MODE		= Default
		c.UARTS_USE_TERMIOS		= Default
		c.WATCHDOG_TIMEOUT		= Default


class t32mppc(Base):
	name = "powerpc/t32mppc"

	def build(self, c):
		c.CFLAGS		= ['-mcpu=8540', '-meabi', '-msdata', '-fno-common', '-msoft-float', '-D__ppc_generic']
		c.LINKCMDS		= ['src/lib/libbsp/powerpc/t32mppc/startup/linkcmds.t32mppc', 'src/lib/libbsp/powerpc/shared/startup/linkcmds.base']
		c.LINK_START	= ['ecrti.o', '${RTEMS}/rtems_crti.o', 'crtbegin.o', '${RTEMS}/start.o']
		c.LINK_END		= ['crtend.o', 'ecrtn.o']
		c.LINK_LINK		= ['-dc', '-dp', '-u', '__vectors', '-N']

	def header(self, c):
		c.BSP_INSTRUCTION_CACHE_ENABLED		= True
		c.BSP_DATA_CACHE_ENABLED			= True



class tqm8xx_shared(Base):
	def header(self, c):
		c.BSP_USE_NETWORK_FEC		= Default
		c.BSP_USE_NETWORK_SCC		= True
		c.CONSOLE_CHN		= "CONS_CHN_SMC1"
		c.CONS_SCC1_MODE		= Default
		c.CONS_SCC2_MODE		= Default
		c.CONS_SCC3_MODE		= Default
		c.CONS_SCC4_MODE		= Default
		c.CONS_SMC1_MODE		= Default
		c.CONS_SMC2_MODE		= Default
		c.PRINTK_CHN		= "CONS_CHN_SMC1"
		c.SPI_BOARD_INIT_FNC		= Default
		c.SPI_SEND_ADDR_FNC		= Default
		c.SPI_SEND_STOP_FNC		= Default

	def build(self, c):
		c.CFLAGS		= ['-mcpu=860', '-Dmpc860', '-mstrict-align', '-fno-strict-aliasing',
					   '-meabi', '-msdata', '-fno-common']
		c.LINKCMDS		= ['src/lib/libbsp/powerpc/tqm8xx/startup/linkcmds.tqm8xx',
					   'src/lib/libbsp/powerpc/tqm8xx/startup/linkcmds.base']
		c.LINK_START		= ['ecrti.o', '${RTEMS}/rtems_crti.o', 'crtbegin.o',
					   '${RTEMS}/start.o', '-u', '__vectors']
		c.LINK_END		= ['crtend.o', 'ecrtn.o']


class pghplus(tqm8xx_shared):
	name = "powerpc/pghplus"

	def header(self, c):
		c.BSP_USE_NETWORK_FEC		= True
		c.BSP_USE_NETWORK_SCC		= Default
		c.CONS_SMC1_MODE		= "CONS_MODE_IRQ"
		c.SPI_BOARD_INIT_FNC		= "bsp_pghplus_spi_init"
		c.SPI_SEND_ADDR_FNC		= "bsp_pghplus_spi_sel_addr"
		c.SPI_SEND_STOP_FNC		= "bsp_pghplus_spi_send_stop"

class tqm8xx_stk8xx(tqm8xx_shared):
	name = "powerpc/tqm8xx_stk8xx"

	def header(self, c):
		c.CONS_SMC1_MODE		= "CONS_MODE_POLLED"
		c.CONS_SMC2_MODE		= "CONS_MODE_POLLED"



class virtex(Base):
	name = "powerpc/virtex"

	def build(self, c):
		c.CFLAGS		= ['-mcpu=403', '-Dppc405']
		c.LINKCMDS		= ['src/lib/libbsp/powerpc/virtex/startup/linkcmds']
		c.LINK_START	= ['ecrti.o', '${RTEMS}/rtems_crti.o', 'crtbegin.o', '-u', '__vectors', '-u', 'download_entry']
		c.LINK_END		= ['crtend.o', 'ecrtn.o']

	def header(self, c):
		c.PPC_USE_SPRG			= Default
		c.PPC_VECTOR_FILE_BASE	= Default
		c.RTEMS_XPARAMETERS_H	= Default
		c.RTEMS_XPPC_BASE		= Default


class virtex4(Base):
	name = "powerpc/virtex4"

	def build(self, c):
		c.CFLAGS		= ['-mcpu=405', '-Dppc405']
		c.LINKCMDS		= ['src/lib/libbsp/powerpc/virtex4/startup/linkcmds']
		c.LINK_START	= ['ecrti.o', '${RTEMS}/rtems_crti.o', 'crtbegin.o']
		c.LINK_END		= ['crtend.o', 'ecrtn.o']
		c.LINK_LINK		= ['-dc', '-dp', '-Bstatic', '-u', '__vectors', '-u', 'download_entry', '-N']

		def header(self, c):
			c.PPC_USE_DATA_CACHE		= True
			c.PPC_USE_SPRG				= True
			c.PPC_VECTOR_FILE_BASE		= "0x0100"


class virtex5(Base):
	name = "powerpc/virtex5"

	def build(self, c):
		c.CFLAGS		= ['-mcpu=440', '-Dppc440', '-msoft-float']
		c.LINKCMDS		= ['src/lib/libbsp/powerpc/virtex5/startup/linkcmds']
		c.LINK_START	= ['ecrti.o', '${RTEMS}/rtems_crti.o', 'crtbegin.o']
		c.LINK_END		= ['crtend.o', 'ecrtn.o']
		c.LINK_LINK		= ['-dc', '-dp', '-Bstatic', '-u', '__vectors', '-u', 'download_entry', '-N']

		def header(self, c):
			c.PPC_USE_DATA_CACHE		= True
			c.PPC_USE_SPRG				= True
			c.PPC_VECTOR_FILE_BASE		= "0x0100"
