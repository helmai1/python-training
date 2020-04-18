import random

def hangman():

    word = random.choice(["mouse","keyboard","monitor","speaker"]) #jawaban
    validLetters = 'abcdefghijklmnopqrstuvwxyz' #data yang dapat diinputkan
    turns = 10 #nyawa
    guessmade = '' #variable untuk menyimpan jawaban

    while len(word) > 0: #looping word length
        main = "" #variable untuk menyimpan jawaban pada  _ _ _
        missed = 0 #salah

        for letter in word: #looping kata
            #jika jawaban benar dan salah
            if letter in guessmade:
                main = main + letter #huruf jawaban akan diisi contoh menjawab "m" pada mouse akan menjad m _ _ _ _
            else:
                main = main + "_" + " " #jika tidak atau salah maka akan tetap menjadi " _ "

        if main == word: #kondisi jika variable sama dengan jawban maka anda menang!
            print(main)
            print("You win!")
            break

        print("Guess the word:" , main)
        guess = input() #input jawaban

        #kondisi jika jawaban yang diinputkan valid atau tidak valid
        if guess in validLetters:
            guessmade = guessmade + guess
        else:
            print("Enter a valid character")
            guess = input()

        if guess not in word: #kondisi jika jawaban salah
            turns = turns - 1 #mengurangi nyawa -1
            if turns == 9:
                print("9 turns left")
                print("  --------  ")
            if turns == 8:
                print("8 turns left")
                print("  --------  ")
                print("     O      ")
            if turns == 7:
                print("7 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
            if turns == 6:
                print("6 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    /       ")
            if turns == 5:
                print("5 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 4:
                print("4 turns left")
                print("  --------  ")
                print("   \ O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 3:
                print("3 turns left")
                print("  --------  ")
                print("   \ O /    ")
                print("     |      ")
                print("    / \     ")
            if turns == 2:
                print("2 turns left")
                print("  --------  ")
                print("   \ O /|   ")
                print("     |      ")
                print("    / \     ")
            if turns == 1:
                print("1 turns left")
                print("Last breaths counting, Take care!")
                print("  --------  ")
                print("   \ O_|/   ")
                print("     |      ")
                print("    / \     ")
            if turns == 0:
                print("You loose")
                print("You let a kind man die")
                print("  --------  ")
                print("     O_|    ")
                print("    /|\      ")
                print("    / \     ")
                break


name = input("input your name : ")
print("Welcome ", name)
print("===============================")
print("try guess the pc device")
hangman()
print()
