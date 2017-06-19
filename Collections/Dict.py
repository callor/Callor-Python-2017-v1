import operator
alist ={'a':100,'c':20,'b':30}
blist ={2:'a',1:'c',5:'d',3:'f'}

# sorted_x = sorted(x.items(), key=operator.itemgetter(0))

bKeylist = list(blist.keys())
bKeylist.sort()
for i in bKeylist:
    print(i)

keylist = list(alist.keys())
print(type(keylist))
keylist.sort()

for i in keylist :
    print(i,':',alist[i])
