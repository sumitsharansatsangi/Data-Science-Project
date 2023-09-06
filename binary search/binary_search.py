sort=[2,5,9,10,13,18,20,29,30,35]
l=0
u=len(sort)
print(u)
search=15
while(True):
    if(u==l+1):
        print("Not exist")
        break
    m=(l+u)//2
    if(sort[m]<search):
        l=m
        print("l= ",l," u = ",u)
    if(sort[m]>search):
        u=m
        print("u= ",u," l = ",l)
    if(sort[m]==search):
        print("Found at " ,m)
        break

