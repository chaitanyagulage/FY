def set_operations():
    print("--- 2. Set Operations ---")

    # 2.1 Create and access set elements
    set_A = {1, 2, 3, 4, 5}
    set_B = {4, 5, 6, 7, 8}
    print(f"Set A: {set_A}")
    print(f"Set B: {set_B}")
    
    # Note: Sets do not support indexing (e.g., set_A[0] will fail).
    # You access elements by iterating or checking presence.
    print(f"Is 3 in Set A? {3 in set_A}")

    # 2.2 Union of the elements (All unique elements from both)
    union_set = set_A.union(set_B) # OR set_A | set_B
    print(f"Union: {union_set}")

    # 2.3 Intersection of the elements (Common elements)
    intersection_set = set_A.intersection(set_B) # OR set_A & set_B
    print(f"Intersection: {intersection_set}")

    # 2.4 Difference of the elements (Elements in A but not in B)
    difference_set = set_A.difference(set_B) # OR set_A - set_B
    print(f"Difference (A - B): {difference_set}")
    print("-" * 30)

set_operations()
