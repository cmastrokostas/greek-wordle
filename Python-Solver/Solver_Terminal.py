from ast import If
import os
import requests
import json

blackwords = []
existing_letters=[]

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
    letterSequence=input("Εισάγετε μία λέξη : ")
    colorSequence=input("Εισάγετε ένα συνδυασμό χρωμάτων, όπως φαίνεται παρακάτω.\nΓια παράδειγμα 'ΚΜΜΠΠ': ")
    for iter in range(0,len(letterSequence)):
        combSequence.append([letterSequence[iter],colorSequence[iter]])
    return combSequence

def findWords(letter,color,position,words,wordlist):
    for word in words:
        if word=='':break
        elif color == 'π' or color == 'Π':
            if word[position]==letter:
                wordlist.append(word)
                existing_letters.append(letter)

        elif color == 'μ' or color == 'Μ':
            if word[position]==letter or (letter in word and letter not in existing_letters):
                blackwords.append(word)

            else: ##
                wordlist.append(word)

        elif color == 'κ' or color == 'Κ':
            wordlist.append(word)
            existing_letters.append(letter)
    wordlist = [word for word in wordlist if word not in blackwords]
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
                  
        print("Πιθανές Λέξεις: ",*matches)
        exitInp=str(input('Θες να συνεχίσεις (ΝΑΙ/ΟΧΙ) :'))
        if exitInp=='ΟΧΙ':
          break
        else:
          position=0
          continue    
        
        
if __name__=='__main__':
  possibleMatches()