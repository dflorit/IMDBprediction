import sys

from Data import *
from Classifiers import *
from Utils import *
from FeatureExtractors import *

#python main.py classifier featre_extractor

#classifier
svm = 'svm'
neural_nets = 'nn'
linear_r = 'lr'
random_forest = 'rf'
mode_classifier = 'mc'
classifiers = [svm, neural_nets, linear_r, random_forest, mode_classifier]

#Feature Extractors
numeric = 'numeric'
cast_director = 'cd'
all = 'all'
feature_extractors = [numeric, cast_director, all]

default_feature_extractor = numeric
default_classifier = mode_classifier #svm

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
		print "classifier is Mode"
		classifier = None
		
	return classifier

#returns testing and training data
def get_data(which_extractor):
	data = None
	FE = Feature_Extractors()

	if which_extractor == numeric:
		print "Numeric feature extractor"
		data = FE.numeric_feature_extractor(imdb_table_path)
	elif which_extractor == cast_director:
		data = None #TODO: change this
	elif which_extractor == all:
		data = None #TODO: change this
	
	training_data, testing_data = split_data(data, 0.80)
	
	return training_data, testing_data

def clasify(classifier, training_data, testing_data):
	predictions = None
	if classifier == None:
		print "classifier is mode"
		predictions = get_mode(training_data, testing_data)
		print "predictions"
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
print "stats:"
display_statistics(testing_data_with_predictions)


