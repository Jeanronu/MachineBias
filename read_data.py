""" This code read the information in the compas-score.csv file and turn it in a list of dictionaries"""

import csv


def read_data():
    csv_file = 'compas-scores.csv'

    """Transform the data in dicts"""
    with open(csv_file) as f:  # open de file to work with it
        reader = csv.DictReader(f)  # convert each row of the csv in a dictionary
        list_defendants = []

        """Put the data in a list"""
        for row in reader:
            list_defendants.append(row)  # add the dictionaries to a list
        return list_defendants


print(read_data())  # it returns a list with various dictionaries inside
