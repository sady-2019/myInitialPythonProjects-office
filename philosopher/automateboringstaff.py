
catNames=[]

# while True:
#     name=input("Enter the name of the cat:")
#     catNames= catNames+ [name]
#     print(catNames)

spam={'cat':2,'rat':5,'bat':3}
# print("cat" in spam.keys())
#
# print( 'I have ' + str(spam.get('cat', 0))+ ' cats')
#
# spam.setdefault('hat',8)
# print(spam)

# import pprint
#
# message='It was a bright cold day in April, and the clocks were striking thirteen.'
# count={}
#
# for charecter in message:
#     count.setdefault(charecter,0)
#     count[charecter]+=1
#
# pprint.pprint(count)


'''Tic tac toe game 
(very basic one )'''

# theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
# 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
# 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
#
# def printBoard(board):
#     print(board["top-L"]+ '|' +board["top-M"]+ '|' +board["top-R"])
#     print('-+-+-')
#     print(board["mid-L"] + '|' + board["mid-M"] + '|' + board["mid-R"])
#     print('-+-+-')
#     print(board["low-L"] + '|' + board["low-M"] + '|' + board["low-R"])
#
# turn= 'x'
# for i in range(9):
#     printBoard(theBoard)
#     print('Now the turn is for '+ turn + ' Which cell do you want it to be?')
#     cell=input()
#     theBoard[cell]= turn
#     if turn=='x':
#         turn='0'
#     else:
#         turn='x'
#
# printBoard(theBoard)

'''Picnic'''

# allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
# 'Bob': {'ham sandwiches': 3, 'apples': 2},
# 'Carol': {'cups': 3, 'apple pies': 1}}
#
#
# def f(dic,key):
#     itemBoughtinPicnic=0
#     for k,v in dic.items():
#         itemBoughtinPicnic+=v.get(key,0)
#     return itemBoughtinPicnic
#
# print(" Name of things bought in the picnic")
# print('pretzels-'+str(f(allGuests,'pretzels')))
# print('ham sandwiches-'+str(f(allGuests,'ham sandwiches')))
# print('cups-'+str(f(allGuests,'cups')))
# print('apple pies-'+str(f(allGuests,'apple pies')))

'''Inventory.py'''

# stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
#
# def inventory(inventory):
#     print('Inventory')
#     itemTotal=0
#     for k,v in inventory.items():
#         print(str(v) + ' '+ k )
#         itemTotal += v
#     print("Total item: "+ str(itemTotal))
#
# inventory(stuff)


'''Fantasy Game'''



def addToInventory(inventory, addedItems):
    for k,v in inventory.items():


inv = {}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)

