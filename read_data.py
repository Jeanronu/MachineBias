" This code read the information in the compas-score.csv file and turn it in a list of dictionaries"

import csv


def read_data():
    csv_file = 'compas-scores.csv'
    with open(csv_file) as f:
        reader = csv.DictReader(f)
        list_defendants = []

        for row in reader:
            list_defendants.append(row)
        return list_defendants


print(read_data())
