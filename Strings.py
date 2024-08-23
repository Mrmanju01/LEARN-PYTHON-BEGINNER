%%writefile st.py
#concatenation of strings
s="manju"
k="natha"
r="Reddy"
print(s+k+r)

%%writefile st.py
#concatenation of strings
s="manju"
k="natha"
r="Reddy"
print(s+k+r)


%%writefile st2.py
s="manjunathareddy"
print(s.upper())

%%writefile st3.py
s="MANJUNATHAREDDY"
print(s.lower())


%%writefile st4.py
m="naveen"
print(m.replace('e','i'))

%%writefile st5.py
s="manjunathareddy"
print(s.find("d"))

%%writefile st6.py
s="manjunathareddy"
for i in range(0,len(s),1):
    print(s[i],end="   ")

%%writefile slicee.py
a="manju"
print(a[2:6])
print(a[:6])
print(a[2:])
print(a[-5:])
print(a[:-2])
print(a[-5:-1])

%%writefile Stripp.py
s="  manjunatha reddy"
print(s.strip())

%%writefile splitt.py
a="manjunatha2reddy"

print(a.split("2"))

%%writefile stings.py
age=36

print(f"My name is Manju,i'm {age}")
t="My name is Manju,i'm {}"
print(t.format(age))

%%writefile echar.py
print("manjunathareddy \r is son of \"K.Nageswarareddy\" ")
print("manjunathreddy  is good boy \n he is always doing \bsmart works \t he is clever \f person")

%%writefile loop.py
k="manju"
for x in k:
    print(x,end="")


%%writefile loop1.py
a=["manju","manasa","kalpana","deepu"]
for x in a:
    print(x,end=" ")
    if x=="kalpana":
      break


%%writefile loop2.py
a=["manju","manasa","kalpana","deepu"]
for x in a:
   if x=="kalpana":
      continue
   print(x,end=" ")

%%writefile rng.py
for x in range(0,50,5):
    print(x)

%%writefile nestedloop.py
a=["good","clever","hero","waste"]
b=["hemanth","manoj","narasimha","manju"]
for i in a:
    for j in b:

      print(a,b)


%%writefile temp.py
unit=input("enter unit C/F?")
tmp=float(input("enter the temperature"))
if unit=='C' or 'c':
    tmp=round((9*tmp)/5+32,2)
    print("the fahrenheat temp is", tmp)
elif unit=='F' or 'f':
    tmp=round((tmp-32)*5/9,2)
    print("the temp is in celesius is :",tmp)
else:
    print("invalid")


%%writefile email.py
email=input("enter email:")
ind=email.index("@")
u_s=email[:ind]
domain=email[ind+1:]

print(f"yours {u_s} and domain is {domain}")
