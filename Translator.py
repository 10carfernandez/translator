from urllib.request import Request, urlopen
import re

#Get current directory
cd = "C:\\Users\\Carlos\\Documents\\DiversityHackathonFiles\\"

#Open dictionary used for translating
dicfilename = "JavaKeywords.txt"
dicfile = open(cd + dicfilename)
dic = dicfile.read()
dicfile.close()
#Convert file into an array
dicarray = dic.split("\n")
dictArray = []
for pair in dicarray:
    dictArray.append(pair.split(","))
      
def OpenFile(filename):
    #Open txt file to translate and gather contents
    cdfilename = "{0}.txt".format(filename)
    cdfile = open(cd + cdfilename)
    contents = cdfile.read()
    cdfile.close()
    return contents

#Function that translate from English to Spanish:
def EnglishToSpanish(filename):
    newcontents = OpenFile(filename)
    for i in range(0, len(dictArray)):
        newcontents = newcontents.replace(dictArray[i][0], dictArray[i][1])
    flname = "Spanish" + filename + ".txt"
    testdat = open(cd + flname, "w")
    print(newcontents, file = testdat)
    testdat.close()

#Function that translate from Spanish to English:
def SpanishToEnglish(filename):
    newcontents = OpenFile(filename)
    for i in range(0, len(dictArray)):
        newcontents = newcontents.replace(dictArray[i][1], dictArray[i][0])
    flname = "English" + filename + ".txt"
    testdat = open(cd + flname, "w")
    print(newcontents, file = testdat)
    testdat.close()

EnglishToSpanish("samplejavacode")
SpanishToEnglish("Spanishsamplejavacode")
