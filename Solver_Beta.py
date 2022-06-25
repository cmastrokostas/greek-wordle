
def possibleMatches():
    words = []
    letter="ω"
    position=1
    wordlist=[]
    with open('src/el_GR_n_5.txt',encoding='utf8') as w:
      words = w.readlines()
    print(words)
    while letter!='':
      del wordlist[:]
      
      letter=input("What letter do you know? : ")
      color=input("What color is it? (Y,G,B) : ")
      if color == 'g' or color == 'G' or color == 'y' or color == 'Y':
        position=int(input("What position is it? (1-5) : "))-1
      for word in words:
        if color == 'g' or color == 'G':
          if word[position]==letter:
            wordlist.append(word)
        elif color == 'b' or color == 'B':
          if letter not in word:
            wordlist.append(word)
        elif color == 'y' or color == 'Y':
          if letter in word:
            if word[position]!=letter:
              wordlist.append(word)
      words=wordlist.copy()
      
      print(*wordlist)
      print(words)
  
if __name__=='__main__':
    t=possibleMatches()