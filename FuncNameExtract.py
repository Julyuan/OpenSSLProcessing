import os,re

funcstr = """123123
int func1(int a, 
    int c);"""
def FindFunc(addr):
    file = open(addr)
    filestr = file.read()
    #             函数返回值类型 函数名 函数参数列表
    #pattern1str = "^(\w+)\s\w+(\((\w|,|\s)+\));$"
    #pattern1str = "^(.+?);$"
    pattern1str = "^([0-9A-Za-z_]+)(\s*)(\w+)\(.+?\);$"


    pattern1 = re.compile(pattern1str,flags = re.DOTALL |re.MULTILINE)
    #print(funcstr)
    #res1 = re.search(pattern1,funcstr)
    res_list = []
    while True:
        res1 = re.search(pattern1, filestr)
        if res1 == None:
            break
        else:
            res_list.append(res1.group(0))
            filestr = filestr[res1.span()[1]:]
    return res_list
    #print(res1.span()[1])
    #print(filestr[1788:])



#jly = FindFunc("./bn.h")
#for i in jly:
#    print(i)
#    print()


def FindSpan(func_name, file_str):

    print("func_name =",func_name)
    print("file_str =",file_str)
    pattern1 = re.compile(func_name)
    res1 = re.search(pattern1, file_str)

    if res1 != None:
        start_pos = res1.span()[1]
        end_pos = start_pos
        brace_count = 1
        while True:
            if file_str[end_pos]=='{':
                end_pos+=1
                break
            start_pos+=1

        while True:
            if file_str[end_pos]=="{":
                brace_count+=1
            elif file_str[end_pos]=="}":
                brace_count-=1

            if brace_count==0:
                break

        return (start_pos, end_pos)
    else:
        return (-1,-1)


str1 = """int fun(int a, int b);"""
str2 = """int fun(int a, int b){
            int c = a+b;
            return c;
            }"""

a = FindSpan(str1[:len(str1)-1],str2)

print(a)