u_list = [1,21,3,6,11,9,2]
s_list=u_list
l = int(len(s_list)/2)
while l > 0:
    for i in range(l, int(len(s_list)),+1):
        temp = s_list[i]
        j = i
        while j >= l and s_list[j-l] > temp:
           s_list[j] = s_list[j-l]
           j = j-l
        s_list[j] = temp
    l = l/2
print(s_list)
