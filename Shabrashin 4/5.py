def sortSentence(self, s: str) -> str:
    words = s.split(' ')
    new_list = ['']*len(words)
    for word in words:
        ind = word[-1]


print(sortSentence("is2 sentence4 This1 a3"))