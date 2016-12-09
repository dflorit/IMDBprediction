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
	#print rows[0]
	
	#print len(feature_list)
	#print len(feature_name_to_number)
	#print feature_name_to_number
	
	
	d = {}
	for e in feature_list:
		if e not in d:
			d[e] = 1
		else:
			d[e] += 1
	
	for e in d:
		if d[e] > 1:
			print e
	#print headers
	#print rows[3]
	#print len(rows[3])
	'''
	print '------------------------------------------------'
	for row in rows:
		for e in row:
			if e == '':
				print row
				print e
	'''
test_reading_table()
