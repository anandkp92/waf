#if defined(HEADER_WARNING)
#warning "This header should not be included directly."
#endif


#if defined(__rtems_arm_beagleboardorig__)
#  include <arm/beagleboardorig/bsp/i2c.h>
#elif defined(__rtems_arm_beagleboardxm__)
#  include <arm/beagleboardxm/bsp/i2c.h>
#elif defined(__rtems_arm_beagleboneblack__)
#  include <arm/beagleboneblack/bsp/i2c.h>
#elif defined(__rtems_arm_beaglebonewhite__)
#  include <arm/beaglebonewhite/bsp/i2c.h>
#elif defined(__rtems_arm_lpc17xx_ea_ram__)
#  include <arm/lpc17xx_ea_ram/bsp/i2c.h>
#elif defined(__rtems_arm_lpc17xx_ea_rom_int__)
#  include <arm/lpc17xx_ea_rom_int/bsp/i2c.h>
#elif defined(__rtems_arm_lpc17xx_plx800_ram__)
#  include <arm/lpc17xx_plx800_ram/bsp/i2c.h>
#elif defined(__rtems_arm_lpc17xx_plx800_rom_int__)
#  include <arm/lpc17xx_plx800_rom_int/bsp/i2c.h>
#elif defined(__rtems_arm_lpc2362__)
#  include <arm/lpc2362/bsp/i2c.h>
#elif defined(__rtems_arm_lpc23xx_tli800__)
#  include <arm/lpc23xx_tli800/bsp/i2c.h>
#elif defined(__rtems_arm_lpc24xx_ea__)
#  include <arm/lpc24xx_ea/bsp/i2c.h>
#elif defined(__rtems_arm_lpc24xx_ncs_ram__)
#  include <arm/lpc24xx_ncs_ram/bsp/i2c.h>
#elif defined(__rtems_arm_lpc24xx_ncs_rom_ext__)
#  include <arm/lpc24xx_ncs_rom_ext/bsp/i2c.h>
#elif defined(__rtems_arm_lpc24xx_ncs_rom_int__)
#  include <arm/lpc24xx_ncs_rom_int/bsp/i2c.h>
#elif defined(__rtems_arm_lpc24xx_plx800_ram__)
#  include <arm/lpc24xx_plx800_ram/bsp/i2c.h>
#elif defined(__rtems_arm_lpc24xx_plx800_rom_int__)
#  include <arm/lpc24xx_plx800_rom_int/bsp/i2c.h>
#elif defined(__rtems_arm_lpc32xx_mzx__)
#  include <arm/lpc32xx_mzx/bsp/i2c.h>
#elif defined(__rtems_arm_lpc32xx_mzx_stage_1__)
#  include <arm/lpc32xx_mzx_stage_1/bsp/i2c.h>
#elif defined(__rtems_arm_lpc32xx_mzx_stage_2__)
#  include <arm/lpc32xx_mzx_stage_2/bsp/i2c.h>
#elif defined(__rtems_arm_lpc32xx_phycore__)
#  include <arm/lpc32xx_phycore/bsp/i2c.h>
#elif defined(__rtems_arm_lpc40xx_ea_ram__)
#  include <arm/lpc40xx_ea_ram/bsp/i2c.h>
#elif defined(__rtems_arm_lpc40xx_ea_rom_int__)
#  include <arm/lpc40xx_ea_rom_int/bsp/i2c.h>
#elif defined(__rtems_arm_stm32f105rc__)
#  include <arm/stm32f105rc/bsp/i2c.h>
#elif defined(__rtems_arm_stm32f4__)
#  include <arm/stm32f4/bsp/i2c.h>
#elif defined(__rtems_arm_xilinx_zynq_a9_qemu__)
#  include <arm/xilinx_zynq_a9_qemu/bsp/i2c.h>
#elif defined(__rtems_arm_xilinx_zynq_zc702__)
#  include <arm/xilinx_zynq_zc702/bsp/i2c.h>
#elif defined(__rtems_arm_xilinx_zynq_zc706__)
#  include <arm/xilinx_zynq_zc706/bsp/i2c.h>
#elif defined(__rtems_arm_xilinx_zynq_zedboard__)
#  include <arm/xilinx_zynq_zedboard/bsp/i2c.h>
#elif defined(__rtems_powerpc_brs5l__)
#  include <powerpc/brs5l/bsp/i2c.h>
#elif defined(__rtems_powerpc_brs6l__)
#  include <powerpc/brs6l/bsp/i2c.h>
#elif defined(__rtems_powerpc_dp2__)
#  include <powerpc/dp2/bsp/i2c.h>
#elif defined(__rtems_powerpc_icecube__)
#  include <powerpc/icecube/bsp/i2c.h>
#elif defined(__rtems_powerpc_pm520_cr825__)
#  include <powerpc/pm520_cr825/bsp/i2c.h>
#elif defined(__rtems_powerpc_pm520_ze30__)
#  include <powerpc/pm520_ze30/bsp/i2c.h>
#else
#  error "__rtems_<arch>_<bsp>__ must be defined, for example: __rtems_sparc_erc32__"
#endif
