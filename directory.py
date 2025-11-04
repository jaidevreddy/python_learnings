# import os

# path = os.getcwd()

# print(path)

# path2 = os.chdir('/Users/jaidevreddy/Documents/Documents - Jaidev’s MacBook Pro/sem 7/GCP/file_encryption') #this path is from different directory

# file = open('tesst.txt','r')

# print(file.read())

# # path3 = os.makedirs('/Users/jaidevreddy/Documents/Documents - Jaidev’s MacBook Pro/python/test_dir')
# path3_alt = ('/Users/jaidevreddy/Documents/Documents - Jaidev’s MacBook Pro/python/test_dir')

# # element = os.path.basename(path3_alt)
# # element = os.path.dirname(path3_alt)

# element = os.path.split(path3_alt)

# print(element)

# os.rmdir('/Users/jaidevreddy/Documents/Documents - Jaidev’s MacBook Pro/python/test_dir')

from pathlib import Path

folder = Path('/Users/jaidevreddy/Documents/Documents - Jaidev’s MacBook Pro/python') / 'test.txt'

my_file = open(folder,'r')

print(my_file.read())









