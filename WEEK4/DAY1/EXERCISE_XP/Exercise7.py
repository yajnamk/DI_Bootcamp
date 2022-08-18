num = int(input("Please enter a number "))

if (num % 2) == 0:
    print(str(num) + " is an even number")
else:
    print(str(num) + " is an Odd number")
print("Next Exercise\n")

#Exercise 8 : What’s Your Name ?
#Write code that asks the user for their name and determines whether or not you have the same name, print out a funny message based on the outcome.

fname = input("Please enter your name:")
cname = "Yajna"
if fname == cname:
    print("Hey we have the same name")
else:
    print("Sorry bro we have different name")
print("Next Exercise\n")
