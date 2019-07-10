s=input()
q=['a','b,'c','d','e','f','g','h,'i','j','k','l','m','n','o','p','q','s','t','u','v','w','x','y','z']
c=0
for i in s:
    for j in q:
       if i==j:
       c=c+1
       q.remove(j)
print(c)
