from random import *

class Data:
	def __init__(self):
		self.length = 0
		self.feature_vectors = []
		self.labels = []
		self.predictions = []
		self.feature_names = []
		self.numeric_labels = []
	
	#feature_vectors = [phi(I1), phi(I2),...,phi(In)]
	def set_feature_vectors(self, feature_vectors):
		self.length = len(feature_vectors)
		self.feature_vectors = feature_vectors
	
	def get_feature_vectors(self):
		return self.feature_vectors
	
	
	#labels = [l1,l2,...,ln]
	def set_labels(self, labels):
		self.length = len(labels)
		self.labels = labels
	
	def get_labels(self):
		return self.labels
		
	
	#numeric_labels = [l1,l2,...,ln]
	def set_numeric_labels(self, numeric_labels):
		self.length = len(numeric_labels)
		self.numeric_labels = numeric_labels
	
	def get_numeric_labels(self):
		return self.numeric_labels
		
	#predictions = [p1, p2, ...., pn]
	def set_predictions(self, predictions):
		self.length = len(predictions)
		self.predictions = predictions	
	
	def get_predictions(self):
		return self.predictions
		
	
	#feature names = [feature_1_name_str, feature_2_name_str, ...]	
	def set_feature_names(self, feature_names):
		self.length = len(feature_names)
		self.feature_names = feature_names
	
	def get_feature_names(self):
		return self.feature_names

	def get_length(self):
		return self.length
	
	def __str__(self):
		string = ''
		string += 'length: ' + str(self.length) + '\n \n'
		string += 'feature_names: ' + str(self.feature_names) + '\n \n'
		string += 'feature_vectors: ' + str(self.feature_vectors) + '\n \n'
		string += 'labels: ' + str(self.labels) + '\n \n'
		string += 'predictions: ' + str(self.predictions) + '\n \n'
		
		return string




class Statistics:

	def __init__(self, data, label_to_number):
		self.labels = data.get_labels()
		self.predictions = data.get_predictions()
		self.length = data.get_length()
		self.label_to_number = label_to_number
		self.calculate_confusion_matrix()
		self.calculate_accuracy()
	
	def calculate_confusion_matrix(self):
		self.confusion_matrix = {}
		
		for labels in self.label_to_number:
			for predictions in self.label_to_number:
				self.confusion_matrix[(labels, predictions)] = 0.0
		
		for i in range(len(self.labels)):
			self.confusion_matrix[(self.labels[i], self.predictions[i])] += 1.0
	
	def calculate_accuracy(self):
		total = 0
		self.accuracy = 0
		for (label, prediction) in self.confusion_matrix:
			total += self.confusion_matrix[(label, prediction)]
			if label == prediction:
				self.accuracy += self.confusion_matrix[(label, prediction)]
		
		if total == 0:
			total = 0.00001
		self.accuracy = 1.0* self.accuracy / total
		
	
	def get_statistics(self):
		return {'Accuracy': self.accuracy}

	
# ---------------------------Useful functions related to Data ---------------------------

# Split Data instance into data_training and data_testing, given a percentage for training
# returns two instances of Data: data_training and data_testing
def split_data(data, percentage_training):
	length_data = data.get_length()
	length_training_data = int(percentage_training * length_data)
	feature_names = data.get_feature_names()
	data_training = Data()
	data_testing = Data()
	
	if length_data == 0:
		return data_training, data_testing
	
	#shuffle data:
	shuffled_indices = [i for i in range(length_data)]
	shuffle(shuffled_indices)
	
	#Getting variables and shuffling them
	feature_vectors = [data.get_feature_vectors()[i] for i in shuffled_indices if len(data.get_feature_vectors()) != 0]
	labels = [data.get_labels()[i] for i in shuffled_indices if len(data.get_labels()) != 0]
	predictions = [data.get_predictions()[i] for i in shuffled_indices if len(data.get_predictions()) != 0]
	
	
	#splitting variable content
	feature_vectors_training = [feature_vectors[i] for i in range(length_data) if i <= length_training_data if feature_vectors != []]
	feature_vectors_testing = [feature_vectors[i] for i in range(length_data) if i > length_training_data if feature_vectors != []]
	
	labels_training = [labels[i] for i in range(length_data) if i <= length_training_data if labels != []]
	labels_testing = [labels[i] for i in range(length_data) if i > length_training_data if labels != []]
	
	predictions_training = [predictions[i] for i in range(length_data) if i <= length_training_data if predictions != []]
	predictions_testing = [predictions[i] for i in range(length_data) if i > length_training_data if predictions != []]
	
	
	feature_names_training = feature_names
	feature_names_testing = feature_names
	
	
	data_training.set_feature_vectors(feature_vectors_training)
	data_training.set_labels(labels_training)
	data_training.set_predictions(predictions_training)
	data_training.set_feature_names(feature_names_training)
	
	data_testing.set_feature_vectors(feature_vectors_testing)
	data_testing.set_labels(labels_testing)
	data_testing.set_predictions(predictions_testing)
	data_testing.set_feature_names(feature_names_testing)
	

	return data_training, data_testing


def split_data_by_labels(data):
	length_data = data.get_length()
	feature_names = data.get_feature_names()
	data_with_labels = Data()
	data_without_labels = Data()
	
	if length_data == 0:
		return data_with_labels, data_without_labels
	
	
	#getting variables
	labels = data.get_labels()
	numeric_labels = data.get_numeric_labels()
	
	labels_with = []
	numeric_labels_with = []
	
	labels_without = []
	numeric_labels_without = []
	
	for i in range(len(labels)):
		if labels[i] == None:
			labels_without.append(labels[i])
			numeric_labels_without.append(numeric_labels[i])
		else:
			labels_with.append(labels[i])
			numeric_labels_with.append(numeric_labels[i])
	
	data_with_labels.set_labels(labels_with)
	data_with_labels.set_numeric_labels(numeric_labels_with)
	
	
	data_without_labels.set_labels(labels_without)
	data_without_labels.set_numeric_labels(numeric_labels_without)
	
	return data_with_labels, data_without_labels 
