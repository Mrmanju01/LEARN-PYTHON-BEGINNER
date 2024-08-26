#set creation 
my_set={"manju",1,100.2,True,6+i,False}

#adding elements
my_set.add("manjunathareddy")

#remove elements
my_set.remove(100.2)
#set operations=UNION,INTERSECTION,DIFFERENCE,SYMMETRIC DIFFERENCE

#union
s={"manju","natha","reddy"}
t={"deepu","kalpana","kalpu","reddy"}
s.union(t)
s.intersection(t)
s.difference(t) // output:{manju,natha}
t.difference(s) // output:{deepu,kalpana,kalpu}
s.symmetric_difference(t) // output:{manju,natha,deepu,kalpana,kalpu}

# Define two sets
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Perform operations
print("Union:", set_a.union(set_b))
print("Intersection:", set_a.intersection(set_b))
print("Difference (set_a - set_b):", set_a.difference(set_b))
print("Symmetric Difference:", set_a.symmetric_difference(set_b))



# Define a set
fruits = {"apple", "banana", "cherry"}

# Check if an element is in the set
if "banana" in fruits:
    print("Banana is in the set")
else:
    print("Banana is not in the set")
