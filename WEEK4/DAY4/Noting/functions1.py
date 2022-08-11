def my_f1(age = 6):
    print(f"Hello {age}")

def my_f2(age):
    print("Word")

def my_f3(age):
    print("This is Rick!")

mytasks = [my_f1, my_f2, my_f3]
print(mytasks)

for task in mytasks:
    task(10)