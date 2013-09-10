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
	y_1 = np.dot(A,x_1)
	plt.plot(x, y, 'r', label='actual curve')
	plt.plot(x, y_1, 'g--', label='Degree: 1')
	print "1st plot RMS=", np.sqrt(np.mean((y_1 -y)**2))

	#degree 2 
	A = np.ones(shape=(100, 3))
	A[:,1] = x
	A[:,2] = np.power(x, 2)
	x_2 = np.linalg.lstsq(A,y)[0] 
	y_2 = np.dot(A, x_2)
	plt.plot(x, y_2, 'b--', label='Degree: 2')
	print "1st plot RMS=", np.sqrt(np.mean((y_2 - y)**2))

	#degree 3
	A = np.ones(shape=(100, 4))
	A[:,1] = x
	A[:,2] = np.power(x, 2)
	A[:,3] = np.power(x, 3)
	x_3 = np.linalg.lstsq(A,y)[0]
	y_3 = np.dot(A, x_3)
	plt.plot(x, y_3, 'k--', label='Degree: 3') 
	print "3rd plot RMS=", np.sqrt(np.mean((y_3 - y)**2))

	#degree 4
	A = np.ones(shape=(100, 5))
	A[:,1] = x
	A[:,2] = np.power(x, 2)
	A[:,3] = np.power(x, 3)
	A[:,4] = np.power(x, 4)
	x_4 = np.linalg.lstsq(A,y)[0]
	y_4 = np.dot(A, x_4)
	plt.plot(x, y_4, 'm--', label='Degree: 4') 
	print "4th plot RMS=", np.sqrt(np.mean((y_4 - y)**2))

	plt.legend() #to show labels
	plt.show()



if __name__ == "__main__":
	eval()
