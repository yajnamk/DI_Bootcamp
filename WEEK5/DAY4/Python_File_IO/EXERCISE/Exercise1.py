# Read only the 5th line of the file

f = open("nameslist.txt", "r+")
x=f.readlines()
print(x[5])
f.close()