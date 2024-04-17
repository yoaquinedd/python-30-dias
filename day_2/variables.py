#'Day 2: 30 Days of python programming'

first_name = 'Joaquin'
last_name = 'Poblete'
full_name = first_name +" "+ last_name
country = "Chile"
city = "Chillan"
age = 23
year = 2024
is_married = False
is_true = True
is_light_on = False
backend_framework, frontend_framework, cloud_service = 'Express.js', 'Angular', 'AWS'


print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(backend_framework))
print(type(frontend_framework))
print(type(cloud_service))

print(len(first_name))

num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one/num_two
remainder = num_two%num_one
exp = num_one ** num_two
floor_division = num_one // num_two

pi = 3.1416

area_of_circle = pi * (30**2)

circum_of_circle = 2 * pi * 30

radius_usr_input = input('Ingrese el radio del circulo: ')

area_of_circle = pi* int(radius_usr_input) ** 2

print(
      "El area del circulo es: ", area_of_circle 
)

first_name =input("Ingresa tu first_name")
last_name =input("Ingresa tu last_name")
country =input("Ingresa tu country")
age =input("Ingresa tu age")