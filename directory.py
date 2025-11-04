import os

path = os.getcwd()

print(path)

path2 = os.chdir('/Users/jaidevreddy/Documents/Documents - Jaidev’s MacBook Pro/sem 7/GCP/file_encryption') #this path is from different directory

file = open('tesst.txt','r')

print(file.read())

path3 = os.makedirs('/Users/jaidevreddy/Documents/Documents - Jaidev’s MacBook Pro/python/test_dir')

