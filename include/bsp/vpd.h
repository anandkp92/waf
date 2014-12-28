#if defined(HEADER_WARNING)
#warning "This header should not be included directly."
#endif


#if defined(__rtems_powerpc_beatnik__)
#  include <powerpc/beatnik/bsp/vpd.h>
#elif defined(__rtems_powerpc_mvme3100__)
#  include <powerpc/mvme3100/bsp/vpd.h>
#else
#  error "__rtems_<arch>_<bsp>__ must be defined, for example: __rtems_sparc_erc32__"
#endif
