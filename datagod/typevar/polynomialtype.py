from typebase import *
import numpy as np
import matplotlib.pyplot as plt
from random import *
from .. import reporter

class PolynomialType(TypeBase) :
	"""Polynomial Type class"""
	def __init__(self, termsLst, lowRange = None, highRange = None, step = None, swing = None):
		super(PolynomialType, self).__init__()
		self.termsLst = termsLst
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
		if (swing == None):
			self.swing = 0.1
		else:
			self.swing = swing

	def __str__(self):
		return "Polynomial Type"

	def printinfo(self, info):
		print reporter.Reporter.OKBLUE + 'Info: ' + reporter.Reporter.ENDC + 'coff: ' + str(info[0])
		print reporter.Reporter.OKBLUE + 'Info: ' + reporter.Reporter.ENDC + 'residuals: ' + str(info[1][0])
		print reporter.Reporter.OKBLUE + 'Info: ' + reporter.Reporter.ENDC + 'rank: ' + str(info[1][1])
		print reporter.Reporter.OKBLUE + 'Info: ' + reporter.Reporter.ENDC + 'singular_values: ' + str(info[1][2])
		print reporter.Reporter.OKBLUE + 'Info: ' + reporter.Reporter.ENDC + 'rcond: ' + str(info[1][3])

	def draw(self):
		# real data
		x = np.linspace(self.lowRange, self.highRange)
		y = np.polynomial.polynomial.polyval(x, self.termsLst)
		# cheat the data
		cheatY = map(lambda yEle: yEle + self.swing * yEle * (2 * random() - 1), y)
		# cheat line
		line2, = plt.plot(x, cheatY, 'ro')
		# assert(true)
		## fit the data using cheat data
		info = np.polynomial.polynomial.polyfit(x, cheatY, len(self.termsLst) - 1, full=True)
		# may be a bug in num.py? np.polyfit is different from np.polynomial.polynomial.polyfit
		# wrong fit when use np.polyfit
		# coffnp = np.polyfit(x, cheatY, len(self.termsLst) - 1)
		self.printinfo(info)
		realY = np.polynomial.polynomial.polyval(x, info[0])
		line1, = plt.plot(x, realY)
		dashes = [10, 5, 100, 5] # 10 points on, 5 off, 100 on, 5 off
		line1.set_dashes(dashes)
		# show
		plt.legend([line1, line2], ['Fitting Curve', 'Row Data'])
		plt.show()
