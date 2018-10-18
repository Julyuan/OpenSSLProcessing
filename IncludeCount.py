import os
import re

addr_list = os.listdir("new/")
file_list = []

def read_file_list(lis):
    a = []
    for i in lis:
        tmp = open("new/" + i,'r')
        tmp1 = tmp.read()
        tmp.close()
        a.append(tmp1)
    return a

file_list = read_file_list(addr_list)

include_set = set()

pattern1 = re.compile("../include/\w+.h")

for i in file_list:
    matcher1 = re.findall(pattern1,i)
    for j in matcher1:
        temp = j.split("/")
        include_set.add(temp[2])


count = 0
include_set = sorted(include_set)
for i in include_set:
    print(i,end = " ")
    count+=1
    if count==5:
        count = 0
        print()

