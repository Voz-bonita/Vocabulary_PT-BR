import os

all_words = []
for file in os.listdir():
    if ".txt" in file:
        words = open(file).readline()
        words = words.split(";")
        all_words.extend(words)

print(len(set(all_words)))

with open("vocabulary.txt", "a") as file:
    file.write(";".join(all_words))
    file.close()
