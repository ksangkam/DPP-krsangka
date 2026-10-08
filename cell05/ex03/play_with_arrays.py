#!/usr/bin/env python3

original_array = [2, 8, 9, 48, 8, 22, -12, 2]
new_list = [x + 2 for x in original_array if x > 5]
new_array = set(new_list)

print(original_array)
print(new_array)
