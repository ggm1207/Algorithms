nums = [str(i) for i in range(11)]

def solution(dartResult):
    dart = []
    left = 0
    right = 0
    length = len(dartResult)
    for i in range(1,length): 
        if dartResult[i] in nums:
            right = i
            if right - left < 2:
                continue
            dart.append(dartResult[left:right])
            left = right
    dart.append(dartResult[left:])
    print(dart)
    length = len(dart)
    for i in range(length):
        dartpos = list(dart[i])
        if dartpos[0] == '1' and dartpos[1] == '0':
            dartpos = ['10'] + dartpos[2:]
        score, section, options = int(dartpos[0]), dartpos[1], 0
        if len(dartpos) == 3:
            options = dartpos[2]
        if section == 'S':
            dart[i] = score
        elif section == 'D':
            dart[i] = pow(score,2)
        else:
            dart[i] = pow(score,3)
        if options:
            if options == '*':
                if i > 0:
                    dart[i-1] *= 2
                dart[i] *= 2
            else:
                dart[i] *= -1
    answer = sum(dart)

    return answer