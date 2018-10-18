import re
import os


addr_list = os.listdir("old/")
file_list = []

def read_file_list(lis):
    a = []
    for i in lis:
        tmp = open("old/" + i,'r')
        tmp1 = tmp.read()
        tmp.close()
        a.append(tmp1)
    return a

file_list = read_file_list(addr_list)

pattern1 = re.compile("<openssl/\w+.h>")
pattern2 = re.compile("\"internal/\w+.h\"")
#print(file_list[0])
print(addr_list)
for j in range(len(addr_list)):
    matcher1 = re.findall(pattern1,file_list[j])#同样是查询
    matcher2 = re.findall(pattern2,file_list[j])
    replacer1 = []
    replacer2 = []

    for i in matcher1:
        i = str(i)
        i = i.replace("openssl","include")
        i = i.strip("<")
        i = i.strip(">")
        i = "\"../" + i + "\""
        replacer1.append(i)


    for i in matcher2:
        i = str(i)
        i = i.replace("internal","include")
        i = i.strip("\"")
        i = "\"../" + i + "\""
        replacer2.append(i)

    for i in range(len(matcher1)):
        file_list[j] = file_list[j].replace(matcher1[i], replacer1[i])

    for i in range(len(matcher2)):
        file_list[j] = file_list[j].replace(matcher2[i], replacer2[i])


    f = open("new/" + addr_list[j],"w")
    f.write(file_list[j])
    f.close()
#print(file_list[0])