def buter(s,d):
    while len(s)!=0:
        if min(s)==min(d) and s[0]!=d[0]:
            break
        if s[0]==d[0]:
            s.pop(0)
            d.pop(0)
        else: s.append(s.pop(0))
    return len(s)

print(buter(list(input()),list(input())))