"""
This function get various parameters to calculate the percent of defendants.

>>> defendants_percent("w","n","High")
'23.5%'

>>> defendants_percent("w","y","Low")
'47.7%'

>>> defendants_percent("b","n","High")
'44.8%'

>>> defendants_percent("b","y","Low")
'28.0%'

"""

from read_data import read_data
from Logic import *

dic = read_data()  # Content the output of the other file with all defendants information


def defendants_percent(r: str, o: str, s: str) -> float:

    offend = []
    r_defendant = []
    amount_defendant = []

    """Take the r_defendant list and insert in it all the defendants of that race"""
    if r == "w":
        for white in dic:  # Analyze each defendant in the csv file who is white
            if white['race'] == "Caucasian":
                r_defendant.append(white)  # add the people to the r_defendant list
    else:
        for black in dic:  # Analyze each defendant in the csv file who is black
            if black['race'] == "African-American":
                r_defendant.append(black)  # add the people to the r_defendant list

    """ Analyze who did or did not re-offended and add them to the offend list"""
    if o == 'y':
        for offended in r_defendant:  # Analyze each defendant in the r_defendant list who re-offended
            if offended['two_year_recid'] != '0':
                offend.append(offended)  # add the people to the 'offend' list
    else:
        for offended in r_defendant:
            if offended['two_year_recid'] == '0':  # Analyze each defendant in the r_defendant list who did not re-offended
                offend.append(offended)  # add the people to the 'offend' list

    """ Separate who were classify as Low or High
    People who got a 'Medium' risk level were mixed with the 'High' ones """
    if s == "Low":
        for defendant in offend:
            if defendant['score_text'] == s:  # Analyze each defendant in the 'offend' list who have a 'Low' risk level
                amount_defendant.append(defendant)  # add the people to the 'amount_defendant' list
    else:
        for defendant in offend:
            if defendant['score_text'] == s or defendant['score_text'] == "Medium":  # Analyze each defendant in the 'offend' list who have a 'High' or 'Medium' risk level
                amount_defendant.append(defendant)  # add the people to the 'amount_defendant' list

    """This part take all the information before and calculate the percentage"""
    percentage = (len(amount_defendant) / len(offend)) * 100  # Calculate the percentage by dividing the length of
    # amount-defendant list with the length of offend list
    percentages = round(percentage * 10) / 10  # This round the number to the first tenth
    percentages = str(percentages)  # Convert the number in a string to later can add the '%'
    return percentages + "%"
