import csv

def omit_missing(list):
	print "Omitting the missing instances in the " + str(len(list)) + " rows..."
	new_list = []
	for instance in list:
		
		if instance['plasma_glucose_concentration']!= 0 and \
		instance['diastolic_blood_pressure']!= 0 and \
		instance['tricep_skin_fold_pressure']!= 0 and \
		instance['2h_serum_insulin']!= 0 and \
		instance['bmi']!= 0 and \
		instance['diabetes_pedigree_function']!= 0:
			new_list.append(instance)


	print "Rows with missing values have been discarded."
	print "New list has " + str(len(new_list)) + " rows."

	return new_list


def average_missing(list, headers):
	print "assign average value for missing"
	# preprocessing of the headers
	# remove the nominal values and numerical values that can be 0 (i.e. not missing)
	headers.remove("num_pregnant")
	headers.remove("age")
	headers.remove("class")

	average_dict = calculate_average(list, headers)

	for header in headers:
		for instance in list:
			if instance[header] == 0:
				instance[header] = round(average_dict[header], 3)

	return list


def calculate_average(list, headers):
	print "calculating the average for attribute"

	average_dict = {}

	for header in headers:
		count = 0
		total = 0
		for instance in list:
			if instance[header] != 0:
				total += instance[header]
				count += 1

		average_dict[header] = total/count

	return average_dict


def output_csv(list, headers, tag):
	#todo
	filename = r'D:\Users\Jung\Desktop\Uni\comp3308\ass\jung\pima-indians-diabetes-' + tag + '.csv' 
	with open(filename, 'wb') as output_file:
		w = csv.DictWriter(output_file, headers)
		w.writeheader()
		for instance in list:
			w.writerow(instance)


def main():
	with open(r'D:\Users\Jung\Desktop\Uni\comp3308\ass\jung\pima-indians-diabetes.csv', 'rb') as csvfile:
		reader = csv.reader(csvfile)
		d=[]
		
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
			
			d.append(d_row)
		
		omitted_missing_list = omit_missing(d[:])
		output_csv(omitted_missing_list, headers, 'omit')

		averaged_missing_list = average_missing(d[:], headers[:])
		output_csv(averaged_missing_list, headers, 'avg')
		

if __name__ == "__main__":
    main()

    # this, is, it, can, hop, had, race, rabbit, run
