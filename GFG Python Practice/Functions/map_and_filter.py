# Map and Filter
l = [1, 2, 3, 4]
sq = list(map(lambda x: x*x, l))
even = list(filter(lambda x: x%2==0, l))
print(sq, even)
