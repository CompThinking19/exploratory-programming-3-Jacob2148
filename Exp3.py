import re
def search(book):
    if type(book) != str:
        raise TypeError("does not exist")
    result = re.findall("[A-Za-z]+at\\b", book)
    at_words = []
    for word in result:
        if len(word) > 3:
            at_words.append(word)
    return at_words
source = open("expl3.txt")
group = source.read()
print search(group)
