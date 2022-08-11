country = "Mauritius"

def hello_world(name="world", age="unknown", language="EN"):
    global country #will take the country inside the function #Rodrigues
    country="Rodrigues"
    if(language=="EN"):
        string = f"hello {name}. Age is {age}. And I live in {country}" #Rodrigues
    elif(language=="FR"):
        string = f"bonjour {name}. Age est {age}"
    else:
        string = "language is not not supported"
    return string

def is_even(num):
    if num%2 == 0:
        return True, f"{num} is even"
    else:
        return False, f"{num} is odd"

def is_list_even(list):
    for number in list: #1 , 3 , 4 , 7 , 8
        print(is_even(number)[1])

# x = hello_world("Pragassen", 24, "FR")
# print(x)
# hello_world(name="Yajna", language="FR")
# hello_world(language="Kreole")
# hello_world() #this will print hello world by default.

# print(country) #Mauritius

# x = print(is_even(2))
# print(x)
# print(is_even(15))

is_list_even([1, 3, 4, 7, 8])