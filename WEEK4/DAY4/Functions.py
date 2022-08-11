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
        return True
    else:
        return False

x = hello_world("Pragassen", 24, "FR")
print(x)
hello_world(name="Yajna", language="FR")
hello_world(language="Kreole")
hello_world() #this will print hello world by default.

print(country) #Mauritius

print(is_even(2))
print(is_even(15))