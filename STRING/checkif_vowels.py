# check if all letters are vowels
def vowels_check(word):
    vowels="aeiouAEIOU"
    for i in word:
        if i not in vowels:
            return False
        return True
word=input("enter a word")
res=vowels_check(word)
print(res)


