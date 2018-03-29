import json
from difflib import get_close_matches
data =json.load(open("data.json"))
def meaning(s):
    if s in data:
        return data[s]
    elif len(get_close_matches(s,data.keys(),3,0.8))>0:
        l=get_close_matches(s,data.keys(),3,0.8)[0]
        c=input("did you mean '%s' ,If yes then enter Y or N if No : "%l)
        if c.upper()=='Y':
            return data[l]
        elif c.upper()=='N':
            return "Please Double check the word"
        else:
            return "we didn't understanf the Query"
    else:
        return "The word Does not Exist,please Double chech It."
word=input("enter a word: ")
out=meaning(word)
if type(out)== list :
    for item in out:
        print(item)
else:
    print(out)
