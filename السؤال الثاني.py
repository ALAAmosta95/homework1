b=input("enter an binary number: ")
d=0
l=[]
for i in b:
    l.append(int(i))
l.reverse()
for i in range(len (l)):
        d+=l[i]*2**i
print(d)

