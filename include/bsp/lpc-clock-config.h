#if defined(HEADER_WARNING)
#warning "This header should not be included directly."
#endif


#if defined(__rtems_arm_lpc1768_mbed__)
#  include <arm/lpc1768_mbed/bsp/lpc-clock-config.h>
#elif defined(__rtems_arm_lpc1768_mbed_ahb_ram__)
#  include <arm/lpc1768_mbed_ahb_ram/bsp/lpc-clock-config.h>
#elif defined(__rtems_arm_lpc1768_mbed_ahb_ram_eth__)
#  include <arm/lpc1768_mbed_ahb_ram_eth/bsp/lpc-clock-config.h>
#elif defined(__rtems_arm_lpc17xx_ea_ram__)
#  include <arm/lpc17xx_ea_ram/bsp/lpc-clock-config.h>
#elif defined(__rtems_arm_lpc17xx_ea_rom_int__)
#  include <arm/lpc17xx_ea_rom_int/bsp/lpc-clock-config.h>
#elif defined(__rtems_arm_lpc17xx_plx800_ram__)
#  include <arm/lpc17xx_plx800_ram/bsp/lpc-clock-config.h>
#elif defined(__rtems_arm_lpc17xx_plx800_rom_int__)
#  include <arm/lpc17xx_plx800_rom_int/bsp/lpc-clock-config.h>
#elif defined(__rtems_arm_lpc2362__)
#  include <arm/lpc2362/bsp/lpc-clock-config.h>
#elif defined(__rtems_arm_lpc23xx_tli800__)
#  include <arm/lpc23xx_tli800/bsp/lpc-clock-config.h>
#elif defined(__rtems_arm_lpc24xx_ea__)
#  include <arm/lpc24xx_ea/bsp/lpc-clock-config.h>
#elif defined(__rtems_arm_lpc24xx_ncs_ram__)
#  include <arm/lpc24xx_ncs_ram/bsp/lpc-clock-config.h>
#elif defined(__rtems_arm_lpc24xx_ncs_rom_ext__)
#  include <arm/lpc24xx_ncs_rom_ext/bsp/lpc-clock-config.h>
#elif defined(__rtems_arm_lpc24xx_ncs_rom_int__)
#  include <arm/lpc24xx_ncs_rom_int/bsp/lpc-clock-config.h>
#elif defined(__rtems_arm_lpc24xx_plx800_ram__)
#  include <arm/lpc24xx_plx800_ram/bsp/lpc-clock-config.h>
#elif defined(__rtems_arm_lpc24xx_plx800_rom_int__)
#  include <arm/lpc24xx_plx800_rom_int/bsp/lpc-clock-config.h>
#elif defined(__rtems_arm_lpc32xx_mzx__)
#  include <arm/lpc32xx_mzx/bsp/lpc-clock-config.h>
#elif defined(__rtems_arm_lpc32xx_mzx_stage_1__)
#  include <arm/lpc32xx_mzx_stage_1/bsp/lpc-clock-config.h>
#elif defined(__rtems_arm_lpc32xx_mzx_stage_2__)
#  include <arm/lpc32xx_mzx_stage_2/bsp/lpc-clock-config.h>
#elif defined(__rtems_arm_lpc32xx_phycore__)
#  include <arm/lpc32xx_phycore/bsp/lpc-clock-config.h>
#elif defined(__rtems_arm_lpc40xx_ea_ram__)
#  include <arm/lpc40xx_ea_ram/bsp/lpc-clock-config.h>
#elif defined(__rtems_arm_lpc40xx_ea_rom_int__)
#  include <arm/lpc40xx_ea_rom_int/bsp/lpc-clock-config.h>
#else
#  error "__rtems_<arch>_<bsp>__ must be defined, for example: __rtems_sparc_erc32__"
#endif
