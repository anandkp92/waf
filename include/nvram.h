#if defined(HEADER_WARNING)
#warning "This header should not be included directly."
#endif


#if defined(__rtems_m68k_mcf5206elite__)
#  include <m68k/mcf5206elite/nvram.h>
#elif defined(__rtems_powerpc_mcp750__)
#  include <powerpc/mcp750/nvram.h>
#elif defined(__rtems_powerpc_mtx603e__)
#  include <powerpc/mtx603e/nvram.h>
#elif defined(__rtems_powerpc_mvme2100__)
#  include <powerpc/mvme2100/nvram.h>
#elif defined(__rtems_powerpc_mvme2307__)
#  include <powerpc/mvme2307/nvram.h>
#elif defined(__rtems_powerpc_qemuprep__)
#  include <powerpc/qemuprep/nvram.h>
#elif defined(__rtems_powerpc_qemuprep_altivec__)
#  include <powerpc/qemuprep-altivec/nvram.h>
#else
#  error "__rtems_<arch>_<bsp>__ must be defined, for example: __rtems_sparc_erc32__"
#endif
