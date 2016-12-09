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
mode_classifier = 'mc'
classifiers = [svm, neural_nets, linear_r, mode_classifier]


#Feature Extractors
numeric = 'numeric'
cast_director = 'cd'
mode_feature_extractor = 'mf'
feature_extractors = [numeric, cast_director, mode_feature_extractor]

 
default_feature_extractor = numeric
default_classifier = svm

def get_classifier(which_classifier):
	classifier = None
	
	if which_classifier == neural_nets:
		classifier = NN_Classifier()
	elif which_classifier == svm:
		classifier = SVC_Classifier()
	elif which_classifier == linear_r:
		classifier = LR_Classifier()
	elif which_classifier == mode_classifier:
		print 'IDK'
		
	return classifier

#returns testing and training data
def get_data(which_extractor):
	data = None

	if which_extractor == numeric:
		print 'IDK'
	elif which_extractor == cast_director:
		print 'IDK'
	elif which_extractor == mode_feature_extractor:
		print 'IDK'
	
	training_data, testing_data = split_data(data, 0.80)
	
	return training_data, testing_data

def clasify(classifier, training_data, testing_data):
	print 'IDK'
#------------------------Main-----------------------------
classifier = sys.argv[1]
feature_extractor = sys.argv[2]

classifier = get_classifier(classifier)
training_data, testing_data = get_data(feature_extractor)
