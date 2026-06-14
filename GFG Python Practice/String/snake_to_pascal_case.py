# Snake to Pascal Case
s = 'snake_case_string'
print(''.join(x.capitalize() for x in s.split('_')))
