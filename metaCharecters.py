# Meta Character with RegEx match() function
from re import match
'''
Here are some meta charecter:

dot/a..b: a and b er moddhye zekuno duiti letter takbe. duiti letter, beshi hole hobe na

*/a*: string e a letter takteo pare na taktheo pare

a*b: b er age a takteo pare na takteo pare

+/+a: string er a ek ba ekadik takte hobe.

a+b: string e a er por b ek ba ekadik takte hobe.

{and}/ a{1,3}: string e a ek theke 3 ta takte hobe.

^$/ ^ab....cle$: string must ab diye suru hobe ebong e diye shesh hobe.
?:ice(-)?cream: ice and cream er moddhye ekti highpen takte pare nao takte pare. orthat icecream and ice-cream lekha zay.
''' 
pattern=r"^sw..t$"
text='sweet is delicioust'
if match(pattern, text):
    print("// Matched")
else:
    print("// Don't matched")