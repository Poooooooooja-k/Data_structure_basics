# print max length of word in sentence
def max_length(sen):
    words = sen.split()
    length = [len(word) for word in words]
    print(max(length))
sen = input("enter the sentence: ")
max_length(sen)
