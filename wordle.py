# Wordle Unlimited by Pluto_Guy
# This project is under the mit license
# https://mit-license.org/

# Libraries
import random # For picking a random word
import colorama
from colorama import Fore, Back, Style # For coloring if the answer is right or wrong

colorama.init(autoreset=True)

print(Fore.BLUE+"WORDLE UNLIMITED"+"\n")

words = ["a p p l e","c r e m e","s n a k e","s l u r p","f i x e d","s e v e n","v e r v e", "p l u t o","l a u g h","f u z z y","m u z z y","d i z z y","q u i c k","j a m m y","c r a z y","j o k e y","q u i f f","b o o z y","c o z e y","w h e e l","s t e e l","k n e e l","f r o z e","s t o o l","p a n d a","u n d e r","p l a n e","c r a n e","p a y e d","s n a r e","g l a r e","b a n g o","s t a r s","s t a r t","b u n n y","s t a c k","d o g g y","f u n n y"] # Word list

word = random.choice(words) # Picks a random word from the word list
word = word.split(" ") # Splits the words into indiviual letters for the program to understand

onecontainindex = 0
onecontentindicator = ""

for i in range(6):
  # Variables for telling the program what letters the user got right
  numberone = False
  numbertwo = False
  numberthree = False
  numberfour = False
  numberfive = False

  userinput = input("Word > ") # Creates an input for the user to type their word

  def checkvalidword(): # Checks if the word is valid
    spacegon = ""
    spacegonlist = []
    global userinput

    for word in words:
      spacegone = word.replace(" ","")
      spacegonlist.append(spacegone)

    if userinput in spacegonlist:
      return 0
    else:
      print(Fore.RED+"Not in word list")
      userinput = input("Word > ")
      checkvalidword()

  checkvalidword()

  for i in range(len(word)):
    if word[i] == userinput[0]:
      numberone = "contains"
      onecontentindex = i
      if i == 0:
        onecontentindicator = "wordone"
      elif i == 1:
        onecontentindicator = "wordtwo"
      elif i == 2:
        onecontentindicator = "wordthree"
      elif i == 3:
        onecontentindicator = "wordfour"
      elif i == 4:
        onecontentindicator = "wordfive"

  # See if the user input contains the a letter in the word

  if word[0] == userinput[0]:
    numberone = True
  elif userinput[0] in word:
    for i in range(len(word)):
      if word[i] == userinput[0]:
        numberone = "contains"
        onecontentindex = i
        if i == 0:
          onecontentindicator = "wordone"
        elif i == 1:
          onecontentindicator = "wordtwo"
        elif i == 2:
          onecontentindicator = "wordthree"
        elif i == 3:
          onecontentindicator = "wordfour"
        elif i == 4:
          onecontentindicator = "wordfive"

  else:
    numberone = False

  if word[1] == userinput[1]:
    numbertwo = True
  else:
    numbertwo = False

  if word[2] == userinput[2]:
    numberthree = True
  else:
    numberthree = False

  if word[3] == userinput[3]:
    numberfour = True
  else:
    numberfour = False

  if word[4] == userinput[4]:
    numberfive = True
  else:
    numberfive = False

  # Sets the colours

  wordone = ""
  wordtwo = ""
  wordthree = ""
  wordfour = ""
  wordfive = ""

  if numberone == True:
    wordone = Fore.GREEN + userinput[0]
  elif userinput[0] in word:
    wordone = Fore.YELLOW + userinput[0]
  else:
    wordone = Fore.RED + userinput[0]

  if numbertwo == True:
    wordtwo = Fore.GREEN + userinput[1]
  elif userinput[1] in word:
    wordtwo = Fore.YELLOW + userinput[1]
  elif numbertwo == False:
    wordtwo = Fore.RED + userinput[1]

  if numberthree == True:
    wordthree = Fore.GREEN + userinput[2]
  elif userinput[2] in word:
    wordthree = Fore.YELLOW + userinput[2]
  elif numberthree == False:
    wordthree = Fore.RED + userinput[2]

  if numberfour == True:
    wordfour = Fore.GREEN + userinput[3]
  elif userinput[3] in word:
    wordfour = Fore.YELLOW + userinput[3]
  elif numberfour == False:
    wordfour = Fore.RED + userinput[3]

  if numberfive == True:
    wordfive = Fore.GREEN + userinput[4]
  elif userinput[4] in word:
    wordfive = Fore.YELLOW + userinput[4]
  elif numberfive == False:
    wordfive = Fore.RED + userinput[4]

  # Prints the output to see the users result

  print(wordone+wordtwo+wordthree+wordfour+wordfive)

  # Checks if the user got the word right
  if numberone == True and numbertwo == True and True == True and numberfour == True and numberfive == True:
    print(random.choice(["Splendid!","Great!","Amazing!"])) # Randomizes the winning message
    if True: # Used for an indent
      break  # Breaks the game after winning message

# Says the word
print("The word was",word[0]+word[1]+word[2]+word[3]+word[4])
