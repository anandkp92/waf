#if defined(HEADER_WARNING)
#warning "This header should not be included directly."
#endif


#if defined(__rtems_powerpc_mbx821_001__)
#  include <powerpc/mbx821_001/bsp/8xx_immap.h>
#elif defined(__rtems_powerpc_mbx821_002__)
#  include <powerpc/mbx821_002/bsp/8xx_immap.h>
#elif defined(__rtems_powerpc_mbx821_002b__)
#  include <powerpc/mbx821_002b/bsp/8xx_immap.h>
#elif defined(__rtems_powerpc_mbx860_001b__)
#  include <powerpc/mbx860_001b/bsp/8xx_immap.h>
#elif defined(__rtems_powerpc_mbx860_002__)
#  include <powerpc/mbx860_002/bsp/8xx_immap.h>
#elif defined(__rtems_powerpc_mbx860_005b__)
#  include <powerpc/mbx860_005b/bsp/8xx_immap.h>
#elif defined(__rtems_powerpc_mbx860_1b__)
#  include <powerpc/mbx860_1b/bsp/8xx_immap.h>
#elif defined(__rtems_powerpc_pghplus__)
#  include <powerpc/pghplus/bsp/8xx_immap.h>
#elif defined(__rtems_powerpc_tqm8xx_stk8xx__)
#  include <powerpc/tqm8xx_stk8xx/bsp/8xx_immap.h>
#else
#  error "__rtems_<arch>_<bsp>__ must be defined, for example: __rtems_sparc_erc32__"
#endif
