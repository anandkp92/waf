#if defined(HEADER_WARNING)
#warning "This header should not be included directly."
#endif


#if defined(__rtems_lm32_lm32_evr__)
#  include <lm32/lm32_evr/system_conf.h>
#elif defined(__rtems_lm32_milkymist__)
#  include <lm32/milkymist/system_conf.h>
#else
#  error "__rtems_<arch>_<bsp>__ must be defined, for example: __rtems_sparc_erc32__"
#endif
