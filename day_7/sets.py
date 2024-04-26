# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
it_companies.add("Twitter")

it_companies.update(["Sermaluc","Kibernum","Apply","Teamcore"])

it_companies.pop()

print(A.union(B))

print(A.issubset(B))

print(A.isdisjoint(B))

print(A.union(B))
print(B.union(A))

print(A.symmetric_difference(B))

del A, B

print(len(age))

C = set(age)
print(len(C))

sentence = "I am a teacher and I love to inspire and teach people."

sentence_array = sentence.split(" ")

print(sentence_array)


unique_words = set(sentence_array)

print( unique_words )
print(len(unique_words))