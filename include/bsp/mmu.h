#if defined(HEADER_WARNING)
#warning "This header should not be included directly."
#endif


#if defined(__rtems_arm_lpc32xx_mzx__)
#  include <arm/lpc32xx_mzx/bsp/mmu.h>
#elif defined(__rtems_arm_lpc32xx_mzx_stage_1__)
#  include <arm/lpc32xx_mzx_stage_1/bsp/mmu.h>
#elif defined(__rtems_arm_lpc32xx_mzx_stage_2__)
#  include <arm/lpc32xx_mzx_stage_2/bsp/mmu.h>
#elif defined(__rtems_arm_lpc32xx_phycore__)
#  include <arm/lpc32xx_phycore/bsp/mmu.h>
#elif defined(__rtems_arm_raspberrypi__)
#  include <arm/raspberrypi/bsp/mmu.h>
#elif defined(__rtems_powerpc_qoriq_core_0__)
#  include <powerpc/qoriq_core_0/bsp/mmu.h>
#elif defined(__rtems_powerpc_qoriq_core_1__)
#  include <powerpc/qoriq_core_1/bsp/mmu.h>
#elif defined(__rtems_powerpc_qoriq_p1020rdb__)
#  include <powerpc/qoriq_p1020rdb/bsp/mmu.h>
#elif defined(__rtems_powerpc_virtex4__)
#  include <powerpc/virtex4/bsp/mmu.h>
#elif defined(__rtems_powerpc_virtex5__)
#  include <powerpc/virtex5/bsp/mmu.h>
#else
#  error "__rtems_<arch>_<bsp>__ must be defined, for example: __rtems_sparc_erc32__"
#endif
