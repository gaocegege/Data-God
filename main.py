#!/usr/bin/python
from datagod.datagod import *

def main():
	testcase = DataGodFactory()
	testcase.setStep(1).setType("poly").setLowRange(0).setHighRange(100).setTermList([10000, 0, 2]).build().draw()

main()