def tol(x, y):
    if x == y or abs(x-y) == 5 or (x+y) == 5:
        return True
    else:
        return False

print(tol(7, 2))
print(tol(3, 2))
print(tol(2, 2))
