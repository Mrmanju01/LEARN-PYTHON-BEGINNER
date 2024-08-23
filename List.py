%%writefile list0.py
a=["Manju","Manasa","NageswaraReddy","Vanitha","KK"]
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[-1])
print(a[-2])
print(a[-3])
print(a[-4])
print(a[-5])
print(f"{a[0]} is son of {a[2]} ")
print(f"{a[1]} is daughter of {a[2]} ")
print(f"{a[3]} is wife of {a[2]} ")
print(f"{a[0]} is hubby of {a[-1]} ")
print(f"{a[-1]} is sister-in-law of {a[1]} ")



%%writefile list2.py
a=["CSE","ECE","EEE","CE","ME","DS","AI","AIDS","AIML"]
print(len(a))
print(a[0:])
print(a[:8])
print(a[0:5])


%%writefile list3.py

m=["CSE","ECE","EEE","CE","ME","DS","AI","AIDS","AIML"]
print(m.sort())
del m[-2]
print(m)
print(m[5:8])
print(max(m))
print(min(m))
