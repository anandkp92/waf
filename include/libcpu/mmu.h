#if defined(HEADER_WARNING)
#warning "This header should not be included directly."
#endif


#if defined(__rtems_arm_csb336__)
#  include <arm/csb336/libcpu/mmu.h>
#elif defined(__rtems_arm_csb337__)
#  include <arm/csb337/libcpu/mmu.h>
#elif defined(__rtems_arm_csb637__)
#  include <arm/csb637/libcpu/mmu.h>
#elif defined(__rtems_arm_gp32__)
#  include <arm/gp32/libcpu/mmu.h>
#elif defined(__rtems_arm_gumstix__)
#  include <arm/gumstix/libcpu/mmu.h>
#elif defined(__rtems_arm_kit637_v6__)
#  include <arm/kit637_v6/libcpu/mmu.h>
#elif defined(__rtems_arm_smdk2410__)
#  include <arm/smdk2410/libcpu/mmu.h>
#elif defined(__rtems_bfin_TLL6527M__)
#  include <bfin/TLL6527M/libcpu/mmu.h>
#elif defined(__rtems_bfin_bf537Stamp__)
#  include <bfin/bf537Stamp/libcpu/mmu.h>
#elif defined(__rtems_bfin_eZKit533__)
#  include <bfin/eZKit533/libcpu/mmu.h>
#elif defined(__rtems_powerpc_beatnik__)
#  include <powerpc/beatnik/libcpu/mmu.h>
#elif defined(__rtems_powerpc_br_uid__)
#  include <powerpc/br_uid/libcpu/mmu.h>
#elif defined(__rtems_powerpc_brs5l__)
#  include <powerpc/brs5l/libcpu/mmu.h>
#elif defined(__rtems_powerpc_brs6l__)
#  include <powerpc/brs6l/libcpu/mmu.h>
#elif defined(__rtems_powerpc_dp2__)
#  include <powerpc/dp2/libcpu/mmu.h>
#elif defined(__rtems_powerpc_ep1a__)
#  include <powerpc/ep1a/libcpu/mmu.h>
#elif defined(__rtems_powerpc_gwlcfm__)
#  include <powerpc/gwlcfm/libcpu/mmu.h>
#elif defined(__rtems_powerpc_haleakala__)
#  include <powerpc/haleakala/libcpu/mmu.h>
#elif defined(__rtems_powerpc_hsc_cm01__)
#  include <powerpc/hsc_cm01/libcpu/mmu.h>
#elif defined(__rtems_powerpc_icecube__)
#  include <powerpc/icecube/libcpu/mmu.h>
#elif defined(__rtems_powerpc_mbx821_001__)
#  include <powerpc/mbx821_001/libcpu/mmu.h>
#elif defined(__rtems_powerpc_mbx821_002__)
#  include <powerpc/mbx821_002/libcpu/mmu.h>
#elif defined(__rtems_powerpc_mbx821_002b__)
#  include <powerpc/mbx821_002b/libcpu/mmu.h>
#elif defined(__rtems_powerpc_mbx860_001b__)
#  include <powerpc/mbx860_001b/libcpu/mmu.h>
#elif defined(__rtems_powerpc_mbx860_002__)
#  include <powerpc/mbx860_002/libcpu/mmu.h>
#elif defined(__rtems_powerpc_mbx860_005b__)
#  include <powerpc/mbx860_005b/libcpu/mmu.h>
#elif defined(__rtems_powerpc_mbx860_1b__)
#  include <powerpc/mbx860_1b/libcpu/mmu.h>
#elif defined(__rtems_powerpc_mcp750__)
#  include <powerpc/mcp750/libcpu/mmu.h>
#elif defined(__rtems_powerpc_mpc5566evb__)
#  include <powerpc/mpc5566evb/libcpu/mmu.h>
#elif defined(__rtems_powerpc_mpc5566evb_spe__)
#  include <powerpc/mpc5566evb_spe/libcpu/mmu.h>
#elif defined(__rtems_powerpc_mpc5643l_dpu__)
#  include <powerpc/mpc5643l_dpu/libcpu/mmu.h>
#elif defined(__rtems_powerpc_mpc5643l_evb__)
#  include <powerpc/mpc5643l_evb/libcpu/mmu.h>
#elif defined(__rtems_powerpc_mpc5668g__)
#  include <powerpc/mpc5668g/libcpu/mmu.h>
#elif defined(__rtems_powerpc_mpc5674f_ecu508_app__)
#  include <powerpc/mpc5674f_ecu508_app/libcpu/mmu.h>
#elif defined(__rtems_powerpc_mpc5674f_ecu508_boot__)
#  include <powerpc/mpc5674f_ecu508_boot/libcpu/mmu.h>
#elif defined(__rtems_powerpc_mpc5674f_rsm6__)
#  include <powerpc/mpc5674f_rsm6/libcpu/mmu.h>
#elif defined(__rtems_powerpc_mpc5674fevb__)
#  include <powerpc/mpc5674fevb/libcpu/mmu.h>
#elif defined(__rtems_powerpc_mpc5674fevb_spe__)
#  include <powerpc/mpc5674fevb_spe/libcpu/mmu.h>
#elif defined(__rtems_powerpc_mpc8260ads__)
#  include <powerpc/mpc8260ads/libcpu/mmu.h>
#elif defined(__rtems_powerpc_mpc8309som__)
#  include <powerpc/mpc8309som/libcpu/mmu.h>
#elif defined(__rtems_powerpc_mpc8313erdb__)
#  include <powerpc/mpc8313erdb/libcpu/mmu.h>
#elif defined(__rtems_powerpc_mpc8349eamds__)
#  include <powerpc/mpc8349eamds/libcpu/mmu.h>
#elif defined(__rtems_powerpc_mtx603e__)
#  include <powerpc/mtx603e/libcpu/mmu.h>
#elif defined(__rtems_powerpc_mvme2100__)
#  include <powerpc/mvme2100/libcpu/mmu.h>
#elif defined(__rtems_powerpc_mvme2307__)
#  include <powerpc/mvme2307/libcpu/mmu.h>
#elif defined(__rtems_powerpc_mvme3100__)
#  include <powerpc/mvme3100/libcpu/mmu.h>
#elif defined(__rtems_powerpc_mvme5500__)
#  include <powerpc/mvme5500/libcpu/mmu.h>
#elif defined(__rtems_powerpc_pghplus__)
#  include <powerpc/pghplus/libcpu/mmu.h>
#elif defined(__rtems_powerpc_phycore_mpc5554__)
#  include <powerpc/phycore_mpc5554/libcpu/mmu.h>
#elif defined(__rtems_powerpc_pm520_cr825__)
#  include <powerpc/pm520_cr825/libcpu/mmu.h>
#elif defined(__rtems_powerpc_pm520_ze30__)
#  include <powerpc/pm520_ze30/libcpu/mmu.h>
#elif defined(__rtems_powerpc_psim__)
#  include <powerpc/psim/libcpu/mmu.h>
#elif defined(__rtems_powerpc_qemuppc__)
#  include <powerpc/qemuppc/libcpu/mmu.h>
#elif defined(__rtems_powerpc_qemuprep__)
#  include <powerpc/qemuprep/libcpu/mmu.h>
#elif defined(__rtems_powerpc_qemuprep_altivec__)
#  include <powerpc/qemuprep-altivec/libcpu/mmu.h>
#elif defined(__rtems_powerpc_qoriq_core_0__)
#  include <powerpc/qoriq_core_0/libcpu/mmu.h>
#elif defined(__rtems_powerpc_qoriq_core_1__)
#  include <powerpc/qoriq_core_1/libcpu/mmu.h>
#elif defined(__rtems_powerpc_qoriq_p1020rdb__)
#  include <powerpc/qoriq_p1020rdb/libcpu/mmu.h>
#elif defined(__rtems_powerpc_score603e__)
#  include <powerpc/score603e/libcpu/mmu.h>
#elif defined(__rtems_powerpc_ss555__)
#  include <powerpc/ss555/libcpu/mmu.h>
#elif defined(__rtems_powerpc_t32mppc__)
#  include <powerpc/t32mppc/libcpu/mmu.h>
#elif defined(__rtems_powerpc_tqm8xx_stk8xx__)
#  include <powerpc/tqm8xx_stk8xx/libcpu/mmu.h>
#elif defined(__rtems_powerpc_virtex__)
#  include <powerpc/virtex/libcpu/mmu.h>
#elif defined(__rtems_powerpc_virtex4__)
#  include <powerpc/virtex4/libcpu/mmu.h>
#elif defined(__rtems_powerpc_virtex5__)
#  include <powerpc/virtex5/libcpu/mmu.h>
#else
#  error "__rtems_<arch>_<bsp>__ must be defined, for example: __rtems_sparc_erc32__"
#endif
