vector1=vector()
vector2=vector()
n=as.integer(readline(prompt="Enter the size of list : "))
for (i in 1:n)
{
  x=as.integer(readline(prompt = "Enter : "))
  vector1<-c(vector1,x)
}  
print("Entered entries :")
print(vector1)
inc_sort<-function(x,i,vector2){
  m=min(x)
  vector2[i]=m
  i=i+1
  x<-x[!x==m]
  if(length(x)!=0){
    inc_sort(x,i,vector2)
  }
  else{
    return(vector2)
  }

}  
b=inc_sort(vector1,1,vector2)
print("In increasing order : ")
print(b)
