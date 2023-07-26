from re import match,search,findall,sub
# Re hocce Python er regular expression library
# Python regular expression (RegEx): RegEx are tool for manipulating string.

'''
search() => puru string er moddhye khuje, object return kore. sei object er modhye end(), start(), span() thake.

search() er return kora object function gulu list-index return kore.

match() => sentence/string er protome khuje. boolean value true/false return kore.

findall() => puru *string/sentence er modhye khuze. zekhane zekhane pattern match korbe sei pattern string niye ekti array/list return kore. 

sub()=> sub() method *3 ti argument recieve kore. *sub(pattern, replaceValue, text). text sentence/string e *pattern match korle *replaceValue diye sei match kora ongsho ke replace kore dey.
'''
pattern='msa'
text='My name is msa. MSA is an entrepreneur'
if match(pattern,text):
    print('// Matched')
else:
    print("// Don't matched")

# don't matched // My name is msa. MSA is an entrepreneur
# matched // MSA is an entrepreneur