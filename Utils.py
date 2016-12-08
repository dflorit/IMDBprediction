from numpy import *
from math import *

#------------------------------Math Tools---------------------------------------
#precondition: The 2 vectors have the same dimensions
#This function calculates the dot product of vectors v1 and v2. The same index on v1 and
#v2 represents the same dimension
#v1 is a vector represented as numpy array.
#v2 is a vector represented as numpy array.
#returns a scalar = the value of the dot product
def dot_product(v1, v2):
	dot_product_scalar = 1.0*sum(v1*v2)
	return dot_product_scalar
	
#precondition: The 2 vectors have the same dimensions
#This function calculates the sum of vectors v1 and v2
#v1 is a vector represented as a numpy array.
#v2 is a vector represented as a numpy array.
#returns a vector which is the sum of v1 and v2
def sum_vectors(v1, v2):
	sum_vector = v1 + v2
	return sum_vector

#This function multiplies a vector times a constant
#v is a vector
#c is a constant
#returns a new vector = c*v
def scalar_multiplication(v, c):
	scalar_mult_vector = c*v
	return scalar_mult_vector		

#This function finds the norm of a vector
#v is a vector
#returns the value of the norm of v
def norm(v):
	norm = sqrt(sum(v**2))
	return norm


#applies the sigmoid function to either a constant of a numpy array
def sigmoid_function(x, theta):
	return 1.0/(1+e**(-1.0*theta*x))


#h_x is the predictions and y is the actual label
#This is not vectorized. h_x and y are constants
def logistic_regression_cost(h_x, y):
	return -1.0*y*log(h_x)-(1-y)*log(1-h_x)

#x_j is the x that is mappe to the current theta
#This is not vectorized all parameters are constants
def logistic_regression_derivative_cost(xs_j, h_x, y):
	return (h_x - y)*xs_j

#J
#cost is the cost function to be used. In the case of logistic regression send logistic_regression_cost
#h_xs are the predictions (a numpy array)
#ys are the actual labels (a numpy array)
def cost_function(h_xs, ys, cost):
	m = 1.0*len(ys)
	total_cost = 0.0
	
	for i in range(h_xs):
		total_cost += cost(h_xs[i], ys[i])
	
	averaged_cost = total_cost/m
	
	return averaged_cost


#derivative cost function (d/dtheta) J
#J
#cost is the cost function to be used. In the case of logistic regression send logistic_regression_derivative_cost
#h_xs are the predictions (a numpy array)
#ys are the actual labels (a numpy array)
#xs
def cost_function_derivative(xs_j, h_xs, ys, derivative_cost):
	m = 1.0*len(ys)
	total_cost = 0.0
	
	for i in range(h_xs):
		total_cost += derivative_cost(xs_j, h_xs[i], ys[i])
	
	averaged_cost = total_cost/m
	
	return averaged_cost


#------------------------------------Ploting Tools----------------------------------
def plot_points(xs, ys, labels, filename=None):
	
	
	for i in range(len(xs)):
		plt.scatter(xs[i],ys[i], c=colors[labels[i]], label=labels[i])
	
	plt.legend()
	plt.grid(True)
	if filename == None:
		plt.show()
	else:
		plt.savefig(filename+'png')
		
