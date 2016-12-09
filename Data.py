from random import *
from numpy import *

class Data:
	def __init__(self):
		self.length = 0
		self.feature_vectors = []
		self.labels = []
		self.predictions = []
		self.feature_names = []
		self.numeric_labels = []
		self.table_ids = []
	
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
	
	#ids from table. this would be the movie title
	def set_table_ids(self, table_ids):
		self.length = len(table_ids)
		self.table_ids = table_ids
	
	def get_table_ids(self):
		return self.table_ids
	
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
		string += 'table_ids: ' + str(self.table_ids) + '\n \n'
		string += 'feature_names: ' + str(self.feature_names) + '\n \n'
		string += 'feature_vectors: ' + str(self.feature_vectors) + '\n \n'
		string += 'labels: ' + str(self.labels) + '\n \n'
		string += 'predictions: ' + str(self.predictions) + '\n \n'
		
		return string

class Statistics:

	def __init__(self, data, posible_labels):
		self.labels = data.get_labels()
		self.predictions = data.get_predictions()
		self.length = data.get_length()
		self.posible_labels = posible_labels
		self.calculate_confusion_matrix()
		self.get_metrics()
	
	def calculate_confusion_matrix(self):
		self.confusion_matrix = {}
		
		for labels in self.posible_labels:
			for predictions in self.posible_labels:
				self.confusion_matrix[(labels, predictions)] = 0.0
		
		for i in range(self.length):
			self.confusion_matrix[(self.labels[i], self.predictions[i])] += 1.0
		
	
	def get_metrics(self):
		
		accuracy = 0
		TP = zeros(10)
		TN = zeros(10)
		FP = zeros(10)
		FN = zeros(10)
		precision = zeros(10)
		sensitivity = zeros(10)
		specificity = zeros(10)
		
		for i in range(self.length): #possible classes Ground Truth 
			TP[i] = self.confusion_matrix[(i+1,i+1)]
			TN[i] = sum([self.confusion_matrix[x,y] for x in range(1,self.length+1) for y in range(1,self.length+1) if x != (i+1) if y != (i+1)])
			FP[i] = sum([self.confusion_matrix[x,y] for x in range(1,self.length+1) for y in range(1,self.length+1) if x != (i+1) if y == (i+1)])
			FN[i] = sum([self.confusion_matrix[x,y] for x in range(1,self.length+1) for y in range(1,self.length+1) if x == (i+1) if y != (i+1)])
			
			#to avoid dividing by zero:
			if TP[i] == 0: TP[i] = 0.0001
			if TN[i] == 0: TN[i] = 0.0001
			if FP[i] == 0: FP[i] = 0.0001
			if FN[i] == 0: FN[i] = 0.0001
			
			#calculating precision, specificity and sensitivity for each class:
			precision[i] = 1.0*TP[i] / (1.0*(TP[i] + FP[i]))
			sensitivity[i] = 1.0*TP[i] / (1.0*(TP[i] + FN[i]))
			specificity[i] = 1.0*TN[i] / (1.0*(TN[i] + FP[i]))
		
		
		#Metrics
		self.accuracy = 1.0 * (sum(TP) + sum(TP)) / (sum(TP) + sum(TP) + sum(FP) + sum(FN))
		self.averagePrecision = 1.0*sum(precision) / self.length
		self.averageSensitivity = 1.0*sum(sensitivity) / self.length
		self.averageSpecificity = 1.0*sum(specificity) / self.length
		
	
	def get_statistics(self):
		return {'Accuracy': self.accuracy, 'Average Precision': self.averagePrecision, 'Average Sensitivity': self.averageSensitivity, \
		'Average Specificity': self.averageSpecificity}

	
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
	table_ids = [data.get_table_ids()[i] for i in shuffled_indices if len(data.get_table_ids()) != 0]
	
	#splitting variable content
	feature_vectors_training = [feature_vectors[i] for i in range(length_data) if i <= length_training_data if feature_vectors != []]
	feature_vectors_testing = [feature_vectors[i] for i in range(length_data) if i > length_training_data if feature_vectors != []]
	
	labels_training = [labels[i] for i in range(length_data) if i <= length_training_data if labels != []]
	labels_testing = [labels[i] for i in range(length_data) if i > length_training_data if labels != []]
	
	predictions_training = [predictions[i] for i in range(length_data) if i <= length_training_data if predictions != []]
	predictions_testing = [predictions[i] for i in range(length_data) if i > length_training_data if predictions != []]
	
	table_ids_training = [table_ids[i] for i in range(length_data) if i <= length_training_data if table_ids != []]
	table_ids_testing = [table_ids[i] for i in range(length_data) if i > length_training_data if table_ids != []]
	
	
	feature_names_training = feature_names
	feature_names_testing = feature_names
	
	
	data_training.set_feature_vectors(feature_vectors_training)
	data_training.set_labels(labels_training)
	data_training.set_predictions(predictions_training)
	data_training.set_feature_names(feature_names_training)
	data_training.set_table_ids(table_ids_training)
	
	data_testing.set_feature_vectors(feature_vectors_testing)
	data_testing.set_labels(labels_testing)
	data_testing.set_predictions(predictions_testing)
	data_testing.set_feature_names(feature_names_testing)
	data_testing.set_table_ids(table_ids_testing)
	

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
