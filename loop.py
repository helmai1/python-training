#Macam-macam looping di python

x = [0,1,2,3,4,5]
y = ["hello","mhanx","garox"]

for value in x :
    print(value + 10)
for value in y:
    print(value + "hello")

for i in x:
    x[i] = input("tulis kalimat : ")
    print(x)

i=0
while i<6:
    print(i)
    i+=1

# looping with break
for value in y:
    print(value)
    if value == y[1]:
        break
    # print(value)

print("")

#looping with continue
for value in y:
    if value == y[1]:
        continue
    print(value)

print("")

#looping with range and else
x = input("angka 1 : ")
y = input("angka 2 : ")
for value in range(int(x),int(y),4):
    print(value)
else:
    print("penuh")
