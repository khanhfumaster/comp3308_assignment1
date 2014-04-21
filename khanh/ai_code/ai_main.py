import csv
import copy
from knn import KNearestNeighbours
from naive_bayes import NaiveBayes

def main():

	# List of patient objects
	patient_list = parse_csv()


	# 10-fold stratified cross validation
	ten_folds_strat_list = stratify_data(patient_list)

	for x in range(0, 10):
		# one fold 
		testing_fold_id = 9 - x
		testing_data = copy.deepcopy(ten_folds_strat_list[testing_fold_id])
		# the nine folds for training
		training_data = []

		for i in range(0, 10):
			if i != testing_fold_id:
				for instance in ten_folds_strat_list[i]:
					training_data.append(instance)

		naivebayes1 = NaiveBayes(training_data)
		# knn1 = KNearestNeighbours(patient_list)

		print "fold" + str(x+1)

		correct = 0.0
		incorrect = 0.0

		for instance in testing_data:
			expected_class = instance['class']
			del instance['class']

			predicted_class = naivebayes1.on(instance)
			# predicted_class = knn1.on(instance, 10)

			if predicted_class == expected_class:
				correct += 1
			else:
				incorrect += 1

		print "correct: ", correct
		print "incorrect: ", incorrect
		print "success rate: ", 100*correct/(correct+incorrect)

		# new line
		print ""


def parse_csv():
	patients = []

	# Read the pima.csv file
	with open('pima.csv', 'rb') as csvfile:
		reader = csv.reader(csvfile)
		
		# store the headers
		headers = reader.next()

		for row in reader:
			d_row = {}
			
			for idx, value in enumerate(row):
				try:
					v = float(value)
				except ValueError:
					v = value

				k = headers[idx]
				d_row[k] = v

			patients.append(d_row)

	return patients

def stratify_data(csv_data):
	
	#split data by class
	class0_list = []
	class1_list = []

	for instance in csv_data:
		if instance['class'] == 'class0':
			class0_list.append(instance)
		elif instance['class'] == 'class1':
			class1_list.append(instance)

	class0_per_fold = len(class0_list)/10
	class1_per_fold = len(class1_list)/10

	stratified_lists = [] 

	# divide up the instances
	for i in range(0, 10):
		strat_list = []

		for j in range(0, class0_per_fold):
			strat_list.append(class0_list.pop())

		for j in range(0, class1_per_fold):
			strat_list.append(class1_list.pop())

		stratified_lists.append(strat_list)

	# deal with leftovers
	if len(class0_list) != 0:
		for i in range(0, len(class0_list)):
			stratified_lists[i].append(class0_list.pop())

	if len(class1_list) != 0:
		for i in range(0, len(class1_list)):
			stratified_lists[i].append(class1_list.pop())

	return stratified_lists

if __name__ == "__main__":
    main()