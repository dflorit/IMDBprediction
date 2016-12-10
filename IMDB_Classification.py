from Classifiers import *


def testing_prediction():
	#xs = array([[20,20],[10,10],[30,20],[10,20],[12,13],[50,50]])
	#ys = array([0,0,1,1,1,3])
	xs = array([[0,0],[1,1],[3,2],[21,20],[23,25],[50,50],[51,52],[-1,-2],[-3,-4],[-5,-6]])
	ys = array([0,0,0,1,1,2,2,3,3,3])

	training_data = Data()
	training_data.set_feature_vectors(xs)
	training_data.set_labels(ys)

	predict = array([[1,0], [2,1], [22,22], [52,52], [52,53], [53,53], [-1,-1],[-2,-2]])
	#expected_predictions = array([0,1])

	testing_data = Data()
	testing_data.set_feature_vectors(predict)

	#classifier = SVC_Classifier()
	#classifier.set_training_data(training_data)
	#classifier.set_testing_data(testing_data)

	#classifier.train()
	#print classifier.predict()

	print get_mode(training_data, testing_data)
	

def test_reading_table():
	headers, rows = read_file(imdb_table_path)
	#print headers
	#print rows[0]
	for i in range(len(rows)):
		if rows[i][0] == '':
			print i
			#print row


def test_get_Labels():
	headers, rows = read_file(imdb_table_path)
	print get_labels(rows)

def test_get_colors():
	headers, rows = read_file(imdb_table_path)
	print get_colors(rows)

def test_num_critic_for_reviews():
	headers, rows = read_file(imdb_table_path)
	print get_num_critic_for_reviews(rows)

def test_get_duration():
	headers, rows = read_file(imdb_table_path)
	print get_duration(rows)

def test_director_facebook_likes():
	headers, rows = read_file(imdb_table_path)
	print get_director_facebook_likes(rows)

def test_num_voted_users():
	headers, rows = read_file(imdb_table_path)
	print get_num_voted_users(rows)
	
def get_movie_titles():
	headers, rows = read_file(imdb_table_path)
	print get_movie_title(rows)

def generate_plots():
	headers, rows = read_file(imdb_table_path)
	
	imdb_score_vector = get_imdb_score(rows)
	
	colors_name, colors_vector = get_colors(rows)
	critics_reviews_name, critics_reviews_vector = get_num_critic_for_reviews(rows)
	facebook_likes_name, facebook_likes_vector = get_cast_total_facebook_likes(rows)
	budget_name, budget_vector = get_budget(rows)
	
	duration_name, duration_vector = get_duration(rows)
	movie_facebook_name, movie_facebook_vector = get_movie_facebook_likes(rows)
	director_facebook_name, director_facebook_vector = get_director_facebook_likes(rows)
	year_name, year_vector = get_title_year(rows)
	plot2D(colors_vector, imdb_score_vector, colors_name, imdb_score)
	plot2D(critics_reviews_vector, imdb_score_vector, critics_reviews_name, imdb_score)
	plot2D(facebook_likes_vector, imdb_score_vector, facebook_likes_name, imdb_score)
	plot2D(budget_vector, imdb_score_vector, budget_name, imdb_score)
	plot_points(facebook_likes_vector, budget_vector, imdb_score_vector, facebook_likes_name, budget_name)
	plot_points(facebook_likes_vector, critics_reviews_vector, imdb_score_vector, facebook_likes_name, critics_reviews_name)
	plot_points(duration_vector, movie_facebook_vector, imdb_score_vector, duration_name, movie_facebook_name)
	plot_points(movie_facebook_vector, director_facebook_vector, imdb_score_vector, movie_facebook_name, director_facebook_name)
	plot_points(budget_vector, year_vector, imdb_score_vector, budget_name, year_name)
	plot_points(critics_reviews_vector, movie_facebook_vector, imdb_score_vector, critics_reviews_name, movie_facebook_name)
	
		 	

def test_get_directors():
	headers, rows = read_file(imdb_table_path)
	get_direcrors_numeric(rows)


def test_get_deirector_vector():
	headers, rows = read_file(imdb_table_path)
	director_names, director_vectors = get_directors_vector(rows)
	print director_names
	print director_vectors

def test_get_actors_vectors():
	headers, rows = read_file(imdb_table_path)
	names, vectors = get_actors_vector(rows)
	print names

def test_get_vectors():
	headers, rows = read_file(imdb_table_path)
	names, vectors = get_genera_vectors(rows)
	print names
	print vectors

def test_key_words():
	headers, rows = read_file(imdb_table_path)
	names, vectors = get_key_word_vectors(rows)
	print names
	print vectors
#test_reading_table()
#test_get_Labels()
#test_get_colors()
#test_num_critic_for_reviews()
#test_get_duration()
#test_director_facebook_likes()
#test_num_voted_users()
#test_get_directors()
#test_get_deirector_vector()
#print normalize([1,2,4])

#get_movie_titles()
#generate_plots()
#test_get_actors_vectors()
#test_get_vectors()
#['Action', 'Adventure', 'Fantasy', 'Sci-Fi', 'Thriller', 'Documentary', 'Romance', 'Drama', 'History', 'Family', 'Animation', 'Comedy', 'Sport', 'Crime', 'Horror', 'Mystery', 'War', 'Musical', 'Western', 'Biography', 'Music', 'Game-Show', 'Reality-TV', 'News', 'Short', 'Film-Noir']
#test_key_words()
generate_plots()
