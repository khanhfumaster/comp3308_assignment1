import csv
from knn import KNearestNeighbours
from naive_bayes import NaiveBayes

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

def main():

	# List of patient objects
	patient_list = parse_csv()

	# for patient in patient_list:
	# 	print patient

	test_patient = {'age': 0.016667, 'bmi': 0.265849, 'diabetes_pedigree_function': 0.471392, 'plasma_glucose_concentration': 0.593548, '2h_serum_insulin': 0.17013, 'diastolic_blood_pressure': 0.469388, 'num_pregnant': 0.235294, 'tricep_skin_fold_pressure': 0.240793}
	
	knn1 = KNearestNeighbours(patient_list)

	print knn1.on(test_patient, 10)
	
	nb1 = NaiveBayes(patient_list)

	print nb1.on(test_patient)

if __name__ == "__main__":
    main()