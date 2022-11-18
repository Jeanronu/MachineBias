"""
This file was for break down the problem. This file calculates the amount of prisioners depending on the fiters,
it also has a user interface, is not in the assigment.

>>> defendants_amount("b","n","Low")
('The amount of', 'black defendants', 'who', 'did not', 'offend with a', 'Low', 'risk is: ', 990)

>>> defendants_amount("","","")
('The amount of', 'all defendants', 'who', 'did and did not', 'offend is:', 7214)

>>> defendants_amount("", "y", "")
('The amount of', 'all defendants', 'who', 'did', 'offend is:', 3251)

>>> defendants_amount("w","","Low")
('The amount of', 'white defendants', 'who', 'did and did not', 'offend with a', 'Low', 'risk is: ', 1600)

>>> defendants_amount("b","y","")
('The amount of', 'black defendants', 'who', 'did', 'offend is:', 1901)

>>> defendants_amount("","y","High")
('The amount of', 'all defendants', 'who', 'did', 'offend with a', 'High', 'risk is: ', 2035)

>>> defendants_amount("w","n","High")
('The amount of', 'white defendants', 'who', 'did not', 'offend with a', 'High', 'risk is: ', 349)

>>> defendants_amount("w","n","Low")
('The amount of', 'white defendants', 'who', 'did not', 'offend with a', 'Low', 'risk is: ', 1139)

"""

from read_data import read_data
dic = read_data()  # Content the output of the other file with all defendants information


def defendants_race():
    def_race = "p"
    while def_race != "w" and def_race != "b" and def_race != "":  # this part star the while loop
        def_race = str(input("Type 'w' to look for White people percent or 'b' for Black people amount: "))
        if def_race != "w" and def_race != "b" and def_race != "":
            print("Sorry you have to answer w or b or leave it blank for all")

    return def_race


def re_offend():
    re_offended = 'p'
    while re_offended != "y" and re_offended != "n" and re_offended != "":  # this part star the while loop
        re_offended = str(input("Type 'n' to look for people who did not offended again and type 'y' if so: "))
        if re_offended != "n" and re_offended != "y" and re_offended != "":
            print("Sorry you have to answer y or n")

    return re_offended


def defendants_score():
    score = -1
    while not (-1 < score < 11):  # this part make sure that the score insert is > -1
        try:
            score = int(input("Insert the score you are looking for: "))
            if score < 0 or score > 10:  # always that the score is not in the range from 0 to 10 is going to repeat
                print("Sorry your score go out of the scale")
        except ValueError:
            print("The scale go from 0 to 10!!!")
    if -1 < score < 5:
        score = "Low"
        return score

    elif 4 < score < 11:
        score = 'High'
        return score


def defendants_amount(r: str, o: str, s: str) -> float:
    offend = []
    r_defendant = []
    amount_defendant = []

    if r == "":
        color = "all defendants"
        r_defendant = dic
    elif r == "w":
        color = "white defendants"
        for white in dic:
            if white['race'] == "Caucasian":
                r_defendant.append(white)
    else:
        color = "black defendants"
        for black in dic:
            if black['race'] == "African-American":
                r_defendant.append(black)
    if o == "":
        offend = r_defendant
        do = "did and did not"
    elif o == 'y':
        do = "did"
        for offended in r_defendant:
            if offended['two_year_recid'] != '0':
                offend.append(offended)
    else:
        do = "did not"
        for offended in r_defendant:
            if offended['two_year_recid'] == '0':
                offend.append(offended)
    if s == "":
        return "The amount of", color, "who", do, "offend is:", len(offend)
    elif s == "Low":
        for defendant in offend:
            if defendant['score_text'] == s:
                amount_defendant.append(defendant)
    else:
        for defendant in offend:
            if defendant['score_text'] == s or defendant['score_text'] == "Medium":
                amount_defendant.append(defendant)
    return "The amount of", color, "who", do, "offend with a", s, "risk is: ", len(amount_defendant)


print(defendants_amount(defendants_race(), re_offend(), defendants_score()))


# TEST VERSION
# def defendants_UI() -> tuple:
#     defendant_race = "p"
#     while defendant_race != "w" and defendant_race != "b" and defendant_race != "":  # this part star the while loop
#         defendant_race = str(input("Type 'w' to look for White people percent or 'b' for Black people percent "))
#         if defendant_race != "w" and defendant_race != "b" and defendant_race != "":
#             print("Sorry you have to answer w or b or leave it blank for all")
#
#     if defendant_race == "w" and defendant_race == "":
#         re_offend = 'p'
#         while re_offend != "y" and re_offend != "n" and re_offend != "":  # this part star the while loop
#             re_offend = str(input("Type 'n' to look for people who did not offended again and type 'y' if so: "))
#             if re_offend != "n" and re_offend != "y" and re_offend != "":
#                 print("Sorry you have to answer y or n")
#
#         if re_offend == "y" or re_offend == "":
#             score = -1
#             while not (score > -1):  # this part make sure that the score insert is > -1
#                 try:
#                     score = input("Insert the score you are looking for: ")
#                     if score != "":
#                         print("Have to insert a number between 0 and 10 or leave it blank for all")
#                     elif score < 0 or score > 10:  # always that the score is not in the range from 0 to 10 is going to repeat
#                         print("Sorry your score go out of the scale")
#                 except ValueError:
#                     print("The scale go from 0 to 10!!!")
#             if score == "":
#                 return defendant_race, re_offend, score
#             elif -1 < score < 5:
#                 score = "Low"
#                 return defendant_race, re_offend, score
#
#             elif 4 < score < 8:
#                 return "This score", score, "belong to the Medium score, sadly we don't have specific data about this group"
#
#             elif 7 < score < 11:
#                 score = 'High'
#                 return defendant_race, re_offend, score
#
#         else:
#             score = -1
#             while not (score > -1):  # this part make sure that the score insert is > -1
#                 try:
#                     score = input("Insert the score you are looking for: ")
#                     if score != "":
#                         print("Have to insert a number between 0 and 10 or leave it blank for all")
#                     elif score < 0 or score > 10:  # always that the score is not in the range from 0 to 10 is going to repeat
#                         print("Sorry your score go out of the scale")
#                 except ValueError:
#                     print("The scale go from 0 to 10!!!")
#             if score == "":
#                 return defendant_race, re_offend, score
#             elif -1 < score < 5:
#                 score = "Low"
#                 return defendant_race, re_offend, score
#
#             elif 4 < score < 8:
#                 return "This score", score, "belong to the Medium score, sadly we don't have specific data about this group"
#
#             elif 7 < score < 11:
#                 score = 'High'
#                 return defendant_race, re_offend, score
#
#     else:
#         re_offend = 'p'
#         while re_offend != "y" and re_offend != "n" and re_offend != "":  # this part star the while loop
#             re_offend = str(input("Type 'n' to look for people who did not offended again and type 'y' if so: "))
#             if re_offend != "n" and re_offend != "y" and re_offend != "":
#                 print("Sorry you have to answer y or n pr blank for all")
#
#         if re_offend == "y" or re_offend == "":
#             score = -1
#             while not (score > -1):  # this part make sure that the score insert is > -1
#                 try:
#                     score = input("Insert the score you are looking for: ")
#                     if score == "":
#                         return defendant_race, re_offend, score
#                     elif score < 0 or score > 10:  # always that the score is not in the range from 0 to 10 is going to repeat
#                         print("Sorry your score go out of the scale")
#                 except ValueError:
#                     print("The scale go from 0 to 10!!!")
#             if -1 < score < 5:
#                 score = "Low"
#                 return defendant_race, re_offend, score
#
#             elif 4 < score < 8:
#                 return "This score", score, "belong to the Medium score, sadly we don't have specific data about this group"
#
#             elif 7 < score < 11:
#                 score = 'High'
#                 return defendant_race, re_offend, score
