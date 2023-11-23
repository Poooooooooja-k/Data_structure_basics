# print the word with even length
def even_length(sent):
    words=sent.split()
    for word in words:
        if len(word)%2==0:
            print(word)
sent=input("enter the sentence")
even_length(sent)