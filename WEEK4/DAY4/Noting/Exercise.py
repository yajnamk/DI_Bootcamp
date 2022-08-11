persons = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]
four_letter = filter(lambda person: len(person)<=4, persons)


print(list(four_letter))