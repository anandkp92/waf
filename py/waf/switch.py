def options(ctx):
	ctx.load('compiler_c')
	ctx.load('compiler_cxx')

	ctx.add_option('--enable-tests', action='store_true', default=False, help='Enable tests (TEMP OPTION!)')

	grp = ctx.add_option_group("config (configuration file) options")
	grp.add_option('--bsp', dest='bsps', help="Command seperated list of BSPs to build.", type='string')
	grp.add_option('--list', action='store_true', default=False, help='List available BSPs.')
	grp.add_option('--prefix', dest='prefix', help="Install prefix.", type='string')
	grp.add_option('--path-tools', dest='path_tools', help="Directory for RTEMS tools.", type='string')
	grp.add_option('--force', action='store_true', default=False, help='Force overwriting config.cfg.')

	grp = ctx.add_option_group("docs documentation options")
	grp.add_option('--out', dest='file_out', default="options.html", help="Output file (default: %default)", type='string')
	grp.add_option('--html', action='store_true', default=True, help='Generate HTML documentation. (default: yes)')
	grp.add_option('--txt', action='store_true', default=True, help='Generate Text documentation. (default: no)')

	grp = ctx.add_option_group("developer options")
	grp.add_option('--build-config', action='store_true', default=False, help="Write build configuration. (default: no)")
	grp.add_option('--build-json', action='store_true', default=False, help="Write JSON build log.. (default: no)")
