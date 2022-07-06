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
    letterSequence=input("Εισάγετε μία λέξη : ")
    colorSequence=input("Εισάγετε ένα συνδυασμό χρωμάτων, όπως φαίνεται παρακάτω.\nΓια παράδειγμα 'ΚΜΜΠΠ': ")
    for iter in range(0,len(letterSequence)):
        combSequence.append([letterSequence[iter],colorSequence[iter]])
    return [combSequence,letterSequence,colorSequence]

def findWords(letter,color,position,words,wordlist,letterSeq,colorSeq):

    for word in words:
        if word=='':break
        
        if color == 'π' or color == 'Π':
            if word[position]==letter:
                wordlist.append(word)
                
        if color == 'μ' or color == 'Μ':
            if word[position]==letter:
                words.remove(word)
            
        if color == 'κ' or color == 'Κ':
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
        for comb in combSequence[0]:
            
            letter=str(comb[0])
            color=str(comb[1])
            if position==0 and first==0:
                matches=findWords(letter,color,int(position),words,matches,combSequence[1],combSequence[2])
                position+=1
                first=1
            else:
                emptyList=[]
                matches=findWords(letter,color,int(position),matches,emptyList,combSequence[1],combSequence[2])
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