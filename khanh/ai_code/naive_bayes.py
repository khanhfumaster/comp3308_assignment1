import copy
import numpy
from math import sqrt, exp, pi

class NaiveBayes():
	def on(self, test_patient):
		# Let E be test_patient
		# P(class0|E) = (P(E1|class0)P(E2|class0)P(E3|class0)P(E4|class0)P(class0))/P(E)
		# calculate the numerator only since P(E) will be same in comparison

		results = {}

		for klass in ['class0', 'class1']:
			numerator = self._p_class(klass)

			for attr in test_patient:
				numerator *= self._p_e_class(attr, test_patient[attr], klass)

			results[klass] = numerator
		
		if results['class0'] > results['class1']:
			return 'class0'
		else:
			return 'class1' 

		# TODO tie breaker

	# P(E = x|class) = 1/(SD * sqrt(2*pi)) * exp(-(x-MEAN)^2/(2*SD^2)) 
	def _p_e_class(self, key, val, klass): 
		# find set which has key: key
		key_set = []
		for instance in self.training_data:
			if instance['class'] == klass:
				key_set.append(instance[key])

		arr = numpy.array(key_set)
		
		# find the mean
		mean = numpy.mean(arr)

		# find the standard deviation
		std = numpy.std(arr)

		# calculate probability
		return 1/(std * sqrt(2*pi)) * exp(-((val-mean)**2)/((2*std)**2)) 
		
	# P(class)
	def _p_class(self, klass):
		class_count = 0.0
		total_count = float(len(self.training_data))
		for instance in self.training_data:
			if instance['class'] == klass:
				class_count += 1
		return class_count/total_count


