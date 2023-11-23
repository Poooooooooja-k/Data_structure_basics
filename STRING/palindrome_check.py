# check if given word is palindrome or not 
def palind(word):
    if word==word[::-1]:
        print("word is palindrome")
    else:
        print("word is not palindrome")
word=input("enter a word")
palind(word)