# age = int(input("Introduzca su edad\n"))

# if age >= 18:
#     print("Yo are old enough to drive")
# else:
#     wait = 18 - age
#     print("You have to wait ",wait,"years to drive.")

# my_age = 23

# your_age = int(input("Introduce tu edad\n"))

# if your_age == my_age:
#     print("We have the same age")
# elif abs(your_age-my_age) == 1:
#     print("We have 1 year difference")
# else: 
#     print("We have {} year difference".format(abs(your_age-my_age)))


# a = int(input("Enter number one\n"))
# b = int(input("Enter number two\n"))

# if a > b:
#     print("{} es mayor que {}".format(a,b))
# elif a < b:
#     print("{} es menor que {}".format(a,b))
# else:
#     print("{} es igual que {}".format(a,b))


# score = int(input("Enter your score\n"))

# if score>0 and score<=49:
#     print("F")
# elif score>=50 and score<=59:
#     print("D")
# elif score>=60 and score<=69:
#     print("C")
# elif score>=70 and score<=79:
#     print("B")
# elif score>=80 and score<=100:
#     print("A")


# month = input("Enter the month\n")

# if month == "September" or month == "October" or month == "November":
#     print("The season is autumn")
# elif month == "December" or month == "January" or month == "February":
#     print("The season is winter")
# elif month == "March" or month =="April" or  month =="May":
#     print("The season is spring")
# else:
#     print("The season is Summer")


# fruits = ['banana', 'orange', 'mango', 'lemon']

# fruit = input("Ingrese una fruta\n")

# if fruits.count(fruit) >= 1:
#     print("La fruta ya se encuentra")
# else:
#     fruits.append(fruit)
#     print("Fruta agregada correctamente")
#     print(fruits)


person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}


if person.get('skills'):
    midlle_index = len(person['skills'])//2
    print(person['skills'][midlle_index])
    if person['skills'].count('Python') >= 1:
        print("Si tiene python")

        if set (person['skills']) == {'JavaScript', 'React'}:
            print('Es un desarrollador Frontend')
        elif set (person['skills']) == {'Node', 'Python', 'MongoDB'}:
            print('Es un desarrollador Backend')
        elif {'React','Node','MongoDB'}.issubset(set(person['skills'])):
            print('Es un desarrollador Fullstack')

if person.get('is_married') and person.get('country') == 'Finland':   
    print(f"{person['first_name']} {person['last_name']} está casado y vive en Finlandia.")
#  Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
#  Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
#  If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
#  If the person is married and if he lives in Finland, print the information in the following format: