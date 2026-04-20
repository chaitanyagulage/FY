#Create a Set
setA = {1, 2, 3, 4, 5}
setB = {4, 5, 6, 7, 8}
print("Set A:", setA)
print("Set B:", setB)
#Acessing set items and union, intersection, difference of Sets
for item in setA:
    print("Item in Set A:", item)
for item in setB:
    print("Item in Set B:", item)
unionSet = setA | setB
print("Union of Set A and Set B:", unionSet)
intersectionSet = setA&setB
print("Intersection of Set A and Set B:", intersectionSet)
differenceSet = setA-setB
print("Difference of Set A and Set B (A - B):", differenceSet)