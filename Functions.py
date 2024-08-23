%%writefile daddy.py
def recap(a,b,n):
    print("arithmatic operations")
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
    print(a//b)
    print(a%b)
    print(a**b)
    a,b=b,a
    print("swapping")
    print(a,b)
    print("Factorial")
    fact=1
    for i in range(1,n,1):
             fact=fact*i

    print(fact)

    print("biggest number")
    if(a>b):
       print(f"{a} is bigger")
    else:
       print(f"{b} is bigger")


a=int(input("enter a value"))
b=int(input("enter b value"))
n=int(input("enter n value"))
recap(a,b,n)



%%writefile recapp.py
def recap1(n):
    if n%2==0:
      print("even")
    else:
      print("odd")



n=int(input("enter n value : "))
recap1(n)


%%writefile hiii.py
def mani(n) :
    print("reverse")
    while n>0:
          r=n%10
          print(r,end="")
          n=n//10

k=int(input("enter k value"))
mani(k)


%%writefile hi.py
def manishi(r):
    t=r
    s=0
    while r>0:
          k=r%10
          s=s+k*k*k
          r=r/10
    if s==t:
       print("armstrong")
    else:
       print("not a armstrong")
n=int(input("enter n value : "))
manishi(n)



%%writefile logi.py
def logicalfun(a,b,c):
    if a>b and a>c:
        print(f"{a} is big")
    elif(b>c):
        print(f"{b} is big")
    else:
        print(f"{c} is big")

    print(a&b)
    print(a|b)
    print(a^b)
    print(a<<2)
    print(a>>2)

    print(type(a))
    print(max(a,b,c))
    print(min(a,b,c))
    print(id(a))




    print(bin(200))
    print(oct(66))

    print(hex(10))



a=int(input("enter value"))

b=int(input("enter value"))

c=int(input("enter value"))
logicalfun(a,b,c)



%%writefile functions.py
def stry(s):
    k="hello"
    print(s+k)
    print(len(s))
    print(s[1:])
    print(s.replace('M','R'))
    print(s.upper()  )
    print(s.lower() )
    print(s.find("Man"))
    print(s.strip())
    print(s.split("j"))

s=input("enter yor string : ")
stry(s)
