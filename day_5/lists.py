list = list()

list2 = ["item1","item2","item3","item4","item5"]

print(len(list2))

last_index = len(list2)-1
middle_index = int(len(list2)/2)

print(list2[0], list2[middle_index], list2[last_index])

mixed_data_types = [ "Joaquin", 23, 1.75, "Casado", "Las violetas 2939" ]

print(mixed_data_types)

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Amazon"]

print(it_companies)

last_index = len(it_companies)-1
middle_index = int(len(it_companies)/2)

print(it_companies[0], it_companies[middle_index],it_companies[last_index])

it_companies[2] = "Azure"

print(it_companies)

it_company = "Sermaluc"

it_companies.append(it_company)
middle_index = int(len(it_companies)/2)

print(it_companies)

it_company_2 = "Kibernum"

it_companies.insert(middle_index,it_company_2)

print(it_companies)

print(it_companies[4].upper())

does_exist = "Apple" in it_companies

print(does_exist)
it_companies.sort()
print(it_companies)
it_companies.reverse()
print(it_companies)

print(it_companies[0:3])
print(it_companies[len(it_companies)-4:len(it_companies)-1])

middle_index = int(len(it_companies)/2)

print(it_companies[middle_index:middle_index+1])

it_companies.pop(0)

print(it_companies)

it_companies.pop(middle_index)

print(it_companies)

it_companies.pop()
print(it_companies)
it_companies.clear()
print(it_companies)
del it_companies

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

techs = front_end + back_end

full_stack = techs.copy()

print(full_stack)

full_stack.index("Redux")
print(full_stack.index("Redux"))

# Insertar Python y SQL después de Redux
full_stack.insert(full_stack.index('Redux') + 1, 'Python')
full_stack.insert(full_stack.index('Redux') + 2, 'SQL')

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()

print(ages)

last_index = len(ages) - 1

print(ages[0], ages[last_index] )

ages.append(19)
ages.append(26)

print(ages)

ages.sort()

middle_index = len(ages)//2

ages.sort()

print(ages)

print(middle_index)

print( ages[middle_index]  )


