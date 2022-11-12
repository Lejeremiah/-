import string
import base64
dic = string.ascii_uppercase+string.ascii_lowercase+string.digits+'+/'


class Base:
    def __init__(self):
        self.dic = string.ascii_uppercase+string.ascii_lowercase+string.digits+'+/'
    def b64encode(self,m):
        self.m = m.decode()
        length = len(self.m)
        group_len = length // 3
        res = ""
        if length%3 == 0:
            res = self.get_case(self.m,length,group_len)
        elif length%3 == 1:
            res = self.get_case(self.m+'\00\00',length,group_len+1)[:-2]+'=='
        elif length%3 == 2:
            res = self.get_case(self.m+'\00',length,group_len+1)[:-1]+'='
        return res.encode()

    def get_case(self,m,length,group_len):
        res = ""
        for i in range(group_len):
            res += self.three2four(m[i*3:(i+1)*3])
        return res
    def three2four(self,t):
        res = ''
        for i in range(3):
            temp = t[i]
            temp = ord(temp)
            temp = int(temp)
            temp = '0' + bin(temp)[2:]
            # print(temp)
            res += temp
        res = res
        tar = ''
        for i in range(4):
            temp = res[i * 6:(i + 1) * 6]
            temp = int('0b00' + temp, 2)
            temp = dic[temp]
            tar += temp
            # print(tar)
        return  tar
m = '!&*'
base = Base()
a = base.b64encode(m.encode()).decode()
b = base64.b64encode(m.encode()).decode()
print(a)
print(b)
