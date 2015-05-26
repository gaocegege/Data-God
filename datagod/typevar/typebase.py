class TypeBase(object):
	"""Type Base Class"""
	def __init__(self):
		self.type = -1
		self.lowRange = 1
		self.highRange = 10
		self.step = 1
		self.swing = 0.1

	def draw(self):
		pass