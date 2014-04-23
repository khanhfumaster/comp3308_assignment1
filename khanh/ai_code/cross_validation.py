import copy

# Divide up the instance into 10 equal sets with the same class ratio as the original data.
# Leftovers are equally distributed to the sets
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

# 10-fold stratified cross validation
def ten_fold_strat_cross_validation(classifer, data, k=None):
	ten_folds_data = copy.deepcopy(data)

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

		correct = 0.0
		incorrect = 0.0

		for instance in testing_data:
			expected_class = instance['class']
			del instance['class']

			predicted_class = classifer.on(instance)

			instance['class'] = predicted_class

			if predicted_class == expected_class:
				correct += 1
			else:
				incorrect += 1

		accuracy = 100 * correct/(correct+incorrect)

		print "correct: ", correct
		print "incorrect: ", incorrect
		print "success rate: ", accuracy

		# new line
		print ""