Summary of collections Module:
namedtuple: Creates tuples with named fields for better code readability.
deque: A double-ended queue supporting fast appends and pops from either end.
Counter: A dict subclass for counting hashable objects (e.g., elements, characters).
OrderedDict: A dict subclass that remembers the insertion order of keys.
defaultdict: A dict subclass that provides default values for missing keys.
ChainMap: Combines multiple dictionaries into a single view.
UserDict, UserList, UserString: Classes that allow custom modifications of the behavior of dict, list, and string objects.





#namedtuple
from collections import namedtuple


# Define a named tuple
Person = namedtuple('Person', ['name', 'age', 'city'])

# Create instances
person1 = Person(name="Alice", age=30, city="New York")
person2 = Person(name="Bob", age=25, city="San Francisco")

# Accessing values
print(person1.name)  # Output: Alice
print(person2.city)  # Output: San Francisco


#deque
from collections import deque

# Create a deque
d = deque([1, 2, 3])

# Append to both ends
d.append(4)      # Append to the right
d.appendleft(0)  # Append to the left

# Pop elements from both ends
d.pop()         # Removes 4
d.popleft()     # Removes 0

print(d)  # Output: deque([1, 2, 3])

#counter
from collections import Counter

# Count elements in a list
nums = [1, 2, 2, 3, 3, 3, 4]
count = Counter(nums)

# Output: Counter({3: 3, 2: 2, 1: 1, 4: 1})
print(count)

# Get the most common elements
print(count.most_common(1))  # Output: [(3, 3)]


#orderedDict
from collections import OrderedDict

# Create an OrderedDict
od = OrderedDict()

# Insert key-value pairs
od['a'] = 1
od['b'] = 2
od['c'] = 3

print(od)  # Output: OrderedDict([('a', 1), ('b', 2), ('c', 3)])


#defaultDict
from collections import defaultdict

# Create a defaultdict with int as default type
dd = defaultdict(int)

# Accessing a non-existent key returns the default value (0)
print(dd['unknown'])  # Output: 0

# defaultdict for lists
dd_list = defaultdict(list)
dd_list['fruits'].append('apple')
print(dd_list)  # Output: defaultdict(<class 'list'>, {'fruits': ['apple']})

#Chainmap
from collections import ChainMap

# Create two dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# Chain the dictionaries
chain = ChainMap(dict1, dict2)
print(chain['b'])  # Output: 2 (from dict1)
print(chain['c'])  # Output: 4 (from dict2)


#UserDict
from collections import UserDict

class MyDict(UserDict):
    def __setitem__(self, key, value):
        print(f"Setting {key} to {value}")
        super().__setitem__(key, value)

my_dict = MyDict()
my_dict['key'] = 'value'  # Output: Setting key to value





