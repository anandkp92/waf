list_bsp = {
	"arm": [
		"arm1136jfs",
		"arm1136js",
		"arm7tdmi",
		"arm920",
		"armcortexa9",
		"csb336",
		"csb337",
		"csb637",
		"edb7312",
		"gba",
		"gp32",
		"gumstix",
		"kit637_v6",
		"lm3s3749",
		"lm3s6965",
		"lm3s6965_qemu",
		"lpc17xx_ea_ram",
		"lpc17xx_ea_rom_int",
		"lpc17xx_plx800_ram",
		"lpc17xx_plx800_rom_int",
		"lpc2362",
		"lpc23xx_tli800",
		"lpc24xx_ea",
		"lpc24xx_ncs_ram",
		"lpc24xx_ncs_rom_ext",
		"lpc24xx_ncs_rom_int",
		"lpc24xx_plx800_ram",
		"lpc24xx_plx800_rom_int",
		"lpc32xx_mzx",
		"lpc32xx_mzx_stage_1",
		"lpc32xx_mzx_stage_2",
		"lpc32xx_phycore",
		"nds",
		"raspberrypi",
		"realview_pbx_a9_qemu",
		"rtl22xx",
		"rtl22xx_t",
		"smdk2410",
		"stm32f4",
		"xilinx_zynq_a9_qemu",
	],

	"avr": [
		"avrtest",
	],

	"bfin": [
		"bf537stamp",
		"ezkit533",
		"tll6527m",
	],

	"h8300": [
		"h8sim",
		"h8sxsim",
	],

	"i386": [
		"pc386",
		"pc486",
		"pc586",
		"pc586-sse",
		"pc686",
		"pcp4",
	],

	"lm32": [
		"lm32_evr",
		"milkymist",
	],

	"m32c": [
		"m32csim",
	],

	"m32r": [
		"m32rsim",
	],

	"m68k": [
		"av5282",
		"cobra5475",
		"csb360",
		"gen68302",
		"gen68340",
		"gen68360",
		"gen68360_040",
		"idp",
		"m5484fireengine",
		"mcf5206elite",
		"mcf52235",
		"mcf5225x",
		"mcf5235",
		"mcf5329",
		"mrm332",
		"mvme136",
		"mvme147",
		"mvme147s",
		"mvme162",
		"mvme162lx",
		"mvme167",
		"ods68302",
		"pgh360",
		"sim68000",
		"simcpu32",
		"uc5282",
	],

	"mips": [
		"csb350",
		"genmongoosev",
		"hurricane",
		"jmr3904",
		"malta",
		"rbtx4925",
		"rbtx4938",
	],

	"moxie": [
		"moxiesim",
	],

	"nios2": [
		"nios2_iss",
	],

	"powerpc": [
		"beatnik",
		"br_uid",
		"brs5l",
		"brs6l",
		"dp2",
		"ep1a",
		"gwlcfm",
		"haleakala",
		"hsc_cm01",
		"icecube",
		"mbx821_001",
		"mbx821_002",
		"mbx821_002b",
		"mbx860_001b",
		"mbx860_002",
		"mbx860_005b",
		"mbx860_1b",
		"mcp750",
		"mpc5566evb",
		"mpc5566evb_spe",
		"mpc5643l_dpu",
		"mpc5643l_evb",
		"mpc5674f_ecu508_app",
		"mpc5674f_ecu508_boot",
		"mpc5674f_rsm6",
		"mpc5674fevb",
		"mpc5674fevb_spe",
		"mpc8260ads",
		"mpc8309som",
		"mpc8313erdb",
		"mpc8349eamds",
		"mtx603e",
		"mvme2100",
		"mvme2307",
		"mvme3100",
		"mvme5500",
		"pghplus",
		"phycore_mpc5554",
		"pm520_cr825",
		"pm520_ze30",
		"psim",
		"qemuppc",
		"qemuprep",
		"qemuprep-altivec",
		"qoriq_core_0",
		"qoriq_core_1",
		"qoriq_p1020rdb",
		"score603e",
		"ss555",
		"t32mppc",
		"tqm8xx_stk8xx",
		"virtex",
		"virtex4",
		"virtex5",
	],

	"sh": [
		"gensh1",
		"gensh2",
		"gensh4",
		"simsh1",
		"simsh2",
		"simsh2e",
		"simsh4",
	],

	"sparc": [
		"erc32",
		"leon2",
		"leon3",
		"sis",
	],

	"sparc64": [
		"niagara",
		"usiii",
	],

	"v850": [
		"v850e1sim",
		"v850e2sim",
		"v850e2v3sim",
		"v850esim",
		"v850essim",
		"v850sim",
	]
}



"""
list_bsp = {
	"arm": [
		"lm3s3749",
		"lm3s6965",
		"lm3s6965_qemu",
		"lpc17xx_ea_ram",
		"lpc17xx_ea_rom_int",
		"lpc17xx_plx800_ram",
		"lpc17xx_plx800_rom_int",
		"lpc24xx_plx800_ram",
		"lpc24xx_plx800_rom_int",
		"raspberrypi",
		"realview_pbx_a9_qemu",
		"stm32f4",
		"xilinx_zynq_a9_qemu",
	],

	"i386": [
		"pcp4",
	],

	"mips": [
		"malta",
	],

	"moxie": [
		"moxiesim",
	],

	"nios2": [
		"nios2_iss",
	],

	"powerpc": [
		"br_uid",
		"brs6l",
		"mpc5566evb_spe",
		"mpc5643l_dpu",
		"mpc5643l_evb",
		"mpc5674f_ecu508_app",
		"mpc5674f_ecu508_boot",
		"mpc5674f_rsm6",
		"mpc5674fevb",
		"mpc5674fevb_spe",
		"mpc8309som",
		"phycore_mpc5554",
		"qemuprep",
		"qemuprep-altivec",
		"qoriq_core_0",
		"qoriq_core_1",
		"qoriq_p1020rdb",
		"t32mppc",
		"virtex4",
		"virtex5",
	],

	"v850": [
		"v850e1sim",
		"v850e2sim",
		"v850e2v3sim",
		"v850esim",
		"v850essim",
		"v850sim",
	]
}
"""

#for arch in sorted(list_bsp):
#	for bsp in sorted(list_bsp[arch]):
#		print "%s/%s" % (arch, bsp)
