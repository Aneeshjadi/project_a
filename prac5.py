
n=int(input("enter any number"))
m=n
rev=0
while(n>0):
  r=n%10
  rev=r+rev*10
  n=n//10
if (rev==m):
  print(rev," is palin no")
else:
  print(rev,"is not palin no")

