from ast import If
import os
import requests
import json

def apiDATA():
    response_API = requests.get('http://localhost:8080/wordlist')
    data = response_API.text
    parse_json = json.loads(data)
    
    return parse_json['data']
    

def correctFile(apiData):
    
    apiData[0]=apiData[0].strip('\ufeff')
    return apiData

def enterSequence():
    combSequence=[]
    letterSequence=input("Enter Word : ")
    colorSequence=input("Enter color that matches every letter as a sequence.\nFor example 'YBBGG' : ")
    for iter in range(0,len(letterSequence)):
        combSequence.append([letterSequence[iter],colorSequence[iter]])
    return combSequence

def findWords(letter,color,position,words,wordlist):

    for word in words:
        if word=='':break
        
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
    words = correctFile(apiDATA())

    letter="ω"
    matches=[]
    
    
    position=0
    first=0
    while letter!='':
        combSequence=enterSequence()
        for comb in combSequence:
            
            letter=str(comb[0])
            color=str(comb[1])
            if position==0 and first==0:
                matches=findWords(letter,color,int(position),words,matches)
                position+=1
                first=1
            else:
                emptyList=[]
                matches=findWords(letter,color,int(position),matches,emptyList)
                position+=1
                  
        print("- ",*matches)
        exitInp=str(input('Do you want to continue? (y/n) :'))
        if exitInp=='n':
          break
        else:
          position=0
          continue    
        
        
if __name__=='__main__':
  possibleMatches()