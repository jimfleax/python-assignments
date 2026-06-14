# Word Frequency
s = 'apple banana apple'
d = {}
for w in s.split(): d[w] = d.get(w, 0) + 1
print(d)
