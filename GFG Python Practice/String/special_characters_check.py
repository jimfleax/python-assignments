# Special Characters Check
import re
s = 'hello@world'
print(bool(re.search('[@_!#$%^&*()<>?/\|}{~:]', s)))
