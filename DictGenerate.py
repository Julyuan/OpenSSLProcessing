import pandas as pd

def ReadTableFromAddr(addr):
    df = pd.read_csv(addr)
    print(df.values)
    return df.values


def DictGenerator(table):
    res_dict = {}
    for i in table:
        term = str(i[0]).split()
        if len(term) == 3:
            res_dict[term[0]] = (term[1],term[2])
        else:
            res_dict[term[0]] = (term[1])
    return res_dict


addr = "./resultTable"

a = ReadTableFromAddr(addr)
b = DictGenerator(a)
print(b)
