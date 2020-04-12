#macam-macam cara untuk function di python


def add(x,y=" kamu"):
    z = x + y
    return print(z)
a = "hello "
b = input("name: ")
add(a,b)


def angka(x=0,y=0):
    z = x + y
    return print(z)
a = input("angka 1 : ")
b = input("angka 2 : ")
# convert ke angka
angka(int(a))


def name(x="",y=""):
    # kondisi di python and, or, not jika dijava &&, ||, !
    if(x == "" or y == ""):
        return print("isi nama dengan benar!")
    else:
        z = x + y
        return print(z)
a=input("masukan nama depan : ")
b=input("masukan nama belakang : ")
name(a,b)
