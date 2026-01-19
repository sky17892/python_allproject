from operator import itemgetter

students = [
    {"name": "jane", "age": 23, "grade": 'A'},
    {"name":"dave", "age": 33, "grade":'B'},
    {"name":"sally", "age": 18, "grade": 'C'},
]

result = sorted(students, key=itemgetter('name'))
print(result)
result2 = sorted(students, key=itemgetter('age'))
print(result2)
result3 = sorted(students, key=itemgetter('grade'))
print(result3)
