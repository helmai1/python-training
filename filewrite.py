#untuk menambah data pada file yang baru dibuat
x = ["red","blue","yellow","green"] #input data

file = open("test.txt","w")
for value in x:
    file.write(value + "\n")

file.close()
