from operator import itemgetter

students = [
    ("jane", 23, 'A'),
    ("dave", 33, 'B'),
    ("sally", 18, 'C'),
]

result = sorted(students, key=itemgetter(0))
print(result)
