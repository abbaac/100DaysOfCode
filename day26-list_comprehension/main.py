student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas as pd

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

nato_df = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {rows.letter:rows.code for (index, rows) in nato_df.iterrows()}

# nato_dict = {letter:word in (letter:)}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Type in the word you want to be converted: ").upper()
nato_representation = [nato_dict.get(letter) for letter in word if letter in nato_dict.keys()]
print(nato_representation)