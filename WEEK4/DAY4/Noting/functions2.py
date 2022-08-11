from unicodedata import name


country = "Mauritius"
things_I_like_to_eat = ["Pizza", "Burger"]

def hello_world(*args:)
    print(args)
    return

# print(hello_world("Yajna",24,"EN"))
print(hello_world(name = "Yajna", eat=things_I_like_to_eat.copy(), favourite_car="BMW"))