def dict_operations():
    print("--- 4. Dictionary Operations ---")

    # 4.1 Create and access dictionary elements
    student = {
        "name": "Alice",
        "age": 20,
        "course": "Computer Science"
    }
    print(f"Dictionary: {student}")
    print(f"Access 'name': {student['name']}")

    # 4.2 Update Dictionary
    student["age"] = 21            # Update existing key
    student["grade"] = "A"         # Add new key
    print(f"After Update: {student}")

    # 4.3 Removing Elements
    removed_val = student.pop("course")
    print(f"After removing 'course': {student}")

    # 4.4 Merging dictionaries
    extra_info = {"city": "New York", "hobbies": ["Reading", "Coding"]}
    student.update(extra_info)
    print(f"Merged Dictionary: {student}")
    print("-" * 30)

dict_operations()
