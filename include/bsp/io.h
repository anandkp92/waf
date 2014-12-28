#if defined(HEADER_WARNING)
#warning "This header should not be included directly."
#endif


#if defined(__rtems_arm_lm3s3749__)
#  include <arm/lm3s3749/bsp/io.h>
#elif defined(__rtems_arm_lm3s6965__)
#  include <arm/lm3s6965/bsp/io.h>
#elif defined(__rtems_arm_lm3s6965_qemu__)
#  include <arm/lm3s6965_qemu/bsp/io.h>
#elif defined(__rtems_arm_lm4f120__)
#  include <arm/lm4f120/bsp/io.h>
#elif defined(__rtems_arm_lpc1768_mbed__)
#  include <arm/lpc1768_mbed/bsp/io.h>
#elif defined(__rtems_arm_lpc1768_mbed_ahb_ram__)
#  include <arm/lpc1768_mbed_ahb_ram/bsp/io.h>
#elif defined(__rtems_arm_lpc1768_mbed_ahb_ram_eth__)
#  include <arm/lpc1768_mbed_ahb_ram_eth/bsp/io.h>
#elif defined(__rtems_arm_lpc17xx_ea_ram__)
#  include <arm/lpc17xx_ea_ram/bsp/io.h>
#elif defined(__rtems_arm_lpc17xx_ea_rom_int__)
#  include <arm/lpc17xx_ea_rom_int/bsp/io.h>
#elif defined(__rtems_arm_lpc17xx_plx800_ram__)
#  include <arm/lpc17xx_plx800_ram/bsp/io.h>
#elif defined(__rtems_arm_lpc17xx_plx800_rom_int__)
#  include <arm/lpc17xx_plx800_rom_int/bsp/io.h>
#elif defined(__rtems_arm_lpc2362__)
#  include <arm/lpc2362/bsp/io.h>
#elif defined(__rtems_arm_lpc23xx_tli800__)
#  include <arm/lpc23xx_tli800/bsp/io.h>
#elif defined(__rtems_arm_lpc24xx_ea__)
#  include <arm/lpc24xx_ea/bsp/io.h>
#elif defined(__rtems_arm_lpc24xx_ncs_ram__)
#  include <arm/lpc24xx_ncs_ram/bsp/io.h>
#elif defined(__rtems_arm_lpc24xx_ncs_rom_ext__)
#  include <arm/lpc24xx_ncs_rom_ext/bsp/io.h>
#elif defined(__rtems_arm_lpc24xx_ncs_rom_int__)
#  include <arm/lpc24xx_ncs_rom_int/bsp/io.h>
#elif defined(__rtems_arm_lpc24xx_plx800_ram__)
#  include <arm/lpc24xx_plx800_ram/bsp/io.h>
#elif defined(__rtems_arm_lpc24xx_plx800_rom_int__)
#  include <arm/lpc24xx_plx800_rom_int/bsp/io.h>
#elif defined(__rtems_arm_lpc40xx_ea_ram__)
#  include <arm/lpc40xx_ea_ram/bsp/io.h>
#elif defined(__rtems_arm_lpc40xx_ea_rom_int__)
#  include <arm/lpc40xx_ea_rom_int/bsp/io.h>
#elif defined(__rtems_arm_stm32f105rc__)
#  include <arm/stm32f105rc/bsp/io.h>
#elif defined(__rtems_arm_stm32f4__)
#  include <arm/stm32f4/bsp/io.h>
#else
#  error "__rtems_<arch>_<bsp>__ must be defined, for example: __rtems_sparc_erc32__"
#endif
