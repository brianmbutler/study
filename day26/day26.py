# list comprehensions

#for loop sytle
numbers = [1,2,3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)
print(new_list)

#comprehension
#new_list = [new_item for item in list]

new_list = [n + 1 for n in numbers]
print(new_list)

name = 'Brian'
new_list = [letter for letter in name]
print(new_list)

new_range = [n * 2 for n in range(1,5)]
print(new_range)

#conditional list comprehension
#new_list = [new_item for item in list if test]

names = ['Alex','Beth','Caroline','Dave','Eleanor','Freddy']
new_list = [name for name in names if len(name) == 4]
print(new_list)

long_names = [name.upper() for name in names if len(name) > 4]
print(long_names)

'''Dictionary Comprehension'''
#new_dict = {new_key:new_value for item in list}
#new_dict = {new_key:new_value for (key,value) in dict.items()}
#new_dict = {new_key:new_value for (key,value) in dict.items() if test}

names = ['Alex','Beth','Caroline','Dave','Eleanor','Freddy']
import random
students_scores = {student:random.randint(1,100) for student in names}
print(students_scores)


passed_students = {student:score for (student,score) in students_scores.items() if score > 60}
#print(passed_students)

import pandas as pd

df = pd.DataFrame(students_scores)

for (index, row) in df.iterrows():
    if row.student == 'Alex':
        print(row.score)