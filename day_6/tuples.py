tuple = ()

brothers = ("Francisco", "Joaquin")

sisters = ("Catalina",)

siblings = brothers + sisters

print("I have ",len(siblings)," siblings" )

family_members = siblings + ("Macarena","Alejandro")

hermano1,hermano2,hermano3, *padres = family_members  

print(padres)

fruits = ("Apple","Orange","Pear","Banana")
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
animal_products = ("Cheese","Milk","Butter")

food_stuff_tp = fruits + vegetables + animal_products

food_stuff_lt = list(food_stuff_tp)

middle_index = len(food_stuff_lt)//2
last_index = len(food_stuff_lt)-1

print(food_stuff_lt[middle_index:middle_index+1])

print(food_stuff_lt[0:3], food_stuff_lt[last_index-2:last_index+1])

del food_stuff_tp

print('Macarena' in family_members)

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)