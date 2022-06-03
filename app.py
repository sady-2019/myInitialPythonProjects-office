# def arc(t, r, angle):
#     arc_length = 2 * math.pi * r * angle / 360
#     n = int(arc_length / 3) + 1
#     step_length = arc_length / n
#     step_angle = angle / n
#
# for i in range(n):
#     t.fd(step_length)
#     t.lt(step_angle)



# def is_divisible (x,y):
#     if x % y==0 :
#         return True
#     else:
#         return False
#
# print(is_divisible (6,4))



# def is_between (x,y,z):
#     if x<= y<= z:
#         return True
#     else:
#         return False
#
# print(is_between(4,5,9))



# def is_factorial(n):
#     if n==0:
#         return True
#     else:
#         recurse= is_factorial(n-1)
#         result=n* recurse
#         return result
#
# print(is_factorial(8))


# def fibonacci(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
#
# print(fibonacci(18))

# def countdown(n):
#     while n > 0:
#         print(n)
#         n = n - 1
#     print('Blastoff!')
#
# print(countdown(5))



# def countdown (n):
#     while n>0:
#         print(n)
#         n = n - 1
#     else:
#         print("blast off")
#
# print(countdown(7))


# def countdown(n):
#     if n <= 0:
#         print ("blast off")
#     else:
#         print(n)
#         countdown(n-1)
#
# print(countdown(7))


# while True:
#     line= input(">>>")
#     if line== "fuck":
#         break
#     print(line)
# print( "Congratulation You guessed right")



# a=16
# x=int(input(""))
# while True:
#     print(x)
#     y=(x+a/x)/2
#     if y==x:
#         break
#     x=y


# fruit='jackfruit'
# # len(fruit)
# index=0
# while index< len(fruit):
#     letter=fruit[index]
#     print(letter)
#     index+=1




# fruit='jackfruit' # exercise page 87
# index=-1
# while -8 <index < len(fruit):
#     letter= fruit[index]
#     print(letter)
#     index=index-1


# y='jackfruit'
# for x in y:
#     print (x)




# prefix= 'jklmnopq'  # exercise in page 87
# suffix_1='ack'
# suffix_2='uack'
#
# for letter in prefix:
#     if letter=='o' :
#         print(letter+suffix_2)
#     elif letter=='q':
#         print(letter+suffix_2)
#     else:
#         print(letter + suffix_1)



# prefix= 'jklmnopq'  # exercise in page 87
# suffix_1='ack'
# suffix_2='uack'
#
# for letter in prefix:
#     if letter=='o' and 'q' :
#         print(letter+suffix_2)
#     else:
#         print(letter + suffix_1)


# name1= "hasib"
# name2='islam'
#
# for letter in name1:
#     if letter in name2:
#         print (letter)
#

# sentence= 'rashed is a doctor'   #this is a example of invocation
# name='rashed'
# profession='doctor'
# search= sentence.find('doctor')
# # uppercase= sentence.upper()
# print(search)


# sum=0
# for i in range (10,18,3):
#     sum+=i
# print(sum)


# mysum=0
# for i in range(19,70,2):
#     mysum+=i
# print(mysum)


# x=3
# ans=0
# iterleft=x
# while iterleft != 0:
#     ans=ans+x
#     iterleft=iterleft-1
# print(str(x)+'x'+str(x)+'='+str(ans))


# fin=open("word.txt")
# line= fin.readline()
# word=line.strip()
#
# def has_no_e(word):
#     for letter in word:
#         letter== "a"
#         return False
#     return False
#
# print(has_no_e(word))



# cube= 8
# for guess in range (abs(cube)+1):
#     if guess**3==cube:
#         print('cube root of',str(cube) , 'is ', str(guess))


# name= input("enter a sentence:")
# for i in range(len(name)):
#     if name[i]=='o'or name[i]=='u':
#         print("there is a 'o' or 'u' in the sentence!!")

# for char in name:
#     if char== 'i' or char== 'o':
#         print("there is a 'o' or 'u' in the sentence!!")


# x='what'
# y= 'mon cheri'
# x=x+'  is your name?'+y
#
# print(x)



# int1= int(input('Enter a integer '))
# int2= int(input('Enter a integer '))
# product=int1*int2
# sum=int1+int2
#
# def provide_output():
#     if product>1000:
#         print(sum)
#     else:
#         print(product)
#
# provide_output()



                  #this example does not work. Needs explanation
# class Infbde:   #class variable
#     brunch='GS'
#     def _init_(self, clkname, sr): #instance variable
#         self.clkname=clkname
#         self.sr=sr
#
# obj1=Infbde('shafiq',1)
# obj2=Infbde('shohel',2)
#
# print(obj1.sr)
# print(obj2.svc)
# print(Infbde.GS)



# class Shark:
#     amimal= 'fish'         #class variable
#     location='ocean'
#     def _init_(self,name,age):
#         self.name=name     #instance variable
#         self.age=age
#
# obj1= Shark("akka",3)
# print(obj1.location)
#
# obj2= Shark("paku",5)
# print(obj2.name)



# import sys
# n=400
# m=400
# print(id(m))
# print(sys.getrefcount(m))

# complex_num= 6.67e-3
# print(complex_num)

# dic= {1:"sady", 3: "urme", 4: "Imran", 5: "Izzan"}
# print(dic[1])

# my_set= {"sady","urme","imram","izzan"}
# my_set.add('salahuddin')
# # print(my_set)
# f_set=frozenset(my_set)
# print(type(my_set))
# print(type(f_set))

# x=5
# y=6
# z=x<y
# print(z)


# pixel=[45,33,55,24,3]
# byte_data=bytes(pixel)
# print(byte_data[4])


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

mypets=['kitty','tommy','billy','gilly']
# print(mypets.index('gilly'))
mypets.append('cally')
print(mypets)
mypets.insert(2,'illa')
print(mypets)
























