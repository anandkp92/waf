from .__init__ import Feature

class FeatureGCC(Feature):
	"""GCC Compiler."""
	name = "gcc"
	description = "GCC Compiler"
	conflicts = ("clang",)

	def build(self, c):
		c.USE_GCC = True
	

class FeatureClang(Feature):
	"""Clang Compiler."""
	name = "clang"
	description = "Clang Compiler"
	conflicts = ("gcc",)

	def build(self, c):
		c.USE_CLANG = True


class FeatureDebug(Feature):
	"""Debug Options"""
	name = "debug"
	description = "Enable debug options"

	def build(self, c):
		c.ENABLE_DEBUG = True

