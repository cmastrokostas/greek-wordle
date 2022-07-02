from ast import If
import os

def correctFile(fname):
    words = []
    with open(os.path.join(os.getcwd(),"Python-Solver",fname),encoding='utf8') as w:
        words = w.readlines()
    words[0]=words[0].strip('\ufeff')
    for i in range(len(words)):
        words[i]=words[i].strip('\n')
    return words

def enterSequence():
    combSequence=[]
    letterSequence=input("Enter Word : ")
    colorSequence=input("Enter color that matches every letter as a sequence.\nFor example 'YBBGG' : ")
    for iter in range(0,len(letterSequence)):
        combSequence.append([letterSequence[iter],colorSequence[iter]])
    return combSequence

def findWords(letter,color,position,words,wordlist):

    for word in words:
        if color == 'g' or color == 'G':
            if word[position]==letter:
                wordlist.append(word)
        if color == 'b' or color == 'B':
            if letter not in word:
                wordlist.append(word)
        if color == 'y' or color == 'Y':
            if letter in word:
                if word[position]!=letter:
                    wordlist.append(word)

    words=wordlist.copy()
    return words


def possibleMatches():
    words = correctFile('el_GR_n_5.txt')

    letter="ω"

    matches=[]
    while  letter!='ΟΧΙ':

        position=0
        combSequence=enterSequence()

        for comb in combSequence:


            letter=str(comb[0])
            color=str(comb[1])
            if position==0:
                matches=findWords(letter,color,int(position),words,matches)
                position+=1
            else:
                emptyList=[]
                matches=findWords(letter,color,int(position),matches,emptyList)
                position+=1

        print(matches)
        break

if __name__=='__main__':

    possibleWords=possibleMatches()
