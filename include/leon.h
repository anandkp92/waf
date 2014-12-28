#if defined(HEADER_WARNING)
#warning "This header should not be included directly."
#endif


#if defined(__rtems_sparc_leon2__)
#  include <sparc/leon2/leon.h>
#elif defined(__rtems_sparc_leon3__)
#  include <sparc/leon3/leon.h>
#elif defined(__rtems_sparc_ngmp__)
#  include <sparc/ngmp/leon.h>
#else
#  error "__rtems_<arch>_<bsp>__ must be defined, for example: __rtems_sparc_erc32__"
#endif
