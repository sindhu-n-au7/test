# Question-   Given a sorted array and a target value, return the index if the target is found. 
# 			If not, return the index where it would be if it were inserted in order. 
# 			[You may assume no duplicates in the array.]

# 			[1,3,5,6], 5 → 2
# 			[1,3,5,6], 2 → 1
# 			[1,3,5,6], 7 → 4
# 			[1,3,5,6], 0 → 0


#Answer-
def searchInsert(lst, target):
    begin = 0
    end = len(lst) - 1
    insertPos = 0
    while begin <= end:
        mid = (begin + end) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] > target:
            end = mid - 1
            insertPos = mid
        else:
            begin = mid + 1
            insertPos = mid + 1
    return insertPos
size = int(input("Enter the size of list ->"))
lst=[]
for i in range(0, size): 
    ele = int(input())
    lst.append(ele)
target = int(input("Enter the value that you want to search ->"))
print("List you entered is ->",lst)
print("Target value you entered is ->", target)
print(searchInsert(lst,target))