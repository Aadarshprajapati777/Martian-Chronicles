list=[3,4,3,2,5,8,6,4]

# bubble sort

for i in range(len(list)-1,0,-1):
    for j in range(i):
        if list[j]>list[j+1]:
            list[j], list[j+1]=list[j+1],list[j]
print(list)

#insertion sort

for i in range(1,len(list)):
    j=i
    while j>0 and list[j]<list[j-1]:
        list[j],list[j-1]=list[j-1],list[j]
        j -=1
print(list)

#selection sort

for i in range(len(list)):
    min=i
    for j in range(i+1,len(list)):
        if list[j]<list[min]:
            min=j
    list[i],list[min]=list[min],list[i]
print(list)
