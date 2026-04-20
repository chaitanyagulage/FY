#Create a Dictionary
my_dict = {"name": "Sanskruti", "age":18, "city": "Pune"}
print(my_dict)
print(f"Original dictionary: {my_dict}")
#Accessing Elements 
print(f"Name: {my_dict['name']}")
#Updating Elements
my_dict['age'] = 19
print(f"Updated age: {my_dict['age']}")
#Removing Elements
del my_dict['city']
print(f"Dictionary after removing city: {my_dict}")
#Merge dictionaries 
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict1.update(dict2)
print(f"Merged dictionary (update()): {dict1}")
