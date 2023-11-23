#remove duplicates 
def remove_dup(sent):
    words = sent.split()
    new = set()
    output = []
    for word in words:
        if word not in new:
            new.add(word)
            output.append(word)
    return " ".join(output)
sent = input("enter the sentence: ")
res = remove_dup(sent)
print(res)
