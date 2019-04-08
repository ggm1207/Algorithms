import sys, math
import os
import numpy as np
import pandas as pd
import re
from time import sleep

class tf_idf:
    def __init__(self, datas):
        self.datalist = datas

    def toSting(self):
        self.token_list, self.totaltokin_list = self.getTokenlist()
        print('token_list: ', self.token_list)
        print('t: ', self.totaltokin_list)
        nparr = np.zeros((len(self.token_list),len(self.totaltokin_list)))
        
        max_doc = len(self.token_list)
        fk = list(self.totaltokin_list.keys())
        for i, token in enumerate(self.token_list):
            print('-'*10, i , 'document','-'*10)
            for (key, value) in token.items():
                tf = value
                idf = math.log10(max_doc/self.totaltokin_list[key])
                tf_idf = tf * idf
                msg = "{:10}: tf = {:2} | idf = {:.2} | tf-idf = {:.2}" .format(key ,tf, idf, tf_idf)
                nparr[i][fk.index(key)] = round(tf_idf,2)
                print(msg)
        pdarr = pd.DataFrame(nparr, columns = fk)
        print(pdarr)
    
    def getTokenlist(self):
        token_list = []
        totaltokin_list = {}
        for data in self.datalist:
            token = {}
            # datas = data.split()
            for item in data:
                #item = item.lower()
                if item in totaltokin_list and item in token: # 똑같은 문서에서 똑같은 단어가 나온 경우
                    token[item] += 1

                elif item in totaltokin_list and item not in token:
                    totaltokin_list[item] += 1
                    token[item] = 1
                else:
                    token[item] = 1
                    totaltokin_list[item] = 1
            token_list.append(token)
        return token_list, totaltokin_list

def get_datas():
    datapath = './Data/'
    datas = os.listdir(datapath)
    obama = [datas[0]]
    urbine = datas[1:]
    
    datalist = []
    for filename in obama:
        f = open(datapath + filename,'r',encoding='UTF-8')
        p = re.compile('[a-zA-Z\']+')
        for line in f:
            word = list(map(lambda x : x.lower() ,p.findall(line)))
            if word:
                datalist += word
    num = len(datalist)//5
    return [datalist[i*num:(i+1)*num] for i in range(5)]


if __name__ == "__main__":
    str1 = "I love dogs"
    str2 = "I hate dogs and knitting"
    str3 = "Knitting is my hobby and my passion"
    datalist = get_datas()

    test = tf_idf(datalist)
    token, token_list = test.getTokenlist()
    test.toSting()

    # obmas = get_datas()
    

