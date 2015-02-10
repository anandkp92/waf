from rtems_waf.config.options import Boolean, Integer, String, StringList


class ALLOW_IRQ_NESTING(Boolean):
	value	= True
	undef	= True
	descr	= "If set to !0, allow nested irq processing"


class ARM_CLK(Boolean):
	value	= False
	undef	= True
	descr	= "Arm clock in hz"


class BENCHMARK_IRQ_PROCESSING(Boolean):
	value	= False
	undef	= True
	descr	= "If set to !0, enable code to benchmark irq processing"


class BFIN_ON_SKYEYE(Boolean):
	value	= False
	undef	= True
	descr	= """
If defined, disable features which are not supported on skyeye.
		"""


class BSP(StringList):
	value	= []
	undef	= True
	descr	= "List of bsps to build, comma delimited."


class BSP_CONSOLE_BAUD(Integer):
	value	= 9600
	undef	= True
	descr	= "The default console baud rate."


class BSP_CPU_CLOCK_SPEED(Integer):
	value	= 0
	undef	= True
	descr	= "The cpu clock frequency."


class BSP_DATA_CACHE_ENABLED(Boolean):
	value	= True
	undef	= True
	descr	= "Enables the data cache, if defined to a value other than zero"


class BSP_DIRTY_MEMORY(Boolean):
	value	= False
	undef	= True
	descr	= """
If defined, then the bsp framework will put a non-zero pattern into the rtems
workspace and C program heap. This should assist in finding code that assumes
memory starts set to zero.
		"""


class BSP_DISABLE_UBOOT_WORK_AREA_CONFIG(Integer):
	value	= 1
	undef	= True
	descr	= "Disable u-boot work area configuration"


class BSP_GPIOPCR_INITMASK(String):
	value	= "0x330F0F77"
	undef	= True
	descr	= """
Defines the bits modified in the mpc5200 gpiopcr register during init. Must
match the hardware requirements
		"""


class BSP_GPIOPCR_INITVAL(String):
	value	= "0x01050444"
	undef	= True
	descr	= """
Defines the bit values written in the mpc5200 gpiopcr register during init.
Must match the hardware requirements
		"""


class BSP_HAS_RM52xx(Integer):
	value	= 1
	undef	= True
	descr	= "This bsp has a rm52xx compatible cpu."


class BSP_HAS_SMP(Integer):
	value	= 1
	undef	= True
	descr	= """
Always defined when on a pc386 to enable the pc386 support for  determining
the cpu core number in an smp configuration.
		"""


class BSP_HAS_TX49xx(Integer):
	value	= 1
	undef	= True
	descr	= "This bsp has a rm52xx compatible cpu."


class BSP_HAS_USC320(Integer):
	value	= 1
	undef	= True
	descr	= "This bsp has a v3 usc320 system controller chip."


class BSP_INSTRUCTION_CACHE_ENABLED(Boolean):
	value	= True
	undef	= True
	descr	= """
Enables the instruction cache, if defined to a value other than zero
		"""


class BSP_INTERRUPT_STACK_AT_WORK_AREA_BEGIN(Integer):
	value	= 1
	undef	= True
	descr	= "Indicate that the interrupt stack is at the work area begin"


class BSP_LEON3_SMP(Integer):
	value	= 1
	undef	= True
	descr	= """
Always defined when on a leon3 to enable the leon3 support for  determining
the cpu core number in an smp configuration.
		"""


class BSP_PRESS_KEY_FOR_RESET(Boolean):
	value	= False
	undef	= True
	descr	= """
If defined, print a message and wait until pressed before resetting board when
application exits.
		"""


class BSP_RESET_BOARD_AT_EXIT(Boolean):
	value	= False
	undef	= True
	descr	= "If defined, reset the board when the application exits."


class BSP_SMALL_MEMORY(Boolean):
	value	= False
	undef	= True
	descr	= "Disable testsuite samples with high memory demands"


class BSP_START_RESET_VECTOR(String):
	value	= ""
	undef	= True
	descr	= "Reset vector address for bsp start"


class BSP_UART_AVAIL_MASK(String):
	value	= "0x01"
	undef	= True
	descr	= """
Bit mask to specify the uarts (pscs), which should be enabled on this board.
Must match the hardware requirements. Psc1 corresponds to the lsb
		"""


class BSP_USE_NETWORK_FEC(Boolean):
	value	= False
	undef	= True
	descr	= """
If defined, then the bsp will use the fast ethernet controller for 10/100mbit
networking and used as primary networking interface.
		"""


class BSP_USE_NETWORK_SCC(Boolean):
	value	= False
	undef	= True
	descr	= """
If defined, then the bsp will use the serial communications controller (scc1)
for 10mbit networking.
		"""


class BSP_USE_UART2(Boolean):
	value	= False
	undef	= True
	descr	= "If defined, enables uart2."


class BSP_USE_UART_INTERRUPTS(Boolean):
	value	= True
	undef	= True
	descr	= "Enable usage of interrupts for the uart modules"


class BSP_VIDEO_80x50(Boolean):
	value	= False
	undef	= True
	descr	= "If defined, set the vga display to 80x50."


class CC(String):
	value	= ""
	undef	= True
	descr	= "C compiler command"


class CCAS(String):
	value	= ""
	undef	= True
	descr	= "Assembler compiler command (defaults to CC)"


class CCASFLAGS(String):
	value	= ""
	undef	= True
	descr	= "Assembler compiler flags (defaults to cflags)"


class CCLK(Boolean):
	value	= False
	undef	= True
	descr	= "Cpu clock in hz"


class CD2401_INT_LEVEL(Integer):
	value	= 1
	undef	= True
	descr	= "Interrupt level for the cd2401 (when cd2401_io_mode == 1)."


class CD2401_IO_MODE(Integer):
	value	= 0
	undef	= True
	descr	= "0 for polled I/O, 1 for interrupt-driven."


class CD2401_USE_TERMIOS(Boolean):
	value	= False
	undef	= True
	descr	= "Enable using termios based console."


class CFLAGS(StringList):
	value	= []
	undef	= True
	descr	= "C compiler flags"


class CFLAGS_DEBUG(String):
	value	= ""
	undef	= True
	descr	= "Debug compiler flags."


class CFLAGS_OPTIMISE(String):
	value	= ""
	undef	= True
	descr	= "Compiler flags for optimisation"


class CLOCK_DRIVER_USE_8254(Integer):
	value	= 0
	undef	= True
	descr	= """
If enabled, the clock driver will use the good old 8254 chip  to report
microsecond-accuracy clock times.  Enable it, if:  - you have nanosecond
timing enabled (you do not have    use_ticks_for_cpu_usage_statistics enabled)
- you do not have clock_driver_use_tsc enabled (use one, the other,    or
neither)  - you do not mind adding roughly 5 microseconds to each context
switch.
		"""


class CLOCK_DRIVER_USE_8254CLOCK_DRIVER_USE_TSC(Boolean):
	value	= False
	undef	= True
	descr	= """
If enabled, the clock driver will use the good old 8254 chip to report
microsecond-accuracy clock times. Enable it, if: 1, you have nanosecond timing
enabled (you do not have use_ticks_for_cpu_usage_statistics enabled)  2, you
do not have clock_driver_use_tsc enabled (use one, the other, or neither  3,
you do not mind adding roughly 5 microseconds to each context switch.
		"""


class CLOCK_DRIVER_USE_FAST_IDLE(Boolean):
	value	= False
	undef	= True
	descr	= """
This sets a mode where the time runs as fast as possible when  a clock isr
occurs while the idle thread is executing.  This can  significantly reduce
simulation times.
		"""


class CLOCK_DRIVER_USE_TSC(Boolean):
	value	= False
	undef	= True
	descr	= """
If enabled, the clock driver will use the tsc register available with pentium-
class cpus to report close to nanosecond-accuracy clock times.  Enable it, if:
1, you have nanosecond timing enabled (you do not have
use_ticks_for_cpu_usage_statistics enabled 2, you do not have
clock_driver_use_8254 enabled (use one, the other, or neither 3, you have a
pentium which supports tsc (all intels, and probably all or most clones 4, you
do not have a variable-speed cpu clock. Note that some motherboard bios will
automatically vary clock speed for thermal control. Note also, however, that
really new pentium-class chips from intel and amd will maintain a constant-
rate tsc regardless.
		"""


class CONFIG_CFLAGS(StringList):
	value	= []
	undef	= True
	descr	= "Default compiler flags for rtems-config"


class CONFIG_CONSOLE(Boolean):
	value	= False
	undef	= True
	descr	= "Configuration for console (uart 0)"


class CONFIG_FPSP(Boolean):
	value	= False
	undef	= True
	descr	= """
If defined enables the motorola floating point support package (fpsp)
		"""


class CONFIG_I2C_0(Boolean):
	value	= False
	undef	= True
	descr	= "Configuration for i2c 0"


class CONFIG_I2C_1(Boolean):
	value	= False
	undef	= True
	descr	= "Configuration for i2c 1"


class CONFIG_I2C_2(Boolean):
	value	= False
	undef	= True
	descr	= "Configuration for i2c 2"


class CONFIG_LDFLAGS(StringList):
	value	= []
	undef	= True
	descr	= "Default linker flags for rtems-config"


class CONFIG_LIBS(StringList):
	value	= []
	undef	= True
	descr	= "= Default libraries for rtems-config"


class CONFIG_U3CLK(Boolean):
	value	= False
	undef	= True
	descr	= "Clock configuration for uart 3"


class CONFIG_U4CLK(Boolean):
	value	= False
	undef	= True
	descr	= "Clock configuration for uart 4"


class CONFIG_U5CLK(Boolean):
	value	= False
	undef	= True
	descr	= "Clock configuration for uart 5"


class CONFIG_U6CLK(Boolean):
	value	= False
	undef	= True
	descr	= "Clock configuration for uart 6"


class CONFIG_UART_1(Boolean):
	value	= False
	undef	= True
	descr	= "Configuration for uart 1"


class CONFIG_UART_2(Boolean):
	value	= False
	undef	= True
	descr	= "Configuration for uart 2"


class CONFIG_UART_3(Boolean):
	value	= False
	undef	= True
	descr	= "Configuration for uart 3"


class CONFIG_UART_CLKMODE(Boolean):
	value	= False
	undef	= True
	descr	= "Clock mode configuration for uarts"


class CONFIGURE_MALLOC_BSP_SUPPORTS_SBRK(Boolean):
	value	= True
	undef	= True
	descr	= """
If defined then the bsp may reduce the available memory size initially. This
can be useful for debugging (reduce the core size) or dynamic loading (std gcc
text offsets/Jumps are < +/-32m). Note that the policy can still be defined by
the application (see sbrk.C, bsp_sbrk_policy). By undefining
configure_malloc_bsp_supports_sbrk this feature is removed and a little memory
is saved.
		"""


class CONS_SCC1_MODE(String):
	value	= "CONS_MODE_UNUSED"
	undef	= True
	descr	= """
(Bsp--scc1 uart if mode) must be defined if scc1 is used as a tty (uart)
channel. Set it to cons_mode_polled for polled operation, cons_mode_irq for
interrupt driven (spooled) operation. Set it to cons_mode_unused, if not used
		"""


class CONS_SCC2_MODE(String):
	value	= "CONS_MODE_UNUSED"
	undef	= True
	descr	= """
(Bsp--scc2 uart if mode) must be defined if scc2 is used as a tty (uart)
channel. Set it to cons_mode_polled for polled operation, cons_mode_irq for
interrupt driven (spooled) operation. Set it to cons_mode_unused, if not used
		"""


class CONS_SCC3_MODE(String):
	value	= "CONS_MODE_UNUSED"
	undef	= True
	descr	= """
(Bsp--scc3 uart if mode) must be defined if scc3 is used as a tty (uart)
channel. Set it to cons_mode_polled for polled operation, cons_mode_irq for
interrupt driven (spooled) operation. Set it to cons_mode_unused, if not used
		"""


class CONS_SCC4_MODE(String):
	value	= "CONS_MODE_UNUSED"
	undef	= True
	descr	= """
(Bsp--scc4 uart if mode) must be defined if scc4 is used as a tty (uart)
channel. Set it to cons_mode_polled for polled operation, cons_mode_irq for
interrupt driven (spooled) operation. Set it to cons_mode_unused, if not used
		"""


class CONS_SMC1_MODE(String):
	value	= "CONS_MODE_UNUSED"
	undef	= True
	descr	= """
(Bsp--smc1 uart if mode) must be defined if smc1 is used as a tty (uart)
channel. Set it to cons_mode_polled for polled operation, cons_mode_irq for
interrupt driven (spooled) operation. Set it to cons_mode_unused, if not
used])
		"""


class CONS_SMC2_MODE(String):
	value	= "CONS_MODE_UNUSED"
	undef	= True
	descr	= """
(Bsp--smc2 uart if mode) must be defined if smc2 is used as a tty (uart)
channel. Set it to cons_mode_polled for polled operation, cons_mode_irq for
interrupt driven (spooled) operation. Set it to cons_mode_unused, if not used
		"""


class CONSOLE_BAUDRATE(Integer):
	value	= 9600
	undef	= True
	descr	= "The baudrate of the console uart."


class CONSOLE_CHN(String):
	value	= "CONS_CHN_SMC1"
	undef	= True
	descr	= """
Bsp--console driver) must be defined to be one of cons_chn_smc1,
cons_chn_smc2, cons_chn_scc1, cons_chn_scc2, cons_chn_scc3, or cons_chn_scc4.
Determines which device will be registered as /Dev/Console.
		"""


class CONSOLE_MINOR(String):
	value	= "SMC1_MINOR"
	undef	= True
	descr	= """
Port to use for the rtems console: 0 - /Dev/Tty0, serial port 1/Console on the
mvme712m, 1 - /Dev/Tty1, serial port 2/Tty01 on the mvme712m, 2 - /Dev/Tty2,
serial port 3 on the mvme712m, 3 - /Dev/Tty3, serial port 4 on the mvme712m.])
		"""


class CONSOLE_MINOR_DUPLICATE(String):
	value	= "SMC2_MINOR"
	undef	= True
	descr	= """
Bsp--console driver) must be defined to be one of smc1_minor, smc2_minor,
scc2_minor, scc3_minor, or scc4_minor.  Determines which device will be
registered as /Dev/Console.
		"""


class CONSOLE_USE_INTERRUPTS(Boolean):
	value	= True
	undef	= False
	descr	= """
The erc32 console driver can operate in either polled or interrupt mode. Under
the simulator (especially when fast_uart is defined), polled seems to operate
better. It is common for a task to print a line (like the end of test message)
and then exit.  In this case, the program returns control to the simulator
command line before the program has even queued the output to the uart. Thus
sis has no chance of getting the data out.
		"""


class CPU_CLOCK_RATE_HZ(Integer):
	value	= 20000000
	undef	= True
	descr	= "Cpu clock rate in hz"


class DISABLE_MMU(Boolean):
	value	= False
	undef	= True
	descr	= "Disable mmu"


class DISABLE_READ_ONLY_PROTECTION(Boolean):
	value	= False
	undef	= True
	descr	= "Disable mmu protection of read-only sections"


class DISABLE_READ_WRITE_DATA_CACHE(Boolean):
	value	= False
	undef	= True
	descr	= "Disable cache for read-write data sections"


class DISPATCH_HANDLER_STAT(Boolean):
	value	= True
	undef	= True
	descr	= "Used by irq/Irq.C"


class EMC_MICRON(Boolean):
	value	= False
	undef	= True
	descr	= "Enable micron configuration for emc"


class EMC_NUMONYX(Boolean):
	value	= False
	undef	= True
	descr	= "Enable numonyx configuration for emc"


class EMC_TEST(Boolean):
	value	= False
	undef	= True
	descr	= "Enable tests for emc"


class ENABLE(Boolean):
	value	= True
	undef	= True
	descr	= "Whether a bsp is enabled or disabled for use."


class ENABLE_DEBUG(Boolean):
	value	= False
	undef	= True
	descr	= "Enable debug build."


class ENABLE_FPSP(Boolean):
	value	= False
	undef	= True
	descr	= "Motorola floating point support package (fpsp)"


class ENABLE_LCD(Boolean):
	value	= False
	undef	= True
	descr	= "If defined, enable use of the sed1356 controller and LCD."


class ENABLE_MP(Boolean):
	value	= False
	undef	= True
	descr	= "Enable multiprocessing."


class ENABLE_MULTILIB(Boolean):
	value	= True
	undef	= True
	descr	= "???"


class ENABLE_NETWORKING(Boolean):
	value	= True
	undef	= True
	descr	= "Enable tcp/Ip stack."


class ENABLE_NEWLIB(Boolean):
	value	= True
	undef	= True
	descr	= "???"


class ENABLE_POSIX(Boolean):
	value	= True
	undef	= True
	descr	= "Enable posix."


class ENABLE_PTHREADS(Boolean):
	value	= True
	undef	= True
	descr	= "Enable pthreads, requires posix."


class ENABLE_SERDBG(Boolean):
	value	= False
	undef	= True
	descr	= "???"


class ENABLE_SHELL(Boolean):
	value	= True
	undef	= True
	descr	= "???"


class ENABLE_SIS_QUIRKS(Boolean):
	value	= False
	undef	= True
	descr	= """
If defined, then the sis simulator specific code in the bsp will be enabled.
In particular, sis requires special initialization not used on real erc32
		"""


class ENABLE_SMP(Boolean):
	value	= False
	undef	= True
	descr	= "Enable smp, available for i386/Sparc only."


class ENABLE_UMON(Boolean):
	value	= False
	undef	= True
	descr	= "If defined, enable use of the umon console."


class ENABLE_UMON_CONSOLE(Boolean):
	value	= False
	undef	= True
	descr	= "If defined, enable use of the micromonitor console device."


class ENABLE_USART0(Boolean):
	value	= False
	undef	= True
	descr	= "If defined, enable use of the usart 0."


class ENABLE_USART1(Boolean):
	value	= False
	undef	= True
	descr	= "If defined, enable use of the usart 1."


class ENABLE_USART2(Boolean):
	value	= False
	undef	= True
	descr	= "If defined, enable use of the usart 2."


class ENABLE_USART3(Boolean):
	value	= False
	undef	= True
	descr	= "If defined, enable use of the usart 3."


class ENABLE_WATCHDOG_RESET(Boolean):
	value	= False
	undef	= True
	descr	= "Bsp_reset() will use the watchdog to reset the chip"


class EPPCBUG_SMC1(Boolean):
	value	= True
	undef	= True
	descr	= """
If defined, smc1 is in use by eppc-bug. The console driver will not re-
initialize that port.
		"""


class EPPCBUG_VECTORS(Boolean):
	value	= True
	undef	= True
	descr	= """
(Bsp--rtems) if defined, vectors branch to eppcbug, except the following:
0x500 (external interrupt), 0x900 (decrementer).])
		"""


class ETHERNET_RMII(Boolean):
	value	= False
	undef	= True
	descr	= "Enable rmii for ethernet"


class GEN83XX_ENABLE_INTERRUPT_NESTING(Boolean):
	value	= True
	undef	= True
	descr	= "Enable interrupt nesting"


class HAS_DBUG(Integer):
	value	= 0
	undef	= True
	descr	= """
If defined, we will not boot from reset, but from freescale dbug monitor.
		"""


class HAS_LOW_LEVEL_INIT(Boolean):
	value	= False
	undef	= True
	descr	= """
If defined, we will do all the low level init of the chip (like
bus/Memory...).
		"""


class HAS_PMC_PSC8(Boolean):
	value	= False
	undef	= True
	descr	= "Whether has a psc8 pmc board attached to pmc slot"


class HAS_SMC91111(Boolean):
	value	= False
	undef	= True
	descr	= "If defined the board has the smc91111 networking chip."


class HAS_UBOOT(Boolean):
	value	= False
	undef	= True
	descr	= "Enable u-boot startup"


class HAVE_SHSIM_IOMEM_PATCH(Boolean):
	value	= True
	undef	= True
	descr	= """
Whether support for functional iomem in shsim/Gdb shall be enabled
		"""


class HCLK(Boolean):
	value	= False
	undef	= True
	descr	= "Ahb bus clock in hz"


class HEAP_EXTEND(Boolean):
	value	= False
	undef	= True
	descr	= "Enable heap extend by ethernet and usb regions"


class IDE_USE_PRIMARY_INTERFACE(Boolean):
	value	= True
	undef	= True
	descr	= """
Determines, whether rtems will try to use the primary ide interface. Disable
it, if: 1, you have no primary ide interface. 2, you have no disk attached to
this interface or 3, you do not want to access disks attached to this
interface.
		"""


class IDE_USE_SECONDARY_INTERFACE(Boolean):
	value	= False
	undef	= True
	descr	= """
Determines, whether rtems will try to use the secondary ide interface.  Enable
it, if: 1, you have a secondary ide interface  2, you have at least one disk
attached to this interface  3, you do want to access disks attached to this
interface.
		"""


class INITIALIZE_COM_PORTS(Boolean):
	value	= False
	undef	= True
	descr	= "???"


class INTERRUPT_USE_TABLE(Boolean):
	value	= True
	undef	= True
	descr	= "Select if interrupt use table or link list"


class LDFLAGS(StringList):
	value	= []
	undef	= True
	descr	= """
Linker flags only, do not use this for directories or libraries
		"""


class LIBS(StringList):
	value	= []
	undef	= True
	descr	= "Libraries to pass to the linker, e.G. -L<library>"


class LINK_END(StringList):
	value	= []
	undef	= True
	descr	= "Objects linked last"


class LINK_START(StringList):
	value	= []
	undef	= True
	descr	= "Objects linked first"


class LINK_LINK(StringList):
	value	= ["-L${RTEMS} -T ${RTEMS}/linkcmds -dc -dp -N"]
	undef	= True
	descr	= "Linker link flags"


class LINKCMDS(StringList):
	value	= []
	undef	= True
	descr	= "Linker command files, first one is installed as linkcmds"


class LPC24XX_CCLK(String):
	value	= "72000000U"
	undef	= True
	descr	= "Cpu clock in hz"


class LPC24XX_CONFIG_CONSOLE(Integer):
	value	= 0
	undef	= True
	descr	= "Configuration for console (uart 0)"


class LPC24XX_CONFIG_I2C_0(Integer):
	value	= 0
	undef	= True
	descr	= "Configuration for i2c 0"


class LPC24XX_CONFIG_I2C_1(Integer):
	value	= 1
	undef	= True
	descr	= "Configuration for i2c 1"


class LPC24XX_CONFIG_I2C_2(String):
	value	= ""
	undef	= True
	descr	= "Configuration for i2c 2"


class LPC24XX_CONFIG_UART_1(Boolean):
	value	= True
	undef	= True
	descr	= "Configuration for uart 1"


class LPC24XX_CONFIG_UART_2(Boolean):
	value	= False
	undef	= True
	descr	= "Configuration for uart 2"


class LPC24XX_CONFIG_UART_3(Boolean):
	value	= False
	undef	= True
	descr	= "Configuration for uart 3"


class LPC24XX_EMC_MICRON(Integer):
	value	= 1
	undef	= True
	descr	= "Enable micron configuration for emc"


class LPC24XX_EMC_NUMONYX(Integer):
	value	= 1
	undef	= True
	descr	= "Enable numonyx configuration for emc"


class LPC24XX_EMC_TEST(String):
	value	= ""
	undef	= True
	descr	= "Enable tests for emc"


class LPC24XX_ETHERNET_RMII(Boolean):
	value	= True
	undef	= True
	descr	= "Enable rmii for ethernet"


class LPC24XX_HEAP_EXTEND(Boolean):
	value	= True
	undef	= True
	descr	= "Enable heap extend by ethernet and usb regions"


class LPC24XX_OSCILLATOR_MAIN(String):
	value	= "12000000U"
	undef	= True
	descr	= "Main oscillator frequency in hz"


class LPC24XX_OSCILLATOR_RTC(String):
	value	= "32768U"
	undef	= True
	descr	= "Rtc oscillator frequency in hz"


class LPC24XX_SPECIAL_TASK_STACKS_SUPPORT(Integer):
	value	= 1
	undef	= True
	descr	= """
Enable special task stack support for task stacks in internal ram
		"""


class LPC24XX_STOP_ETHERNET(Integer):
	value	= 1
	undef	= True
	descr	= "Stop ethernet controller at start-up to avoid dma interference"


class LPC24XX_STOP_GPDMA(Integer):
	value	= 1
	undef	= True
	descr	= "Stop general purpose dma at start-up to avoid dma interference"


class LPC24XX_STOP_USB(Integer):
	value	= 1
	undef	= True
	descr	= "Stop usb controller at start-up to avoid dma interference"


class LPC24XX_UART_BAUD(String):
	value	= "115200U"
	undef	= True
	descr	= "Baud for uarts"


class LPC32XX_ARM_CLK(String):
	value	= "208000000U"
	undef	= True
	descr	= "Arm clock in hz"


class LPC32XX_CONFIG_U3CLK(String):
	value	= ""
	undef	= True
	descr	= "Clock configuration for uart 3"


class LPC32XX_CONFIG_U4CLK(String):
	value	= ""
	undef	= True
	descr	= "Clock configuration for uart 4"


class LPC32XX_CONFIG_U5CLK(String):
	value	= "0x00001386U"
	undef	= True
	descr	= "Clock configuration for uart 5"


class LPC32XX_CONFIG_U6CLK(String):
	value	= ""
	undef	= True
	descr	= "Clock configuration for uart 6"


class LPC32XX_CONFIG_UART_CLKMODE(String):
	value	= "0x00000200U"
	undef	= True
	descr	= "Clock mode configuration for uarts"


class LPC32XX_DISABLE_MMU(Boolean):
	value	= False
	undef	= True
	descr	= "Disable mmu"


class LPC32XX_DISABLE_READ_ONLY_PROTECTION(Boolean):
	value	= False
	undef	= True
	descr	= "Disable mmu protection of read-only sections"


class LPC32XX_DISABLE_READ_WRITE_DATA_CACHE(Boolean):
	value	= False
	undef	= True
	descr	= "Disable cache for read-write data sections"


class LPC32XX_ENABLE_WATCHDOG_RESET(Boolean):
	value	= True
	undef	= True
	descr	= "Enable watchdog reset"


class LPC32XX_ETHERNET_RMII(Boolean):
	value	= True
	undef	= True
	descr	= "Enable rmii for ethernet"


class LPC32XX_HCLK(String):
	value	= "104000000U"
	undef	= True
	descr	= "Ahb bus clock in hz"


class LPC32XX_OSCILLATOR_MAIN(String):
	value	= "13000000U"
	undef	= True
	descr	= "Main oscillator frequency in hz"


class LPC32XX_OSCILLATOR_RTC(String):
	value	= "32768U"
	undef	= True
	descr	= "Rtc oscillator frequency in hz"


class LPC32XX_PERIPH_CLK(String):
	value	= "13000000U"
	undef	= True
	descr	= "Peripheral clock in hz"


class LPC32XX_SCRATCH_AREA_SIZE(Integer):
	value	= 4096
	undef	= True
	descr	= "Size of scratch area"


class LPC32XX_STOP_ETHERNET(Boolean):
	value	= True
	undef	= True
	descr	= "Stop ethernet controller at start-up to avoid dma interference"


class LPC32XX_STOP_GPDMA(Boolean):
	value	= True
	undef	= True
	descr	= "Stop general purpose dma at start-up to avoid dma interference"


class LPC32XX_STOP_USB(Boolean):
	value	= True
	undef	= True
	descr	= "Stop usb controller at start-up to avoid dma interference"


class LPC32XX_UART_1_BAUD(String):
	value	= ""
	undef	= True
	descr	= "Baud for uart 1"


class LPC32XX_UART_2_BAUD(String):
	value	= ""
	undef	= True
	descr	= "Baud for uart 2"


class LPC32XX_UART_7_BAUD(String):
	value	= ""
	undef	= True
	descr	= "Baud for uart 7"


class MPC5200_PSC_INDEX_FOR_GPS_MODULE(Integer):
	value	= 0
	undef	= True
	descr	= "Psc index for gps module, if defined results in '/Dev/Gps'"


class MPC55XX_BOARD_GWLCFM(Boolean):
	value	= True
	undef	= True
	descr	= "If defined, use custom settings for gwlcfm board"


class MPC55XX_BOARD_MPC5566EVB(Boolean):
	value	= False
	undef	= True
	descr	= "If defined, use custom settings for mpc5566evb board"


class MPC55XX_BOARD_MPC5674FEVB(Boolean):
	value	= True
	undef	= True
	descr	= "If defined, use custom settings for mpc5674fevb board"


class MPC55XX_BOARD_PHYCORE_MPC5554(Boolean):
	value	= True
	undef	= True
	descr	= "If defined, use custom settings for phycore mpc5554 board"


class MPC55XX_BOOTFLAGS(String):
	value	= ""
	undef	= True
	descr	= """
If defined, builds in bootflags above the rchw for setup in a debugger to
avoid startup mmu setup
		"""


class MPC55XX_CHIP_TYPE(Integer):
	value	= 5554
	undef	= True
	descr	= "Specifies the chip type in use (e.G. 5554 for mpc5554"


class MPC55XX_CLOCK_EMIOS_CHANNEL(String):
	value	= "MPC55XX_EMIOS_CHANNEL_NUMBER-1"
	undef	= True
	descr	= """
Define to the emios channel to use for the bsp clock.  The default is the last
channel.
		"""


class MPC55XX_EMIOS_PRESCALER(Integer):
	value	= 1
	undef	= True
	descr	= "Must be defined to set the emios prescaler"


class MPC55XX_ESCI_CONSOLE_MINOR(Integer):
	value	= 0
	undef	= True
	descr	= """
Determines which esci device will be registered as /Dev/Console
		"""


class MPC55XX_ESCI_USE_INTERRUPTS(Boolean):
	value	= True
	undef	= True
	descr	= """
Define to zero or one to disable or enable interrupts for the esci devices
		"""


class MPC55XX_FMPLL_CLK_OUT(Integer):
	value	= 128000000
	undef	= True
	descr	= """
Must be defined to be the pll output clock (in hz) for clock generation
		"""


class MPC55XX_FMPLL_MFD(Integer):
	value	= 12
	undef	= True
	descr	= """
Must be defined to be the pll multiplication factor for clock generation
		"""


class MPC55XX_FMPLL_PREDIV(Integer):
	value	= 1
	undef	= True
	descr	= """
Must be defined to be the pll predivider factor for clock generation
		"""


class MPC55XX_FMPLL_REF_CLOCK(Integer):
	value	= 8000000
	undef	= True
	descr	= """
Must be defined to be the external reference clock (in hz) for clock
generation
		"""


class NVRAM_CONFIGURE(Boolean):
	value	= True
	undef	= True
	descr	= """
Define to 1 if you want the console driver, network driver and caches
configured at boot time from parameters stored in nvram. If set to 1, most
parameters below are ignored during the build. If not set to 1, then the
console driver is configured at build time, the network host information is
obtained from application supplied data structures, and the caches are
configured at boot time based on the information supplied in this file.
		"""


class ON_SIMULATOR(Boolean):
	value	= False
	undef	= True
	descr	= """
If defined, this indicates the bsp is being built to run on the lm32 simulator
in gdb.  This enables fast idle support which speeds up the clock ticks while
the idle task is running so time spent in the idle task is minimized.  This
significantly reduces the wall time required to execute the rtems test suites.
It also enables a special exit and alternate printk support.
		"""


class ON_SKYEYE(Boolean):
	value	= False
	undef	= True
	descr	= """
If defined, enable options which optimize executingon the skyeye simulator.
Speed up the clock ticks while the idle task is running so time spent in the
idle task is minimized. This significantly reduces the wall time required to
execute the rtems test suites.
		"""


class OSCILLATOR_MAIN(Boolean):
	value	= False
	undef	= True
	descr	= "Main oscillator frequency in hz"


class OSCILLATOR_RTC(Boolean):
	value	= False
	undef	= True
	descr	= "Rtc oscillator frequency in hz"


class PATH_TOOLS(String):
	value	= ""
	undef	= True
	descr	= "Location of rtems tools."


class PERIPH_CLK(Boolean):
	value	= False
	undef	= True
	descr	= "Peripheral clock in hz"


class PPC_USE_SPRG(Boolean):
	value	= True
	undef	= True
	descr	= """
If defined, then the powerpc specific code in rtems will use some of the
special purpose registers to slightly optimize interrupt response time.  The
use of these registers can conflict with other tools like debuggers.
		"""


class PPC_VECTOR_FILE_BASE(String):
	value	= "0x0100"
	undef	= True
	descr	= """
This defines the base address of the exception table.  Note: vectors are
actually at 0xfff00000 but file starts at offset.
		"""


class PREFIX(String):
	value	= ""
	undef	= True
	descr	= "Install prefix."


class PRINTK_CHN(String):
	value	= "NOT_DEFINED_IN_BSP"
	undef	= True
	descr	= """
(Bsp--console driver) must be defined to be one of cons_chn_smc1,
cons_chn_smc2, cons_chn_scc2,  cons_chn_scc3, or cons_chn_scc4. Determines
which device is used for output y printk(). If the port that printk() uses is
also used for other I/O (e.G. If  printk_chn == console_chn), then both ports
should use the same type of I/O, otherwise the drivers will likely conflict
with each other.
		"""


class PRINTK_IO_MODE(Integer):
	value	= 0
	undef	= True
	descr	= """
(Bsp--console driver)  define to 0 or 1 if you want polled I/O performed by
rtems.  Define to 2 if you want polled I/O performed by eppcbug.  The printk()
port is not configured to use termios. With eppcbug 1.1,  if mode 2 is
selected, printk_minor must be set to smc1_minor.  This is a deficiency of the
firmware: it does not perform serial I/O  on any port other than its default
debug port, which must be smc1.  Printk always uses polled output.
		"""


class PRINTK_MINOR(String):
	value	= "NOT_DEFINED_IN_BSP"
	undef	= True
	descr	= """
Port to use for the rtems console: 0 - /Dev/Tty0, serial port 1/Console on the
mvme712m, 1 - /Dev/Tty1, serial port 2/Tty01 on the mvme712m, 2 - /Dev/Tty2,
serial port 3 on the mvme712m, 3 - /Dev/Tty3, serial port 4 on the mvme712m.])
		"""


class PRINTK_MINOR_DUPLICATE(String):
	value	= "SMC2_MINOR"
	undef	= True
	descr	= """
(Bsp--console driver)  must be defined to be one of smc1_minor, smc2_minor,
scc2_minor, scc3_minor, or scc4_minor. Determines which device is used for
output by printk(). If the port that printk() uses is also used for other I/O
(e.G. If  printk_minor == \$console_minor), then both ports should use the
same type of I/O, otherwise the drivers will likely conflict with each other.
		"""


class QORIQ_CLOCK_TIMER(Integer):
	value	= 0
	undef	= True
	descr	= """
Global timer used for system clock, 0..3 maps to a0..a3, and 4..7 maps to
b0..b3
		"""


class QORIQ_ETSEC_1_PHY_ADDR(Integer):
	value	= -1
	undef	= True
	descr	= "Phy address for etsec interface 1"


class QORIQ_ETSEC_2_PHY_ADDR(Integer):
	value	= 0
	undef	= True
	descr	= "Phy address for etsec interface 2"


class QORIQ_ETSEC_3_PHY_ADDR(Integer):
	value	= 1
	undef	= True
	descr	= "Phy address for etsec interface 3"


class QORIQ_INITIAL_MSR(String):
	value	= "0x02000200"
	undef	= True
	descr	= "Initial msr value"


class QORIQ_INITIAL_SPEFSCR(String):
	value	= "0x00000000"
	undef	= True
	descr	= "Initial spefscr value"


class QORIQ_INTERCOM_AREA_BEGIN(String):
	value	= "0x3000000"
	undef	= True
	descr	= "Inter-processor communication area begin"


class QORIQ_INTERCOM_AREA_SIZE(String):
	value	= "0x1000000"
	undef	= True
	descr	= "Inter-processor communication area size"


class QORIQ_UART_0_ENABLE(Boolean):
	value	= True
	undef	= True
	descr	= "Use 1 to enable uart 0, otherwise use 0"


class QORIQ_UART_1_ENABLE(Boolean):
	value	= True
	undef	= True
	descr	= "Use 1 to enable uart 1, otherwise use 0"


class QORIQ_UART_BRIDGE_0_ENABLE(Boolean):
	value	= True
	undef	= True
	descr	= "Use 1 to enable uart 0 to intercom bridge, otherwise use 0"


class QORIQ_UART_BRIDGE_1_ENABLE(Boolean):
	value	= True
	undef	= True
	descr	= "Use 1 to enable uart 1 to intercom bridge, otherwise use 0"


class QORIQ_UART_BRIDGE_MASTER_CORE(Integer):
	value	= 0
	undef	= True
	descr	= "Uart to intercom bridge master core index"


class QORIQ_UART_BRIDGE_SLAVE_CORE(Integer):
	value	= 1
	undef	= True
	descr	= "Uart to intercom bridge slave core index"


class QORIQ_UART_BRIDGE_TASK_PRIORITY(Integer):
	value	= 250
	undef	= True
	descr	= "Uart to intercom bridge task priority"


class RTEMS_BSP_I2C_EEPROM_DEVICE_NAME(String):
	value	= "eeprom"
	undef	= True
	descr	= "Eeprom name for libi2c"


class RTEMS_BSP_I2C_EEPROM_DEVICE_PATH(String):
	value	= "/dev/i2c1.eeprom"
	undef	= True
	descr	= "Eeprom device file path"


class RTEMS_XPARAMETERS_H(String):
	value	= "<xparameters_dflt.h>"
	undef	= True
	descr	= """
This defines the location of the hardware specific xparameters.H
		"""


class RTEMS_XPPC_BASE(String):
	value	= "."
	undef	= True
	descr	= "Defines path to xilinx xps ppc libraries."


class SCORE603E_OPEN_FIRMWARE(Boolean):
	value	= False
	undef	= True
	descr	= "Use open firmware rom monitor"


class SCORE603E_USE_DINK(Boolean):
	value	= False
	undef	= True
	descr	= "???"


class SCORE603E_USE_NONE(Boolean):
	value	= False
	undef	= True
	descr	= "Use no rom monitor"


class SCORE603E_USE_SDS(Boolean):
	value	= False
	undef	= True
	descr	= "Use sds rom monitor"


class SCRATCH_AREA_SIZE(Boolean):
	value	= False
	undef	= True
	descr	= "Size of scratch area"


class SIMSPARC_FAST_IDLE(Boolean):
	value	= False
	undef	= True
	descr	= """
If defined, speed up the clock ticks while the idle task is running so time
spent in the idle task is minimized. This significantly reduces the wall time
required to execute the rtems test suites.
		"""


class SINGLE_CHAR_MODE(String):
	value	= ""
	undef	= True
	descr	= "Enable single character mode for the psc console driver"


class SMC91111_ENADDR_IS_SETUP(Boolean):
	value	= False
	undef	= True
	descr	= """
If defined the smc91111 chip has the ethernet address loaded at reset.
		"""


class SPECIAL_TASK_STACKS_SUPPORT(Boolean):
	value	= False
	undef	= True
	descr	= """
Enable special task stack support for task stacks in internal ram.
		"""


class SPI_BOARD_INIT_FNC(String):
	value	= "bsp_dummy_spi_init"
	undef	= True
	descr	= """
(Bsp--spi board init function) specify the function that inits the board port
lines and further devices.
		"""


class SPI_SEND_ADDR_FNC(String):
	value	= "bsp_dummy_spi_sel_addr"
	undef	= True
	descr	= """
Bsp--spi send address function) specify the function that addresses spi
devices. Set to bsp_dummy_spi_sel_addr for dummy implementation
		"""


class SPI_SEND_STOP_FNC(String):
	value	= "bsp_dummy_spi_send_stop"
	undef	= True
	descr	= """
Bsp--spi send stop function) specify the function that deaddresses spi
devices. Set to bsp_dummy_spi_send_stop for dummy implementation
		"""


class STANDALONE_EVB(String):
	value	= ""
	undef	= True
	descr	= """
If defined, compiles code to jump-start from flash, without a monitor
		"""


class START_HW_INIT(String):
	value	= ""
	undef	= True
	descr	= """
If defined, selects whether 'early_hw_init()' is called from 'start.S';
'bsp_hw_init()' is always called from 'bspstart.C'
		"""


class STOP_ETHERNET(Boolean):
	value	= False
	undef	= True
	descr	= "Stop ethernet controller at start-up to avoid dma interference"


class STOP_GPDMA(Boolean):
	value	= False
	undef	= True
	descr	= "Stop general purpose dma at start-up to avoid dma interference"


class STOP_USB(Boolean):
	value	= False
	undef	= True
	descr	= "Stop usb controller at start-up to avoid dma interference"


class TESTS_USE_PRINTK(Boolean):
	value	= False
	undef	= True
	descr	= "Tests use printk() for output"


class UART_1_BAUD(Boolean):
	value	= False
	undef	= True
	descr	= "Baud for uart 1"


class UART_2_BAUD(Boolean):
	value	= False
	undef	= True
	descr	= "Baud for uart 2"


class UART_7_BAUD(Boolean):
	value	= False
	undef	= True
	descr	= "Baud for uart 7"


class UART_BAUD(Boolean):
	value	= False
	undef	= True
	descr	= "Baud for uarts"


class UART_USE_DMA(Boolean):
	value	= True
	undef	= True
	descr	= """
The uart driver can operate in dma mode with interrupts. Set true if dma
operation is required
		"""


class UARTS_IO_MODE(Integer):
	value	= 0
	undef	= True
	descr	= """
Define to 0 or 1 if you want polled I/O performed by rtems.  Define to 1 if
you want interrupt-driven performed by rtems.  Define to 2 if you want polled
I/O performed by eppcbug.  There is no provision to have a MIX of interrupt-
driven and polled I/O ports, except that the printk port may use a different
mode from the other ports. If this is done, do not open the printk port from
an rtems application. With eppcbug 1.1, if mode 2 is selected, console_minor
must be set to smc1_minor. This is a deficiency of the firmware: it does not
perform serial I/O on any port other than its default debug port, which must
be smc1.
		"""


class UARTS_USE_TERMIOS(Boolean):
	value	= False
	undef	= True
	descr	= """
Define to 1 if you want termios support for every port.  Termios support is
independent of the choice of uart I/O mode.
		"""


class UARTS_USE_TERMIOS_INT(Boolean):
	value	= True
	undef	= True
	descr	= "Enable interrupt support for the psc console driver"


class USE_COM1_AS_CONSOLE(Boolean):
	value	= False
	undef	= True
	descr	= """
Determines, whether the console will be associated with the standard vga
display or with the com1 serial port.  Currently only the vga display and com1
support printk.
		"""


class WATCHDOG_TIMEOUT(String):
	value	= "0xFFFF"
	undef	= True
	descr	= """
Define to the desired timeout (in steps of 1/20 msec) to enable the watchdog.
Default is to disable the watchdog entirely.
		"""


# These are all hacks, they only exist to enable shared BSPS, they are not
# required and will be removed in the future.

class BOARD_PHYCORE_MPC5554(Boolean):
	value	= False
	undef	= True
	descr	= """
If defined, use custom settings for the phytec phycore mpc5554 som
		"""


class BSP_TYPE_DP2(Boolean):
	value	= False
	undef	= True
	descr	= "Enable settings for dp2"


class csb637(Boolean):
	value	= False
	undef	= True
	descr	= """
If defined, this indicates that the bsp is being built for the  csb637
variant.
		"""


class GEN68360(Boolean):
	value	= False
	undef	= True
	descr	= "If defined, use custom settings for the gen68360 bsp."


class GEN68360_040(Boolean):
	value	= False
	undef	= True
	descr	= "If defined, use custom settings for the gen68360_040 bsp."


class HSC_CM01(Boolean):
	value	= False
	undef	= True
	descr	= "If defined, use custom settings for the hsc_cm01 bsp."


class M5484FIREENGINE(Boolean):
	value	= False
	undef	= True
	descr	= "If defined, use custom settings for the m5484fireengine bsp."


class mpc8240(Boolean):
	value	= False
	undef	= True
	descr	= "Defined for boards with mpc8240 -- undefined for others"


class MPC8313ERDB(Boolean):
	value	= False
	undef	= True
	descr	= "If defined, use custom settings for the mpc8313erdb bsp."


class MPC8349(Boolean):
	value	= False
	undef	= True
	descr	= "If defined, use custom settings for the mpc8349 libcpu family."


class MPC8349EAMDS(Boolean):
	value	= False
	undef	= True
	descr	= "If defined, use custom settings for the mpc8349eamds bsp."


class mvme167(Boolean):
	value	= False
	undef	= True
	descr	= "Defined for mvme167 -- undefined for others"


class mvme2100(Boolean):
	value	= False
	undef	= True
	descr	= "Defined for mvme2100 -- undefined for others"


class PGH360(Boolean):
	value	= False
	undef	= True
	descr	= "If defined, use custom settings for the pgh360 bsp."


class qemu(Boolean):
	value	= False
	undef	= True
	descr	= "Defined for qemu bsp -- undefined for others"


class MPC5200_BOARD_BRS5L(Boolean):
	value	= False
	undef	= True
	descr	= "Enable settings for powerpc MPC5200 BRS5L"

class MPC5200_BOARD_BRS6L(Boolean):
	value	= False
	undef	= True
	descr	= "Enable settings for powerpc MPC5200 BRS6l"

class MPC5200_BOARD_DP2(Boolean):
	value	= False
	undef	= True
	descr	= "Enable settings for powerpc MPC5200 dp2"

class MPC5200_BOARD_ICECUBE(Boolean):
	value	= False
	undef	= True
	descr	= "Enable settings for powerpc MPC5200 icecube"

class MPC5200_BOARD_PM520_CR825(Boolean):
	value	= False
	undef	= True
	descr	= "Enable settings for powerpc MPC5200 PM520_CR825"

class MPC5200_BOARD_PM520_ZE30(Boolean):
	value	= False
	undef	= True
	descr	= "Enable settings for powerpc MPC5200 pm520"


# RTEMS internal options.
class USE_CLANG(Boolean):
	value	= False
	undef	= True
	descr	= "Use Clang compiler."

class USE_GCC(Boolean):
	value	= True
	undef	= True
	descr	= "Use GCC compiler.."




# THESE ARE UNSORTED!


class LPC24XX_PCLKDIV(String):
	value = "1U"
	undef = True
	descr = "clock divider for default PCLK (PCLK = CCLK / PCLKDIV)"


class LPC24XX_EMCCLKDIV(String):
	value = "2U"
	undef = True
	descr = "clock divider for EMCCLK (EMCCLK = CCLK / EMCCLKDIV)"


class LPC24XX_EMC_MT48LC4M16A2(Boolean):
	value = False
	undef = True
	descr = "enable Micron MT48LC4M16A2 configuration for EMC"


class LPC24XX_EMC_W9825G2JB75I(Boolean):
	value = True
	undef = True
	descr = "enable Winbond W9825G2JB75I configuration for EMC"


class LPC24XX_EMC_IS42S32800D7(Boolean):
	value = True
	undef = True
	descr = "enable ISSI IS42S32800D7 configuration for EMC"


class LPC24XX_EMC_IS42S32800B(Boolean):
	value = True
	undef = True
	descr = "enable ISSI IS42S32800B configuration for EMC"


class LPC24XX_EMC_M29W160E(Boolean):
	value = True
	undef = True
	descr = "enable M29W160E configuration for EMC"


class LPC24XX_EMC_M29W320E70(Boolean):
	value = False
	undef = True
	descr = "enable M29W320E70 configuration for EMC"


class LPC24XX_EMC_SST39VF3201(Boolean):
	value = True
	undef = True
	descr = "enable SST39VF3201 configuration for EMC"


class LPC_DMA_CHANNEL_COUNT(Integer):
	value = 2
	undef = True
	descr = "DMA channel count"


class BSP_USB_OTG_TRANSCEIVER_I2C_ADDR(String):
	value = ""
	undef = True
	descr = "USB OTG transceiver I2C address used by USB stack"


class MPC55XX_CHIP_FAMILY(String):
	value = "(MPC55XX_CHIP_TYPE / 10)"
	undef = True
	descr = "specifies the chip family in use (e.g. 555 for MPC5554)"


class SMSC9218I_EDMA_RX_CHANNEL(Integer):
	value = 49
	undef = True
	descr = "receive eDMA channel for SMSC9218I network interface"

class SMSC9218I_EDMA_TX_CHANNEL(Integer):
	value = 48
	undef = True
	descr = "transmit eDMA channel for SMSC9218I network interface"


class SMSC9218I_BIG_ENDIAN_SUPPORT(Boolean):
	value = True
	undef = True
	descr = "enable big endian support for SMSC9218I network interface"


class SMSC9218I_ENABLE_LED_OUTPUTS(Boolean):
	value = True
	undef = True
	descr = "enable LED outputs for SMSC9218I network interface"


class SMSC9218I_RESET_PIN(Integer):
	value = 186
	undef = True
	descr = "reset pin for SMSC9218I network interface"


class SMSC9218I_IRQ_PIN(Integer):
	value = 193
	undef = True
	descr = "IRQ pin for SMSC9218I network interface"


class MPC55XX_SYSTEM_CLOCK_DIVIDER(Integer):
	value = 1
	undef = True
	descr = "system clock divider"


class MPC55XX_REFERENCE_CLOCK(Integer):
	value = 8000000
	undef = True
	descr = "Must be defined to be the external reference clock (in Hz) for clock generation"


class MPC55XX_SYSTEM_CLOCK(Integer):
	value = 8000000
	undef = True
	descr = "The system clock frequency in Hz."


class MPC55XX_FMPLL_ESYNCR1_CLKCFG(Integer):
	value = 7
	undef = True
	descr = "the FMPLL ESYNCR1[CLKCFG] value"

class MPC83XX_BOARD_HSC_CM01(Boolean):
	value = True
	undef = True
	descr = "if defined, then use settings for the HSC_CM01 board"






class LM3S69XX_ENABLE_UART_0(Boolean):
	value = True
	undef = True
	descr = "enable UART 0"


class LM3S69XX_ENABLE_UART_1(Boolean):
	value = True
	undef = True
	descr = "enable UART 1"


class LM3S69XX_ENABLE_UART_2(Boolean):
	value = True
	undef = True
	descr = "enable UART 2"


class LM3S69XX_HAS_UDMA(Boolean):
	value = False
	undef = True
	descr = "defined if MCU supports UDMA"


class LM3S69XX_MCU_LM3S3749(Boolean):
	value = False
	undef = True
	descr = "board has LM3S3749 MCU"


class LM3S69XX_MCU_LM3S6965(Boolean):
	value = False
	undef = True
	descr = "board has LM3S6965 MCU"


class LM3S69XX_NUM_GPIO_BLOCKS(Integer):
	value = 1
	undef = True
	descr = "number of GPIO blocks supported by MCU"


class LM3S69XX_NUM_SSI_BLOCKS(Integer):
	value = 1
	undef = True
	descr = "number of SSI blocks supported by MCU"


class LM3S69XX_SSI_CLOCK(String):
	value = "1000000U"
	undef = True
	descr = "SSI clock in Hz"


class LM3S69XX_SYSTEM_CLOCK(String):
	value = "50000000U"
	undef = True
	descr = "system clock in Hz"


class LM3S69XX_UART_BAUD(String):
	value = "115200U"
	undef = True
	descr = "baud for UARTs"


class LM3S69XX_USE_AHB_FOR_GPIO(Boolean):
	value = False
	undef = True
	descr = "use AHB apperture to access GPIO registers"


class LM3S69XX_XTAL_CONFIG(String):
	value = "0x10"
	undef = True
	descr = "crystal configuration for RCC register"


class BSP_ARM_A9MPCORE_PERIPHCLK(String):
	value = "100000000U"
	undef = True
	descr = "ARM Cortex-A9 MPCore PERIPHCLK clock frequency in Hz"



class STM32F4_HSE_OSCILLATOR(Integer):
	value = 8000000
	undef = True
	descr = "HSE oscillator frequency in Hz"



class STM32F4_SYSCLK(Integer):
	value = 16000000
	undef = True
	descr = "SYSCLK frequency in Hz"



class STM32F4_HCLK(Integer):
	value = 16000000
	undef = True
	descr = "HCLK frequency in Hz"



class STM32F4_PCLK1(Integer):
	value = 16000000
	undef = True
	descr = "PCLK1 frequency in Hz"



class STM32F4_PCLK2(Integer):
	value = 16000000
	undef = True
	descr = "PCLK2 frequency in Hz"



class STM32F4_USART_BAUD(Integer):
	value = 115200
	undef = True
	descr = "baud for USARTs"



class STM32F4_ENABLE_USART_1(Boolean):
	value = False
	undef = True
	descr = "enable USART 1"


class STM32F4_ENABLE_USART_2(Boolean):
	value = False
	undef = True
	descr = "enable USART 2"


class STM32F4_ENABLE_USART_3(Boolean):
	value = True
	undef = True
	descr = "enable USART 3"


class STM32F4_ENABLE_UART_4(Boolean):
	value = False
	undef = True
	descr = "enable UART 4"


class STM32F4_ENABLE_UART_5(Boolean):
	value = False
	undef = True
	descr = "enable UART 5"


class STM32F4_ENABLE_USART_6(Boolean):
	value = False
	undef = True
	descr = "enable USART 6"


class MPC83XX_BOARD_BR_UID(Boolean):
	value = True
	undef = True
	descr = "if defined, then use settings for the BR UID board"


class MPC83XX_NETWORK_INTERFACE_0_PHY_ADDR(String):
	value = "0x11"
	undef = True
	quote = False
	descr = "PHY address of network interface 0"


class MPC83XX_CHIP_TYPE(Integer):
	value = 0
	undef = True
	descr = "chip type of the MPC83XX family"


class MPC83XX_HAS_NAND_LP_FLASH_ON_CS0(Boolean):
	value = True
	undef = True
	descr = "indicates if the board has a NAND large page flash on chip select 0"


class BSP_INTERRUPT_HANDLER_TABLE_SIZE(Integer):
	no_default = True
	undef = True
	descr = "defines the maximum number of interrupt handlers"


class MPC55XX_NULL_POINTER_PROTECTION(Boolean):
	value = True
	undef = True
	descr = "enable NULL pointer protection"


class MPC55XX_CLOCK_PIT_CHANNEL(Integer):
	no_default = True
	undef = True
	descr = "selects the PIT channel for the RTEMS system tick (the default is the last channel"


class MPC55XX_NEEDS_LOW_LEVEL_INIT(Boolean):
	value = True
	undef = True
	descr = "if defined, do low level initialization"


class BSP_DATA_CACHE_USE_WRITE_THROUGH(Boolean):
	no_default = True
	undef = True
	descr = "use write-through for data cache"


class MPC55XX_BOARD_MPC5674F_ECU508(Boolean):
	value = True
	undef = True
	descr = "if defined, use custom settings for ECU508 board"


class MPC55XX_CONSOLE_MINOR(Integer):
	value = 0
	undef = True
	descr = "determines which serial device will be registered as /dev/console"


class MPC55XX_BOARD_MPC5674F_RSM6(Boolean):
	value = True
	quote = False
	undef = True
	descr = "if defined, use custom settings for RSM6 board"


class MPC55XX_ENABLE_START_PROLOGUE(Boolean):
	value = True
	undef = True
	descr = "if defined, enable start prologue"


class BSP_DEFAULT_BAUD_RATE(Integer):
	value = 115200
	undef = True
	descr = "default console baud"


class MPC55XX_EARLY_STACK_SIZE(Integer):
	value = 1024
	undef = True
	descr = "size of the early initialization stack in bytes"

class MPC83XX_BOARD_MPC8309SOM(Boolean):
	value = True
	undef = True
	descr = "if defined, then use settings for the MPC8309SOM board"


class ZYNQ_RAM_ORIGIN(String):
	value = "0x00400000"
	undef = True
	descr = "Normal RAM region origin"

class ZYNQ_RAM_MMU(String):
	value = "%(ZYNQ_RAM_ORIGIN)s"
	quote = False
	undef = True
	descr = "MMU region origin"

class ZYNQ_RAM_MMU_LENGTH(String):
	value = "16k"
	undef = True
	descr = "MMU region length"

class ZYNQ_RAM_ORIGIN_AVAILABLE(String):
	value = "%(ZYNQ_RAM_ORIGIN)s + 0x00004000"
	undef = True
	descr = "Origin of available RAM"

class ZYNQ_RAM_LENGTH_AVAILABLE(String):
	value = "%(BSP_ZYNQ_RAM_LENGTH)s - 1M - 16k"
	undef = True
	descr = "Length of available RAM"

class ZYNQ_RAM_INT_0_ORIGIN(String):
	value = "0x00000000"
	undef = True
	descr = "Internal 0 RAM region origin"

class ZYNQ_RAM_INT_0_LENGTH(String):
	value = "64k + 64k + 64k"
	undef = True
	descr = "Internal 0 RAM region length"

class ZYNQ_RAM_INT_1_ORIGIN(String):
	value = "0xFFFF0000"
	undef = True
	descr = "Internal 1 RAM region origin"

class ZYNQ_RAM_INT_1_LENGTH(String):
	value = "64k - 512"
	undef = True
	descr = "Internal 1 RAM region length"

class BSP_ZYNQ_RAM_LENGTH(String):
	value = "256M"
	quote = False
	undef = True
	descr = "Override a BSP's default RAM length"

class ZYNQ_RAM_NOCACHE_LENGTH(String):
	value = "1M"
	quote = False
	undef = True
	descr = "Length of nocache RAM region"

class ZYNQ_CLOCK_CPU_1X(String):
	value = "111111111U"
	quote = False
	undef = True
	descr = "Zynq cpu_1x clock frequency in Hz"

class ZYNQ_CLOCK_UART(String):
	value = "50000000UL"
	quote = False
	undef = True
	descr = "Zynq UART clock frequency in Hz"


class ZYNQ_CPUS(Integer):
	value = 1
	quote = False
	undef = True
	descr = "Number of active cores"


class IS_DM3730(Boolean):
	value = False
	undef = True
	descr = "true if SOC is DM3730"


class IS_AM335X(Boolean):
	value = False
	undef = True
	descr = "true if SOC is AM335X"


class CONSOLE_POLLED(Boolean):
	value = False
	undef = True
	descr = "Polled console i/o."


class CONSOLE_BAUD(Integer):
	value = 115200
	undef = True
	descr = "initial baud for console UART"

