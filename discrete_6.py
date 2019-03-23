from itertools import combinations # 인터넷에 검색

def ALL(X):
    X = X[:-1]
    count = range(1,len(X)+1)
    lists = []
    for i in count:
        print(i)
        lists.append(list(combinations(X,i))) # combination 함수 사용 X = [1,2,3,4] i = 2 일 경우 (1,2),(1,3),(1,4),(2,3),(2,4),(3,4)

    lists = sum(lists, []) # 이중 리스트를 벗겨줌 [[a],[b]] -> [a,b]
#    print(lists)
    lists = [list(i)+[0] for (i) in lists] # list(i) -> i를 리스트로 만들어준다 그리고 뒤에 0을 붙임
    print(lists)
            
if __name__ == "__main__":
    X = [1,2,3,4,0]
    ALL(X)