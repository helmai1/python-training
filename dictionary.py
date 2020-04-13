import json
from difflib import get_close_matches

data = json.load(open("original.json"))
tryagain = "y"

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        print("maksud anda %s " %get_close_matches(word, data.keys())[0])
        press = input("press y or n ")
        if press == "y":
            return(get_close_matches(word, data.keys())[0])
        elif press == "n":
            return("data tidak ditemukan")

    else:
        input("data tidak ditemukan")


word = input("Enter word to search : ")
# wordlower = word.lower()
output = translate(word)

if type(output)==list:
    for item in output:
        print(item)
else:
    print(output)
