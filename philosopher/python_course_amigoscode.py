'''Creating File'''

# import os.path
#
# filename = "data.csv"
#
# if os.path.isfile(filename):
#     with open(filename,'r') as file:
#         print(file.read())
# else:
#     print(f'File {filename} does not exit')

'''Fetching data from internet'''
from urllib import request
import json


url = 'http://abcsps.blogspot.com/2021/07/building-ai-answers.html'
r = request.urlopen(url)
print(r.getcode())
data = r.read()
jsonData = json.load(data)
print(jsonData)



''''''