import csv
from knn import KNearestNeighbour
from naive_bayes import NaiveBayes
from cross_validation import *

def main():
	# List of patient objects
	patient_list = parse_csv()

	# create the ten folds
	ten_folds_strat_list = stratify_data(patient_list)

	# create the classifer objects
	knn = KNearestNeighbour()
	naive_bayes = NaiveBayes()

	# call the 10-fold cross validation
	ten_fold_strat_cross_validation(knn, ten_folds_strat_list, 10)
	ten_fold_strat_cross_validation(naive_bayes, ten_folds_strat_list)

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

if __name__ == "__main__":
    main()