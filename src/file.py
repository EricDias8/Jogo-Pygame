# Imports
import pygame, sys
from pygame.locals import *
import os

class TextFile():
    def __init__(self, fileName):
       self.file = fileName
       self.tempFile = "rankingtemp.txt"
    
    def readFile(self, newName, newTime, newLife):
        arquivo = open(self.file, "w")

        inserted = False
        with open(self.tempFile) as file:
            for item in file:
                line = item.split(";")
                name = line[0]
                time = line[1]
                life = line[2]

                if int(newLife) > int(life) and inserted == False:
                    arquivo.write(newName)
                    arquivo.write(";")
                    arquivo.write(newTime)
                    arquivo.write(";")
                    arquivo.write(newLife)
                    arquivo.write("\n")
                    inserted = True
                elif int(newLife) == int(life) and inserted == False: 
                    if int(newTime) >= int(time) and inserted == False:
                        arquivo.write(newName)
                        arquivo.write(";")
                        arquivo.write(newTime)
                        arquivo.write(";")
                        arquivo.write(newLife)
                        arquivo.write("\n")
                        inserted = True

                arquivo.write(name)
                arquivo.write(";")
                arquivo.write(time)
                arquivo.write(";")
                arquivo.write(life)

        if inserted == False:
            if os.stat(self.tempFile).st_size != 0:
                arquivo.write("\n") 
            arquivo.write(newName)
            arquivo.write(";")
            arquivo.write(newTime)
            arquivo.write(";")
            arquivo.write(newLife)         


        arquivo.close()


    def copyFileToTemp(self):
        with open("ranking.txt") as f:
            with open("rankingtemp.txt", "w") as f1:
                for line in f:
                    f1.write(line)

    def readTextFile(self):
        line = ""
        with open(self.file) as file:
            for item in file:
                line = item
        return line