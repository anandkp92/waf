from bsp import list_bsp
from py.config.base import config_list


def header():
	return """
<html>
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=us-ascii">

  <title>List of RTEMS BSP Options</title>
  <meta name="Description" content="List of options for RTEMS BSPs">
  <meta name="Keywords" content="RTEMS, BSP, sparc, intel, mips"/>
  <meta name="Author" content="http://www.rtems.org/"/>
  <style>
#download table {
	border-spacing: 3px;
	border-style: outset outset outset outset;
	border-width: 1px 1px 1px 1px;
	background-color: #dcfdc4;
	border-color: black black black black;
	border-collapse: collapse;
}

#download table th {
	background-color: 6c945a;
}

h1, h2, h3, h4 {
	font: bold 1.5em/1.5em sans serif;
	color: #444;
}

  </style>
  <meta name="Copyright" content="Copyright (C) 2015 RTEMS Project"/>
</head>

<body>
<div id='download'>
	"""


def footer():
	return """
</div>
</body>
</html>
	"""


TABLE_START = """
<table style='round' border='1' cellpadding='5'>
<tr align='center'><th>Option</th><th nowrap='nowrap'>Default Value</th><th>Description</th></tr>
"""

TABLE_END = """
</table>
"""

TABLE_ROW ="""
<tr valign='top'>
  <td align='left'>%s</td>
  <td align='left' valign='top'>%s</td>
  <td align='left' align='top'>%s</td>
</tr>
"""

BSP_HEADING = """
<br/>
<hr size='1'>
<h2>%s</h2>
"""

TABLE_HEADING = """
<br/>
<b>%s</b>
"""


def rtems_cmd_docs(ctx):
	fp = open(ctx.options.file_out, "w")
	fp.write(header())

	full = []
	for arch in list_bsp:
		full.append(arch)
		for bsp in list_bsp[arch]:
			full.append("%s/%s" % (arch, bsp))

	all = ["general", "host"] + sorted(full)

	def cfg_get(entry):
		for config in config_list:
			if config.name == entry:
				return config
#		raise Exception("Not found %s" % entry) # XXX: Because not all BSPs are added.

	for entry in all:
		cfg = cfg_get(entry)

		if cfg == None:
			continue # XXX: Hack because not all BSPs are added.
#		print cfg.name, cfg

		c = cfg()

		fp.write(BSP_HEADING % c.name)
		def print_opt(name, values):
			if not list(values):
				return

			fp.write(TABLE_HEADING % "%s Options" % name)
			fp.write(TABLE_START)
			for option in values:
				opt = values[option]
				if type(opt.value) is list:
					value = " ".join(opt.value)
				else:
					value = opt.value
				fp.write(TABLE_ROW % (opt.name, value or "&nbsp", opt.descr))

			fp.write(TABLE_END)

		print_opt("Build", c.option_build)
		print_opt("Header", c.option_header)


	fp.write(footer())

	print("Wrote options.html")
