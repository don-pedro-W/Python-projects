#!/usr/bin/env python

#import strings

#Initialize all list to be used in  program, words and some number list
Wordlist = ["zero","one","two","three","four","five","six","seven","eight","nine","ten"]
Elevenlist =["eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
NumEleven = ["11","12","13","14","15","16","17","18","19"]
Tenslist = ["twenty","thirthy","forty","fifty","sixty","seventy","eighty","ninety"]
NumTens = ["20","30","40","50","60","70","80","90"]
Hundredslist = ["hundred","thousand"]
NumHundreds = ["100","200","300","400","500","600","700","800","900"]





def DtoW(inp):
    num = int(inp)

    length = len(inp)

    #variables to point to number sequence
    x = "0123456789"
    y = "23456789 "

    """Check if input is a number and if it between boundary
     if so, then check the length of the number
       after which loop through the number and compare it to list of the same index
          e.g x[1] in digits is Wordlist[1] in words
                i.e --one--"""


    if (type(num) == type(1)) and (num < 1001):
        #for single digits
        if length == 1:
            for i in range(10):
                if inp == x[i]:
                    print(Wordlist[i])
        #for 2 digit numbers
        elif length == 2:
            if inp == "10":
                print(Wordlist[10])
            elif num > 10 and num < 20:
                for i in range(10):
                    if inp == NumEleven[i]:
                        print(Elevenlist[i])
                        
            elif num > 19 and num < 100:
                for i in NumTens:
                    if i == inp:
                        z = int((int(i)/10)- 2)
                        print(Tenslist[z])

                for i in range(9):
                    if inp[0] == y[i]:
                        for j in range(10):
                            if inp[1] == x[j] and inp[1] != "0":
                                print(Tenslist[i] + "-" + Wordlist[j])
        #for 3 digits
        elif length == 3:
            Word = Wordlist[1:10]
            x = x[1:10]
            if inp in NumHundreds:
                for i in range(9):
                    if inp[0] == x[i]:
                        print(Word[i] +" " + Hundredslist[0])
            
            for i in range(9):
                if inp[0] == x[i]:
                    if inp[1] == "0":
                        for j in range(9):
                            if inp[2] == x[j]:
                                print(Word[i] + " " + Hundredslist[0] + " and " + Word[j])
                    if inp[1:] == "10":
                        print(Word[i] + " " + Hundredslist[0] + " and " + Wordlist[10])
                                
                    for j in range(9):
                        if inp[1:] == NumEleven[j]:
                            print(Word[i] + " " + Hundredslist[0] + " and " + Elevenlist[j])

                    for j in NumTens:
                        if j == inp[1:]:
                            z = int((int(j)/10)- 2)
                            print(Word[i] + " " + Hundredslist[0] + " and " + Tenslist[z])
                    
                    for j in range(9):
                        if inp[1] == y[j]:
                            for k in range(9):
                                if inp[2] == x[k] and inp[2] != "0":
                                    print(Word[i] + " " + Hundredslist[0] + " and " +Tenslist[j] + "-" + Word[k])
        #for 1000
        elif inp == "1000":
            print("one thousand ;-)")

    else:
        print("invalid input: You input should be a number and less than or equal to 1000")
        print("Try again !!!")
        choice()
    choice()
    

def Start():

    #Tell the user how the program works
    print("This program returns any digit between 0 - 1000 in words")
    
    #Prompt user to enter number and change type to integer and save length of string
    x = input("/n Have fun with it ==> ")
    DtoW(x)

def choice():
    print("Do you want to perform another conversion? (Y/N)")
    inp = input("==> ")
    if inp == "Y" or inp == "y":
        Start()
    else:
        exit()

if __name__ == "__main__":
    Start()



            
            
