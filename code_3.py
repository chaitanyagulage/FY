def tuple_operations():
    print("--- 3. Tuple Operations ---")

    # 3.1 Create and access
    my_tuple = (10, 20, 30, "Python")
    print(f"Tuple: {my_tuple}")
    print(f"Second element: {my_tuple[1]}")

    # 3.2 Nested Tuple
    nested_tuple = (1, 2, ("a", "b"), 3)
    print(f"Nested Tuple: {nested_tuple}")
    print(f"Accessing nested element 'b': {nested_tuple[2][1]}")

    # 3.3 Repetition of tuple
    repeat_tuple = ("Hi",) * 3
    print(f"Repetition: {repeat_tuple}")

    # 3.4 Concatenation of tuples
    tuple_1 = (1, 2)
    tuple_2 = (3, 4)
    concat_tuple = tuple_1 + tuple_2
    print(f"Concatenation: {concat_tuple}")
    print("-" * 30)

tuple_operations()
