#if defined(HEADER_WARNING)
#warning "This header should not be included directly."
#endif


#if defined(__rtems_mips_csb350__)
#  include <mips/csb350/bsp/regs.h>
#elif defined(__rtems_mips_genmongoosev__)
#  include <mips/genmongoosev/bsp/regs.h>
#elif defined(__rtems_mips_hurricane__)
#  include <mips/hurricane/bsp/regs.h>
#elif defined(__rtems_mips_jmr3904__)
#  include <mips/jmr3904/bsp/regs.h>
#elif defined(__rtems_mips_malta__)
#  include <mips/malta/bsp/regs.h>
#elif defined(__rtems_mips_rbtx4925__)
#  include <mips/rbtx4925/bsp/regs.h>
#elif defined(__rtems_mips_rbtx4938__)
#  include <mips/rbtx4938/bsp/regs.h>
#else
#  error "__rtems_<arch>_<bsp>__ must be defined, for example: __rtems_sparc_erc32__"
#endif
