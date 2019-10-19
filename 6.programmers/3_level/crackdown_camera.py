"""단속카메라 (https://programmers.co.kr/learn/courses/30/lessons/42884)
routes	                                    return
[[-20,15], [-14,-5], [-18,-13], [-5,-3]]	2
"""
from collections import defaultdict

def solution(routes):
    cam_pos = 40000
    cam_cnt = 0
    # print(sorted(routes))
    for idx, (left, right) in enumerate(sorted(routes)):
        cam_pos = min(right, cam_pos)
        if left > cam_pos:
            # print(left, cam_pos)
            cam_cnt += 1
            prev_cam_pos = cam_pos
            cam_pos = right

        if idx == len(routes) - 1:
            # print(prev_cam_pos, left)
            if prev_cam_pos < left:
                cam_cnt += 1

    return cam_cnt



def prev_solution(routes):
    left_dicts = dict()
    is_left = defaultdict(bool)
    for k, v in routes:
        left_dicts[k] = v
        is_left[k] = True
    
    right_rest = len(routes)
    # right_list = []
    min_right = 40000
    cam_cnt = 0
    for cam_pos in range(-30000, 30001):
        if cam_pos > min_right:
            # print('m:  ',min_right)
            # right_list = []
            min_right = 40000
            cam_cnt += 1
            if right_rest == 0:
                break

        if is_left[cam_pos]: # left 값이 존재하면
            min_right = min(min_right, left_dicts[cam_pos])
            # right_list.append(left_dicts[cam_pos])
            # print(right_list)
            # min_right = min(right_list)
            right_rest -= 1
            
    return cam_cnt


print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]))
print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3], [-3, -1]]))
print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3], [-3, -1], [-1, 3]]))