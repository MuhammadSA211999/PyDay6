from re import match,search,findall,sub
# Re hocce Python er regular expression library
# Python regular expression (RegEx): RegEx are tool for manipulating string.

'''
search() => puru string er moddhye khuje, object return kore. sei object er modhye end(), start(), span() thake.

search() er return kora object function gulu list-index return kore.

search() string er moddhye pattern match holei true/false return korei string theke beriye ase. baki string er moddhye pattern check kore na.

match() => sentence/string er protome khuje. boolean value true/false return kore.

findall() => puru *string/sentence er modhye khuze. zekhane zekhane pattern match korbe sei pattern string niye ekti array/list return kore. 

sub()=> sub() method *3 ti argument recieve kore. *sub(pattern, replaceValue, text). text sentence/string e *pattern match korle *replaceValue diye sei match kora ongsho ke replace kore dey.

sub() method pattern diye replace howya notun string return kore.

'''
# MATCH()
pattern='msa'
text='My name is msa. MSA is an entrepreneur'
if match(pattern,text):
    print('// Matched')
else:
    print("// Don't matched")
# don't matched // My name is msa. MSA is an entrepreneur
# matched // MSA is an entrepreneur

# SEARCH()
pattern='MSA'
text='My name is MSA. MSA is an entrepreneur'
matched=search(pattern,text)
if matched:
    whereStartMatch=matched.start() #11
    whereEndMatch=matched.end() #14
    startToEndMatched=matched.span() #(11,14)
    print(whereStartMatch,whereEndMatch,startToEndMatched)
else:
    print("// Don't matched")

# FINDALL()
pattern='MSA'
text='My name is MSA. MSA is an entrepreneur'
matched=findall(pattern,text)
if matched:
    print(matched)
# [MSA, MSA]


# FINDALL in FUNCTIONAL WAY
def isMatched(pattern,text):
    matchedList=findall(pattern,text)
    if len(matchedList)>0:
        return matchedList
    else:
        return f"{pattern} don't matched on any word: '{text}'"

pattern='MSA'
text='My name is MSA. MSA is an entrepreneur'
howManyMatched=isMatched(pattern,text)
# print(howManyMatched)


# functionally explained sub() method

def replaceWithValue(pt,rpVl,txt):
    if len(pt)>0 and len(rpVl)>0 and len(txt)>0:
        replaced=sub(pt,rpVl,txt)
        print(replaced)
        return replaced
    else:
        return 'You have enter 3 value'

pattern='msa'
replaceValue='MSA'
text='My name is msa. msa is an entrepreneur.'

result=replaceWithValue(pattern,replaceValue,text)
# print(result) My name is MSA. MSA is an entrepreneur.
