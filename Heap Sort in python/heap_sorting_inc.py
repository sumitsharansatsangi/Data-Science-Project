# A list used to store the user defined values 
heap=[]
# A variable to store the  size of the list.
size=int(input("Enter the size of your list: "))
for i  in range(size):
    el=int(input("Enter : "))
    heap.append(el)
heap1=heap
e=[]
d=[]
n1=len(heap)
def heapify_dec(c):
  n=len(c)
  #print(c)
  for i in range(n-1,0,-1):
     if((i>1) and (c[i]<c[int(i/2)-1])):
        c[i],c[int(i/2)-1]=c[int(i/2)-1],c[i]
     if((i==1)and (c[i]<c[0])):
         c[i],c[0]=c[0],c[i]
     #print("i= ",i)
     #print("c = ",c)
  return c
d=heapify_dec(heap)
for i in range(n1):
    element=d[0]
    #print("max = ",element)
    e.append(element)
    d[0]=d[len(d)-1]
    del d[len(d)-1]
    heapify_dec(d)
print("In Decreasing order : ",e)
