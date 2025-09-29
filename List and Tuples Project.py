# STUDENT SUBJECT AND GRADE MANAGER

# Initial Lists
Student_List = ["Jayson", "Justin", "Jasmine", "Jeffrey", "Joson"]
Section_List = ["BSCS", "BSIT", "BSBM", "BSBE", "BSAD"]
print("Student_List:", Student_List)

# Display Specific Name
print("First Student:", Student_List[0])
print("Last Student:", Student_List[-1])

# Length of List
print("Total Students:", len(Student_List))

# Update the List
Student_List.append("Jemimah")
print("After Append:", Student_List)

Student_List.insert(2, "Jewel")
print("After Insert:", Student_List)

Student_List.remove("Jewel")
print("After Remove:", Student_List)

Student_List.pop()
print("After Pop:", Student_List)

# Count
print("Count of Justin:", Student_List.count("Justin"))

# Reverse
Student_List.reverse()
print("Reversed List:", Student_List)

# Sort
Student_List.sort()
print("Sorted List:", Student_List)

# Extend
Student_List.extend(Section_List)
print("Extended List:", Student_List)

# Delete and Clear
del Student_List[3]
print("After Deleting Index 3:", Student_List)

Student_List.clear()
print("After Clearing:", Student_List)

# Tuples
Section = ("BSCS", "BSIT", "BSBM", "BSBE", "BSAD")
print("Original Tuple:", Section)

Casting = list(Section)
print("Tuple Converted to List:", Casting)

Casting[4] = "BSEG"
print("Modified List:", Casting)

Casting_Tuples = tuple(Casting)
print("New Tuple:", Casting_Tuples)
