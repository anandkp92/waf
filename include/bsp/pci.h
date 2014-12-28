#if defined(HEADER_WARNING)
#warning "This header should not be included directly."
#endif


#if defined(__rtems_mips_malta__)
#  include <mips/malta/bsp/pci.h>
#elif defined(__rtems_powerpc_beatnik__)
#  include <powerpc/beatnik/bsp/pci.h>
#elif defined(__rtems_powerpc_ep1a__)
#  include <powerpc/ep1a/bsp/pci.h>
#elif defined(__rtems_powerpc_mcp750__)
#  include <powerpc/mcp750/bsp/pci.h>
#elif defined(__rtems_powerpc_mtx603e__)
#  include <powerpc/mtx603e/bsp/pci.h>
#elif defined(__rtems_powerpc_mvme2100__)
#  include <powerpc/mvme2100/bsp/pci.h>
#elif defined(__rtems_powerpc_mvme2307__)
#  include <powerpc/mvme2307/bsp/pci.h>
#elif defined(__rtems_powerpc_mvme3100__)
#  include <powerpc/mvme3100/bsp/pci.h>
#elif defined(__rtems_powerpc_mvme5500__)
#  include <powerpc/mvme5500/bsp/pci.h>
#elif defined(__rtems_powerpc_qemuprep__)
#  include <powerpc/qemuprep/bsp/pci.h>
#elif defined(__rtems_powerpc_qemuprep_altivec__)
#  include <powerpc/qemuprep-altivec/bsp/pci.h>
#elif defined(__rtems_powerpc_score603e__)
#  include <powerpc/score603e/bsp/pci.h>
#else
#  error "__rtems_<arch>_<bsp>__ must be defined, for example: __rtems_sparc_erc32__"
#endif
