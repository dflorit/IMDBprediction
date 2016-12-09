from numpy import *
from math import *
import matplotlib.pyplot as plt

#------------------------------Variables---------------------------------------
imdb_table_path = 'Data/movie_metadata.csv'

#Column Names
color = 'Color'
director_name = 'Director Name'
num_critic_for_reviews = 'Number Critic For Reviews'
duration = 'Duration'
director_facebook_likes = 'Director Facebook Likes'
actor_3_facebook_likes = 'Actor 3 Facebook Likes'
actor_2_name = 'Actor 2 Name'
actor_1_facebook_likes = 'Actor 1 Facebook Likes'
gross = 'Gross'
genres = 'Genres'
actor_1_name = 'Actor 1 Name'
movie_title = 'Movie Title'
num_voted_users = 'Number Voted Users'
cast_total_facebook_likes = 'Cast Total Facebook Likes'
actor_3_name = 'Actor 3 Name'
facenumber_in_poster = 'Facenumber in Poster'
plot_keywords = 'Plot Keywords'	
movie_imdb_link = 'Movie imdb Link'
num_user_for_reviews = 'Number User for Reviews'
language = 'Language'
country = 'Country'
content_rating = 'Content Rating'
budget = 'Budget'
title_year = 'Title Year'
actor_2_facebook_likes = 'Actor 2 Facebook Likes'
imdb_score = 'Imdb Score'
aspect_ratio = 'Aspect Ratio' 
movie_facebook_likes = 'Movie Facebook Likes'

#column names
feature_list = [color, director_name, num_critic_for_reviews, duration,
						director_facebook_likes, actor_3_facebook_likes, actor_2_name,
						actor_1_facebook_likes, gross, genres, actor_1_name, movie_title,
						num_voted_users, cast_total_facebook_likes, actor_3_name,
						facenumber_in_poster, plot_keywords, movie_imdb_link,
						num_user_for_reviews, language, country, content_rating, budget,
						title_year, actor_2_facebook_likes, imdb_score,	aspect_ratio, 
						movie_facebook_likes]

feature_name_to_number = {color:0, director_name:1, num_critic_for_reviews:2, duration:3,
						director_facebook_likes:4, actor_3_facebook_likes:5, actor_2_name:6,
						actor_1_facebook_likes:7, gross:8, genres:9, actor_1_name:10, movie_title:11,
						num_voted_users:12, cast_total_facebook_likes:13, actor_3_name:14,
						facenumber_in_poster:15, plot_keywords:16, movie_imdb_link:17,
						num_user_for_reviews:18, language:19, country:20, content_rating:21, budget:22,
						title_year:23, actor_2_facebook_likes:24, imdb_score:25, aspect_ratio:26, 
						movie_facebook_likes:27}


#posible labels
posible_labels = [x for x in range(1,11)]

#This is the color on the table
colors_to_numbers = {' Black and White':0, 'Color':1, '':2}

#This is for the purpose of plotting
colors = {1:'black', 2:'lightcoral', 3:'maroon', 4:'orangered', 5:'saddlebrown', 7:'purple', 8:'navy', 9:'skyblue', 6:'green', 10:'yellow'}

#------------------------------Math Tools---------------------------------------

def normalize(l):
	m = 1.0*max(l)
	return list(array(l)/m)
	

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
	#print x
	#print theta
	return 1.0/(1+e**(-1.0*sum(theta*x)))

'''
def dJ(xs, ys, h, j, thetas):
	der = 0.0
	m = 1.0*len(xs)
	
	
	for i in range(len(xs)):
		x_vect = xs[i]
		h_x_vec = h(x_vect, thetas)
		#print "Evaluation = " + str(h_x_vec)
		der += (h_x_vec - ys[i])*xs[i][j]	

	#print "Derivative = " + str(der)
	return der/m
	
	
def gradient_descent(xs, ys, h, alpha=0.01, iterations=10000):
	thetas = array([0]*len(xs[0]))
	
	for iteration in range(iterations):
		for j in range(len(thetas)):
			#print 'AAAAAA ' + str(alpha*dJ(xs,ys,h,j,thetas))
			thetas[j] = thetas[j] - alpha*dJ(xs,ys,h,j,thetas)
			print thetas[j]
	
	return thetas
'''	

def derivative_J(xs, ys, thetas, j):
	cost = 0.0
	
	for i in range(len(xs)):
		cost += xs[i][j] * (sigmoid_function(xs[i], thetas) - ys[i])
	
	return cost/(1.0 * len(xs))


def gradient_descent(xs, ys, h, alpha, iterations, lamda):
	thetas = array([1.0]*len(xs[0]))
	m = len(xs)
	#print 'Sig =', sigmoid_function(array([-0.25, 0.25]), thetas)
	for it in range(iterations):
		for j in range(len(thetas)):
			thetas[j] = thetas[j] - alpha*(derivative_J(xs, ys, thetas, j)+(lamda/m)*thetas[j])
	return thetas
	
#------------------------------------Ploting Tools----------------------------------
def plot_points(xs, ys, labels, labelX, labelY, filename=None):
	dx = {}
	dy = {}
	for i in range(len(xs)):
		key = (labels[i], colors[labels[i]])
		if key in dx:
			dx[key] = dx[key] + [xs[i]]
			dy[key] = dy[key] + [ys[i]]
		else:
			dx[key] = [xs[i]]
			dy[key] = [ys[i]]
	
	for key in dx:
		plt.scatter(dx[key], dy[key], c=key[1], label=key[0]) 
			
	
	#for i in range(len(xs)):
		#plt.scatter(xs[i],ys[i], c=colors[labels[i]], label=labels[i])
	
	
	plt.legend()
	plt.grid(True)
	plt.xlabel(labelX)
	plt.ylabel(labelY)
	plt.title(labelX + ' vs. ' + labelY)
	
	if filename == None:
		plt.show()
	else:
		plt.savefig(filename+'png')


def plot2D(xs, ys, labelX, labelY):
	plt.plot(xs, ys, 'ro')
	plt.xlabel(labelX)
	plt.ylabel(labelY)
	plt.title(labelX + ' vs. ' + labelY)
	plt.show()

#---------------------------------Managing Files tools--------------------------------
#table_path is the path to the excel_table
#return a Data object with feature vectors and labels included
def read_excel_table(table_path):
	#feature_names = []
	#feature_vectors = []
	#data = Data()
	headers = []
	rows = []
	
	f = open(table_path, 'r')
	
	for line in f:
		line = line.replace('\n', '')
		splited_line = line.split(',')
		splited_line = filter(lambda a: a != '', splited_line)
		splited_line = filter(lambda a: a != '\r', splited_line)
	
		if len(headers) == 0:
			headers = splited_line
		else:
			#feature_vectors.append([float(feature) for feature in splited_line])
			rows.append(splited_line)
	
	f.close()
	
	#data.set_feature_vectors(array(feature_vectors))
	#data.set_feature_names(array(feature_names))
	
	return (headers, rows)
	
	
	
def read_file(filename):
		f = open(filename, 'r')
		file_data = []
		
		
		for line in f:
			#row_dict = {}
			row = []
			splited = line.split(',')
			if len(splited) > 28:
				offset = len(splited) - 28
			else:
				offset = 0
				
			for i in range(len(feature_list)):
				val = splited[i]
				if feature_list[i] == 'Movie Title':
					for iter in range(offset):
						val = ", ".join([val, splited[i+iter+1]])
				elif i > 11:
					val = splited[i + offset]
					if i == (len(feature_list) - 1):
						val = val.split('\r')[0]
			
				#row_dict[self.feature_list[i]] = val
				row.append(val)
		
			#self.file_data.append(row_dict)
			file_data.append(row)
		headers = file_data.pop(0)
		return headers, file_data

def get_imdb_score(rows):
	labels = []
	rating_index = feature_name_to_number[imdb_score]
	for row in rows:
		labels.append(int(round(float(row[rating_index]))))
	return labels
		
def get_colors(rows):
	colors = []
	for row in rows:
		colors.append(colors_to_numbers[row[feature_name_to_number[color]]])
	return color, colors

def get_movie_title(rows):
	ids = []
	
	for row in rows:
		ids.append(row[feature_name_to_number[movie_title]])
	
	return ids

	
def get_int_column(rows, column_name):
	output = []
	output_ne = []
	
	for row in rows:
		strg = row[feature_name_to_number[column_name]]
		if strg == '':
			output.append(strg)
		else:
			output.append(int(strg))
			output_ne.append(int(strg))
	
	avg = sum(output_ne)/len(output_ne)
	
	for i in range(len(output)):
		if output[i] == '':
			output[i] = avg
	
	return column_name, output

def get_num_critic_for_reviews(rows):
	return get_int_column(rows, num_critic_for_reviews)

def get_duration(rows):
	return get_int_column(rows, duration)

def get_director_facebook_likes(rows):
	return get_int_column(rows, director_facebook_likes)
	
def get_num_voted_users(rows):
	return get_int_column(rows, num_voted_users)

def get_cast_total_facebook_likes(rows):
	return get_int_column(rows, cast_total_facebook_likes)

def get_facenumber_in_poster(rows):
	return get_int_column(rows, facenumber_in_poster)

def get_num_user_for_reviews(rows):
	return get_int_column(rows, num_user_for_reviews)

def get_budget(rows):
	return get_int_column(rows, budget)
	
def get_title_year(rows):
	return get_int_column(rows, title_year)

def get_movie_facebook_likes(rows):
	return get_int_column(rows, movie_facebook_likes)
