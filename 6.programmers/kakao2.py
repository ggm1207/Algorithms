
def solution(s):
    answer = []
    s_split = s[2:-2].split('},{')
    s_split_row = list(map(lambda x : set(map(int,x.split(','))), s_split))
    s_split_row.append({})
    s_split_sorted = sorted(s_split_row, key = lambda x: len(x))
    
    for i in range(len(s_split_sorted) - 1):
        answer.append(s_split_sorted[i+1].difference(s_split_sorted[i]).pop())
    return answer

if __name__ == "__main__":
    s = "{{2},{2,1,3},{2,1},{2,1,3,4}}"
    s_split = s[2:-2].split('},{')
    s_split_row = list(map(lambda x : set(map(int,x.split(','))), s_split))
    s_split_row.append({})
    s_split_sorted = sorted(s_split_row, key = lambda x: len(x))
    
    answer = []
    for i in range(len(s_split_sorted) - 1):
        answer.append(s_split_sorted[i+1].difference(s_split_sorted[i]).pop())


    print(s_split)
    print(s_split_row)
    print(s_split_sorted)
    print(answer)
    
    pass