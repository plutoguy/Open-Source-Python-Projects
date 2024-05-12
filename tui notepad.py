# A text user interface notepad by Pluto_Guy
# This project is under the mit license
# https://mit-license.org/

import os

try:
  os.makedirs("notes") #Creates a notes if the directory does not exist
except:
  pass   

while True:
  user = input("NoteBook > ")
  if user == "create":
    name = input("Name of file")
    file = open("notes/"+name+".txt","x")
    var = input("Type [/newlinenote] > ")
    var = var.replace("/newlinenote","\n")
    file.write(var)
  elif user == "edit":
    for file in os.listdir("notes"):
      file = file.replace(".txt","")
      print(file)
    file = input("File to edit > ")
    filevalue = open("notes/"+file+".txt","r")
    file = open("notes/"+file+".txt","a")
    var = input("Type [/newlinenote] > ")
    var = var.replace("/newlinenote","\n")
    var = filevalue.read()+var
    file.write(var)
  elif user == "read":
    for file in os.listdir("notes"):
      file = file.replace(".txt","")
      print(file)
    file = input("File to read > ")
    filevalue = open("notes/"+file+".txt","r").read()
    print(filevalue)
