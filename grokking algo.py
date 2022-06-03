#binaary search # grokking algorithm page 9
def binary_search (list,item):
    low=0
    high=len(list)-1
    while low<= high:
        mid=(low+high)
        guess=list[mid]
        if guess== item:
            return mid
        elif guess>item:
            high= mid-1
        else:
            low=mid+1
    return none

my_list=[0,1,2,3,4,5]
print(binary_search(my_list,2))