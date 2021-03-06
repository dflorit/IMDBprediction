from Classifiers import *
from Data import *
from FeatureExtractors import *


def testing_prediction():
	#xs = array([[20,20],[10,10],[30,20],[10,20],[12,13],[50,50]])
	#ys = array([0,0,1,1,1,3])
	xs = array([[0,0],[1,1],[3,2],[21,20],[23,25],[50,50],[51,52],[-1,-2],[-3,-4],[-5,-6]])
	ys = array([4,4,4,1,1,2,2,3,3,3])

	training_data = Data()
	training_data.set_feature_vectors(xs)
	training_data.set_labels(ys)
	
	predictions = array([4,4,2,1,1,2,2,1,3,3])
	training_data.set_predictions(predictions)
	
	S = Statistics(training_data, posible_labels)
	print S.get_statistics()
	

	predict = array([[1,0], [2,1], [22,22], [52,52], [52,53], [53,53], [-1,-1],[-2,-2]])
	#expected_predictions = array([0,1])

	testing_data = Data()
	testing_data.set_feature_vectors(predict)

	classifier = SVC_Classifier()
	classifier.set_training_data(training_data)
	classifier.set_testing_data(testing_data)

	classifier.train()
	print classifier.predict()

	print get_mode(training_data, testing_data)
	
def test_reading_table():
	headers, rows = read_file(imdb_table_path)
	#print headers
	#print rows[0]
	for i in range(len(rows)):
		if rows[i][0] == '':
			print i
			print row
			
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

def testing_feature_extractor():
	FE = Feature_Extractors()
	D = FE.numeric_feature_extractor(imdb_table_path)
	print D

def testing_program_structure():
	FE = Feature_Extractors()
	D = FE.numeric_feature_extractor(imdb_table_path)
	D_training, D_testing = split_data(D, 0.80)
	
	predictions = get_mode(D_training, D_testing)
	D_testing.set_predictions(predictions)
	
	#classifier = LR_Classifier()
	#classifier.set_training_data(D_training)
	#classifier.set_testing_data(D_testing)
	#classifier.train()
	#predictions = classifier.predict()
	#D_testing.set_predictions(predictions)
	
	S = Statistics(D_testing, posible_labels)
	print S.get_statistics()

	
#test_reading_table()
#test_get_Labels()
#test_get_colors()
#test_num_critic_for_reviews()
#test_get_duration()
#test_director_facebook_likes()
#test_num_voted_users()
#print normalize([1,2,4])
#get_movie_titles()
#testing_prediction()
#testing_feature_extractor()
testing_program_structure()

