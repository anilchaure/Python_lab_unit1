"""2) Create a list of 10 integers, a tuple of 5 fruit names, a dictionary of 5 student names mapped to
marks, and a set of 6 numbers (with duplicates). Perform: indexing/slicing on the list and tuple,
add/update/delete on the dictionary, and union/intersection/difference on two sets."""

# Program 2: Collection Operations

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print("List =", numbers)
print("Indexing =", numbers[2])
print("Slicing =", numbers[2:5])

fruits = ("Apple", "Mango", "Banana", "Orange", "Grapes")

print("\nTuple =", fruits)
print("Indexing =", fruits[1])
print("Slicing =", fruits[1:4])

students = {"Anil": 85, "Rahul": 78, "Priya": 92, "Sneha": 88, "Amit": 75}

print("\nDictionary =", students)

students["Riya"] = 90
print("After Adding =", students)

students["Rahul"] = 82
print("After Updating =", students)

del students["Amit"]
print("After Deleting =", students)

set1 = {1, 2, 3, 4, 4, 5}
set2 = {4, 5, 6, 7, 7, 8}

print("\nSet 1 =", set1)
print("Set 2 =", set2)

print("Union =", set1.union(set2))
print("Intersection =", set1.intersection(set2))
print("Difference =", set1.difference(set2))
