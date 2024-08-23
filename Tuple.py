%%writefile tuple1.py
#ordered,immutable,duplicates allowed
ann=("manju","manasa","nagesh","vanitha",1,18)
print(len(ann))
print(dir(ann))
print(help(ann))
print(ann.index("vanitha"))
print(ann.count("manasa"))




%%writefile llpp.py
#conversion of tuple into list.........😎
man=[("manju","manasa","kk","sravani","sarala","bhavya")]
print(type(man))
