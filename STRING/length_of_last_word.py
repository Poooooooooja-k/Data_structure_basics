def length_last(sent):
    words = sent.split()
    return len(words[-1])
sent = input("enter a sentence: ")
res = length_last(sent)
print(res)
