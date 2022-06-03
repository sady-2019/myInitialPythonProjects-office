#prob-2
# import sys
# print('python version')
# print(sys.version)
# print('Version Info')
# print(sys.version_info)

# #prob-3
# import datetime
# now=datetime.datetime.now()
# print('Current date and time: ')
# print(now.strftime("%y-%m-%d \n%H-%M-%S"))


# #prob-4
# import math
# radius=int(input('Type the radius of the circle: '))
# area= math.pi *(radius**2)
# print(:area)

#altn soln
# from math import pi
# r = float(input ("Input the radius of the circle : "))
# print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))


#prob-5
# firstName=str(input('Enter your first name: '))
# lastName=str(input('Enter your last name: '))
# print(lastName,firstName)


#prob-6
# num=str(input("Enter a number with comma: "))
# List= num.split(",")
# Tuple= tuple(List)
# print("List is ", List)
# print("Tuple is ", Tuple)


#prob-7
# fileName=str(input('Enter the file name: '))
# fileExt=fileName.split('.')
# print('Extention of file name is '+ repr(fileExt[-1]))

# altn soln
# fileName=input('Enter the file name: ')
# fileExt=fileName.rsplit(sep=None,maxsplit=1)
# ext=str(fileExt)
# print('Extention of file name is ')
# print(fileExt)


#prob-8
# color_list = ["Red","Green","White" ,"Black"]
# firstcolors=color_list[0]
# lastcolors=color_list[-1]
# print(firstcolors,lastcolors)

#altn soln
# color_list = ["Red","Green","White" ,"Black"]
# print('%s %s'%(color_list[0],color_list[-1]))




# prob- extra
# distCovered= input('what is the distance you covered? ')
# timeTaken= input('how much time it has taken? ')
# destination=input('where were you going? ')
# speed=round(float(distCovered)/float(timeTaken),2)
# # print('In your jounney to %s your avg speed was %s'%(destination,speed))
# print('In your jounney to {} your avg speed was {}'.format(destination,speed))
# print(f'In your jounney to {destination} your avg speed was {speed}')

# prob-9
# exam_st_date = (11, 12, 2014)
# print(f'Exam will start at {exam_st_date[0]}/{exam_st_date[1]}/{exam_st_date[2]}')

# # prob-10
# n=int(input('Enter a value:'))
# n1=int(f'{n}')
# n2=int(f'{n1}{n1}')
# n3=int(f'{n2}{n1}')
# sum=n1+n2+n3
# print(sum)

#prob-12
# import calendar
# print("Calendar of this yr is:")
# print(calendar.calendar(2021,2,1,6,6))
# print(calendar.month(2021,7))

# prob-13
# print("""
# a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string --------> example
# """)


# prob-14
