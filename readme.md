# Data God

A Open Source program focused on faking data, you can use it when you need some fitting graph, inspired by MCM.

## Example

For example, you give me a function such as `f(x) = x`, the code is:

	from datagod import *
	def main():
		testcase = DataGodBuilder()
		testcase.setType(GraphType.getPolynomialType())\
		.setTermList([0, 1])\
		.build()\
		.draw()
	main()

The program will return a graph: 

<figure>
	<img src="./image/example.png" alt="Example" height="500">
</figure>

The module get a input such as a polynomial function. first, the program will fake some data around the function, and fit a curve using the faked data. So finally, you will get a graph, and some info about the fitting curve. In this case, the info is:

	Info: coff: [-0.03219724  0.99218986]
	Info: residuals: [ 6.13295169]
	Info: rank: 2
	Info: singular_values: [ 1.  1.]
	Info: rcond: 1.11022302463e-14

# Use

Every thing begins with `DataGodBuilder` class, so you need to get a DataGodBuilder, and there are some common config:

* `setLowRange(x1: float)` and `setHighRange(x2: float)` are used to set the domain of the graph, [x1, x2]. default is [0, 10]

## Polynomial

A polynomial in a single indeterminate can be written in the form: `p[0] * 1 + p[1] * x + p[2] * x ** 2 + ... + p[n] * x ** n`, so if get the list of terms p, then can get the polynomial.

* `setType(GraphType.getPolynomialType())` is needed to tell the builder that it need to build a graph about Polynomial.
* `setTermList(termlist: float List)` is needed to tell the builder the coefficients,  in order of increasing degree, i.e., [1, 2, 3] give 1 + 2*x + 3*x**2.

## Logarithm

A Logarithm can be written in the form: `term * log(base)[x] + intercept`, so tell me the term, base and intercept, I will know the log functon. 

* `setLogTerm(term: float)`
* `setBase(base: float)`
* `setIntercept(intercept: float)`

Notice: 0 in domain is bad.

# Requirements

1. numpy
2. matplotlib
3. scipy

# Tasks

* pygraphviz, what is it~?
* How to implement a Python Package
* How to upload the package to pip

# Goals

Requiment:
	The map function needed to cheat
	some parameters to decide how the data should shows
	(such as 波动分布，数据间隔)

随机分布：
	可能需要一些库，包括泊松分布，等等。这些能不自己实现就不自己实现吧。