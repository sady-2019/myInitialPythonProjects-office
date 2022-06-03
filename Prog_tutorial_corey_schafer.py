#programing terms first class function

# def square (n):
#     return n*n
#
# def cube(n):
#     return n*n*n
#
# def my_map(func, arg_list):
#     result=[]
#     for i in arg_list:
#         result.append(func(i))
#     return result
#
# num=[1,2,3,4,5,6,7,8,9]
# squares=my_map(square,num )
# cubes=my_map(cube,num)
#
# print(squares, cubes)


# def logger (msg):
#     def logger_msg():
#         print('Log:',msg)
#     return logger_msg
#
# log_hi=logger('Hi')
# log_hi()

# def html_tag(tag):
#     def wrap_txt(msg):
#         print('<{0}><{1}></{0}>'.format(tag,msg))
#
#     return wrap_txt
#
# print_hi=html_tag('h1')
# print_hi('What is your name?')







# Programming terms : Closures

# def outer_func():
#     message='hi'
#
#     def inner_func():
#         print(message)
#
#     return inner_func()
#
# outer_func()


# def outer_func():
#     message='hi'
#
#     def inner_func():
#         print(message)
#
#     return inner_func
#
# my_func=outer_func()
#
# my_func()
# my_func()
# my_func()


# def outer_func(msg):
#     message= msg
#
#     def inner_func():
#         print(message)
#
#     return inner_func
#
# hi_func=outer_func('Hi')
# hello_func=outer_func('hello')
#
# hi_func()
# hello_func()


# def html_tag(tag):
#     def wrap_txt(msg):
#         print('<{0}><{1}></{0}>'.format(tag,msg))
#
#     return wrap_txt
#
# print_func=html_tag('h')
# print_func("What is your name?")



# import logging
# logging.basicConfig(filename='example.log',level=logging.INFO)
#
# def logger(func):
#     def log_func(*args):
#         logging.info('Running "{}" with argument "{}"'.format(func.__name__, args))
#         print (func(*args))
#
#     return  log_func
#
# def add(x,y):
#     return x+y
#
# def sub(x,y):
#     return x-y
#
# add_logger=logger(add)
# sub_logger=logger(sub)
#
# add_logger(2,5)
# sub_logger(5,3)



# Decorator


def decorator_function(original_function):
    def wrapper_function(*args,**kwargs):
        print('wrappr funtion is executed before {}'.format(original_function.__name__))
        return original_function(*args,**kwargs)

    return wrapper_function

# def display():
#     print("Display function ran")
#
# display_decorator= decorator_function(display)
#
# display_decorator()

@decorator_function
def display():
    print('Display function ran. This is a new convention')

@decorator_function
def display_info(name,age):
    print('display_info function ran with argument ({},{})'.format(name,age))



display()
display_info("John", 24)










