# Check if word contain numbers
from timeit import repeat


def is_number(s):
    return any(i.isdigit() for i in s)

wordList = []


# Load words into list
with open("words.txt") as wordsTxtFile:
    print("\nLoading words...\n")
    for line in wordsTxtFile:
        # Append to the wordList[]
        wordList.append(line.rstrip())
    print("Loaded!\n")


# Remove words like aaa, bbb, zzz and so on
for word in sorted(wordList):
    for i in word:
        if word.count(i) == len(word):
            repeatedBool = True
            try:
                wordList.remove(word)
                print(f"Removed word: {word}")
            except ValueError:
                pass
            
        # elif len(word) < 5 and word.count(i) > 2:
        #     try:
        #         wordList.remove(word)
        #         print(f"Removed word: {word}")
        #     except ValueError:
        #         print(f"Word {word} already removed.")
                



# If word contains a number - remove it
rNumWords = 0
checked_Num_words = 0

for word in sorted(wordList):
    checked_Num_words += 1

    if is_number(word):
        wordList.remove(word)
        rNumWords += 1

    print(' - Removing words with numbers: Will be removed[%d] - Checked words: %d/%d\r'%(rNumWords, checked_Num_words, len(wordList)), end="")

print("\nFinished removing words with numbers!\n")



# Remove words with symbols
symbols = [",", ".", "%", "-", "_", ":", "'", '"', "&", "$", "*", "/", "!", " "]

checkedSymbolCounter = 0


for sym in symbols:
    checkedSymbolCounter += 1
    wordList = [w.replace(sym, '') for w in wordList]
    print(' - Removing words with symbols: - Checked symbols: %d\r'%(checkedSymbolCounter), end="")

print("\nFinished removing words with symbols!\n")



# # Remove words shorter than 3 digits and longer than 6
rLengthWords = 0

for word in sorted(wordList):
    if len(word) < 4:
        wordList.remove(word)
        rLengthWords += 1

    elif len(word) > 6:
        wordList.remove(word)
        rLengthWords += 1

    print(' - Removing words with numbers: Will be removed[%d] - Total left words: %d\r'%(rLengthWords, len(wordList)), end="")
print("\nFinished removing words shorter than 4 digits and longer than 6!\n")


# Writing back to the text file
print("\nFinishing...please wait...")
with open('words.txt', 'w') as wordsTxtFile:  # Open in mode "w" removes all the data from the file.
    for word in wordList:
        wordsTxtFile.write(word.lower() + ".eth" + "\n")  # Writes the entire list into the file
print("All finished!!")
