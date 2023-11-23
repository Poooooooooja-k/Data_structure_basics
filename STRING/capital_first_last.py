# capitalize 1st and last character of a string
def caps(sent):
    return sent[0].upper()+sent[1:-1]+sent[-1].upper()
sent=input("enter a string: ")
res=caps(sent)
print(res)