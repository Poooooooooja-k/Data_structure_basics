# reverse a given sentence
def reverse(sent):
    words=sent.split()
    rev=words[::-1]
    return ' '.join(rev)
sent=input("enter a sentence: ")
res=reverse(sent)
print(res)

