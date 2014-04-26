import copy

# Divide up the instance into 10 equal sets with the same class ratio as the original data.
# Leftovers are equally distributed to the sets
def stratify_data(csv_data, csv_filename):
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

	# output the list to a pima-folds.csv
	filename = csv_filename.replace(".csv", "-folds.csv")

	with open(filename, 'wb') as output_file:
		for idx, fold in enumerate(stratified_lists):			
			fold_str = 'fold ' + str(idx + 1)
			output_file.write(fold_str)
			output_file.write('\n')

			for instance in fold:
				for i, attr in enumerate(instance):
					if (i != 0):
						output_file.write(',')
					output_file.write(str(instance[attr]))
					
				output_file.write('\n')

			if (idx != 9):
				output_file.write('\n')

	return stratified_lists

# 10-fold stratified cross validation
def ten_fold_strat_cross_validation(classifer, data, k=None):
	title = classifer.type + " 10-fold stratified cross validation"
	if k is not None:
		title += ", k=" + str(k)

	print "--------------------------------------------------------"
	print title
	print "--------------------------------------------------------"

	ten_folds_data = copy.deepcopy(data)

	accuracy_sum = 0.0
	total_correct = 0
	total_incorrect= 0

	for x in range(0, 10):
		# one fold 
		testing_fold_id = 9 - x
		testing_data = copy.deepcopy(ten_folds_data[testing_fold_id])
		# the nine folds for training
		training_data = []

		for i in range(0, 10):
			if i != testing_fold_id:
				for instance in ten_folds_data[i]:
					training_data.append(instance)

		classifer.training_data = training_data
		if k is not None:
			classifer.k = k

		print "fold" + str(x+1)
		# add new line (use writeline)

		correct = 0
		incorrect = 0

		for instance in testing_data:
			expected_class = instance['class']
			del instance['class']

			predicted_class = classifer.on(instance)

			instance['class'] = predicted_class

			if predicted_class == expected_class:
				correct += 1
			else:
				incorrect += 1

		accuracy = 100 * float(correct)/(float(correct)+float(incorrect))
		accuracy_sum += accuracy
		total_correct += correct
		total_incorrect += incorrect

		print "Correct: ", correct
		print "Incorrect: ", incorrect
		print "Total: ", str(correct + incorrect)
		print "Accuracy: ", str(round(accuracy, 4)) + '%'


		# new line
		print ""


	average_accuracy = accuracy_sum/10
	print "---- Summary ----"
	print "Correctly Classified Instances: ", total_correct
	print "Incorrectly Classified Instances: ", total_incorrect
	print "Total Instances: ", str(total_correct + total_incorrect)
	print "Average Accuracy: ", str(round(average_accuracy, 4)) + '%'
	print ""