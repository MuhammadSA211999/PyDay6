# charecter class: set of charecter
# example: pattern: r"[A-Z][a-z][0-9]" => charecter class
from re import match
# pattern=r"[aeiou]"
pattern=r"[A-Z][a-z][0-9]"
text='Msa01'
if match(pattern, text):
    print('Matched')
else:
    print("Don't matched")