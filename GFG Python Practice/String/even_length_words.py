# Even Length Words
s = 'this is a test'
print([w for w in s.split() if len(w) % 2 == 0])
