# Find Winner
from collections import Counter
votes = ['a', 'b', 'a', 'c', 'b', 'a']
c = Counter(votes)
print(max(c, key=c.get))
