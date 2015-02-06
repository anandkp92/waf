#if defined(HEADER_WARNING)
#warning "This header should not be included directly."
#endif


#if defined(__rtems_bfin_TLL6527M__)
#  include <bfin/TLL6527M/cplb.h>
#elif defined(__rtems_bfin_eZKit533__)
#  include <bfin/eZKit533/cplb.h>
#else
#  error "__rtems_<arch>_<bsp>__ must be defined, for example: __rtems_sparc_erc32__"
#endif
