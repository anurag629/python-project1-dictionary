import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word=word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys()))>0:
        yn=input("Did you mean %s instead.\nIf Yes press[y/Y] If Not press[n/N]: "%get_close_matches(word,data.keys())[0])
        if yn=='y' or yn=='Y':
            return data[get_close_matches(word,data.keys())[0]]
        elif yn=="n" or yn=="N":
            return "The word does not exist. Please double check it." 
        else:
            return "We don't understand, Try Again!"       
    else:
        return "The word does not exist. Please double check it."

word = input("Enter word:")

output=(translate(word))
if type(output)==list :
    for out in output:
        print(out)
else:
    print(output)        
