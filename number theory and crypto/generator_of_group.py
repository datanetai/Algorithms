def generator(s,n):
    assert type(s) is set
    assert n>0
    results=[]
    for a in range(n):
        g=set()
        g.add(0) # zero is trivial
        for j in s:
            g.add(a**j%n)
        if g==s:
            results.append(a)
    return results

print(generator(set([0,1,2,3,4]),6)
)

