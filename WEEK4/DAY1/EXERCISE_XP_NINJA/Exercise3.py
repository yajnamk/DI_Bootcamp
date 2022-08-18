3 <= 3 < 9  #True
3 == 3 == 3  #True
bool(0)  #False
bool(5 == "5")  #False
bool(4 == 4) == bool("4" == "4")  #False
bool(bool(None))  #False
x = (1 == True)  #True
y = (1 == False)  #False
a = True + 4
b = False + 10

print("x is", x)  #value of x is True
print("y is", y)  #value of y is False
print("a:", a)  # value of a is 5
print("b:", b)  #value of b is 10