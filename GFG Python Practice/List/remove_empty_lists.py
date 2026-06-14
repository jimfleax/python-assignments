# Remove Empty Lists
l = [1, [], 2, [], [], 3]
print([x for x in l if x != []])
