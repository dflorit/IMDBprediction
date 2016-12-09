import warnings
from Data import Data
from sklearn import *
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier
from Utils import *
from theano import *
import theano.tensor as T

#Use: train() predict()	
class Classifier(object):

	def __init__(self):
		self.training_data = None
		self.testing_data = None
		self.trained = False
	
	def set_training_data(self, training_data):
		self.training_data = training_data
	
	def get_training_data(self):
		return self.training_data
		
	def set_testing_data(self, testing_data):
		self.testing_data = testing_data
	
	def get_testing_data(self):
		return self.testing_data
	
	#No input no output
	def train(self): raise NotImplementedError('Override me')
	
	#returns testing_data with set predictions!!
	def predict(self): raise NotImplementedError('Override me')
	
#-------------------------Implement Classifiers-----------------------------------

#SVM implementation using svm.SVC()
class SVC_Classifier(Classifier):
	def __init__(self):
		super(SVC_Classifier, self).__init__()
		self.clf = svm.SVC()
		
		#parameters
		self.kernel = 'linear'#linear
		self.degree = 3
		self.verbose = False
		self.C = 1.0
		self.probability = False
		self.shrinking = True
		self.max_iter = -1
		self.decision_function_shape = None
		self.random_state = None
		self.tol = 0.001
		self.cache_size = 200
		self.coef0 = 0.0 
		self.gamma = 'auto'
		self.class_weight = None

	def train(self):
		feature_vectors_training = self.training_data.get_feature_vectors()
		labels_training = self.training_data.get_labels()
		self.clf.fit(feature_vectors_training, labels_training)
	
	def predict(self):
		feature_vectors_testing = self.testing_data.get_feature_vectors()
		predictions = self.clf.predict(feature_vectors_testing)
		self.testing_data.set_predictions(predictions)
		return predictions
	
	def get_parameters(self):
		return self.clf.get_params()
	
	#setters for different parameters. This does not set the parameters on the classifier
	#just the global variables for the class
	def set_kernel(self, kernel):
		self.kernel = kernel
		
	def set_degree(self, degree):
		self.degree = degree
		
	def set_random_state(self, random_state):
		self.random_state = random_state
	
	#this function applies all changes to the parameters in the classifier
	def set_parameters(self):
		
		params = dict(C= self.C, kernel = self.kernel, degree = self.degree, \
		gamma = self.gamma, coef0 = self.coef0, shrinking= self.shrinking, \
		probability = self.probability, tol= self.tol, cache_size = self.cache_size, \
		class_weight = self.class_weight, verbose = self.verbose, max_iter= self.max_iter,\
		decision_function_shape = self.decision_function_shape, random_state = self.random_state)
		
		self.clf.set_params(**params)

#Neural Network implementation using MLPClassifier()
class NN_Classifier(Classifier):
	def __init__(self):
		super(NN_Classifier, self).__init__()
		self.clf = MLPClassifier()
		
		# default parameters
		self.activation='relu'
		self.alpha=1e-05
		self.batch_size='auto'
		self.beta_1=0.9
		self.beta_2=0.999
		self.early_stopping=False
		self.epsilon=1e-08
		self.hidden_layer_sizes=(130,2)#(5,2)
		self.learning_rate='constant'
		self.learning_rate_init=0.001
		self.max_iter=-1
		self.momentum=0.9
		self.nesterovs_momentum = True
		self.power_t = 0.5
		self.random_state = 1
		self.shuffle = True
		self.solver = 'lbfgs'
		self.tol=0.0001
		self.validation_fraction=0.1
		self.verbose=False
		self.warm_start=False
		
		self.params = dict( activation = self.activation, alpha = self.alpha, \
		batch_size = self.batch_size, beta_1 = self.beta_1, beta_2 = self.beta_2, \
		early_stopping = self.early_stopping, epsilon = self.epsilon, \
		hidden_layer_sizes = self.hidden_layer_sizes, learning_rate = self.learning_rate, \
		learning_rate_init = self.learning_rate_init, max_iter = self.max_iter, \
		momentum = self.momentum, nesterovs_momentum = self.nesterovs_momentum, \
		power_t = self.power_t, random_state = self.random_state, shuffle = self.shuffle, \
		solver = self.solver, tol = self.tol, validation_fraction = self.validation_fraction, \
		verbose = self.verbose, warm_start = self.warm_start)
		
	def train(self):
		feature_vectors_training = self.training_data.get_feature_vectors()
		labels_training = self.training_data.get_labels()
		self.clf.fit(feature_vectors_training, labels_training)
	
	def predict(self):
		feature_vectors_testing = self.testing_data.get_feature_vectors()
		predictions = self.clf.predict(feature_vectors_testing)
		self.testing_data.set_predictions(predictions)
		return predictions
	
	def get_parameters(self):
		return self.params
	
	#setters for different parameters. This does not set the parameters on the classifier
	#just the global variables for the class
	def set_hidden_layer_sizes(self, hidden_layer_sizes):
		self.hidden_layer_sizes = hidden_layer_sizes
		
	def set_tol(self, tol):
		self.tol = tol
		
	def set_alpha(self, alpha):
		self.alpha = alpha
	
	#this function applies all changes to the parameters in the classifier
	def set_parameters(self):
		self.clf.set_params(**self.params)

#Random forest implementation using 
class RF_Classifier(Classifier):
	def __init__(self):
		super(RF_Classifier, self).__init__()
		self.clf = RandomForestClassifier()

	def train(self):
		feature_vectors_training = self.training_data.get_feature_vectors()
		labels_training = self.training_data.get_labels()
		self.clf.fit(feature_vectors_training, labels_training)
	
	def predict(self):
		feature_vectors_testing = self.testing_data.get_feature_vectors()
		predictions = self.clf.predict(feature_vectors_testing)
		self.testing_data.set_predictions(predictions)
		return predictions
		
#Logistic Regression
class LR_Classifier(Classifier):
	def __init__(self):
		super(LR_Classifier, self).__init__()
		self.thetas = None
		self.alpha = None
		self.iterations = None
	
	def train_one(self, input_x, input_y):

		classes = unique(input_y)

		n_classes = 10 #unique(input_y).shape[0]

		n_instances, n_feats = input_x.shape

		n_epoches = 1200

		

		train_x = input_x.astype('int32')

		train_y = zeros(n_instances).astype('int32')

		

		for i in range(n_instances):

			train_y[i] = input_y[i]

		
		x = T.matrix("x")
		y = T.ivector("y")
		w = shared(random.randn(n_feats,n_classes), name="w")
		b = shared(zeros(n_classes), name="b")
		
		# construct Theano expression graph
		p_y_given_x = T.nnet.softmax(T.dot(x, w) + b)
		xent = -T.mean(T.log(p_y_given_x)[T.arange(n_instances), y])
		cost = xent + 0.01 * (w ** 2).sum()       # The cost to minimize
		gw, gb = T.grad(cost, [w, b])             # Compute the gradient of the cost
		y_pred = T.argmax(p_y_given_x, axis=1)
		error = T.mean(T.neq(y_pred, y))

		#compile
		train = function(inputs=[x,y], outputs=[error, cost], updates=((w, w - 0.1 * gw), (b, b - 0.1 * gb)))
		
		#train
		#print "Training:" 
		for i in range(n_epoches):
			error, cost = train(train_x, train_y)
			
		self.trained = True
		#print "---- w ", w.get_value()
		#print "---- b ", b.get_value()
		return w.get_value(), b.get_value()
    	
	def predict_one(self, input_x, w, b):
		if self.trained == False:
			raise ValueError("Model not trained. Cannot test")
			return 0
		else:
			n_instances, n_feats = input_x.shape
			test_x = input_x.astype('int32')
			
			x = T.matrix("x")
			y = T.ivector("y")
			w = shared(w, name="w")
			b = shared(b, name="b")
			
			p_y_given_x = T.nnet.softmax(T.dot(x, w) + b)
			
			test = function([x], p_y_given_x)
			
			probability_matrix = test(test_x)
			
			p_y1_given_x = zeros(n_instances)
			
			for i in range(n_instances):
				p_y1_given_x[i] = probability_matrix[i][1]
			
			return p_y1_given_x
	
	
	
	def train(self):
		number_classes = len(set(list(self.training_data.get_labels())))
		self.thetas = []
		self.bias = []
		f_vectors = self.training_data.get_feature_vectors()
		original_labels = self.training_data.get_labels()
		multiple_class_labels = []
		self.classes = []
		
		for i in range(min(original_labels), max(original_labels)+1):
			new_labels = []
			self.classes.append(i)
			for label in original_labels:
				if i == label:
					new_labels.append(1)
				else:
					new_labels.append(0)
			multiple_class_labels.append(new_labels)
		
		multiple_class_labels = array(multiple_class_labels)
		
		for class_labels in multiple_class_labels:
			theta, b = self.train_one(f_vectors, class_labels)
			self.thetas.append(theta)
			self.bias.append(b)
		
		
		
	
	def predict(self):
		xs_vectors = self.testing_data.get_feature_vectors()
		
		probabilities = []
		#print "w ", self.thetas
		#print "b ", self.bias
		for x_vector in xs_vectors:
			probability = []
			for i in range(len(self.thetas)):
				#print i
				#print array([x_vector])
				#print self.thetas[i]
				#print "bias ", self.bias[i]
				probability.append(self.predict_one(array([x_vector]), self.thetas[i], self.bias[i])[0])
			probabilities.append(probability)
		
		probabilities = array(probabilities)
		predictions = []
		
		for probability in probabilities:
			predictions.append(self.classes[argmax(probability)])
		
		self.testing_data.set_predictions(predictions)
		return predictions
		
	
	def get_parameters(self):
		return {'alpha':self.alpha, 'iterations':self.iterations}
	
	def get_theta_values(self):
		return self.thetas
		
	def set_iterations(self, iterations):
		self.iterations = iterations
		
	def set_alpha(self, alpha):
		self.alpha = alpha

def find_mode(l):
	count = {}
	
	for e in l:
		if e not in count:
			count[e] = 1
		else:
			count[e] +=1
	
	mode = None
	max = -1
	for key in count:
		if count[key] > max:
			max = count[key]
			mode = key
	return mode

def get_mode(training_data, testing_data):
	print "classifying with SVM"
	classifier_svm = SVC_Classifier()
	classifier_svm.set_training_data(training_data)
	classifier_svm.set_testing_data(testing_data)
	classifier_svm.train()
	predictions_svm = classifier_svm.predict()
	
	print "classifying with NN"
	classifier_nn = NN_Classifier()
	classifier_nn.set_training_data(training_data)
	classifier_nn.set_testing_data(testing_data)
	classifier_nn.train()
	predictions_nn = classifier_nn.predict()
	
	print "classifying with RF"
	classifier_rf = RF_Classifier()
	classifier_rf.set_training_data(training_data)
	classifier_rf.set_testing_data(testing_data)
	classifier_rf.train()
	predictions_rf = classifier_rf.predict()
	
	#print "classifying with LR"
	#classifier_lr = LR_Classifier()
	#classifier_lr.set_training_data(training_data)
	#classifier_lr.set_testing_data(testing_data)
	#classifier_lr.train()
	#predictions_lr = classifier_lr.predict()
	
	predictions = []
	
	for i in range(len(predictions_nn)):
		predictions.append(find_mode([predictions_nn[i], predictions_svm[i], predictions_rf[i]]))
		#predictions.append(find_mode([predictions_lr[i], predictions_nn[i], predictions_svm[i], predictions_rf[i]]))
	return predictions
	
		
		
		
