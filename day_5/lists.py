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
