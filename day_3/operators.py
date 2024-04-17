age = 23
height = 1.75
complex = 4 + 3j

base = input('Ingresa la base del triangulo ')
height = input('Ingresa la altura del triangulo ')

print(
    'El area del triangulo es: ', 0.5 * int(height) * int(base)
)

side_a = int(input('Enter side a ')) 
side_b = int(input('Enter side b '))
side_c = int(input('Enter side c '))

print(
    "El perimetro del triangulo es: ", side_a + side_b + side_c 
)

length = int(input('Ingresa el largo del rectangulo '))
width = int(input('Ingresa el ancho del rectangulo '))

print(
    'El area del rectangulo es: ', length*width, "El perimetro del rectangulo es: ", 2*(length+width)
)

radius = int(input('Enter radius: '))
print(
    'El area del circulo es: ', 3.14*(radius**2), 'La circunferencia es: ', 2*3.14*radius
)

print(len("python"))
print(len("dragon"))
print( len('python') != len("dragon") )

print('on se encuentra en python y dragon?: ', 'on' in ('python' and 'dragon'))

print('jargon se encuentra en I hope this course is not full of jargon.?: ', 'jargon' in ('I hope this course is not full of jargon.'))

print('on no se encuentra en python ni dragon ', 'on' not in ('python' and 'dragon'))

print(type(str(float(len('python')))))

number = int(input('Ingresa el numero '))


print('Es par ',number%2 is 0)

print( 
    7//3 == int(2.7)
)

print( type(10) == type('10') )

print( int(9.8) == 10 )
hours = int(input('Ingrese las horas que trabja: '))
rate = int(input('Ingrese cuanto gana por hora: '))

print('Sus ganancias semanales son: ', hours*rate)

year_lived = int(input('Enter how many years you have lived '))

print('You have lived for ', year_lived*60*60*24*365 ,'Seconds')