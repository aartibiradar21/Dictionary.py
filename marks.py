dic={'Math':81, 'Physics':83, 'Chemistry':87}
list1=[]
for i in dic:
    list1.append(dic[i])
s=0
while s<len(list1):
    j=0
    while j<len(list1):
        if list1[s]>list1[j]:
            tem=list1[s]
            list1[s]=list1[j]
            list1[j]=tem
        j+=1
    s+=1
# print(list1)
dict2={}
for i in list1:
    for k in dic:
        if dic[k]==i:
            dict2.update({k:i})
print(dict2)


