
#tutorial 43/ lambda function

# from functools import reduce
#
# nums=[1,2,3,4,5,6,7,8,9.10,11,12,13,14,15,16,17,18,19,20]

# def is_even(n):
#     return n%2==0

#even= list(filter(is_even,nums))

# def update(n):
#     return n*2

# doubles= list(map(update,even))

# def add_all(a,b):
#     return a+b
#
# doubles= list(map(update,even))

# even= list(filter(lambda n:n%2==0,nums))
# doubles= list(map(lambda n:n*3,even))
# sum= reduce(lambda a,b: a+b, doubles)
#
# print(sum)


def f():
    m=1
    list = []
    for m in range (200):
        if 1000/5*m==0 :
            m=m+1
            list.append(5*m)

    print(list)
    s= sum(list)
    print(s)
f()

# m=1
# for m in range(1,100):
#     m= 1000/3
#     m=m+1
#     list=[]
#     list.append(m)
#     print(list)

# l=[]
# for i in range(20):
#     l.append(2)
# print (l)
