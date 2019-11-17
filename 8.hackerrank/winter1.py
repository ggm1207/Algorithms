from sys import stdin, stdout
from collections import defaultdict
import math

if __name__ == "__main__":

    user_item_rating = defaultdict(float)
    total_itemlist = set()
    total_userlist = set()
    user_itemlist = defaultdict(set)

    #### input start
    num_sim_user_topk = int(stdin.readline().rstrip('\n'))
    num_item_rec_topk = int(stdin.readline().rstrip('\n'))
    num_users = int(stdin.readline().rstrip('\n'))
    num_items = int(stdin.readline().rstrip('\n'))
    num_rows = int(stdin.readline().rstrip('\n'))
    for _ in range(num_rows):
        user_id, item_id, rating = stdin.readline().rstrip('\n').split()
        user_id, item_id, rating = int(user_id), int(item_id), float(rating)
        user_item_rating[(user_id, item_id)] = rating
        total_itemlist.add(item_id)
        total_userlist.add(user_id)
        user_itemlist[user_id].add(item_id)
    num_reco_users = int(stdin.readline().rstrip('\n'))
    reco_users = [int(stdin.readline().rstrip('\n')) for _ in range(num_reco_users)]
    #### input end

    # print(num_sim_user_topk)    # rating 예측 시 사용할 유사 유저수
    # print(num_item_rec_topk)    # 각 유저별로 추천해줘야 하는 아이템 개수
    # print(num_users)            # 데이터에 있는 유저 수
    # print(num_items)            # 데이터에 있는 아이템 수
    # print(total_itemlist)       # 총 아이템 리스트
    # print(num_rows)             # 
    # print(user_item_rating)     # 유저, 아이템, 레이팅 dict
    # print(num_reco_users)       # 
    # print(reco_users)           # 추천결과를 만들어야 할 유저 ID

    avg_dict = defaultdict(float)
    def avg(x): # check
        if avg_dict[x]:
            return avg_dict[x]
        avg = 0
        for item in user_itemlist[x]:
            avg += user_item_rating[(x,item)]
        avg_dict[x] =  avg / len(user_itemlist[x])
        return avg_dict[x]
            
    simil_dict = defaultdict(float)
    def simil(x, y): # check
        if simil_dict[x,y]:
            return simil_dict[x,y]
        ist_itemlist = user_itemlist[x].intersection(user_itemlist[y])
        rx_, ry_ = avg(x), avg(y)
        l_d = math.sqrt(sum(map(lambda item: pow(user_item_rating[(x,item)] - rx_, 2), ist_itemlist)))
        r_d = math.sqrt(sum(map(lambda item: pow(user_item_rating[(y,item)] - ry_, 2), ist_itemlist)))
        up = sum(map(lambda item: (user_item_rating[(x,item)] - rx_)*(user_item_rating[(y,item)] - ry_), ist_itemlist))
        if (l_d * r_d) == 0 or len(ist_itemlist) == 0:
            return 0
        simil_dict[x,y] = up / (l_d * r_d)
        simil_dict[y,x] = simil_dict[x,y]
        return simil_dict[x,y]

    # print('total_user:', total_userlist)
    def get_setU(reco_user):
        reco_user_simillist = [(user, simil(reco_user, user)) for user in total_userlist if user != reco_user]
        return sorted(reco_user_simillist, key = lambda x: x[1], reverse=True)[:num_sim_user_topk]

    def get_delU(U_, reco_user, item):
        reco_user_simillist = []
        for sim_user, _ in U_:
            if (sim_user, item) not in user_item_rating:
                continue
            reco_user_simillist.append(sim_user)
        return reco_user_simillist

    ### solve
    for reco_user in reco_users:
        reco_ratinglist = []
        reco_items = list(total_itemlist.difference(user_itemlist[reco_user]))
        U_ = get_setU(reco_user)
        
        for reco_item in reco_items:
            D_ = get_delU(U_, reco_user, reco_item) 
            # print('reco_item:', reco_item)
            # print('D_', D_)
            r_ = avg(reco_user)
            sim = sum([abs(simil(reco_user, sim_user)) for sim_user in D_])
            k = (1 / sim) if sim else 0
            last = sum([simil(reco_user, sim_user)*(user_item_rating[(sim_user, reco_item)]  - avg(sim_user)) for sim_user in D_])
            # print(k, last)
            rui = r_ +  k * last
            reco_ratinglist.append(rui)

        _, reco_items =  zip(*sorted(zip(reco_ratinglist, reco_items), reverse=True))
        stdout.writelines(" ".join(map(str,reco_items[:num_item_rec_topk]))+'\n')
        