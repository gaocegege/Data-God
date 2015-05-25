from typebase import *
import numpy as np
import matplotlib.pyplot as plt
from .. import *

class PolynomialType(TypeBase) :
	"""Polynomial Type class"""
	def __init__(self, termsLst, lowRange = None, highRange = None, step = None):
		super(PolynomialType, self).__init__()
		self.termsLst = termsLst
		self.type = 1
		if (lowRange == None):
			self.lowRange = 1
		else:
			self.lowRange = lowRange
		if (highRange == None):
			self.highRange = 10
		else:
			self.highRange = highRange
		if (step == None):
			self.step = 1
		else:
			self.step = step

	def __str__(self):
		return "Polynomial Type"

	def draw(self):
		x = np.linspace(self.lowRange, self.highRange)
		y = np.polynomial.polynomial.polyval(x, self.termsLst)
		line, = plt.plot(x, y)
		print x, y
		dashes = [10, 5, 100, 5] # 10 points on, 5 off, 100 on, 5 off
		line.set_dashes(dashes)
		plt.show()
