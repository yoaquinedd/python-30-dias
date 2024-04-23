first_word = "Thirty"
second_word = "Days"
third_word = "of"
fourth_word = "Python"
space = " "
sentence = first_word + space +second_word +space+ third_word +space+ fourth_word

print(sentence)

first_word = "Coding"
second_word = "For"
third_word = "All"

sentence = first_word + space + second_word + space +third_word
print(sentence)


company = "Coding For All"
print(company)
print(len(company))
print(company.upper())
print(company.lower())


print(company.capitalize())
print(company.title())
print(company.swapcase())

print( company[0:6]) 

print(company.replace("Coding",""))

print(company.index("Coding"))
company=company.replace("Coding","Python")
print(company)
company = company.replace("All","Everyone")
print(company)
company = "Coding For All"

print(company.split(" "))

companies ="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(" "))

print(company[0])
print(len(company)-1)

print(company[10])
company = company.split(" ");

firts_ac = company[0]
second_ac = company[1]
third_ac = company[2]

print(firts_ac[0]+second_ac[0]+third_ac[0])

company = "Coding For All"

print(company.index('C'))

phrase = "Coding For All People"

print(phrase.rindex("l"))

phrase = "You cannot end a sentence with because because because is a conjunction"


print(phrase.index("because"))

print(phrase.rindex("because"))

print(phrase[30:55])

print(company.startswith("Coding"))
print(company.endswith("coding"))

company = " Coding For All "

print(company.strip())

print("30daysofpython".isidentifier())
print("thirty_days_of_python".isidentifier())

libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']

result = "# ".join(libraries)

print(result)

print("I am enjoying this challenge.\nI just wonder what is next.")

print("Name\tAge\tCountry\tCity")
print("Joaquin\t23\tChile\tChillan")

radius = 10
area = 3.14 * radius**2

print("The area of a circle with radius {} is {} meters square".format(radius, area))
a = 8
b = 6



print("{} + {} = {}".format(a,b,a + b))
print("{} - {} = {}".format(a,b,a - b))
print("{} * {} = {}".format(a,b,a * b))
print("{} / {} = {}".format(a,b,a / b))
print("{} // {} = {}".format(a,b,a // b))
print("{} ** {} = {}".format(a,b,a ** b))