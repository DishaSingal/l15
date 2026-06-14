print("How many characters?")
n = int(input())
file = open("f.txt","r")
print(file.read(n))
print()
file.close()

file = open
file = open("f.txt","r")
x = file.readlines()
len(x)
print(len(x))

for i in range(len(x)):
    print(x[i])
file.close()

word = input("Which lines to skip?")
file = open("f.txt","r")
for i in file:
    if i.startswith(word):
        print("skip ->", i.strip())
    else:
        print("keep ->", i.strip())
file.close()
print()

file = open("f.txt","r")
x = file.readlines()
file.close()
out = open("odd-lines.txt","w")
for i in range(0, len(x), 2):
    out.write(x[i])
out.close()
print()
