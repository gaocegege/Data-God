from typebase import *
import numpy as np
import matplotlib.pyplot as plt
from random import *
from .. import reporter
import math
from scipy.optimize import curve_fit


class LogType(TypeBase):
	"""docstring for LogType"""
	def __init__(self, term, base, intercept, lowRange = None, highRange = None, step = None, swing = None):
		super(LogType, self).__init__()
		self.term = term
		self.base = base
		self.intercept = intercept
		# how to hide the code by putting it in parent class?
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
		return "Log Type"

	# trick, may have bug, math.log return ZeroDivisionError when base == 1
	def __mathLog__(self, x, base):
		if (base == 1):
			return np.log(x) / (1e-8)
		else:
			return np.log(x) / np.log(base)

	def __arrayLog__(self, x, term = None, base = None, intercept = None):
		_term = term
		_base = base
		_intercept = intercept
		if (term == None):
			_term = self.term
		if (base == None):
			_base = self.base
		if (intercept == None):
			_intercept = self.intercept
		res = map(lambda xEle: _term * self.__mathLog__(xEle, _base) + _intercept, x)
		return res

	# remove the zero and inf, tricks
	def __removeZero__(self, x):
		for i in range(len(x)):
			if (x[i] == 0):
				x[i] = 1e-8
		xbuf = x[x != np.inf]
		xbuf = xbuf[xbuf != -np.inf]
		x[x == -np.inf] = (np.amin(xbuf) - np.amax(xbuf)) / 2
		x[x == np.inf] = (np.amin(xbuf) + 3 * np.amax(xbuf)) / 2
		return x

	def draw(self):
		# real data
		x = np.linspace(self.lowRange, self.highRange)
		y = self.__arrayLog__(x)
		x = [float(xn) for xn in x] #every element (xn) in x becomes a float
		y = [float(yn) for yn in y] #every element (yn) in y becomes a float
		x = np.array(x) #transform your data in a numpy array, 
		y = np.array(y) #so the curve_fit can work
		x = self.__removeZero__(x)#remove zero to make sure self.__mathLog__() can work
		y = self.__removeZero__(y)#remove zero to make sure self.__mathLog__() can work
		# cheat the data
		print x
		print y
		cheatY = map(lambda yEle: yEle + self.swing * yEle * (2 * random() - 1), y)
		cheatY = self.__removeZero__(cheatY)
		# cheat line
		line2, = plt.plot(x, cheatY, 'ro')
		popt, pcov = curve_fit(lambda xbuf, term, base, intercept: self.__arrayLog__(xbuf, term, base, intercept), x, cheatY)
		realY = self.__arrayLog__(x, popt[0], popt[1], popt[2])
		line1, = plt.plot(x, realY)
		dashes = [10, 5, 100, 5] # 10 points on, 5 off, 100 on, 5 off
		line1.set_dashes(dashes)
		# show
		plt.legend([line1, line2], ['Fitting Curve', 'Row Data'])
		plt.show()