#if defined(HEADER_WARNING)
#warning "This header should not be included directly."
#endif


#if defined(__rtems_i386_pc386__)
#  include <i386/pc386/libcpu/byteorder.h>
#elif defined(__rtems_i386_pc486__)
#  include <i386/pc486/libcpu/byteorder.h>
#elif defined(__rtems_i386_pc586__)
#  include <i386/pc586/libcpu/byteorder.h>
#elif defined(__rtems_i386_pc586_sse__)
#  include <i386/pc586-sse/libcpu/byteorder.h>
#elif defined(__rtems_i386_pc686__)
#  include <i386/pc686/libcpu/byteorder.h>
#elif defined(__rtems_i386_pcp4__)
#  include <i386/pcp4/libcpu/byteorder.h>
#elif defined(__rtems_powerpc_beatnik__)
#  include <powerpc/beatnik/libcpu/byteorder.h>
#elif defined(__rtems_powerpc_br_uid__)
#  include <powerpc/br_uid/libcpu/byteorder.h>
#elif defined(__rtems_powerpc_brs5l__)
#  include <powerpc/brs5l/libcpu/byteorder.h>
#elif defined(__rtems_powerpc_brs6l__)
#  include <powerpc/brs6l/libcpu/byteorder.h>
#elif defined(__rtems_powerpc_dp2__)
#  include <powerpc/dp2/libcpu/byteorder.h>
#elif defined(__rtems_powerpc_ep1a__)
#  include <powerpc/ep1a/libcpu/byteorder.h>
#elif defined(__rtems_powerpc_gwlcfm__)
#  include <powerpc/gwlcfm/libcpu/byteorder.h>
#elif defined(__rtems_powerpc_haleakala__)
#  include <powerpc/haleakala/libcpu/byteorder.h>
#elif defined(__rtems_powerpc_hsc_cm01__)
#  include <powerpc/hsc_cm01/libcpu/byteorder.h>
#elif defined(__rtems_powerpc_icecube__)
#  include <powerpc/icecube/libcpu/byteorder.h>
#elif defined(__rtems_powerpc_mbx821_001__)
#  include <powerpc/mbx821_001/libcpu/byteorder.h>
#elif defined(__rtems_powerpc_mbx821_002__)
#  include <powerpc/mbx821_002/libcpu/byteorder.h>
#elif defined(__rtems_powerpc_mbx821_002b__)
#  include <powerpc/mbx821_002b/libcpu/byteorder.h>
#elif defined(__rtems_powerpc_mbx860_001b__)
#  include <powerpc/mbx860_001b/libcpu/byteorder.h>
#elif defined(__rtems_powerpc_mbx860_002__)
#  include <powerpc/mbx860_002/libcpu/byteorder.h>
#elif defined(__rtems_powerpc_mbx860_005b__)
#  include <powerpc/mbx860_005b/libcpu/byteorder.h>
#elif defined(__rtems_powerpc_mbx860_1b__)
#  include <powerpc/mbx860_1b/libcpu/byteorder.h>
#elif defined(__rtems_powerpc_mcp750__)
#  include <powerpc/mcp750/libcpu/byteorder.h>
#elif defined(__rtems_powerpc_mpc5566evb__)
#  include <powerpc/mpc5566evb/libcpu/byteorder.h>
#elif defined(__rtems_powerpc_mpc5566evb_spe__)
#  include <powerpc/mpc5566evb_spe/libcpu/byteorder.h>
#elif defined(__rtems_powerpc_mpc5643l_dpu__)
#  include <powerpc/mpc5643l_dpu/libcpu/byteorder.h>
#elif defined(__rtems_powerpc_mpc5643l_evb__)
#  include <powerpc/mpc5643l_evb/libcpu/byteorder.h>
#elif defined(__rtems_powerpc_mpc5668g__)
#  include <powerpc/mpc5668g/libcpu/byteorder.h>
#elif defined(__rtems_powerpc_mpc5674f_ecu508_app__)
#  include <powerpc/mpc5674f_ecu508_app/libcpu/byteorder.h>
#elif defined(__rtems_powerpc_mpc5674f_ecu508_boot__)
#  include <powerpc/mpc5674f_ecu508_boot/libcpu/byteorder.h>
#elif defined(__rtems_powerpc_mpc5674f_rsm6__)
#  include <powerpc/mpc5674f_rsm6/libcpu/byteorder.h>
#elif defined(__rtems_powerpc_mpc5674fevb__)
#  include <powerpc/mpc5674fevb/libcpu/byteorder.h>
#elif defined(__rtems_powerpc_mpc5674fevb_spe__)
#  include <powerpc/mpc5674fevb_spe/libcpu/byteorder.h>
#elif defined(__rtems_powerpc_mpc8260ads__)
#  include <powerpc/mpc8260ads/libcpu/byteorder.h>
#elif defined(__rtems_powerpc_mpc8309som__)
#  include <powerpc/mpc8309som/libcpu/byteorder.h>
#elif defined(__rtems_powerpc_mpc8313erdb__)
#  include <powerpc/mpc8313erdb/libcpu/byteorder.h>
#elif defined(__rtems_powerpc_mpc8349eamds__)
#  include <powerpc/mpc8349eamds/libcpu/byteorder.h>
#elif defined(__rtems_powerpc_mtx603e__)
#  include <powerpc/mtx603e/libcpu/byteorder.h>
#elif defined(__rtems_powerpc_mvme2100__)
#  include <powerpc/mvme2100/libcpu/byteorder.h>
#elif defined(__rtems_powerpc_mvme2307__)
#  include <powerpc/mvme2307/libcpu/byteorder.h>
#elif defined(__rtems_powerpc_mvme3100__)
#  include <powerpc/mvme3100/libcpu/byteorder.h>
#elif defined(__rtems_powerpc_mvme5500__)
#  include <powerpc/mvme5500/libcpu/byteorder.h>
#elif defined(__rtems_powerpc_pghplus__)
#  include <powerpc/pghplus/libcpu/byteorder.h>
#elif defined(__rtems_powerpc_phycore_mpc5554__)
#  include <powerpc/phycore_mpc5554/libcpu/byteorder.h>
#elif defined(__rtems_powerpc_pm520_cr825__)
#  include <powerpc/pm520_cr825/libcpu/byteorder.h>
#elif defined(__rtems_powerpc_pm520_ze30__)
#  include <powerpc/pm520_ze30/libcpu/byteorder.h>
#elif defined(__rtems_powerpc_psim__)
#  include <powerpc/psim/libcpu/byteorder.h>
#elif defined(__rtems_powerpc_qemuppc__)
#  include <powerpc/qemuppc/libcpu/byteorder.h>
#elif defined(__rtems_powerpc_qemuprep__)
#  include <powerpc/qemuprep/libcpu/byteorder.h>
#elif defined(__rtems_powerpc_qemuprep_altivec__)
#  include <powerpc/qemuprep-altivec/libcpu/byteorder.h>
#elif defined(__rtems_powerpc_qoriq_core_0__)
#  include <powerpc/qoriq_core_0/libcpu/byteorder.h>
#elif defined(__rtems_powerpc_qoriq_core_1__)
#  include <powerpc/qoriq_core_1/libcpu/byteorder.h>
#elif defined(__rtems_powerpc_qoriq_p1020rdb__)
#  include <powerpc/qoriq_p1020rdb/libcpu/byteorder.h>
#elif defined(__rtems_powerpc_score603e__)
#  include <powerpc/score603e/libcpu/byteorder.h>
#elif defined(__rtems_powerpc_ss555__)
#  include <powerpc/ss555/libcpu/byteorder.h>
#elif defined(__rtems_powerpc_t32mppc__)
#  include <powerpc/t32mppc/libcpu/byteorder.h>
#elif defined(__rtems_powerpc_tqm8xx_stk8xx__)
#  include <powerpc/tqm8xx_stk8xx/libcpu/byteorder.h>
#elif defined(__rtems_powerpc_virtex__)
#  include <powerpc/virtex/libcpu/byteorder.h>
#elif defined(__rtems_powerpc_virtex4__)
#  include <powerpc/virtex4/libcpu/byteorder.h>
#elif defined(__rtems_powerpc_virtex5__)
#  include <powerpc/virtex5/libcpu/byteorder.h>
#elif defined(__rtems_sparc_erc32__)
#  include <sparc/erc32/libcpu/byteorder.h>
#elif defined(__rtems_sparc_leon2__)
#  include <sparc/leon2/libcpu/byteorder.h>
#elif defined(__rtems_sparc_leon3__)
#  include <sparc/leon3/libcpu/byteorder.h>
#elif defined(__rtems_sparc_ngmp__)
#  include <sparc/ngmp/libcpu/byteorder.h>
#elif defined(__rtems_sparc_sis__)
#  include <sparc/sis/libcpu/byteorder.h>
#else
#  error "__rtems_<arch>_<bsp>__ must be defined, for example: __rtems_sparc_erc32__"
#endif
