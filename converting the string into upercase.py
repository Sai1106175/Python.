
NamesList = ["sai", "Sharan", "varun"]

newnameslist =[]
for i in NamesList:
    newnameslist.append(i.upper())

print(newnameslist)

upercasewords =[]
upercasewords = list(map(str.upper, newnameslist)) # Cant directly conver the list of string at once.
print(upercasewords)
