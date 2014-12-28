#if defined(HEADER_WARNING)
#warning "This header should not be included directly."
#endif


#if defined(__rtems_powerpc_beatnik__)
#  include <powerpc/beatnik/bsp/gtpcireg.h>
#elif defined(__rtems_powerpc_mvme5500__)
#  include <powerpc/mvme5500/bsp/gtpcireg.h>
#else
#  error "__rtems_<arch>_<bsp>__ must be defined, for example: __rtems_sparc_erc32__"
#endif
