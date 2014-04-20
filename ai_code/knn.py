from math import sqrt
from operator import itemgetter

class KNearestNeighbours():
	def __init__(self, patient_list, test_patient, k):
		self.patient_list = patient_list
		self.test_patient = test_patient
		self.k = k
		# run the calculate method
		self._calculate()
		
	def _calculate(self):
		# Eucledian distance
		# D(A,B) = sqrt((a1-b1)^2 + (a2-b2)^2 + ... + (an-bn)^2)

		for patient in self.patient_list:
			inner_sum = 0
			for attr in patient:
				# do check for numerical or nominal value
				if isinstance(self.test_patient[attr], str):
					if self.test_patient[attr] != patient[attr]:
						inner_sum += 1
				else:
					inner_sum += (self.test_patient[attr] - patient[attr])**2
			patient['distance'] = sqrt(inner_sum)

		# sort the list by distance calculated
		sorted_list = sorted(self.patient_list, key=itemgetter('distance')) 

		# only take the nearest k
		class0_counter = 0
		class1_counter = 0

		for neighbour in sorted_list[:self.k]:
			if neighbour['class'] == "class0":
				class0_counter += 1
			elif neighbour['class'] == "class1":
				class1_counter += 1

		if class0_counter == class1_counter:
			#TODO: decide on a tie breaker method
			print "Tie. Deal with it."
		elif class0_counter > class1_counter:
			print "class0"
		elif class1_counter > class0_counter:
			print "class1"