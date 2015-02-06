#if defined(HEADER_WARNING)
#warning "This header should not be included directly."
#endif


#if defined(__rtems_arm_altcycv_devkit__)
#  include <arm/altcycv_devkit/bsp/irq.h>
#elif defined(__rtems_arm_altcycv_devkit_smp__)
#  include <arm/altcycv_devkit_smp/bsp/irq.h>
#elif defined(__rtems_arm_arm1136jfs__)
#  include <arm/arm1136jfs/bsp/irq.h>
#elif defined(__rtems_arm_arm1136js__)
#  include <arm/arm1136js/bsp/irq.h>
#elif defined(__rtems_arm_arm7tdmi__)
#  include <arm/arm7tdmi/bsp/irq.h>
#elif defined(__rtems_arm_arm920__)
#  include <arm/arm920/bsp/irq.h>
#elif defined(__rtems_arm_armcortexa9__)
#  include <arm/armcortexa9/bsp/irq.h>
#elif defined(__rtems_arm_beagleboardorig__)
#  include <arm/beagleboardorig/bsp/irq.h>
#elif defined(__rtems_arm_beagleboardxm__)
#  include <arm/beagleboardxm/bsp/irq.h>
#elif defined(__rtems_arm_beagleboneblack__)
#  include <arm/beagleboneblack/bsp/irq.h>
#elif defined(__rtems_arm_beaglebonewhite__)
#  include <arm/beaglebonewhite/bsp/irq.h>
#elif defined(__rtems_arm_csb336__)
#  include <arm/csb336/bsp/irq.h>
#elif defined(__rtems_arm_csb337__)
#  include <arm/csb337/bsp/irq.h>
#elif defined(__rtems_arm_csb637__)
#  include <arm/csb637/bsp/irq.h>
#elif defined(__rtems_arm_edb7312__)
#  include <arm/edb7312/bsp/irq.h>
#elif defined(__rtems_arm_gba__)
#  include <arm/gba/bsp/irq.h>
#elif defined(__rtems_arm_gp32__)
#  include <arm/gp32/bsp/irq.h>
#elif defined(__rtems_arm_gumstix__)
#  include <arm/gumstix/bsp/irq.h>
#elif defined(__rtems_arm_kit637_v6__)
#  include <arm/kit637_v6/bsp/irq.h>
#elif defined(__rtems_arm_lm3s3749__)
#  include <arm/lm3s3749/bsp/irq.h>
#elif defined(__rtems_arm_lm3s6965__)
#  include <arm/lm3s6965/bsp/irq.h>
#elif defined(__rtems_arm_lm3s6965_qemu__)
#  include <arm/lm3s6965_qemu/bsp/irq.h>
#elif defined(__rtems_arm_lm4f120__)
#  include <arm/lm4f120/bsp/irq.h>
#elif defined(__rtems_arm_lpc1768_mbed__)
#  include <arm/lpc1768_mbed/bsp/irq.h>
#elif defined(__rtems_arm_lpc1768_mbed_ahb_ram__)
#  include <arm/lpc1768_mbed_ahb_ram/bsp/irq.h>
#elif defined(__rtems_arm_lpc1768_mbed_ahb_ram_eth__)
#  include <arm/lpc1768_mbed_ahb_ram_eth/bsp/irq.h>
#elif defined(__rtems_arm_lpc17xx_ea_ram__)
#  include <arm/lpc17xx_ea_ram/bsp/irq.h>
#elif defined(__rtems_arm_lpc17xx_ea_rom_int__)
#  include <arm/lpc17xx_ea_rom_int/bsp/irq.h>
#elif defined(__rtems_arm_lpc17xx_plx800_ram__)
#  include <arm/lpc17xx_plx800_ram/bsp/irq.h>
#elif defined(__rtems_arm_lpc17xx_plx800_rom_int__)
#  include <arm/lpc17xx_plx800_rom_int/bsp/irq.h>
#elif defined(__rtems_arm_lpc2362__)
#  include <arm/lpc2362/bsp/irq.h>
#elif defined(__rtems_arm_lpc23xx_tli800__)
#  include <arm/lpc23xx_tli800/bsp/irq.h>
#elif defined(__rtems_arm_lpc24xx_ea__)
#  include <arm/lpc24xx_ea/bsp/irq.h>
#elif defined(__rtems_arm_lpc24xx_ncs_ram__)
#  include <arm/lpc24xx_ncs_ram/bsp/irq.h>
#elif defined(__rtems_arm_lpc24xx_ncs_rom_ext__)
#  include <arm/lpc24xx_ncs_rom_ext/bsp/irq.h>
#elif defined(__rtems_arm_lpc24xx_ncs_rom_int__)
#  include <arm/lpc24xx_ncs_rom_int/bsp/irq.h>
#elif defined(__rtems_arm_lpc24xx_plx800_ram__)
#  include <arm/lpc24xx_plx800_ram/bsp/irq.h>
#elif defined(__rtems_arm_lpc24xx_plx800_rom_int__)
#  include <arm/lpc24xx_plx800_rom_int/bsp/irq.h>
#elif defined(__rtems_arm_lpc32xx_mzx__)
#  include <arm/lpc32xx_mzx/bsp/irq.h>
#elif defined(__rtems_arm_lpc32xx_mzx_stage_1__)
#  include <arm/lpc32xx_mzx_stage_1/bsp/irq.h>
#elif defined(__rtems_arm_lpc32xx_mzx_stage_2__)
#  include <arm/lpc32xx_mzx_stage_2/bsp/irq.h>
#elif defined(__rtems_arm_lpc32xx_phycore__)
#  include <arm/lpc32xx_phycore/bsp/irq.h>
#elif defined(__rtems_arm_lpc40xx_ea_ram__)
#  include <arm/lpc40xx_ea_ram/bsp/irq.h>
#elif defined(__rtems_arm_lpc40xx_ea_rom_int__)
#  include <arm/lpc40xx_ea_rom_int/bsp/irq.h>
#elif defined(__rtems_arm_nds__)
#  include <arm/nds/bsp/irq.h>
#elif defined(__rtems_arm_raspberrypi__)
#  include <arm/raspberrypi/bsp/irq.h>
#elif defined(__rtems_arm_realview_pbx_a9_qemu__)
#  include <arm/realview_pbx_a9_qemu/bsp/irq.h>
#elif defined(__rtems_arm_realview_pbx_a9_qemu_smp__)
#  include <arm/realview_pbx_a9_qemu_smp/bsp/irq.h>
#elif defined(__rtems_arm_rtl22xx__)
#  include <arm/rtl22xx/bsp/irq.h>
#elif defined(__rtems_arm_rtl22xx_t__)
#  include <arm/rtl22xx_t/bsp/irq.h>
#elif defined(__rtems_arm_smdk2410__)
#  include <arm/smdk2410/bsp/irq.h>
#elif defined(__rtems_arm_stm32f105rc__)
#  include <arm/stm32f105rc/bsp/irq.h>
#elif defined(__rtems_arm_stm32f4__)
#  include <arm/stm32f4/bsp/irq.h>
#elif defined(__rtems_arm_tms570ls3137_hdk__)
#  include <arm/tms570ls3137_hdk/bsp/irq.h>
#elif defined(__rtems_arm_tms570ls3137_hdk_intram__)
#  include <arm/tms570ls3137_hdk_intram/bsp/irq.h>
#elif defined(__rtems_arm_tms570ls3137_hdk_sdram__)
#  include <arm/tms570ls3137_hdk_sdram/bsp/irq.h>
#elif defined(__rtems_arm_xilinx_zynq_a9_qemu__)
#  include <arm/xilinx_zynq_a9_qemu/bsp/irq.h>
#elif defined(__rtems_arm_xilinx_zynq_zc702__)
#  include <arm/xilinx_zynq_zc702/bsp/irq.h>
#elif defined(__rtems_arm_xilinx_zynq_zc706__)
#  include <arm/xilinx_zynq_zc706/bsp/irq.h>
#elif defined(__rtems_arm_xilinx_zynq_zedboard__)
#  include <arm/xilinx_zynq_zedboard/bsp/irq.h>
#elif defined(__rtems_i386_pc386__)
#  include <i386/pc386/bsp/irq.h>
#elif defined(__rtems_i386_pc486__)
#  include <i386/pc486/bsp/irq.h>
#elif defined(__rtems_i386_pc586__)
#  include <i386/pc586/bsp/irq.h>
#elif defined(__rtems_i386_pc586_sse__)
#  include <i386/pc586-sse/bsp/irq.h>
#elif defined(__rtems_i386_pc686__)
#  include <i386/pc686/bsp/irq.h>
#elif defined(__rtems_i386_pcp4__)
#  include <i386/pcp4/bsp/irq.h>
#elif defined(__rtems_lm32_milkymist__)
#  include <lm32/milkymist/bsp/irq.h>
#elif defined(__rtems_m68k_COBRA5475__)
#  include <m68k/COBRA5475/bsp/irq.h>
#elif defined(__rtems_m68k_m5484FireEngine__)
#  include <m68k/m5484FireEngine/bsp/irq.h>
#elif defined(__rtems_mips_csb350__)
#  include <mips/csb350/bsp/irq.h>
#elif defined(__rtems_mips_genmongoosev__)
#  include <mips/genmongoosev/bsp/irq.h>
#elif defined(__rtems_mips_hurricane__)
#  include <mips/hurricane/bsp/irq.h>
#elif defined(__rtems_mips_jmr3904__)
#  include <mips/jmr3904/bsp/irq.h>
#elif defined(__rtems_mips_malta__)
#  include <mips/malta/bsp/irq.h>
#elif defined(__rtems_mips_rbtx4925__)
#  include <mips/rbtx4925/bsp/irq.h>
#elif defined(__rtems_mips_rbtx4938__)
#  include <mips/rbtx4938/bsp/irq.h>
#elif defined(__rtems_or1k_or1ksim__)
#  include <or1k/or1ksim/bsp/irq.h>
#elif defined(__rtems_powerpc_beatnik__)
#  include <powerpc/beatnik/bsp/irq.h>
#elif defined(__rtems_powerpc_br_uid__)
#  include <powerpc/br_uid/bsp/irq.h>
#elif defined(__rtems_powerpc_brs5l__)
#  include <powerpc/brs5l/bsp/irq.h>
#elif defined(__rtems_powerpc_brs6l__)
#  include <powerpc/brs6l/bsp/irq.h>
#elif defined(__rtems_powerpc_dp2__)
#  include <powerpc/dp2/bsp/irq.h>
#elif defined(__rtems_powerpc_ep1a__)
#  include <powerpc/ep1a/bsp/irq.h>
#elif defined(__rtems_powerpc_gwlcfm__)
#  include <powerpc/gwlcfm/bsp/irq.h>
#elif defined(__rtems_powerpc_haleakala__)
#  include <powerpc/haleakala/bsp/irq.h>
#elif defined(__rtems_powerpc_hsc_cm01__)
#  include <powerpc/hsc_cm01/bsp/irq.h>
#elif defined(__rtems_powerpc_icecube__)
#  include <powerpc/icecube/bsp/irq.h>
#elif defined(__rtems_powerpc_mbx821_001__)
#  include <powerpc/mbx821_001/bsp/irq.h>
#elif defined(__rtems_powerpc_mbx821_002__)
#  include <powerpc/mbx821_002/bsp/irq.h>
#elif defined(__rtems_powerpc_mbx821_002b__)
#  include <powerpc/mbx821_002b/bsp/irq.h>
#elif defined(__rtems_powerpc_mbx860_001b__)
#  include <powerpc/mbx860_001b/bsp/irq.h>
#elif defined(__rtems_powerpc_mbx860_002__)
#  include <powerpc/mbx860_002/bsp/irq.h>
#elif defined(__rtems_powerpc_mbx860_005b__)
#  include <powerpc/mbx860_005b/bsp/irq.h>
#elif defined(__rtems_powerpc_mbx860_1b__)
#  include <powerpc/mbx860_1b/bsp/irq.h>
#elif defined(__rtems_powerpc_mcp750__)
#  include <powerpc/mcp750/bsp/irq.h>
#elif defined(__rtems_powerpc_mpc5566evb__)
#  include <powerpc/mpc5566evb/bsp/irq.h>
#elif defined(__rtems_powerpc_mpc5566evb_spe__)
#  include <powerpc/mpc5566evb_spe/bsp/irq.h>
#elif defined(__rtems_powerpc_mpc5643l_dpu__)
#  include <powerpc/mpc5643l_dpu/bsp/irq.h>
#elif defined(__rtems_powerpc_mpc5643l_evb__)
#  include <powerpc/mpc5643l_evb/bsp/irq.h>
#elif defined(__rtems_powerpc_mpc5668g__)
#  include <powerpc/mpc5668g/bsp/irq.h>
#elif defined(__rtems_powerpc_mpc5674f_ecu508_app__)
#  include <powerpc/mpc5674f_ecu508_app/bsp/irq.h>
#elif defined(__rtems_powerpc_mpc5674f_ecu508_boot__)
#  include <powerpc/mpc5674f_ecu508_boot/bsp/irq.h>
#elif defined(__rtems_powerpc_mpc5674f_rsm6__)
#  include <powerpc/mpc5674f_rsm6/bsp/irq.h>
#elif defined(__rtems_powerpc_mpc5674fevb__)
#  include <powerpc/mpc5674fevb/bsp/irq.h>
#elif defined(__rtems_powerpc_mpc5674fevb_spe__)
#  include <powerpc/mpc5674fevb_spe/bsp/irq.h>
#elif defined(__rtems_powerpc_mpc8260ads__)
#  include <powerpc/mpc8260ads/bsp/irq.h>
#elif defined(__rtems_powerpc_mpc8309som__)
#  include <powerpc/mpc8309som/bsp/irq.h>
#elif defined(__rtems_powerpc_mpc8313erdb__)
#  include <powerpc/mpc8313erdb/bsp/irq.h>
#elif defined(__rtems_powerpc_mpc8349eamds__)
#  include <powerpc/mpc8349eamds/bsp/irq.h>
#elif defined(__rtems_powerpc_mtx603e__)
#  include <powerpc/mtx603e/bsp/irq.h>
#elif defined(__rtems_powerpc_mvme2100__)
#  include <powerpc/mvme2100/bsp/irq.h>
#elif defined(__rtems_powerpc_mvme2307__)
#  include <powerpc/mvme2307/bsp/irq.h>
#elif defined(__rtems_powerpc_mvme3100__)
#  include <powerpc/mvme3100/bsp/irq.h>
#elif defined(__rtems_powerpc_mvme5500__)
#  include <powerpc/mvme5500/bsp/irq.h>
#elif defined(__rtems_powerpc_pghplus__)
#  include <powerpc/pghplus/bsp/irq.h>
#elif defined(__rtems_powerpc_phycore_mpc5554__)
#  include <powerpc/phycore_mpc5554/bsp/irq.h>
#elif defined(__rtems_powerpc_pm520_cr825__)
#  include <powerpc/pm520_cr825/bsp/irq.h>
#elif defined(__rtems_powerpc_pm520_ze30__)
#  include <powerpc/pm520_ze30/bsp/irq.h>
#elif defined(__rtems_powerpc_psim__)
#  include <powerpc/psim/bsp/irq.h>
#elif defined(__rtems_powerpc_qemuppc__)
#  include <powerpc/qemuppc/bsp/irq.h>
#elif defined(__rtems_powerpc_qemuprep__)
#  include <powerpc/qemuprep/bsp/irq.h>
#elif defined(__rtems_powerpc_qemuprep_altivec__)
#  include <powerpc/qemuprep-altivec/bsp/irq.h>
#elif defined(__rtems_powerpc_qoriq_core_0__)
#  include <powerpc/qoriq_core_0/bsp/irq.h>
#elif defined(__rtems_powerpc_qoriq_core_1__)
#  include <powerpc/qoriq_core_1/bsp/irq.h>
#elif defined(__rtems_powerpc_qoriq_p1020rdb__)
#  include <powerpc/qoriq_p1020rdb/bsp/irq.h>
#elif defined(__rtems_powerpc_score603e__)
#  include <powerpc/score603e/bsp/irq.h>
#elif defined(__rtems_powerpc_ss555__)
#  include <powerpc/ss555/bsp/irq.h>
#elif defined(__rtems_powerpc_t32mppc__)
#  include <powerpc/t32mppc/bsp/irq.h>
#elif defined(__rtems_powerpc_tqm8xx_stk8xx__)
#  include <powerpc/tqm8xx_stk8xx/bsp/irq.h>
#elif defined(__rtems_powerpc_virtex__)
#  include <powerpc/virtex/bsp/irq.h>
#elif defined(__rtems_powerpc_virtex4__)
#  include <powerpc/virtex4/bsp/irq.h>
#elif defined(__rtems_powerpc_virtex5__)
#  include <powerpc/virtex5/bsp/irq.h>
#elif defined(__rtems_sparc_erc32__)
#  include <sparc/erc32/bsp/irq.h>
#elif defined(__rtems_sparc_leon2__)
#  include <sparc/leon2/bsp/irq.h>
#elif defined(__rtems_sparc_leon3__)
#  include <sparc/leon3/bsp/irq.h>
#elif defined(__rtems_sparc_ngmp__)
#  include <sparc/ngmp/bsp/irq.h>
#elif defined(__rtems_sparc_sis__)
#  include <sparc/sis/bsp/irq.h>
#else
#  error "__rtems_<arch>_<bsp>__ must be defined, for example: __rtems_sparc_erc32__"
#endif
