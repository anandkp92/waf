#if defined(HEADER_WARNING)
#warning "This header should not be included directly."
#endif


#if defined(__rtems_arm_altcycv_devkit__)
#  include <arm/altcycv_devkit/rtems/score/cpu_asm.h>
#elif defined(__rtems_arm_altcycv_devkit_smp__)
#  include <arm/altcycv_devkit_smp/rtems/score/cpu_asm.h>
#elif defined(__rtems_arm_arm1136jfs__)
#  include <arm/arm1136jfs/rtems/score/cpu_asm.h>
#elif defined(__rtems_arm_arm1136js__)
#  include <arm/arm1136js/rtems/score/cpu_asm.h>
#elif defined(__rtems_arm_arm7tdmi__)
#  include <arm/arm7tdmi/rtems/score/cpu_asm.h>
#elif defined(__rtems_arm_arm920__)
#  include <arm/arm920/rtems/score/cpu_asm.h>
#elif defined(__rtems_arm_armcortexa9__)
#  include <arm/armcortexa9/rtems/score/cpu_asm.h>
#elif defined(__rtems_arm_beagleboardorig__)
#  include <arm/beagleboardorig/rtems/score/cpu_asm.h>
#elif defined(__rtems_arm_beagleboardxm__)
#  include <arm/beagleboardxm/rtems/score/cpu_asm.h>
#elif defined(__rtems_arm_beagleboneblack__)
#  include <arm/beagleboneblack/rtems/score/cpu_asm.h>
#elif defined(__rtems_arm_beaglebonewhite__)
#  include <arm/beaglebonewhite/rtems/score/cpu_asm.h>
#elif defined(__rtems_arm_csb336__)
#  include <arm/csb336/rtems/score/cpu_asm.h>
#elif defined(__rtems_arm_csb337__)
#  include <arm/csb337/rtems/score/cpu_asm.h>
#elif defined(__rtems_arm_csb637__)
#  include <arm/csb637/rtems/score/cpu_asm.h>
#elif defined(__rtems_arm_edb7312__)
#  include <arm/edb7312/rtems/score/cpu_asm.h>
#elif defined(__rtems_arm_gba__)
#  include <arm/gba/rtems/score/cpu_asm.h>
#elif defined(__rtems_arm_gp32__)
#  include <arm/gp32/rtems/score/cpu_asm.h>
#elif defined(__rtems_arm_gumstix__)
#  include <arm/gumstix/rtems/score/cpu_asm.h>
#elif defined(__rtems_arm_kit637_v6__)
#  include <arm/kit637_v6/rtems/score/cpu_asm.h>
#elif defined(__rtems_arm_lm3s3749__)
#  include <arm/lm3s3749/rtems/score/cpu_asm.h>
#elif defined(__rtems_arm_lm3s6965__)
#  include <arm/lm3s6965/rtems/score/cpu_asm.h>
#elif defined(__rtems_arm_lm3s6965_qemu__)
#  include <arm/lm3s6965_qemu/rtems/score/cpu_asm.h>
#elif defined(__rtems_arm_lm4f120__)
#  include <arm/lm4f120/rtems/score/cpu_asm.h>
#elif defined(__rtems_arm_lpc1768_mbed__)
#  include <arm/lpc1768_mbed/rtems/score/cpu_asm.h>
#elif defined(__rtems_arm_lpc1768_mbed_ahb_ram__)
#  include <arm/lpc1768_mbed_ahb_ram/rtems/score/cpu_asm.h>
#elif defined(__rtems_arm_lpc1768_mbed_ahb_ram_eth__)
#  include <arm/lpc1768_mbed_ahb_ram_eth/rtems/score/cpu_asm.h>
#elif defined(__rtems_arm_lpc17xx_ea_ram__)
#  include <arm/lpc17xx_ea_ram/rtems/score/cpu_asm.h>
#elif defined(__rtems_arm_lpc17xx_ea_rom_int__)
#  include <arm/lpc17xx_ea_rom_int/rtems/score/cpu_asm.h>
#elif defined(__rtems_arm_lpc17xx_plx800_ram__)
#  include <arm/lpc17xx_plx800_ram/rtems/score/cpu_asm.h>
#elif defined(__rtems_arm_lpc17xx_plx800_rom_int__)
#  include <arm/lpc17xx_plx800_rom_int/rtems/score/cpu_asm.h>
#elif defined(__rtems_arm_lpc2362__)
#  include <arm/lpc2362/rtems/score/cpu_asm.h>
#elif defined(__rtems_arm_lpc23xx_tli800__)
#  include <arm/lpc23xx_tli800/rtems/score/cpu_asm.h>
#elif defined(__rtems_arm_lpc24xx_ea__)
#  include <arm/lpc24xx_ea/rtems/score/cpu_asm.h>
#elif defined(__rtems_arm_lpc24xx_ncs_ram__)
#  include <arm/lpc24xx_ncs_ram/rtems/score/cpu_asm.h>
#elif defined(__rtems_arm_lpc24xx_ncs_rom_ext__)
#  include <arm/lpc24xx_ncs_rom_ext/rtems/score/cpu_asm.h>
#elif defined(__rtems_arm_lpc24xx_ncs_rom_int__)
#  include <arm/lpc24xx_ncs_rom_int/rtems/score/cpu_asm.h>
#elif defined(__rtems_arm_lpc24xx_plx800_ram__)
#  include <arm/lpc24xx_plx800_ram/rtems/score/cpu_asm.h>
#elif defined(__rtems_arm_lpc24xx_plx800_rom_int__)
#  include <arm/lpc24xx_plx800_rom_int/rtems/score/cpu_asm.h>
#elif defined(__rtems_arm_lpc32xx_mzx__)
#  include <arm/lpc32xx_mzx/rtems/score/cpu_asm.h>
#elif defined(__rtems_arm_lpc32xx_mzx_stage_1__)
#  include <arm/lpc32xx_mzx_stage_1/rtems/score/cpu_asm.h>
#elif defined(__rtems_arm_lpc32xx_mzx_stage_2__)
#  include <arm/lpc32xx_mzx_stage_2/rtems/score/cpu_asm.h>
#elif defined(__rtems_arm_lpc32xx_phycore__)
#  include <arm/lpc32xx_phycore/rtems/score/cpu_asm.h>
#elif defined(__rtems_arm_lpc40xx_ea_ram__)
#  include <arm/lpc40xx_ea_ram/rtems/score/cpu_asm.h>
#elif defined(__rtems_arm_lpc40xx_ea_rom_int__)
#  include <arm/lpc40xx_ea_rom_int/rtems/score/cpu_asm.h>
#elif defined(__rtems_arm_nds__)
#  include <arm/nds/rtems/score/cpu_asm.h>
#elif defined(__rtems_arm_raspberrypi__)
#  include <arm/raspberrypi/rtems/score/cpu_asm.h>
#elif defined(__rtems_arm_realview_pbx_a9_qemu__)
#  include <arm/realview_pbx_a9_qemu/rtems/score/cpu_asm.h>
#elif defined(__rtems_arm_realview_pbx_a9_qemu_smp__)
#  include <arm/realview_pbx_a9_qemu_smp/rtems/score/cpu_asm.h>
#elif defined(__rtems_arm_rtl22xx__)
#  include <arm/rtl22xx/rtems/score/cpu_asm.h>
#elif defined(__rtems_arm_rtl22xx_t__)
#  include <arm/rtl22xx_t/rtems/score/cpu_asm.h>
#elif defined(__rtems_arm_smdk2410__)
#  include <arm/smdk2410/rtems/score/cpu_asm.h>
#elif defined(__rtems_arm_stm32f105rc__)
#  include <arm/stm32f105rc/rtems/score/cpu_asm.h>
#elif defined(__rtems_arm_stm32f4__)
#  include <arm/stm32f4/rtems/score/cpu_asm.h>
#elif defined(__rtems_arm_tms570ls3137_hdk__)
#  include <arm/tms570ls3137_hdk/rtems/score/cpu_asm.h>
#elif defined(__rtems_arm_tms570ls3137_hdk_intram__)
#  include <arm/tms570ls3137_hdk_intram/rtems/score/cpu_asm.h>
#elif defined(__rtems_arm_tms570ls3137_hdk_sdram__)
#  include <arm/tms570ls3137_hdk_sdram/rtems/score/cpu_asm.h>
#elif defined(__rtems_arm_xilinx_zynq_a9_qemu__)
#  include <arm/xilinx_zynq_a9_qemu/rtems/score/cpu_asm.h>
#elif defined(__rtems_arm_xilinx_zynq_zc702__)
#  include <arm/xilinx_zynq_zc702/rtems/score/cpu_asm.h>
#elif defined(__rtems_arm_xilinx_zynq_zc706__)
#  include <arm/xilinx_zynq_zc706/rtems/score/cpu_asm.h>
#elif defined(__rtems_arm_xilinx_zynq_zedboard__)
#  include <arm/xilinx_zynq_zedboard/rtems/score/cpu_asm.h>
#elif defined(__rtems_avr_avrtest__)
#  include <avr/avrtest/rtems/score/cpu_asm.h>
#elif defined(__rtems_bfin_TLL6527M__)
#  include <bfin/TLL6527M/rtems/score/cpu_asm.h>
#elif defined(__rtems_bfin_bf537Stamp__)
#  include <bfin/bf537Stamp/rtems/score/cpu_asm.h>
#elif defined(__rtems_bfin_eZKit533__)
#  include <bfin/eZKit533/rtems/score/cpu_asm.h>
#elif defined(__rtems_lm32_lm32_evr__)
#  include <lm32/lm32_evr/rtems/score/cpu_asm.h>
#elif defined(__rtems_lm32_milkymist__)
#  include <lm32/milkymist/rtems/score/cpu_asm.h>
#elif defined(__rtems_m32c_m32csim__)
#  include <m32c/m32csim/rtems/score/cpu_asm.h>
#elif defined(__rtems_m32r_m32rsim__)
#  include <m32r/m32rsim/rtems/score/cpu_asm.h>
#elif defined(__rtems_nios2_nios2_iss__)
#  include <nios2/nios2_iss/rtems/score/cpu_asm.h>
#elif defined(__rtems_or1k_or1ksim__)
#  include <or1k/or1ksim/rtems/score/cpu_asm.h>
#elif defined(__rtems_v850_v850e1sim__)
#  include <v850/v850e1sim/rtems/score/cpu_asm.h>
#elif defined(__rtems_v850_v850e2sim__)
#  include <v850/v850e2sim/rtems/score/cpu_asm.h>
#elif defined(__rtems_v850_v850e2v3sim__)
#  include <v850/v850e2v3sim/rtems/score/cpu_asm.h>
#elif defined(__rtems_v850_v850esim__)
#  include <v850/v850esim/rtems/score/cpu_asm.h>
#elif defined(__rtems_v850_v850essim__)
#  include <v850/v850essim/rtems/score/cpu_asm.h>
#elif defined(__rtems_v850_v850sim__)
#  include <v850/v850sim/rtems/score/cpu_asm.h>
#else
#  error "__rtems_<arch>_<bsp>__ must be defined, for example: __rtems_sparc_erc32__"
#endif
