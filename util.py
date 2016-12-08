#test 2
import matplotlib.pyplot as plt
from numpy import *


class Util:
	
	def __init__(self):
	
		#Column Names
		color = 'Color'
		director_name = 'Director Name'
		num_critic_for_reviews = 'Number Critic For Reviews'
		duration = 'Duration'
		director_facebook_likes = 'Director Facebook Likes'
		actor_3_facebook_likes = 'Actor 3 Facebook Likes'
		actor_2_name = 'Actor 2 Name'
		actor_1_facebook_likes = 'Actor 3 Facebook Likes'
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

		#Column names organized in a list
		self.feature_list = [color, director_name, num_critic_for_reviews, duration,
						director_facebook_likes, actor_3_facebook_likes, actor_2_name,
						actor_1_facebook_likes, gross, genres, actor_1_name, movie_title,
						num_voted_users, cast_total_facebook_likes, actor_3_name,
						facenumber_in_poster, plot_keywords, movie_imdb_link,
						num_user_for_reviews, language, country, content_rating, budget,
						title_year, actor_2_facebook_likes, imdb_score,	aspect_ratio, 
						movie_facebook_likes]

		#It will be a list of dictionaries (each dictionary represents a row) that map from 
		#column name to a string which is the value of that column in that row
		self.file_data = []				

	def read_file(self, filename):
		f = open(filename, 'r')
		
		for line in f:
			#row_dict = {}
			row = []
			splited = line.split(',')
			if len(splited) > 28:
				offset = len(splited) - 28
			else:
				offset = 0
				
			for i in range(len(self.feature_list)):
				val = splited[i]
				if self.feature_list[i] == 'Movie Title':
					for iter in range(offset):
						val = ", ".join([val, splited[i+iter+1]])
				elif i > 11:
					val = splited[i + offset]
					if i == (len(self.feature_list) - 1):
						val = val.split('\r')[0]
			
				#row_dict[self.feature_list[i]] = val
				row.append(val)
		
			#self.file_data.append(row_dict)
			self.file_data.append(row)
		temp = self.file_data.pop(0)
		return self.file_data 

	def getColumn(self, columnName):
		column = []	
		for row in self.file_data: 	#row is a dictionary
			column.append(row[columnName])
		return column
	
	def getAllColumns(self):
		allColumns = {}
		for feature in self.feature_list:
			allColumns[feature] = self.getColumn(feature)
		return allColumns
	
	def plot2D(self, xs, ys, labelX, labelY):
		plt.plot(xs, ys, 'ro')
		plt.xlabel(labelX)
		plt.ylabel(labelY)
		plt.title(labelX + ' vs. ' + labelY)
		plt.show()

	def displayTrend(self, feature1, feature2):
		xs = self.getColumn(feature1)
		ys = self.getColumn(feature2)
		self.plot2D(xs, ys, str(feature1), str(feature2))
	
	#def displayAllTrends(self):
	#	allColumns = self.getAllColumns()
	#	
	#	for i in range(len(self.feature_list)):
	#		for j in range(i+1, range(len(self.feature_list))):
	#			self.displayTrend(self.feature_list(i), self.feature_list(j))
		
