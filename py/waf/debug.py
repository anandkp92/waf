from hashlib import sha256
from os.path import exists
from json import JSONEncoder
from time import time
import logging
from logging.handlers import MemoryHandler
from waflib.Task import Task
from waflib.Utils import subprocess, check_dir
from waflib.Logs import debug

from os.path import dirname

#from cStringIO import StringIO
#from waflib import Utils

def logger_json_create(ctx):
	logger = logging.getLogger('build.json')
	logger.setLevel(logging.INFO)

	if ctx.variant == "host":
		file = "%s/logs/host.json" % ctx.out_dir
	else:
		file = "%s/logs/%s.json" % (ctx.out_dir, ctx.variant)

	check_dir(dirname(file))
	filetarget = logging.FileHandler(file, mode="w")
	memoryhandler = MemoryHandler(1048576, target=filetarget)

	logger.addHandler(memoryhandler)

	return logger


def hash_files(files):
	h = []
	for file in files:
		if exists(file):
			fp = open(file, "r")
			h.append((file, sha256(fp.read()).hexdigest()))
			fp.close()
	return h


def exec_command_json(self, cmd, **kw):
#	subprocess = Utils.subprocess
	kw['shell'] = isinstance(cmd, str)

	debug('runner_env: kw=%s' % kw)

	try:
		record = {}
		record["time"] = time()
		record["command"] = cmd
		recoard["variant"] = ctx.variant

		task_self = kw["json_task_self"]
		record["type"] = task_self.__class__.__name__

		del kw["json_task_self"]

		record["inputs"] = [x.srcpath() for x in task_self.inputs]
		record["outputs"] = [x.srcpath() for x in task_self.outputs]
		record["cflags"] = self.env.CFLAGS
		record["cc"] = self.env.CC

		kw['stdout'] = kw['stderr'] = subprocess.PIPE

		time_start = time()
		p = subprocess.Popen(cmd, **kw)
		(stdout, stderr) = p.communicate()
		record["time_duration"] = time() - time_start

		if stdout:
			record["stdout"] = stdout
		if stderr:
			record["stderr"] = stderr

		record["hash"] = {}
		record["hash"]["inputs"] = hash_files(record["inputs"])
		record["hash"]["outputs"] = hash_files(record["outputs"])

		record["retval"] = p.returncode
		data = JSONEncoder(sort_keys=False, indent=False).encode(record)

		self.logger_json.info(data)

		return p.returncode

	except OSError:
		return -1


def exec_command_json_extra(self, cmd, **kw):
	kw["json_task_self"] = self
	self.exec_command_real(cmd, **kw)
