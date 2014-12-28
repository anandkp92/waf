#if defined(HEADER_WARNING)
#warning "This header should not be included directly."
#endif


#if defined(__rtems_arm_raspberrypi__)
#  include <arm/raspberrypi/bsp/usart.h>
#elif defined(__rtems_arm_stm32f105rc__)
#  include <arm/stm32f105rc/bsp/usart.h>
#elif defined(__rtems_arm_stm32f4__)
#  include <arm/stm32f4/bsp/usart.h>
#else
#  error "__rtems_<arch>_<bsp>__ must be defined, for example: __rtems_sparc_erc32__"
#endif
