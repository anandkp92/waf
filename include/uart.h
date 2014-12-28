#if defined(HEADER_WARNING)
#warning "This header should not be included directly."
#endif


#if defined(__rtems_arm_edb7312__)
#  include <arm/edb7312/uart.h>
#elif defined(__rtems_arm_rtl22xx__)
#  include <arm/rtl22xx/uart.h>
#elif defined(__rtems_arm_rtl22xx_t__)
#  include <arm/rtl22xx_t/uart.h>
#elif defined(__rtems_i386_pc386__)
#  include <i386/pc386/uart.h>
#elif defined(__rtems_i386_pc486__)
#  include <i386/pc486/uart.h>
#elif defined(__rtems_i386_pc586__)
#  include <i386/pc586/uart.h>
#elif defined(__rtems_i386_pc586_sse__)
#  include <i386/pc586-sse/uart.h>
#elif defined(__rtems_i386_pc686__)
#  include <i386/pc686/uart.h>
#elif defined(__rtems_i386_pcp4__)
#  include <i386/pcp4/uart.h>
#else
#  error "__rtems_<arch>_<bsp>__ must be defined, for example: __rtems_sparc_erc32__"
#endif
