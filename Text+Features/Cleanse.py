import os
import re

all_words = []
for file in os.listdir():
    if ".txt" in file:
        words = open(file).readline()
        words = words.split(";")
        all_words.extend(words)

unique_words = set(all_words)
u_w_copy = unique_words.copy()
for word in u_w_copy:
    if re.findall("[.\s\d]", word):
        unique_words.remove(word)

print(len(unique_words))
with open("vocabulary_cleansed.txt", "a") as file:
    file.write(";".join(unique_words))
    file.close()