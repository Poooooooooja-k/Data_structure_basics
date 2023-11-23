def capital(sen):
    words=sen.split()
    capitals=[word.capitalize() for word in words]
    return ' '.join(capitals)
sen=input("enter a sentence: ")
res=capital(sen)
print(res)