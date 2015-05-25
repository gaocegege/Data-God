__author__ = 'gaoce'

from typevar.typebase import *
from typevar.polynomialtype import *

class GraphType(object):
	"""Type of the graph"""
	@staticmethod
	def getDefaultType():
		return TypeBase()

	@staticmethod
	def getPolynomialType(termLst):
		return PolynomialType(termLst)