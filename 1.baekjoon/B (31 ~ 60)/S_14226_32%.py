import sys
import collections

q = collections.deque()

def fake():
    emoticon = 1
    clipboard = 0
    cnt = 0
    q.append(('copy',cnt+1,emoticon, clipboard))
    # copy -> 그래도
    # paste -> 짝수일때만 가능 // 2
    # delete -> + 1
    dicts = {'copy' : 0 , 'paste' : 1 , 'delete': 2}
    
    visited = [[0 for i in range(1002)] for _ in range(1002)]
    # num clipboard
    while(1):
        act , cnt, emoticon, clipboard = q.popleft()
        # print(act, emoticon , 'depth:',cnt)
        
        if emoticon < 1:
            continue

        if emoticon < 1002 and clipboard < 1002:
            if visited[emoticon][clipboard] == 1:  
                continue
        else:
            continue

        if emoticon == S:
            break

        visited[emoticon][clipboard] = 1

        if act == 'copy':
            clipboard = emoticon
            q.append(('paste',cnt+1,clipboard + emoticon, clipboard))
            q.append(('delete',cnt+1,emoticon-1, clipboard))
        elif act == 'paste':
            q.append(('paste',cnt+1,clipboard+emoticon, clipboard))
            q.append(('copy',cnt+1,emoticon, emoticon))
            q.append(('delete',cnt+1,emoticon-1, clipboard))
        else:
            q.append(('paste',cnt+1,clipboard+emoticon, clipboard))
            q.append(('copy',cnt+1,emoticon, emoticon))
            q.append(('delete',cnt+1,emoticon-1, clipboard))
    print(cnt)
        
if __name__ == "__main__":
    S = int(input())
    fake()