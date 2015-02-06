#if defined(HEADER_WARNING)
#warning "This header should not be included directly."
#endif


#if defined(__rtems_m68k_mvme162__)
#  include <m68k/mvme162/page_table.h>
#elif defined(__rtems_m68k_mvme162lx__)
#  include <m68k/mvme162lx/page_table.h>
#elif defined(__rtems_m68k_mvme167__)
#  include <m68k/mvme167/page_table.h>
#else
#  error "__rtems_<arch>_<bsp>__ must be defined, for example: __rtems_sparc_erc32__"
#endif
