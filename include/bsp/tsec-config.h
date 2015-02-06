#if defined(HEADER_WARNING)
#warning "This header should not be included directly."
#endif


#if defined(__rtems_powerpc_br_uid__)
#  include <powerpc/br_uid/bsp/tsec-config.h>
#elif defined(__rtems_powerpc_hsc_cm01__)
#  include <powerpc/hsc_cm01/bsp/tsec-config.h>
#elif defined(__rtems_powerpc_mpc8309som__)
#  include <powerpc/mpc8309som/bsp/tsec-config.h>
#elif defined(__rtems_powerpc_mpc8313erdb__)
#  include <powerpc/mpc8313erdb/bsp/tsec-config.h>
#elif defined(__rtems_powerpc_mpc8349eamds__)
#  include <powerpc/mpc8349eamds/bsp/tsec-config.h>
#elif defined(__rtems_powerpc_qoriq_core_0__)
#  include <powerpc/qoriq_core_0/bsp/tsec-config.h>
#elif defined(__rtems_powerpc_qoriq_core_1__)
#  include <powerpc/qoriq_core_1/bsp/tsec-config.h>
#elif defined(__rtems_powerpc_qoriq_p1020rdb__)
#  include <powerpc/qoriq_p1020rdb/bsp/tsec-config.h>
#else
#  error "__rtems_<arch>_<bsp>__ must be defined, for example: __rtems_sparc_erc32__"
#endif
