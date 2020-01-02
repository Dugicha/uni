f = open("essay.txt", "r")

extra_signs = ["", "\n", ".", ",", "!", "?", ":", "(", ")", "-", "/"]
delimiter = " "

input_text = f.read()
f.close()

for extra_sign in extra_signs:
	input_text = input_text.replace(extra_sign, "") 

tempWordList = input_text.split(delimiter)
wordList = []

# Clear extra stuff from tempWordList
for word in tempWordList:
    if word not in extra_signs:
        wordList.append(word)

wordDict = {} # {word: count}

for item in wordList:
	if item not in wordDict:
		wordDict.update({item: 1})
	else:
		wordDict[item] = wordDict[item] + 1

for item in wordDict:
	print("{} - {}".format(item, wordDict[item]))

print("Total words:", len(wordList))

