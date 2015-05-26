#!/usr/bin/python
from datagod import *

def main():
	testcase = DataGodBuilder()
	# testcase.setType(GraphType.getPolynomialType())\
	# .setTermList([0, 1])\
	# .build()\
	# .draw()

	testcase.setType(GraphType.getLogType())\
	.setLogTerm(1)\
	.setBase(11)\
	.setIntercept(0)\
	.setLowRange(2)\
	.build()\
	.draw()

main()