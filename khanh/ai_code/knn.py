import copy
from math import sqrt
from operator import itemgetter

class KNearestNeighbours():
	def __init__(self, training_data):
		self.training_data = copy.deepcopy(training_data)
		
	def on(self, test_patient, k):
		# Eucledian distance
		# D(A,B) = sqrt((a1-b1)^2 + (a2-b2)^2 + ... + (an-bn)^2)

		for patient in self.training_data:
			inner_sum = 0
			for attr in patient:
				if attr != 'class' and attr != 'distance':
					inner_sum += (test_patient[attr] - patient[attr])**2
			patient['distance'] = sqrt(inner_sum)

		# sort the list by distance calculated
		sorted_list = sorted(self.training_data, key=itemgetter('distance')) 

		# only take the nearest k
		class0_counter = 0
		class1_counter = 0

		for neighbour in sorted_list[:k]:
			if neighbour['class'] == "class0":
				class0_counter += 1
			elif neighbour['class'] == "class1":
				class1_counter += 1

		if class0_counter == class1_counter:
			#TODO: decide on a tie breaker method
			return "Tie. Deal with it."
		elif class0_counter > class1_counter:
			return "class0"
		elif class1_counter > class0_counter:
			return "class1"

	def _cleanup(self):
		for instance in self.training_data:
			del instance['distance']