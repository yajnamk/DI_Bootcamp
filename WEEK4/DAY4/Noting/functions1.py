def my_f1():
    print("Hello")

def my_f2():
    print("Word")

def my_f3():
    print("This is Rick!")

mytasks = [my_f1, my_f2, my_f3]
print(mytasks)

for task in mytasks:
    task()