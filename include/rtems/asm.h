#if defined(HEADER_WARNING)
#warning "This header should not be included directly."
#endif


#if defined(__rtems_arm_altcycv_devkit__)
#  include <arm/altcycv_devkit/rtems/asm.h>
#elif defined(__rtems_arm_altcycv_devkit_smp__)
#  include <arm/altcycv_devkit_smp/rtems/asm.h>
#elif defined(__rtems_arm_arm1136jfs__)
#  include <arm/arm1136jfs/rtems/asm.h>
#elif defined(__rtems_arm_arm1136js__)
#  include <arm/arm1136js/rtems/asm.h>
#elif defined(__rtems_arm_arm7tdmi__)
#  include <arm/arm7tdmi/rtems/asm.h>
#elif defined(__rtems_arm_arm920__)
#  include <arm/arm920/rtems/asm.h>
#elif defined(__rtems_arm_armcortexa9__)
#  include <arm/armcortexa9/rtems/asm.h>
#elif defined(__rtems_arm_beagleboardorig__)
#  include <arm/beagleboardorig/rtems/asm.h>
#elif defined(__rtems_arm_beagleboardxm__)
#  include <arm/beagleboardxm/rtems/asm.h>
#elif defined(__rtems_arm_beagleboneblack__)
#  include <arm/beagleboneblack/rtems/asm.h>
#elif defined(__rtems_arm_beaglebonewhite__)
#  include <arm/beaglebonewhite/rtems/asm.h>
#elif defined(__rtems_arm_csb336__)
#  include <arm/csb336/rtems/asm.h>
#elif defined(__rtems_arm_csb337__)
#  include <arm/csb337/rtems/asm.h>
#elif defined(__rtems_arm_csb637__)
#  include <arm/csb637/rtems/asm.h>
#elif defined(__rtems_arm_edb7312__)
#  include <arm/edb7312/rtems/asm.h>
#elif defined(__rtems_arm_gba__)
#  include <arm/gba/rtems/asm.h>
#elif defined(__rtems_arm_gp32__)
#  include <arm/gp32/rtems/asm.h>
#elif defined(__rtems_arm_gumstix__)
#  include <arm/gumstix/rtems/asm.h>
#elif defined(__rtems_arm_kit637_v6__)
#  include <arm/kit637_v6/rtems/asm.h>
#elif defined(__rtems_arm_lm3s3749__)
#  include <arm/lm3s3749/rtems/asm.h>
#elif defined(__rtems_arm_lm3s6965__)
#  include <arm/lm3s6965/rtems/asm.h>
#elif defined(__rtems_arm_lm3s6965_qemu__)
#  include <arm/lm3s6965_qemu/rtems/asm.h>
#elif defined(__rtems_arm_lm4f120__)
#  include <arm/lm4f120/rtems/asm.h>
#elif defined(__rtems_arm_lpc1768_mbed__)
#  include <arm/lpc1768_mbed/rtems/asm.h>
#elif defined(__rtems_arm_lpc1768_mbed_ahb_ram__)
#  include <arm/lpc1768_mbed_ahb_ram/rtems/asm.h>
#elif defined(__rtems_arm_lpc1768_mbed_ahb_ram_eth__)
#  include <arm/lpc1768_mbed_ahb_ram_eth/rtems/asm.h>
#elif defined(__rtems_arm_lpc17xx_ea_ram__)
#  include <arm/lpc17xx_ea_ram/rtems/asm.h>
#elif defined(__rtems_arm_lpc17xx_ea_rom_int__)
#  include <arm/lpc17xx_ea_rom_int/rtems/asm.h>
#elif defined(__rtems_arm_lpc17xx_plx800_ram__)
#  include <arm/lpc17xx_plx800_ram/rtems/asm.h>
#elif defined(__rtems_arm_lpc17xx_plx800_rom_int__)
#  include <arm/lpc17xx_plx800_rom_int/rtems/asm.h>
#elif defined(__rtems_arm_lpc2362__)
#  include <arm/lpc2362/rtems/asm.h>
#elif defined(__rtems_arm_lpc23xx_tli800__)
#  include <arm/lpc23xx_tli800/rtems/asm.h>
#elif defined(__rtems_arm_lpc24xx_ea__)
#  include <arm/lpc24xx_ea/rtems/asm.h>
#elif defined(__rtems_arm_lpc24xx_ncs_ram__)
#  include <arm/lpc24xx_ncs_ram/rtems/asm.h>
#elif defined(__rtems_arm_lpc24xx_ncs_rom_ext__)
#  include <arm/lpc24xx_ncs_rom_ext/rtems/asm.h>
#elif defined(__rtems_arm_lpc24xx_ncs_rom_int__)
#  include <arm/lpc24xx_ncs_rom_int/rtems/asm.h>
#elif defined(__rtems_arm_lpc24xx_plx800_ram__)
#  include <arm/lpc24xx_plx800_ram/rtems/asm.h>
#elif defined(__rtems_arm_lpc24xx_plx800_rom_int__)
#  include <arm/lpc24xx_plx800_rom_int/rtems/asm.h>
#elif defined(__rtems_arm_lpc32xx_mzx__)
#  include <arm/lpc32xx_mzx/rtems/asm.h>
#elif defined(__rtems_arm_lpc32xx_mzx_stage_1__)
#  include <arm/lpc32xx_mzx_stage_1/rtems/asm.h>
#elif defined(__rtems_arm_lpc32xx_mzx_stage_2__)
#  include <arm/lpc32xx_mzx_stage_2/rtems/asm.h>
#elif defined(__rtems_arm_lpc32xx_phycore__)
#  include <arm/lpc32xx_phycore/rtems/asm.h>
#elif defined(__rtems_arm_lpc40xx_ea_ram__)
#  include <arm/lpc40xx_ea_ram/rtems/asm.h>
#elif defined(__rtems_arm_lpc40xx_ea_rom_int__)
#  include <arm/lpc40xx_ea_rom_int/rtems/asm.h>
#elif defined(__rtems_arm_nds__)
#  include <arm/nds/rtems/asm.h>
#elif defined(__rtems_arm_raspberrypi__)
#  include <arm/raspberrypi/rtems/asm.h>
#elif defined(__rtems_arm_realview_pbx_a9_qemu__)
#  include <arm/realview_pbx_a9_qemu/rtems/asm.h>
#elif defined(__rtems_arm_realview_pbx_a9_qemu_smp__)
#  include <arm/realview_pbx_a9_qemu_smp/rtems/asm.h>
#elif defined(__rtems_arm_rtl22xx__)
#  include <arm/rtl22xx/rtems/asm.h>
#elif defined(__rtems_arm_rtl22xx_t__)
#  include <arm/rtl22xx_t/rtems/asm.h>
#elif defined(__rtems_arm_smdk2410__)
#  include <arm/smdk2410/rtems/asm.h>
#elif defined(__rtems_arm_stm32f105rc__)
#  include <arm/stm32f105rc/rtems/asm.h>
#elif defined(__rtems_arm_stm32f4__)
#  include <arm/stm32f4/rtems/asm.h>
#elif defined(__rtems_arm_tms570ls3137_hdk__)
#  include <arm/tms570ls3137_hdk/rtems/asm.h>
#elif defined(__rtems_arm_tms570ls3137_hdk_intram__)
#  include <arm/tms570ls3137_hdk_intram/rtems/asm.h>
#elif defined(__rtems_arm_tms570ls3137_hdk_sdram__)
#  include <arm/tms570ls3137_hdk_sdram/rtems/asm.h>
#elif defined(__rtems_arm_xilinx_zynq_a9_qemu__)
#  include <arm/xilinx_zynq_a9_qemu/rtems/asm.h>
#elif defined(__rtems_arm_xilinx_zynq_zc702__)
#  include <arm/xilinx_zynq_zc702/rtems/asm.h>
#elif defined(__rtems_arm_xilinx_zynq_zc706__)
#  include <arm/xilinx_zynq_zc706/rtems/asm.h>
#elif defined(__rtems_arm_xilinx_zynq_zedboard__)
#  include <arm/xilinx_zynq_zedboard/rtems/asm.h>
#elif defined(__rtems_avr_avrtest__)
#  include <avr/avrtest/rtems/asm.h>
#elif defined(__rtems_bfin_TLL6527M__)
#  include <bfin/TLL6527M/rtems/asm.h>
#elif defined(__rtems_bfin_bf537Stamp__)
#  include <bfin/bf537Stamp/rtems/asm.h>
#elif defined(__rtems_bfin_eZKit533__)
#  include <bfin/eZKit533/rtems/asm.h>
#elif defined(__rtems_h8300_h8sim__)
#  include <h8300/h8sim/rtems/asm.h>
#elif defined(__rtems_h8300_h8sxsim__)
#  include <h8300/h8sxsim/rtems/asm.h>
#elif defined(__rtems_i386_pc386__)
#  include <i386/pc386/rtems/asm.h>
#elif defined(__rtems_i386_pc486__)
#  include <i386/pc486/rtems/asm.h>
#elif defined(__rtems_i386_pc586__)
#  include <i386/pc586/rtems/asm.h>
#elif defined(__rtems_i386_pc586_sse__)
#  include <i386/pc586-sse/rtems/asm.h>
#elif defined(__rtems_i386_pc686__)
#  include <i386/pc686/rtems/asm.h>
#elif defined(__rtems_i386_pcp4__)
#  include <i386/pcp4/rtems/asm.h>
#elif defined(__rtems_lm32_lm32_evr__)
#  include <lm32/lm32_evr/rtems/asm.h>
#elif defined(__rtems_lm32_milkymist__)
#  include <lm32/milkymist/rtems/asm.h>
#elif defined(__rtems_m32c_m32csim__)
#  include <m32c/m32csim/rtems/asm.h>
#elif defined(__rtems_m32r_m32rsim__)
#  include <m32r/m32rsim/rtems/asm.h>
#elif defined(__rtems_m68k_COBRA5475__)
#  include <m68k/COBRA5475/rtems/asm.h>
#elif defined(__rtems_m68k_av5282__)
#  include <m68k/av5282/rtems/asm.h>
#elif defined(__rtems_m68k_csb360__)
#  include <m68k/csb360/rtems/asm.h>
#elif defined(__rtems_m68k_gen68302__)
#  include <m68k/gen68302/rtems/asm.h>
#elif defined(__rtems_m68k_gen68340__)
#  include <m68k/gen68340/rtems/asm.h>
#elif defined(__rtems_m68k_gen68360__)
#  include <m68k/gen68360/rtems/asm.h>
#elif defined(__rtems_m68k_gen68360_040__)
#  include <m68k/gen68360_040/rtems/asm.h>
#elif defined(__rtems_m68k_idp__)
#  include <m68k/idp/rtems/asm.h>
#elif defined(__rtems_m68k_m5484FireEngine__)
#  include <m68k/m5484FireEngine/rtems/asm.h>
#elif defined(__rtems_m68k_mcf5206elite__)
#  include <m68k/mcf5206elite/rtems/asm.h>
#elif defined(__rtems_m68k_mcf52235__)
#  include <m68k/mcf52235/rtems/asm.h>
#elif defined(__rtems_m68k_mcf5225x__)
#  include <m68k/mcf5225x/rtems/asm.h>
#elif defined(__rtems_m68k_mcf5235__)
#  include <m68k/mcf5235/rtems/asm.h>
#elif defined(__rtems_m68k_mcf5329__)
#  include <m68k/mcf5329/rtems/asm.h>
#elif defined(__rtems_m68k_mrm332__)
#  include <m68k/mrm332/rtems/asm.h>
#elif defined(__rtems_m68k_mvme136__)
#  include <m68k/mvme136/rtems/asm.h>
#elif defined(__rtems_m68k_mvme147__)
#  include <m68k/mvme147/rtems/asm.h>
#elif defined(__rtems_m68k_mvme147s__)
#  include <m68k/mvme147s/rtems/asm.h>
#elif defined(__rtems_m68k_mvme162__)
#  include <m68k/mvme162/rtems/asm.h>
#elif defined(__rtems_m68k_mvme162lx__)
#  include <m68k/mvme162lx/rtems/asm.h>
#elif defined(__rtems_m68k_mvme167__)
#  include <m68k/mvme167/rtems/asm.h>
#elif defined(__rtems_m68k_ods68302__)
#  include <m68k/ods68302/rtems/asm.h>
#elif defined(__rtems_m68k_pgh360__)
#  include <m68k/pgh360/rtems/asm.h>
#elif defined(__rtems_m68k_sim68000__)
#  include <m68k/sim68000/rtems/asm.h>
#elif defined(__rtems_m68k_simcpu32__)
#  include <m68k/simcpu32/rtems/asm.h>
#elif defined(__rtems_m68k_uC5282__)
#  include <m68k/uC5282/rtems/asm.h>
#elif defined(__rtems_mips_csb350__)
#  include <mips/csb350/rtems/asm.h>
#elif defined(__rtems_mips_genmongoosev__)
#  include <mips/genmongoosev/rtems/asm.h>
#elif defined(__rtems_mips_hurricane__)
#  include <mips/hurricane/rtems/asm.h>
#elif defined(__rtems_mips_jmr3904__)
#  include <mips/jmr3904/rtems/asm.h>
#elif defined(__rtems_mips_malta__)
#  include <mips/malta/rtems/asm.h>
#elif defined(__rtems_mips_rbtx4925__)
#  include <mips/rbtx4925/rtems/asm.h>
#elif defined(__rtems_mips_rbtx4938__)
#  include <mips/rbtx4938/rtems/asm.h>
#elif defined(__rtems_moxie_moxiesim__)
#  include <moxie/moxiesim/rtems/asm.h>
#elif defined(__rtems_nios2_nios2_iss__)
#  include <nios2/nios2_iss/rtems/asm.h>
#elif defined(__rtems_or1k_or1ksim__)
#  include <or1k/or1ksim/rtems/asm.h>
#elif defined(__rtems_powerpc_beatnik__)
#  include <powerpc/beatnik/rtems/asm.h>
#elif defined(__rtems_powerpc_br_uid__)
#  include <powerpc/br_uid/rtems/asm.h>
#elif defined(__rtems_powerpc_brs5l__)
#  include <powerpc/brs5l/rtems/asm.h>
#elif defined(__rtems_powerpc_brs6l__)
#  include <powerpc/brs6l/rtems/asm.h>
#elif defined(__rtems_powerpc_dp2__)
#  include <powerpc/dp2/rtems/asm.h>
#elif defined(__rtems_powerpc_ep1a__)
#  include <powerpc/ep1a/rtems/asm.h>
#elif defined(__rtems_powerpc_gwlcfm__)
#  include <powerpc/gwlcfm/rtems/asm.h>
#elif defined(__rtems_powerpc_haleakala__)
#  include <powerpc/haleakala/rtems/asm.h>
#elif defined(__rtems_powerpc_hsc_cm01__)
#  include <powerpc/hsc_cm01/rtems/asm.h>
#elif defined(__rtems_powerpc_icecube__)
#  include <powerpc/icecube/rtems/asm.h>
#elif defined(__rtems_powerpc_mbx821_001__)
#  include <powerpc/mbx821_001/rtems/asm.h>
#elif defined(__rtems_powerpc_mbx821_002__)
#  include <powerpc/mbx821_002/rtems/asm.h>
#elif defined(__rtems_powerpc_mbx821_002b__)
#  include <powerpc/mbx821_002b/rtems/asm.h>
#elif defined(__rtems_powerpc_mbx860_001b__)
#  include <powerpc/mbx860_001b/rtems/asm.h>
#elif defined(__rtems_powerpc_mbx860_002__)
#  include <powerpc/mbx860_002/rtems/asm.h>
#elif defined(__rtems_powerpc_mbx860_005b__)
#  include <powerpc/mbx860_005b/rtems/asm.h>
#elif defined(__rtems_powerpc_mbx860_1b__)
#  include <powerpc/mbx860_1b/rtems/asm.h>
#elif defined(__rtems_powerpc_mcp750__)
#  include <powerpc/mcp750/rtems/asm.h>
#elif defined(__rtems_powerpc_mpc5566evb__)
#  include <powerpc/mpc5566evb/rtems/asm.h>
#elif defined(__rtems_powerpc_mpc5566evb_spe__)
#  include <powerpc/mpc5566evb_spe/rtems/asm.h>
#elif defined(__rtems_powerpc_mpc5643l_dpu__)
#  include <powerpc/mpc5643l_dpu/rtems/asm.h>
#elif defined(__rtems_powerpc_mpc5643l_evb__)
#  include <powerpc/mpc5643l_evb/rtems/asm.h>
#elif defined(__rtems_powerpc_mpc5668g__)
#  include <powerpc/mpc5668g/rtems/asm.h>
#elif defined(__rtems_powerpc_mpc5674f_ecu508_app__)
#  include <powerpc/mpc5674f_ecu508_app/rtems/asm.h>
#elif defined(__rtems_powerpc_mpc5674f_ecu508_boot__)
#  include <powerpc/mpc5674f_ecu508_boot/rtems/asm.h>
#elif defined(__rtems_powerpc_mpc5674f_rsm6__)
#  include <powerpc/mpc5674f_rsm6/rtems/asm.h>
#elif defined(__rtems_powerpc_mpc5674fevb__)
#  include <powerpc/mpc5674fevb/rtems/asm.h>
#elif defined(__rtems_powerpc_mpc5674fevb_spe__)
#  include <powerpc/mpc5674fevb_spe/rtems/asm.h>
#elif defined(__rtems_powerpc_mpc8260ads__)
#  include <powerpc/mpc8260ads/rtems/asm.h>
#elif defined(__rtems_powerpc_mpc8309som__)
#  include <powerpc/mpc8309som/rtems/asm.h>
#elif defined(__rtems_powerpc_mpc8313erdb__)
#  include <powerpc/mpc8313erdb/rtems/asm.h>
#elif defined(__rtems_powerpc_mpc8349eamds__)
#  include <powerpc/mpc8349eamds/rtems/asm.h>
#elif defined(__rtems_powerpc_mtx603e__)
#  include <powerpc/mtx603e/rtems/asm.h>
#elif defined(__rtems_powerpc_mvme2100__)
#  include <powerpc/mvme2100/rtems/asm.h>
#elif defined(__rtems_powerpc_mvme2307__)
#  include <powerpc/mvme2307/rtems/asm.h>
#elif defined(__rtems_powerpc_mvme3100__)
#  include <powerpc/mvme3100/rtems/asm.h>
#elif defined(__rtems_powerpc_mvme5500__)
#  include <powerpc/mvme5500/rtems/asm.h>
#elif defined(__rtems_powerpc_pghplus__)
#  include <powerpc/pghplus/rtems/asm.h>
#elif defined(__rtems_powerpc_phycore_mpc5554__)
#  include <powerpc/phycore_mpc5554/rtems/asm.h>
#elif defined(__rtems_powerpc_pm520_cr825__)
#  include <powerpc/pm520_cr825/rtems/asm.h>
#elif defined(__rtems_powerpc_pm520_ze30__)
#  include <powerpc/pm520_ze30/rtems/asm.h>
#elif defined(__rtems_powerpc_psim__)
#  include <powerpc/psim/rtems/asm.h>
#elif defined(__rtems_powerpc_qemuppc__)
#  include <powerpc/qemuppc/rtems/asm.h>
#elif defined(__rtems_powerpc_qemuprep__)
#  include <powerpc/qemuprep/rtems/asm.h>
#elif defined(__rtems_powerpc_qemuprep_altivec__)
#  include <powerpc/qemuprep-altivec/rtems/asm.h>
#elif defined(__rtems_powerpc_qoriq_core_0__)
#  include <powerpc/qoriq_core_0/rtems/asm.h>
#elif defined(__rtems_powerpc_qoriq_core_1__)
#  include <powerpc/qoriq_core_1/rtems/asm.h>
#elif defined(__rtems_powerpc_qoriq_p1020rdb__)
#  include <powerpc/qoriq_p1020rdb/rtems/asm.h>
#elif defined(__rtems_powerpc_score603e__)
#  include <powerpc/score603e/rtems/asm.h>
#elif defined(__rtems_powerpc_ss555__)
#  include <powerpc/ss555/rtems/asm.h>
#elif defined(__rtems_powerpc_t32mppc__)
#  include <powerpc/t32mppc/rtems/asm.h>
#elif defined(__rtems_powerpc_tqm8xx_stk8xx__)
#  include <powerpc/tqm8xx_stk8xx/rtems/asm.h>
#elif defined(__rtems_powerpc_virtex__)
#  include <powerpc/virtex/rtems/asm.h>
#elif defined(__rtems_powerpc_virtex4__)
#  include <powerpc/virtex4/rtems/asm.h>
#elif defined(__rtems_powerpc_virtex5__)
#  include <powerpc/virtex5/rtems/asm.h>
#elif defined(__rtems_sh_gensh1__)
#  include <sh/gensh1/rtems/asm.h>
#elif defined(__rtems_sh_gensh2__)
#  include <sh/gensh2/rtems/asm.h>
#elif defined(__rtems_sh_gensh4__)
#  include <sh/gensh4/rtems/asm.h>
#elif defined(__rtems_sh_simsh1__)
#  include <sh/simsh1/rtems/asm.h>
#elif defined(__rtems_sh_simsh2__)
#  include <sh/simsh2/rtems/asm.h>
#elif defined(__rtems_sh_simsh2e__)
#  include <sh/simsh2e/rtems/asm.h>
#elif defined(__rtems_sh_simsh4__)
#  include <sh/simsh4/rtems/asm.h>
#elif defined(__rtems_sparc_erc32__)
#  include <sparc/erc32/rtems/asm.h>
#elif defined(__rtems_sparc_leon2__)
#  include <sparc/leon2/rtems/asm.h>
#elif defined(__rtems_sparc_leon3__)
#  include <sparc/leon3/rtems/asm.h>
#elif defined(__rtems_sparc_ngmp__)
#  include <sparc/ngmp/rtems/asm.h>
#elif defined(__rtems_sparc_sis__)
#  include <sparc/sis/rtems/asm.h>
#elif defined(__rtems_sparc64_niagara__)
#  include <sparc64/niagara/rtems/asm.h>
#elif defined(__rtems_sparc64_usiii__)
#  include <sparc64/usiii/rtems/asm.h>
#elif defined(__rtems_v850_v850e1sim__)
#  include <v850/v850e1sim/rtems/asm.h>
#elif defined(__rtems_v850_v850e2sim__)
#  include <v850/v850e2sim/rtems/asm.h>
#elif defined(__rtems_v850_v850e2v3sim__)
#  include <v850/v850e2v3sim/rtems/asm.h>
#elif defined(__rtems_v850_v850esim__)
#  include <v850/v850esim/rtems/asm.h>
#elif defined(__rtems_v850_v850essim__)
#  include <v850/v850essim/rtems/asm.h>
#elif defined(__rtems_v850_v850sim__)
#  include <v850/v850sim/rtems/asm.h>
#else
#  error "__rtems_<arch>_<bsp>__ must be defined, for example: __rtems_sparc_erc32__"
#endif
