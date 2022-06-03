# name= input('tell your name:')
# age= int(input ('tell your age:'))
# if name == 'sady':
#     print('hi sady')
# elif age<12:
#     print('hi you are not sady')



# name= ''
# while name != 'albert':
#     print('please enter your name')
#     name= input()
# print('Thank you')

# while True:
#     print('Enter your name')
#     name=input()
#     if name== 'albert':
#         break
# print('Thank You')


# while True:
#     print('enter your name')
#     name= input()
#     if name!= 'sady':
#         continue
#     print('hellow joe what is the pass word , its a fish!')
#     password=input()
#     if password=='sowrdfish':
#         break
# print('Thank You')


# name=''
# while not name:
#     print('Enter your name')
#     name= input()
# print('How many guest ?')
# numofguest= input()
#
# if numofguest:
#     print('Be sure that enough room is left')
# print('done')



# total=0
# for i in range(10):
#     total=total+i
# print(total)


# import random
# for i in range(5):
#     print(random.randint(1,100))


# import sys
#
# while True:
#     print('type exit to exit')
#     respose=input()
#     if respose== 'exit':
#         sys.exit()
# print('donee')

# spam=int(input())
# if spam==1:
#     print("hello")
# elif spam==2:
#     print('howdy')
# else:
#     print('greetings')



# for i in range(1,11):
#     print(i)

# i=1
# while i<11:
#     print(i)
#     i=i+1

# def countdown(i):
#     print(i)
#     countdown(i-1)
# print(countdown(10))

# def countdown(i):
#     print(i)
#     if i<=0:
#         return
#     else:
#         countdown(i-1)
# print(countdown(10))

# import random
# def answer(word):
#     if word==2:
#         return 'its a good number'
#
# r=random.randint(1,2)
# fortun=answer(r)
# print(fortun)

# print ('my','name','is','sady')


# def spam(devidedby):
#     try:
#         return 42/devidedby
#     except ZeroDivisionError:
#         print('invalid')
#
# print(spam(2))
# print(spam(22))
# print(spam(0))
# print(spam(8))


#Guess game (book: Automate th boring staff)

# import random
# secretNum= random.randint(1,10)
#
# print ('I am thinking of a number. Can you guess it?')
#
# for guesstaken in range(1,7):
#     print('take a guess:')
#     guess= int(input())
#     if guess<secretNum:
#         print('your guess is too low')
#     elif guess>secretNum:
#         print('Your guess is too high')
#     else:
#         break
# if guess==secretNum:
#     print('Well done! you corrcetly guessed in '+ str(guesstaken)+ ' guesses')
# else:
#     print('You failed to guess correctly')


#Exercise Problem

# def collatz(number):
#     if number%2==0:
#         print('number//2')
#         return number//2
#     print('3*number+1')
#     23return 3*number+1
#
#
# try:
#     num = int(input('Enter a Number: '))
#     result = collatz(num)
#     while result != 1:
#         collatz(result)

# except ValueError:
#     print('Enter a valid number')

# spam=[['cat','bat','rat','hat'],[10,30,40,50,45,34,37]]
# print(spam[1][2])


#
# spam1=['cat','bat','rat','hat']
# # # print(spam1[0:3])
# spam1=spam1 +[1,2,3,5]
# # print(spam1[-8])
#
# list=['tuhin','islam','rifat','shahin','karim','lenin','hasnain']
# list=list+spam1
#
# del list[-8:-2]
# print(list)


# catnames=[]                                                         #prog using list, amazing experience
#
# while True:
#     name=input("Enter your number " +str(len(catnames)+1) + " cat's name: ")
#     if name=='':
#         break
#     catnames=catnames+[name]
# print ('My cats names are  ')
# for name in catnames:
#     print (name)


# list=['tuhin','islam','rifat','shahin','karim','lenin','hasnain']
# for i in range(len(list)):
#     print("Index "+ str(i)+ ' belongs to '+ list[i])


# list=['tuhin','islam','rifat','shahin','karim','lenin','hasnain']
# 'sady' in list


# mypets=['kitty','tommy','billy','gilly']

# while True:
#     name = input('Enter the name of the animal you see here ')
#     if name in mypets:
#         print(name + ' is my pet')
#         break
#     else:
#         print('I dont have a pet named as ' + name)

# cat=['kitty','fat','white','aggressive']
# # name,disposition,color,temperment=cat
# # print(cat[3])
# hun='hakka'
# hun+=' how are you?'
# print(hun)

# motto=['hakka']
# motto*=5
# print(motto)

# mypets=['kitty','tommy','billy','gilly']
# print(mypets.index('gilly'))
# mypets.append('cally')
# print(mypets)
# mypets.insert(2,'illa')
# mypets.remove('billy')
# print(mypets)

# mypets.sort(reverse=True)
# print(mypets)


# import random                                                   #Magicball game
# customer_helpline_reply=['how can I help you','I am sorry','you are most welcome',
#                          'can you specify the issue','our tech team will contact you',
#                          'Is there any other issue we may solve','We shall fall back to you']
# print(customer_helpline_reply[random.randint(0,len(customer_helpline_reply)-1)])


# name='tanvir'
# for i in name:
#     print('________'+i+'________')


#
# customer_helpline_reply=['how can I help you','I am sorry','you are most welcome',
#                          'can you specify the issue','our tech team will contact you',
#                          'Is there any other issue we may solve','We shall fall back to you']

# for i in customer_helpline_reply:
#     print('-----'+i+'-------')
#

# name='sophie is a girl'
# newname= name[:9]+ ' one of the '+name[11:]
# print(newname)

# print(tuple(['cat','rat','bat','hat']))
# print(list(('cat', 'rat', 'bat', 'hat')))
# print(list('sady'))
# print (tuple('sady'))


# def multiple():  #projecteular problem1
#     sum = 0
#     multiple_of_five = 0
#     multiple_of_three = 0
#     for i in range(999):
#         if i % 3 == 0:
#             multiple_of_three += i
#         elif i % 5 == 0:
#             multiple_of_five += i
#         sum = multiple_of_three + multiple_of_five
#         print(sum)



# import copy
# alpha=['a','b','c','d']
# bravo=copy.copy(alpha)
# bravo[3]='aha'
# print(alpha)
# print(bravo)


# spam=['aha','maha','gaha','ruhu']
#
# # for i in spam:
# print(spam[:-1])
#

# print('Four score and seven \n\t\t\tyears ago...')



# def comma_code(items):
#     """ Combines list into a string of the form item1, item2, and item 3
#     Args:
#         items (list): List of strings
#     Returns:
#         string: list items combined into a string
#     """
#     item_len = len(items)
#
#     if item_len == 0:
#         return ''
#     elif item_len == 1:
#         return items[0]
#
#     return ', '.join(items[:-1]) + ', and ' + items[-1]
#
#
# if __name__ == "__main__":
#     spam = ['apples', 'bananas', 'tofu', 'cats']
#     print(comma_code(spam))



# cheese=['mango','jackfruit','apple','book']
# num=[1,2,4,6,9]
# for i in range(len(num)):
#     num[i]=num[i]+1
#
# print(num)



# for x in []:
#     print('This never happens')

# t=['g','a','b','c',]
# t.sort()



# set=[1,4,5,3,7,8]

# def add_all(t):
#     total=0
#     for i in t:
#         total=total+i
#     return total
# print(add_all(set))

# print(sum(set))



# cheese=['mango','jackfruit','apple','book']
# def capitalize_all(t):
#     res=[]
#     for i in t:
#         res.append(i.swapcase())
#     return res
#
# print(capitalize_all(cheese))

# cheese=['mango','Jackfruit','AP','book']

# def only_upper(t):
#     res=[]
#     for i in t:
#         if i.isupper():
#             res.append(i)
#     return res
#
# print(only_upper(cheese))


# cheese=['mango','Jackfruit','AP','book']
# var=cheese.pop(3)
# del cheese[:2]
# cheese.remove('AP')
# print(cheese)


# t='I am a good man'
# delimiter=' '
# list2=t.split(delimiter)
# print(list2)

# t=['I', 'am', 'a', 'good', 'man']
# delimiter=' '
# list2=delimiter.join(t)
# print(list2)


# eng2fren=dict ()
# eng2fren['i']='je'
# eng2fren['you']='tu'
# eng2fren['he']='il'
# eng2fren['she']='elle'
# eng2fren['they']='ils'
# eng2fren['we']='nous'
#
# val='he' in eng2fren.values()
# print(val)

# lis=['al','bal','cal']
# ord

#
# def histogram(s):
#     d=dict()
#     for l in s:
#         if l not in d:
#             d[l]=1
#         else:
#             d[l]+=1
#     return d
#
# def print_hist(h):
#     for k in sorted(h):
#         print(k,'=', h[k])
#
#
# h=histogram('sadddiis')
# print_hist(h)

# var=17
# while var>0:
#     print("I wont do that again")
#     var= var-1


# def reverse_lookup(d,v):
#     for k in d:
#         if d[k]==v:
#             return k
#     raise LookupError('Value does not contain here')
# h=histogram('imrankaleir')
# k=reverse_lookup(h,3)
# print(k)

# def histogram(s):
#     d=dict()
#     for l in s:
#         if l not in d:
#             d[l]=1
#         else:
#             d[l]+=1
#     return d
#
# def vert_dict(d):
#     inverse = dict()
#     for key in d:
#         val= d[key]
#         if val not in inverse:
#             inverse[val]=key
#         else:
#             inverse[val].append(key)
#     return inverse
#
# # def invert_dict(d):
# #     inverse = dict()
# #     for key in d:
# #         val = d[key]
# #         if val not in inverse:
# #             inverse[val] = [key]
# #         else:
# #             inverse[val].append(key)
# #     return inverse
#
# hist=histogram('iltutmmish')
# print(hist)
# inverse= vert_dict(hist)
# print(inverse)

# t=(1,4,5,6)
# s=(1,4,5,2)
# print(t>s)

# adds = 'sady_tanvir'
# # firstName,lastName = adds.split('_')
# # print(firstName, lastName)
# print(type(adds))

# quo,rem= divmod(123,23)
# print(rem, quo)

# result= 123,23
# def max_min(t):
#     return max(t),min(t)
# result1= max_min(result)
# print(result1)


# def sumall(*args):
#     return sum (args)
# result= sumall(2,4,3,5)
# print(result)



# birthday={'sady': ' 28 Feb','salman':' 23 Aug','rashed':' 2 Mar','foysal':' 1 april'}
#
# while True:
#     print( 'Enter your name:(enter blank for no response) ')
#     name= input()
#     if name== '':
#         break
#     elif name in birthday:
#         print ("Your birthday is"+ birthday[name])
#     else:
#         print('Sorry, I donot have a record of your birthday')
#         print('What is your bithday anyway?')
#         bday= input()
#         birthday[name]=bday
#         print('Your brithday is updated in the list')
#
#
# relief_dist= {'naogao': ' 34 pkt','natore': ' 23 pkt'}
# # for k ,v in relief_dist.items():
# #     print('today total '+ v + ' relief has been distributed in '+ k + ' district')
#
# # for v in relief_dist.values():
# #     print(v)
#
# # for k in relief_dist.keys():
# #     print(k)
#
# print ('7 EB has distributed total ' + str(relief_dist.get('naogao', 0)))


# guessing game function program
# import random

# def guessgame(x):
#     random_num = random.randint(1, x)
#     guess = 0
#     while guess != random_num:
#         print(f'Pl guess a number between 1 and {x}')
#         guess = int(input())
#         if guess < random_num:
#             print('sorry too low')
#         elif guess > random_num:
#             print('sorry too high')
#
#     print('You guessed correctly')
# guessgame(100)

# d={'q':23,'rt':34,'st':12}
# i=d.items()
# print (i)
# for key,value in d.items():
#     print(key,value)


#bithday catalogue
# catalogue=dict()
# count=1
# while True:
#     count+=1
#     name = str(input(f'Ques for no {count} person :what is your first name? '))
#     if name=='':
#         print ('Ok, I understand that you are busy right now'
#                '  we shall try it later')
#         break
#     bithday = str(input('Complementary ques for same person: what is your day? '))
#     catalogue[name]=bithday
# print('So far the list of bithday is ')
# print(catalogue)


# #prob regarding finding dictionary
# massage='with a heavy heart I had to say that we \nare all very surprised at your sudden decesion of quiting the \nservice'
# count=dict()
# for charectar in massage:
#     count.setdefault(charectar,0)
#     count[charectar]+=1
# # print(massage)
# print(count)
# print(count.keys())
# print(count.values())
# print(count.items())
# print(list(count.items()))

# for key ,value in count.items():
#     print(key,value)
# letter=count.get('v',0)
# print(f'you have letter v {letter} times')

# s='he is a good man but some problem'
# l=list(s)
# l2=count.keys()
#
# for pair in zip(l,l2):
#     print(pair)


#tic-tac-toe game,

# board={'t1':' ','t2':' ','t3':' ',
#         'm1':' ','m2':' ','m3':' ',
#         'l1':' ','l2':' ','l3':' '}
#
# def printBoard(X):
#     print(board['t1'] + '\t|' + board['t2'] + '\t|'+ board['t3'])
#     print('----+---+----')
#     print(board['m1'] + '\t|' + board['m2'] + '\t|' + board['m3'])
#     print('----+---+----')
#     print(board['l1'] + '\t|' + board['l2'] + '\t|' + board['l3'])
# turn='X'
# for i in range(9):
#     printBoard(board)
#     print(f'Its the turn of {turn}')
#     move=input('Enter your move.\nPl specify loc indicating row and colm (like m1 middle row 1 colm)')
#     board[move]=turn
#     if turn=='X':
#         turn='O'
#     else:
#         turn='X'


# linear search algorithm
# def linear_search(list,target):
#     for i in range(0, len(list)-1):
#         if list[i]==target:
#             return i
#     return None

# def verify(index):
#     if index is not None:
#         print("The value is position " , index)
#     else:
#         print('The value is not found')
#
# number=[1,2,3,4,5,6,7,8,9,10]
# result=linear_search(number,23)
# verify(result)


#binary search algorithm
# def binary_search(list,target):
#     first= 0
#     last=len(list)-1
#     while first<=last:
#         midpoint= (first +last)//2
#         if list[midpoint]== target:
#            return midpoint
#         elif list[midpoint]<target:
#             first = midpoint + 1
#         else:
#             last=midpoint-1
#     return None
#
# def verify(index):
#     if index is not None:
#         print("The value is position " , index)
#     else:
#         print('The value is not found')
#
# number=[1,2,3,4,5,6,7,8,9,10]
# result=binary_search (number,2)
# verify(result)



#recursive binaray search algorithm
# def recursive_binary_search(list,target):
#     if len(list)==0:
#         return False
#     else:
#         midpoint= (len(list))//2
#         if target==midpoint:
#             return True
#         else:
#             if target<midpoint:
#                return recursive_binary_search(list[midpoint+1:],target)
#             else:
#                 return recursive_binary_search(list[:midpoint-1],target)
# def verify(result):
#     print("Target found :",result)
#
# number=[1,2,3,4,5,6,7,8,9,10]
# result=recursive_binary_search(number,12)
# verify(result)

#inventory
# stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
#
# def displayInventory(inventory):
#     print('Inventory')
#     item= 0
#     for k,v in stuff.items():
#
#         print(str(v)+ " " + str(k))
#         item += v
#     print('total item ', str(item))
# displayInventory(stuff)


# #allguest inventory
# allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
# 'Bob': {'ham sandwiches': 3, 'apples': 2},
# 'Carol': {'cups': 3, 'apple pies': 1}}

# def inventoryList(list, item):
#     itembought=0
#     for k,v in allGuests.items():
#         itembought += v.get(item,0)
#     return itembought
#
# print('List of items being bought by guests')
# print('-apple being bought are', inventoryList(allGuests, 'apples'))


# inv = {'gold coin': 42, 'rope': 1}
# dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
#
# def displayInventory(inventory):
#     print('Inventory')
#     item= 0
#     for k,v in inv.items():
#         print(str(v)+ " " + str(k))
#         item += v
#     print('total item ', str(item))
#
#
# def addToInventory(inventory, addedItems):
#     for i in addedItems:
#         inventory.setdefault(i,0)
#         inventory[i]+=1
#     return inventory

# inv = addToInventory(inv, dragonLoot)
# displayInventory(inv)


# while True:
#     print("Type your password")
#     pass_word=input()
#     if pass_word.isalnum():
#         break
#     print('Pass word can only have alphabate and number')


# while True:
#     print("Enter your age")
#     age=input()
#     if age.isdecimal():
#         break
#     print("Age must be of digit not alphabate")

# name="-"
# name= name.join(['sady','ibrahhim','ikram'])
# print(name)

# name="ragiq is a, good boy"
# name=name.split(',')
# print(name)

# name='iqbal is Boy'
# ans=name.lower().endswith('boy')
# print(ans)



# item={'sandwitch':3,'mango':5,'potato':22,'grape':23}
#
# def picnic_item(item,left_width,right_width):
#     print('PICNIC ITEM'.center(left_width+right_width,'='))
#     for k,v in item.items():
#         print(k.ljust(left_width,'.')+str(v).rjust(right_width))
#
# print(picnic_item(item,20,1))


# name='           iiiiiiitiiitttiittisadyiiiiitttiiti            '
# name=name.lstrip().rstrip().strip('it')
# print(name)

# import pyperclip
# pyperclip.copy('sady')
# pyperclip.paste()


# import sys
# print(sys.argv[0])
# print(len(sys.argv))
# print(str(sys.argv))

# planets=['mars','venus','jupyter','earth','satarn']
#
# short_planets=[planet.upper() + '!'
#          for planet in planets
#          if len(planet)<7]
# print(short_planets)

# count=[2,-3,4,9,-5]
# print(sum(count))

# def has_lucky_number(nums):
#     """Return whether the given list of numbers is lucky. A lucky list contains
#     at least one number divisible by 7.
#     """
#     # for num in nums:
#     #     if num % 7 == 0:
#     #         return True
#     #
#     # return False
# def has_lucky_number(nums):
#     return any([num % 7 == 0 for num in nums])
#
# count=[2,4,6,9,14]
# print(has_lucky_number(count))

# value=['a','b','c']
#
# print(len(value))


# def word_search(doc_list, keyword):
#     """
#     Takes a list of documents (each document is a string) and a keyword.
#     Returns list of the index values into the original list for all documents
#     containing the keyword.
#
#     Example:
#     doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
#     >>> word_search(doc_list, 'casino')
#     >>> [0]
#     """
#     index = []
#     for i, doc in enumerate(doc_list):
#         word_list = doc.split()
#         modified_word_list = [word.rstrip(",.").lower() for word in word_list]
#         if keyword.lower() in modified_word_list:
#             index.append(i)
#     return index
#
# doc_list= ["The Learn Python Challenge Casino.",
#             "They bought a car",
#             "Casinoville",
#             'my name is khan',
#             'your name is not khan']
#
# print(word_search(doc_list,"khan"))


# def word_search(documents, keyword):
#     # list to hold the indices of matching documents
#     indices = []
#     # Iterate through the indices (i) and elements (doc) of documents
#     for i, doc in enumerate(documents):
#         # Split the string doc into a list of words (according to whitespace)
#         tokens = doc.split()
#         # Make a transformed list where we 'normalize' each word to facilitate matching.
#         # Periods and commas are removed from the end of each word, and it's set to all lowercase.
#         normalized = [token.rstrip('.,').lower() for token in tokens]
#         # Is there a match? If so, update the list of matching indices.
#         if keyword.lower() in normalized:
#             indices.append(i)
#     return indices

# documents = ["The Learn Python Challenge Casino.",
#             "They bought a car",
#             "Casinoville",
#             'my name is khan',
#             'your name is not khan']
#
#
# print(word_search(documents,"khan"))

