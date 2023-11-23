# capitalize half of string
def half_cap(sent):
    res=" "
    half=len(sent)//2
    for i in range(len(sent)):
        if i<half:
            res+=sent[i].upper()
        else:
            res+=sent[i]
    return res
sent=input("enter the string")
result=half_cap(sent)
print(result)   