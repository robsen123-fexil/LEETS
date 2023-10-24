num = 432
n = str(num)
splt = list(n)
nest = []

print(splt)
for i in range(len(splt) - 1, -1, -1):
    nest.append(splt[i])

neint = int(''.join(nest))
print(neint)
