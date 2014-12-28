#if defined(HEADER_WARNING)
#warning "This header should not be included directly."
#endif


#if defined(__rtems_sh_gensh1__)
#  include <sh/gensh1/sh/sci.h>
#elif defined(__rtems_sh_gensh2__)
#  include <sh/gensh2/sh/sci.h>
#else
#  error "__rtems_<arch>_<bsp>__ must be defined, for example: __rtems_sparc_erc32__"
#endif
