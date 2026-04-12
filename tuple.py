# 3.1 Create and access tuple
my_tuple = (10, 20, 30, 40)
print("Tuple:", my_tuple)
print("Second element:", my_tuple[1])

# 3.2 Nested tuple
nested_tuple = (1, 2, (3, 4, 5))
print("Nested Tuple:", nested_tuple)
print("Access nested element:", nested_tuple[2][1])

# 3.3 Repetition of tuple
repeated_tuple = my_tuple * 2
print("Repeated Tuple:", repeated_tuple)

# 3.4 Concatenation of tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concat_tuple = tuple1 + tuple2
print("Concatenated Tuple:", concat_tuple)