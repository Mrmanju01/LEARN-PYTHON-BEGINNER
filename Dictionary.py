#creation
dicty={
  1:"manju",
  2:"kalpana",
  3:"deepu"
}
dicty.get(3)
#add
dicty[4]="kalpu"
dicty[5]="kalpu Reddy"
#del
del dicty[4]
#remove
dicty.popitem()

dicty.keys()
dicty.values()
dicty.items()
new_in={5:"kummathi",6:"Kanchireddy"}
dicty.update(new_in)

# Dict comprehension
# Example of dictionary comprehension
squares = {x: x*x for x in range(1, 6)}
print(squares)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

#list comprehension
# Create a list of squares from 1 to 5
squares = [x**2 for x in range(1, 6)]
print(squares)  # Output: [1, 4, 9, 16, 25]

# Nested dictionary
students = {
    'student1': {'name': 'Alice', 'age': 24},
    'student2': {'name': 'Bob', 'age': 22},
}

print(students['student1']['name'])  # Output: Alice


