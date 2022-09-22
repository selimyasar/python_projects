s = "selim yasar"

def solve(s):
    return ' '.join(i.capitalize() for i in s.split(' '))

#print(solve(s))

def solve2(s):
    for i in s.split():
        s = s.replace(i,i.capitalize())
    return s

#print(solve2(s))

def solve3(s):
    s = s.title()
    return s;

print(solve3(s))


