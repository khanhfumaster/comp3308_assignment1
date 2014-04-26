import sys
import csv
import os.path
from knn import KNearestNeighbour
from naive_bayes import NaiveBayes
from cross_validation import *

def main():
	if (len(sys.argv) > 1):
		csv_filename = sys.argv[1]

		# check if the file exists
		if os.path.isfile(csv_filename):
			# List of patient objects
			patient_list = parse_csv(csv_filename)

			# create the ten folds
			ten_folds_strat_list = stratify_data(patient_list, csv_filename)

			# create the classifer objects
			knn = KNearestNeighbour()
			naive_bayes = NaiveBayes()

			# call the 10-fold cross validation
			ten_fold_strat_cross_validation(knn, ten_folds_strat_list, 1)
			ten_fold_strat_cross_validation(knn, ten_folds_strat_list, 5)
			ten_fold_strat_cross_validation(naive_bayes, ten_folds_strat_list)
		else:
			print "File does not exist."	
	else:
		print "Please provide a filepath to the csv file."

def parse_csv(filename):
	patients = []

	# Read the file
	with open(filename, 'rb') as csvfile:
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