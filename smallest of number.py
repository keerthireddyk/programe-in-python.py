a,b=input().split()
b=int(b)
c=len(a)
l=[]
for i in range(0,c):
	k=a[i]
	l.append(k)
w=c-b
l1=[]
for i in range(b,c):
	k=l[i]
	l1.append(k)
print("".join(l1))
