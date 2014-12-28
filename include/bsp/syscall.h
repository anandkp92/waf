#if defined(HEADER_WARNING)
#warning "This header should not be included directly."
#endif


#if defined(__rtems_sh_simsh1__)
#  include <sh/simsh1/bsp/syscall.h>
#elif defined(__rtems_sh_simsh2__)
#  include <sh/simsh2/bsp/syscall.h>
#elif defined(__rtems_sh_simsh2e__)
#  include <sh/simsh2e/bsp/syscall.h>
#elif defined(__rtems_sh_simsh4__)
#  include <sh/simsh4/bsp/syscall.h>
#elif defined(__rtems_v850_v850e1sim__)
#  include <v850/v850e1sim/bsp/syscall.h>
#elif defined(__rtems_v850_v850e2sim__)
#  include <v850/v850e2sim/bsp/syscall.h>
#elif defined(__rtems_v850_v850e2v3sim__)
#  include <v850/v850e2v3sim/bsp/syscall.h>
#elif defined(__rtems_v850_v850esim__)
#  include <v850/v850esim/bsp/syscall.h>
#elif defined(__rtems_v850_v850essim__)
#  include <v850/v850essim/bsp/syscall.h>
#elif defined(__rtems_v850_v850sim__)
#  include <v850/v850sim/bsp/syscall.h>
#else
#  error "__rtems_<arch>_<bsp>__ must be defined, for example: __rtems_sparc_erc32__"
#endif
