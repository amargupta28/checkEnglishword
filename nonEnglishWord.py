# with open('song.txt','r') as f:
#     line = f.readlines()
#     print(line)

import enchant
import re

language = enchant.Dict("en_US")
englishWord=[]
nonEnglishWord=[]

with open('song.txt', 'r') as f:
    songList = f.read().strip()
    wordList =re.split(r"\s+['-]\s*|['-]\s+|[^a-zA-Z-']+", songList)

print(wordList)
finalList =[item for item in wordList if item.strip() != '']
# print(finalList)

for word in finalList:
    if language.check(word):
        englishWord.append(word)
    else:
        nonEnglishWord.append(word)


print("Total Word: ", len(finalList))
print("Total non english word: ", len(nonEnglishWord))
print("Total English word: ", len(englishWord))
print("English Word: ", englishWord)
print("Non English Word: " ,nonEnglishWord)
