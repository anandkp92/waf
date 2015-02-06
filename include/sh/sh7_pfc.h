#if defined(HEADER_WARNING)
#warning "This header should not be included directly."
#endif


#if defined(__rtems_sh_gensh1__)
#  include <sh/gensh1/sh/sh7_pfc.h>
#elif defined(__rtems_sh_gensh2__)
#  include <sh/gensh2/sh/sh7_pfc.h>
#else
#  error "__rtems_<arch>_<bsp>__ must be defined, for example: __rtems_sparc_erc32__"
#endif
