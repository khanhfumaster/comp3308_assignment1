import csv
from knn import KNearestNeighbours

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

	test_patient = {'age': 0.99, 'bmi': 0.55, 'diabetes_pedigree_function': 0.8798798, 'plasma_glucose_concentration': 0.316129, '2h_serum_insulin': 0.4546, 'diastolic_blood_pressure': 0.469388, 'num_pregnant': 0.058824, 'tricep_skin_fold_pressure': 0.26087, 'class': 'class1'}
	
	knn1 = KNearestNeighbours(patient_list, test_patient, 10)


if __name__ == "__main__":
    main()