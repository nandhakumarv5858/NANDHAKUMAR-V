def member(group_data, n):
    for value in group_data:
        if n == value:
            return True
    return False
print(member([1,  3], 8))
print(member([5,3], -6))
