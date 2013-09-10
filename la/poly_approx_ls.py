#! /usr/bin/env python

# Polynomial approximation using least squares

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

def f(x):
	return (4*x)/(1 + 10 * (x**2))

def eval():
	#make y vector for x [0,1)
	x = np.arange(0, 1, .01)
	y = f(x)
	
	#degree 1
	A = np.ones(shape=(100, 2))
	A[:,1] = x
	x_1 = np.linalg.lstsq(A,y)[0]
	plt.plot(x, y, 'r', label='actual curve')
	plt.plot(x, np.dot(A,x_1), 'g--', label='first order')

	#degree 2 
	A = np.ones(shape=(100, 3))
	A[:,1] = x
	A[:,2] = np.power(x, 2)
	x_2 = np.linalg.lstsq(A,y)[0] 
	plt.plot(x, np.dot(A, x_2), 'b--', label='second order')

	#degree 3
	A = np.ones(shape=(100, 4))
	A[:,1] = x
	A[:,2] = np.square(x)
	A[:,3] = np.power(x, 3)
	x_3 = np.linalg.lstsq(A,y)[0]
	plt.plot(x, np.dot(A, x_3), 'k--', label='third order') 
	plt.legend() #to show labels
	plt.show()



if __name__ == "__main__":
	eval()
