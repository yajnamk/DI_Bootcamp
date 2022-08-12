persons = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]
four_letter = list(filter(lambda person: len(person)<=4, persons))


print(four_letter)

def hello_name(name):
    print("hello", name)
    return "hello, {name}"

#Map 4 letters with hello name 

greet = list(map(hello_name, four_letter))
# print(greet)