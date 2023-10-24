num = 432
n = str(num)
splt = list(n)
nest = []
print(splt)
ss=''.join(splt)
print(ss)
for i in range(len(splt) - 1, -1, -1):
    nest.append(splt[i])
ne=''.join(nest)

neint = int(ne)
#print(neint)


