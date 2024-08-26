#normal
x= lambda x:x+10
print(x(5))

# Lambda function that multiplies two numbers
multiply = lambda x, y: x * y

print(multiply(3, 4))  # Output: 12
#muiltiple function
numbers = [1, 2, 3, 4, 5]
# Apply a lambda function to square each number
squared = list(map(lambda x: x ** 2, numbers))

print(squared)  # Output: [1, 4, 9, 16, 25]

#
numbers = [1, 2, 3, 4, 5]
# Filter out only even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))

print(evens)  # Output: [2, 4]
#
points = [(1, 2), (3, 1), (5, 4)]
# Sort the list of tuples by the second element
sorted_points = sorted(points, key=lambda point: point[1])

print(sorted_points)  # Output: [(3, 1), (1, 2), (5, 4)]
