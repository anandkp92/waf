#if defined(HEADER_WARNING)
#warning "This header should not be included directly."
#endif


#if defined(__rtems_powerpc_br_uid__)
#  include <powerpc/br_uid/bsp/u-boot-config.h>
#elif defined(__rtems_powerpc_brs5l__)
#  include <powerpc/brs5l/bsp/u-boot-config.h>
#elif defined(__rtems_powerpc_brs6l__)
#  include <powerpc/brs6l/bsp/u-boot-config.h>
#elif defined(__rtems_powerpc_dp2__)
#  include <powerpc/dp2/bsp/u-boot-config.h>
#elif defined(__rtems_powerpc_hsc_cm01__)
#  include <powerpc/hsc_cm01/bsp/u-boot-config.h>
#elif defined(__rtems_powerpc_icecube__)
#  include <powerpc/icecube/bsp/u-boot-config.h>
#elif defined(__rtems_powerpc_mpc8309som__)
#  include <powerpc/mpc8309som/bsp/u-boot-config.h>
#elif defined(__rtems_powerpc_mpc8313erdb__)
#  include <powerpc/mpc8313erdb/bsp/u-boot-config.h>
#elif defined(__rtems_powerpc_mpc8349eamds__)
#  include <powerpc/mpc8349eamds/bsp/u-boot-config.h>
#elif defined(__rtems_powerpc_pm520_cr825__)
#  include <powerpc/pm520_cr825/bsp/u-boot-config.h>
#elif defined(__rtems_powerpc_pm520_ze30__)
#  include <powerpc/pm520_ze30/bsp/u-boot-config.h>
#elif defined(__rtems_powerpc_qoriq_core_0__)
#  include <powerpc/qoriq_core_0/bsp/u-boot-config.h>
#elif defined(__rtems_powerpc_qoriq_core_1__)
#  include <powerpc/qoriq_core_1/bsp/u-boot-config.h>
#elif defined(__rtems_powerpc_qoriq_p1020rdb__)
#  include <powerpc/qoriq_p1020rdb/bsp/u-boot-config.h>
#else
#  error "__rtems_<arch>_<bsp>__ must be defined, for example: __rtems_sparc_erc32__"
#endif
