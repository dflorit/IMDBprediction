from Data import *
from Utils import *

'''
General template:
	Feature extractor receives the image as a numpy array
	extracts relevant classification features from image
	returns a tuple containing two numpy arrays:
		the first including the feature names
		the second including the features corresponding to those names
'''

class Feature_Extractors:

	def numeric_feature_extractor(self, imdb_table_path):
		headers, rows = read_file(imdb_table_path)
		D = Data()
		
		labels = get_imdb_score(rows)
		D.set_labels(labels)
		
		movie_titles = get_movie_title(rows)
		D.set_table_ids(movie_titles)
		
		#extracting features:
		feature_names1, feature1 = get_colors(rows)
		feature_names2, feature2 = get_num_critic_for_reviews(rows)
		feature_names3, feature3 = get_duration(rows)
		feature_names4, feature4 = get_director_facebook_likes(rows)
		feature_names5, feature5 = get_num_voted_users(rows)
		feature_names6, feature6 = get_cast_total_facebook_likes(rows)
		feature_names7, feature7 = get_facenumber_in_poster(rows)
		feature_names8, feature8 = get_num_user_for_reviews(rows)
		feature_names9, feature9 = get_budget(rows)
		feature_names10, feature10 = get_title_year(rows)
		feature_names11, feature11 = get_movie_facebook_likes(rows)
		
		feature_vectors = []
		for i in range(len(feature1)):
			feature_vector = [feature1[i], feature2[i], feature3[i], feature4[i], feature5[i], \
			feature6[i], feature7[i], feature8[i], feature9[i], feature10[i], feature11[i]]
			feature_vectors.append(feature_vector)
		
		feature_vectors = array(feature_vectors)
		D.set_feature_vectors(feature_vectors)
		
		feature_names = array([feature_names1, feature_names2, feature_names3, feature_names4, \
		feature_names5, feature_names6, feature_names7, feature_names8, feature_names9, \
		feature_names10, feature_names11])
		D.set_feature_names(feature_names)
		
		return D

	def non_numeric_feature_extractor(self, imdb_table_path):
		headers, rows = read_file(imdb_table_path)
		D = Data()
		
		labels = get_imdb_score(rows)
		D.set_labels(labels)
		
		movie_titles = get_movie_title(rows)
		D.set_table_ids(movie_titles)
		
		#extracting features:
		feature_names1, feature1 = get_directors_vector(rows)
		feature_names2, feature2 = get_actors_vector(rows)
		feature_names3, feature3 = get_genera_vectors(rows)
		feature_names4, feature4 = get_key_word_vectors(rows)
		
		feature_vectors = []
		for i in range(len(feature1)):
			feature_vector = feature1[i] + feature2[i] + feature3[i] + feature4[i]
			feature_vectors.append(feature_vector)
		
		feature_vectors = array(feature_vectors)
		D.set_feature_vectors(feature_vectors)
		
		feature_names = array(feature_names1 + feature_names2 + feature_names3 + feature_names4)
		D.set_feature_names(feature_names)
		
		return D
	
	def actors_feature_extractor(self, imdb_table_path):
		headers, rows = read_file(imdb_table_path)
		D = Data()
		
		labels = get_imdb_score(rows)
		D.set_labels(labels)
		
		movie_titles = get_movie_title(rows)
		D.set_table_ids(movie_titles)
		
		#extracting features:
		feature_names1, feature1 = get_actors_vector(rows)
		
		feature_vectors = []
		for i in range(len(feature1)):
			feature_vector = feature1[i]
			feature_vectors.append(feature_vector)
		
		feature_vectors = array(feature_vectors)
		D.set_feature_vectors(feature_vectors)
		
		feature_names = array(feature_names1)
		D.set_feature_names(feature_names)
		
		return D

	def directors_feature_extractor(self, imdb_table_path):
		headers, rows = read_file(imdb_table_path)
		D = Data()
		
		labels = get_imdb_score(rows)
		D.set_labels(labels)
		
		movie_titles = get_movie_title(rows)
		D.set_table_ids(movie_titles)
		
		#extracting features:
		feature_names1, feature1 = get_directors_vector(rows)
		
		feature_vectors = []
		for i in range(len(feature1)):
			feature_vector = feature1[i]
			feature_vectors.append(feature_vector)
		
		feature_vectors = array(feature_vectors)
		D.set_feature_vectors(feature_vectors)
		
		feature_names = array(feature_names1)
		D.set_feature_names(feature_names)
		
		return D
		
	def genera_feature_extractor(self, imdb_table_path):
		headers, rows = read_file(imdb_table_path)
		D = Data()
		
		labels = get_imdb_score(rows)
		D.set_labels(labels)
		
		movie_titles = get_movie_title(rows)
		D.set_table_ids(movie_titles)
		
		#extracting features:
		feature_names1, feature1 = get_genera_vectors(rows)
		
		feature_vectors = []
		for i in range(len(feature1)):
			feature_vector = feature1[i]
			feature_vectors.append(feature_vector)
		
		feature_vectors = array(feature_vectors)
		D.set_feature_vectors(feature_vectors)
		
		feature_names = array(feature_names1)
		D.set_feature_names(feature_names)
		
		return D
		
	def keywords_feature_extractor(self, imdb_table_path):
		headers, rows = read_file(imdb_table_path)
		D = Data()
		
		labels = get_imdb_score(rows)
		D.set_labels(labels)
		
		movie_titles = get_movie_title(rows)
		D.set_table_ids(movie_titles)
		
		#extracting features:
		feature_names1, feature1 = get_key_word_vectors(rows)
		
		feature_vectors = []
		for i in range(len(feature1)):
			feature_vector = feature1[i]
			feature_vectors.append(feature_vector)
		
		feature_vectors = array(feature_vectors)
		D.set_feature_vectors(feature_vectors)
		
		feature_names = array(feature_names1)
		D.set_feature_names(feature_names)
		
		return D
	
	def all_feature_extractor(self, imdb_table_path):
		headers, rows = read_file(imdb_table_path)
		D = Data()
		
		labels = get_imdb_score(rows)
		D.set_labels(labels)
		
		movie_titles = get_movie_title(rows)
		D.set_table_ids(movie_titles)
		
		#extracting features:
		feature_names1, feature1 = get_colors(rows)
		feature_names2, feature2 = get_num_critic_for_reviews(rows)
		feature_names3, feature3 = get_duration(rows)
		feature_names4, feature4 = get_director_facebook_likes(rows)
		feature_names5, feature5 = get_num_voted_users(rows)
		feature_names6, feature6 = get_cast_total_facebook_likes(rows)
		feature_names7, feature7 = get_facenumber_in_poster(rows)
		feature_names8, feature8 = get_num_user_for_reviews(rows)
		feature_names9, feature9 = get_budget(rows)
		feature_names10, feature10 = get_title_year(rows)
		feature_names11, feature11 = get_movie_facebook_likes(rows)
		feature_names12, feature12 = get_directors_vector(rows)
		feature_names13, feature13 = get_actors_vector(rows)
		feature_names14, feature14 = get_genera_vectors(rows)
		feature_names15, feature15 = get_key_word_vectors(rows)
		
		feature_vectors = []
		for i in range(len(feature1)):
			feature_vector = [feature1[i], feature2[i], feature3[i], feature4[i], feature5[i], \
			feature6[i], feature7[i], feature8[i], feature9[i], feature10[i], feature11[i]]
			feature_vectors.append(feature_vector)
			
			feature_vector += feature12[i] + feature13[i] + feature14[i] + feature15[i]
			feature_vectors.append(feature_vector)
		
		feature_vectors = array(feature_vectors)
		D.set_feature_vectors(feature_vectors)
		
		feature_names = [feature_names1, feature_names2, feature_names3, feature_names4, \
		feature_names5, feature_names6, feature_names7, feature_names8, feature_names9, \
		feature_names10, feature_names11]
		
		feature_names += feature_names12 + feature_names13 + feature_names14 + feature_names15
		feature_names = array(feature_names)
		
		D.set_feature_names(feature_names)
		
		return D
		