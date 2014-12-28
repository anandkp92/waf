class rtems_base(object):
	name = None

	def __init__(self, ctx):
		self.ctx = ctx

		if ctx.env.ENABLE_PTHREADS and not ctx.env.ENABLE_POSIX:
			raise ValueError("ENABLE_POSIX required for ENABLE_PTHREADS")

		self.ctx(
			name = "auto_%s_objects" % self.name,
			use  = []
		)


	def _get_id(self, name):
		name_id = "auto_%s" % name

		if name_id not in self.ctx.counter:
			self.ctx.counter[name_id] = 0
			return "%s_0" % name_id
		else:
			self.ctx.counter[name_id] += 1
			return "%s_%d" % (name_id, self.ctx.counter[name_id])


	def _obj_add(self, name, source, **kwarg):

		if "test" in kwarg:
			if not kwarg["test"]:
				return

		if "alias" in kwarg:
			name = "%s_%s" % (name, kwarg["alias"])

		id = self._get_id(name)

		self.ctx.rtems_obj(
			id,
			source,
			**kwarg
		)

		#XXX: Is this OK?
		for g in self.ctx.groups[0]:
			if g.get_name() == "auto_%s_objects" % self.name:
				g.use.append(id)

	def start(self, source, defines=[]):
		from os.path import splitext, basename

		for s in source:
			file = splitext(basename(s))[0]
			self.ctx(
				rule     = '${CC} -DASM ${CFLAGS} ${CPPFLAGS} ${DEFINES_ST:DEFINES} ${CPPPATH_ST:INCPATHS} -c -o ${TGT} ${SRC}',
				source   = s,
				target   = "%s.o" % file,
				name     = "start_%s_o" % file,
				features = "c casm bld_include src_include",
				defines  = defines,
			)

	def source(self, source, **kwarg):
		self._obj_add(self.name, source, **kwarg)

	def debug(self, source, **kwarg):
		if self.ctx.env.ENABLE_DEBUG:
			self._obj_add("%s_debug" % self.name, source, **kwarg)

	def mp(self, source, **kwarg):
		if self.ctx.env.ENABLE_MP:
			self._obj_add("%s_mp" % self.name, source, **kwarg)

	def multilib(self, source, **kwarg):
		if self.ctx.env.ENABLE_MULTILIB:
			self._obj_add("%s_multilib" % self.name, source, **kwarg)

	def networking(self, source, **kwarg):
		if self.ctx.env.ENABLE_NETWORKING:
			self._obj_add("%s_networking" % self.name, source, **kwarg)

	def newlib(self, source, **kwarg):
		if self.ctx.env.ENABLE_NEWLIB:
			self._obj_add("%s_newlib" % self.name, source, **kwarg)

	def posix(self, source, **kwarg):
		if self.ctx.env.ENABLE_POSIX:
			self._obj_add("%s_posix" % self.name, source, **kwarg)

	def pthreads(self, source, **kwarg):
		# pthreads requires POSIX
		if self.ctx.env.ENABLE_PTHREADS and self.ctx.env.ENABLE_POSIX:
			self._obj_add("%s_pthreads" % self.name, source, **kwarg)

	def rpc(self, source, **kwarg):
		if self.ctx.env.ENABLE_RPC:
			self._obj_add("%s_rpc" % self.name, source, **kwarg)

	def serdbg(self, source, **kwarg):
		if self.ctx.env.ENABLE_SERDBG:
			self._obj_add("%s_serdbg" % self.name, source, **kwarg)

	def shell(self, source, **kwarg):
		if self.ctx.env.ENABLE_SHELL:
			self._obj_add("%s_shell" % self.name, source, **kwarg)

	def smp(self, source, **kwarg):
		if self.ctx.env.ENABLE_SMP:
			self._obj_add("%s_smp" % self.name, source, **kwarg)


class libcpu(rtems_base):
	name = "libcpu"

class libbsp(rtems_base):
	name = "libbsp"

	def fpsp(self, source, **kwarg):
		if self.ctx.env.ENABLE_FPSP:
			self._obj_add("%s_fpsp" % self.name, source, **kwarg)
