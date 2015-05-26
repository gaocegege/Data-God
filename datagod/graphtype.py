__author__ = 'gaoce'

from typevar.typebase import *
from typevar.polynomialtype import *

class GraphType(object):
	"""Type of the graph"""
	@staticmethod
	def getDefaultType():
		return -1

	@staticmethod
	def getPolynomialType():
		return "poly"

	@staticmethod
	def getLogType():
		return "log"