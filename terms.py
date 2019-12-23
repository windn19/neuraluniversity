
n = int(input())
terms = []
a = set()
i = 1
while i <= n:
        terms.append(i)
        a.add(i)
        n -= i
        i += 1
else:
    if n not in a:
        r = n
    else:
        terms.pop()
        r = i-1+n
    terms.append(r)
print(len(terms))
print(*terms)
