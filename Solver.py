from turtle import color


words = []
letter="ω"
position=1
wordlist=[]

combDict={}

with open('el_GR_n_5.csv',encoding='utf8') as w:
    words = w.readlines()

while letter!='':
    letterSequence=input("Enter Word : ")
    
    colorSequence=input("Enter color that matches every letter as a sequence.\nFor example 'YBBGG' : ")
    
    for iter in range(max(len(letterSequence),len(colorSequence))):
        combDict[letterSequence[iter]]=colorSequence[iter]
    
    print(combDict)
    break