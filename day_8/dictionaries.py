dog = {}

dog['name'] = 'Beto'
dog['color'] = 'White'
dog['breed'] = 'Fox terrier'
dog['legs'] = 'Strong'
dog['age '] = 13

print(dog)


student = {
    'first_name':'Joaquin',
    'last_name':'Poblete',
    'gender':'Male',
    'age':23,
    'marital_status': 'Single',
    'skills' : ['HTML','JavaScript','Java','Python'],
    'country': 'Chile',
    'city': 'Chillan',
    'adress': 'Las violetas 2939'
}

print(len(student))

print(type(student['skills']))

student['skills'].append('Angular')

keys=student.keys()

print(keys)

values = student.values()

print(values)

as_tuples = student.items()

print(as_tuples)


student.pop('adress')

print(student)


del dog

print(dog)