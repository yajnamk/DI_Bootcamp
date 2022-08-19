
# for line in open('nameslist.txt'):
#     print(line)

f = open("nameslist.txt", "r+")
x=f.readlines()
print(x[5])
f.close()

