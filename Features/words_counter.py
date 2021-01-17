with open("conjugacao-verbos.txt") as file:
    verbs = file.readline()

print(len(verbs.split(";")))


with open("conjugacao-verbos_conjugados.txt") as file:
    verbs = file.readline()

print(len(verbs.split(";")))
print(len(set(verbs.split(";"))))


with open("dicio.txt") as file:
    words = file.readline()

print(len(words.split(";")))