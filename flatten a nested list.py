lis=[['r','e'],['v','a'],'t','h']
lis1=[]
for i in lis:
    for j in i:
        lis1.append(j)
print(lis1)

#        OR 
# lis1=[j for i in lis for j in i]
# print(lis1)
