n = int(input())
a=(n)+(n-1)*(n+1)
for i in range(n):
 for j in range(i+1, n):
  print(' '*len(str(a)),end=' ')
  for j in range (i+1):
   b=(i+1) + i**2 + j*2
   padding=' '*(len(str(a))- len(str(b)))
   print(padding+str(b),end=' ')
   print()