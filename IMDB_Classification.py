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
	
	
	#plot2D(colors_vector, imdb_score_vector, colors_name, imdb_score)
	#plot2D(critics_reviews_vector, imdb_score_vector, critics_reviews_name, imdb_score)
	#plot2D(facebook_likes_vector, imdb_score_vector, facebook_likes_name, imdb_score)
	#plot2D(budget_vector, imdb_score_vector, budget_name, imdb_score)
	#plot_points(facebook_likes_vector, budget_vector, imdb_score_vector, facebook_likes_name, budget_name)
	plot_points(facebook_likes_vector, critics_reviews_vector, imdb_score_vector, facebook_likes_name, critics_reviews_name)
		 	

#test_reading_table()
#test_get_Labels()
#test_get_colors()
#test_num_critic_for_reviews()
#test_get_duration()
#test_director_facebook_likes()
#test_num_voted_users()

#print normalize([1,2,4])

#get_movie_titles()
generate_plots()
