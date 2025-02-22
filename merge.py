import random
def merge_sort(lst):
    if len(lst)>1:
        mid=len(lst)//2
        left_half=lst[:mid]
        right_half=lst[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i=j=k=0
        while i<len(left_half) and j<len(right_half):
            if left_half[i]<right_half[j]:
                lst[k]=left_half[i]
                i+=1
            else:
                lst[k]=right_half[j]
                j+=1
            k+=1
        while i<len(left_half):
            lst[k]=left_half[i]
            i+=1
            k+=1
        while j<len(right_half):
            lst[k]=right_half[j]
            j+=1
            k+=1
    return lst
def insertion_sort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
my_list=[]
for i in range(10):
   my_list.append(random.randint(0,999))
print("unsorted list")
print(my_list)
print("sorted list in insertion sort")
insertion_sort(my_list)
print(my_list)
my_list=[]
for i in range(10):
   my_list.append(random.randint(0,999))
print("unsorted list")
print(my_list)
print("sorted list in merge sort")
merge_sort(my_list)
print(my_list)
