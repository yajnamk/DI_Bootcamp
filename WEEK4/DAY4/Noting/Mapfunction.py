fruits = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
expecs = ["APPLE", "BANANA", "PEAR", "APRICOT", "ORANGE"]
upper_fruits = []

def make_upper(word):
    return word.upper()

# for fruit in fruits:
#     upper_fruits.append(make_upper(fruit))

upper_fruits = list(map(make_upper, fruits))

print(upper_fruits)