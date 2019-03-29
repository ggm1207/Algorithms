import sys, math

class tf_idf:
    def __init__(self, datas):
        self.tf = 0
        self.idf = 0
        self.datalist = datas
    
    def addTf(self):
        self.tf = tf + 1
        
    def setIdf(self,idf):
        self.idf = idf

    def getTf_idf(self):
        return self.tf*self.idf

    def toSting(self):
        token_list, t = self.getTokenlist()
        max_doc = len(token_list)
        for i, token in enumerate(token_list):
            print('-'*10, i , 'document','-'*10)
            for (key, value) in token.items():
                tf = value
                idf = math.log10(max_doc/t[key])
                tf_idf = tf * idf
                msg = "{:10}: tf = {:2} | idf = {:.2} | tf-idf = {:.2}" .format(key ,tf, idf, tf_idf)
                print(msg)

    def getTokenlist(self):
        token_list = []
        totaltokin_list = {}
        for data in self.datalist:
            token = {}
            datas = data.split()
            for item in datas:
                item = item.lower()
                if item in token:
                    token[item] += 1
                elif item in totaltokin_list:
                    totaltokin_list[item] += 1
                else:
                    token[item] = 1
                    totaltokin_list[item] = 1
            token_list.append(token)
        return token_list, totaltokin_list

if __name__ == "__main__":
    str1 = "I love dogs"
    str2 = "I hate dogs and knitting"
    str3 = "Knitting is my hobby and my passion"
    datalist = [str1,str2,str3]
    
    test = tf_idf(datalist)
    token, token_list = test.getTokenlist()
    print(token, token_list, sep = '\n')
    test.toSting()
