import sys
from Data import *
from Classifiers import *
from Utils import *
from FeatureExtractors import *

#expected input:  python main.py classifier featre_extractor

#classifier
svm = 'svm'
neural_nets = 'nn'
linear_r = 'lr'
random_forest = 'rf'
mode_classifier = 'mc'
classifiers = [svm, neural_nets, linear_r, random_forest, mode_classifier]

#Feature Extractors
numeric = 'numeric'
non_numeric = 'non_numeric'
all = 'all'
feature_extractors = [numeric, non_numeric, all]

default_feature_extractor = numeric
default_classifier = mode_classifier #svm

#returns the classifier to be used, or None is the classifier is set to mode
def get_classifier(which_classifier):
	classifier = None
	
	if which_classifier == neural_nets:
		classifier = NN_Classifier()
	elif which_classifier == svm:
		classifier = SVC_Classifier()
	elif which_classifier == linear_r:
		classifier = LR_Classifier()
	elif which_classifier == random_forest:
		classifier = RF_Classifier()
	elif which_classifier == mode_classifier:
		classifier = None
			
	return classifier

#returns testing and training data
def get_data(which_extractor):
	data = None
	FE = Feature_Extractors()

	if which_extractor == numeric:
		data = FE.numeric_feature_extractor(imdb_table_path)
	elif which_extractor == non_numeric:
		data = FE.non_numeric_feature_extractor(imdb_table_path)
	elif which_extractor == all:
		data = FE.all_feature_extractor(imdb_table_path)
	
	training_data, testing_data = split_data(data, 0.80)
	return training_data, testing_data

def clasify(classifier, training_data, testing_data):
	predictions = None
	if classifier == None:
		predictions = get_mode(training_data, testing_data)
	else:
		classifier.set_training_data(training_data)
		classifier.set_testing_data(testing_data)
		classifier.train()
		predictions = classifier.predict()
	
	testing_data.set_predictions(predictions)
	return testing_data
	
def display_statistics(testing_data):
	S = Statistics(testing_data, posible_labels)
	stats = S.get_statistics()
	print "The Accuracy was: ", stats['Accuracy']
	print "The average Precision was: ", stats['Average Precision']
	print "The average Sensitivity was: ", stats['Average Sensitivity']
	print "The average Specificity", stats['Average Specificity']
	
#------------------------Main-----------------------------
if len(sys.argv) == 1:
	classifier = default_classifier
	feature_extractor = default_feature_extractor
else:
	classifier = sys.argv[1]
	feature_extractor = sys.argv[2]

classifier = get_classifier(classifier)
training_data, testing_data = get_data(feature_extractor)
testing_data_with_predictions = clasify(classifier, training_data, testing_data)
display_statistics(testing_data_with_predictions)


