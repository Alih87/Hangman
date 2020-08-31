import os
import random
class Hangman:
    def __init__(self, txt, ntxt = "", Txt = list(), nTxt = list(), index = list(), strike = 0):
        self.txt = txt
        self.index = index
        self.Txt = Txt
        self.nTxt = nTxt
        self.ntxt = ntxt
        self.strike = strike
    def list2str(self, List):
        Str = " ".join(List)
        return Str
    def blanks(self):
        self.txt = self.txt.upper()
        self.Txt = []
        self.Txt[:0] = self.txt
        self.index = list()
        self.nTxt = self.Txt.copy()
        i = 0
        while(i <= (len(self.Txt))//3):
            rand = random.choice(self.Txt)
            self.index.append(self.Txt.index(rand))
            self.nTxt[self.index[-1]] = "_"
            i += 1
        self.ntxt = self.list2str(self.nTxt)
        print(self.ntxt)
    def guess(self):
        x = input("Guess letter: ")
        x = x.upper()
        os.system("cls")
        check = x in self.Txt
        if check:
            for i in self.index:
                check1 = check2 = False
                if x in self.Txt[i]:
                    check1 = x == self.Txt[i]                   
                    index = i
                    break
                elif x in self.nTxt:
                    check1 = True
                    check2 = True
                    index = self.nTxt.index(x)
            if check2:
                self.strike += 1
                if self.strike < 4:
                    print("Wrong! Guess again.. You have " + str(4 - self.strike) 
                    + " chance(s) remaining", end="\n\n")
            if check1:
                self.nTxt[index] = x
                self.ntxt = self.list2str(self.nTxt)
                print(self.ntxt)
        else:
            self.strike += 1
            if self.strike < 4:
                print("Wrong! Guess again.. You have " + str(4 - self.strike) 
                + " chance(s) remaining", end="\n\n")
                print(self.ntxt)
with open("words.txt", "r") as f:
    sel = f.read()
    sel = sel.split()
chose = random.choice(sel)
word = Hangman(chose)
word.blanks()
x = "Y"
while  word.Txt != word.nTxt and x == "Y":
    word.guess()
    if(word.Txt == word.nTxt):
        x = input("Well done! Play again? (Y/N): ")
        x = x.upper()
        if x == "Y":
            os.system("cls")
            chose = random.choice(sel)
            word = Hangman(chose)
            word.blanks()
    elif word.strike == 4:
        x = input("Game Over! The word was " + chose.upper() + ". Try again? (Y/N): ")
        x = x.upper()
        if x == "Y":
            os.system("cls")
            chose = random.choice(sel)
            word = Hangman(chose)
            word.blanks()
            word.strike = 0