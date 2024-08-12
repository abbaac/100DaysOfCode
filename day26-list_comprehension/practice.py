# print([n*2 for n in range(1,5)])

import random
import pandas as pd

student_names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

short_names = [n for n in student_names if len(n) < 5]
long_names_capitalized = [n.upper() for n in student_names if len(n) > 5]

# print(short_names)
# print(long_names_capitalized)


student_scores = {names:random.randint(1, 100) for names in student_names}

# passed_students = {names:student_scores[names] for names in student_scores if student_scores[names] > 60}
passed_students = {student:score for (student, score) in student_scores.items() if score > 60}

# print(student_scores)
# print(passed_students)

student_dict = {
    "Names": ["Alex", "Beth", "Caroline"],
    "Scores": [61, 88, 70]
}

student_df = pd.DataFrame(student_dict) # MUst be dictionary of lists to make dataframe

for (index, row) in student_df.iterrows():
    # if row.Names == "Alex":
    if index == 2:
        print(row.Names)

