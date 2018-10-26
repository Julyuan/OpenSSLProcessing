import os
import shutil



class OsSimulator(object):
    current_path = './'
    def __init__(self):
        self.current_path = os.getcwd()

    def ls(self):
        return os.listdir(self.current_path)

    def ls(self, path):
        return os.listdir(path)

    def cp(self,file_path, des_path):
        shutil.copyfile(file_path,des_path)

    def cd(self,path):
        if path == '..':
            temp = str(self.current_path).split("/")
            self.current_path = '/'.join(temp[0:len(temp) - 1])
        elif path[0]=='/':
            self.current_path = path
        else:
            self.current_path = self.current_path + '/' + path

    def search(self,path,file_name):
        if path[0] == '.':
            path = os.getcwd() + path[1:]
        if file_name in os.listdir(path):
            return (path,True)
        else:
            for subdir in self.ls(path):
                if os.path.isdir(subdir):
                    res = self.search(path+'/'+subdir,file_name)
                    if res[1] == True:
                        return res
        return ('',False)

class FileMover(object):
    minios = OsSimulator()

    def move_files(self, name_set, entry_addr, des_addr):
        pass
        for name in name_set:
            addr = self.minios.search(entry_addr, name)
            if addr[1] == True:
                self.minios.cp(addr[0], des_addr)
            else:
                print('没有找到文件')

def ConsoleSimulator():
    minios = OsSimulator()
    while True:
        input_str = str(input())
        if input_str == "exit":
            break
        elif 'cd' == input_str.split()[0]:
            minios.cd(input_str.split()[1])



example = OsSimulator()
example.cd('..')
a = example.search('.','FileForTest')
print('a = ',a)
print(example.current_path)
