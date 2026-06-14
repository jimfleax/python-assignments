# Pangram Check
import string
s = 'the quick brown fox jumps over the lazy dog'
print(set(string.ascii_lowercase) <= set(s.lower()))
