u_list = [1,21,3,6,11,9,2]
s_list=u_list
for i in range(len(s_list)-1,0,-1):
        for j in range(i):
            if s_list[j]>s_list[j+1]:
                temp = s_list[j]
                s_list[j] = s_list[j+1]
                s_list[j+1] = temp                
print("In Increasing Order : ",s_list)
for i in range(len(u_list)-1,0,-1):
        for j in range(i):
            if u_list[j]<u_list[j+1]:
                temp = u_list[j]
                u_list[j] = u_list[j+1]
                u_list[j+1] = temp
print("In Decreasing Order : ",u_list)
