from itertools import combinations
str1,num1=map(int,input().split())
n1=len(str(str1))
L1=list(combinations(str(str1),n1-num1))
L1=(sorted(L1))
a1="".join(L1[0])
print(a1)
