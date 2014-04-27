import copy
from math import sqrt
from operator import itemgetter
from random import randint

class KNearestNeighbour():		
	def __init__(self):
		self.type = 'KNearestNeighbour'

	def on(self, test_patient):
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

		for neighbour in sorted_list[:self.k]:
			if neighbour['class'] == "class0":
				class0_counter += 1
			elif neighbour['class'] == "class1":
				class1_counter += 1

		if class0_counter == class1_counter:
			self._cleanup()
			rand = randint(0, 1)
			if rand == 0:
				return 'class0'
			elif rand == 1:
				return 'class1'
		elif class0_counter > class1_counter:
			self._cleanup()
			return "class0"
		elif class1_counter > class0_counter:
			self._cleanup()
			return "class1"

	def _cleanup(self):
		for instance in self.training_data:
			del instance['distance']