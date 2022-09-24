
words = []

with open("freeList.txt") as file:
    for line in file:
        words.append(line)
    print("Finished loading...")

with open("sortedFreeList.txt", "w") as sFile:
    for word in sorted(words, key=len):
        sFile.write(word)
    print("Finished sorting...")
