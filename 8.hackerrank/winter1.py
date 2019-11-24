""" 간단한 추천 시스템 """

from sys import stdin, stdout
from collections import defaultdict
import math

if __name__ == "__main__":

    # helper
    user_item_rating = defaultdict(float) # (user, item) = rating
    total_itemlist = set()                # { total item index }
    total_userlist = set()                # { total user index }
    user_itemlist = defaultdict(set)      # { user index : { user item ... }, ... }

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

    avg_dict = defaultdict(float) # cache(maxsize=None)
    def avg(x): # check
        """ 유저가 평가한 아이템들의 평균값을 반환합니다.\n
        Args
            x : int, user index
        Returns
            avg_dict[x] : float, average rating of user x for all the items rated by x
        """
        if avg_dict[x]:
            return avg_dict[x]
        avg = 0
        for item in user_itemlist[x]:
            avg += user_item_rating[(x,item)]
        avg_dict[x] =  avg / len(user_itemlist[x])
        return avg_dict[x]
            
    simil_dict = defaultdict(float) # cache(maxsize=None)
    def simil(x, y): # check
        """ 유저 x와 y의 유사도를 계산합니다. (Pearson correlation)\n
        Args
            x : int, user index
            y : int, user index
        Returns
            simil_dict[x,y] : float, The Pearson correlation similarity of two users x, y 
        """
        if simil_dict[x,y]: # (x, y) in cache
            return simil_dict[x,y]
        ist_itemlist = user_itemlist[x].intersection(user_itemlist[y]) # intersecion of item list
        rx_, ry_ = avg(x), avg(y)
        l_d = math.sqrt(sum(map(lambda item: pow(user_item_rating[(x,item)] - rx_, 2), ist_itemlist))) # left down
        r_d = math.sqrt(sum(map(lambda item: pow(user_item_rating[(y,item)] - ry_, 2), ist_itemlist))) # right down
        up = sum(map(lambda item: (user_item_rating[(x,item)] - rx_)*(user_item_rating[(y,item)] - ry_), ist_itemlist)) # up
        if (l_d * r_d) == 0 or len(ist_itemlist) == 0: # Pearson correlation이 정의되지 않는 경우 #* (분모가 0이거나 겹치는 아이템이 없을 경우)
            return 0
        simil_dict[x,y] = up / (l_d * r_d) # cache(x,y)
        simil_dict[y,x] = simil_dict[x,y] # cache(y,x)
        return simil_dict[x,y]

    def get_setU(reco_user):
        """ reco_user와 취향이 가장 유사한 num_sim_user_topk 명을 리턴합니다.\n
        Args:
            reco_user : int, user index
        Returns:
            U_ : (user, simil(reco_user, user))들을 원소로 가지며 num_sim_user_topk명 까지 유사도가 높은 순으로 정렬된 리스트입니다
        """
        reco_user_simillist = [(user, simil(reco_user, user)) for user in total_userlist if user != reco_user]
        return sorted(reco_user_simillist, key = lambda x: x[1], reverse=True)[:num_sim_user_topk] # U_

    def get_delU(U_, reco_user, item):
        """ U_ 에서 item i에 대해 rating 한 유저 리스트를 반환합니다.\n
        Args:
            U_ : user set from get_setU()
            reco_user : int, user index
            item : int, item index
        Returns:
            D_ : U_에 있는 유저들 중에서 item i 에 대해 rating 한 유저 리스트입니다.
        """
        reco_user_simillist = []
        for sim_user, _ in U_:
            if (sim_user, item) not in user_item_rating:
                continue
            reco_user_simillist.append(sim_user)
        return reco_user_simillist

    ### solve
    for reco_user in reco_users:
        reco_ratinglist = [] # 
        reco_items = list(total_itemlist.difference(user_itemlist[reco_user])) # reco_user가 추천 받을 수 있는 아이템들
        U_ = get_setU(reco_user)
        
        for reco_item in reco_items:
            D_ = get_delU(U_, reco_user, reco_item)
            r_ = avg(reco_user) # 밖으로 빼내는게 좋습니다..
            sim = sum([abs(simil(reco_user, sim_user)) for sim_user in D_])
            k = (1 / sim) if sim else 0 # k 값이 정의 되지 않는 경우 #* sim 값이 0일 때
            last = sum([simil(reco_user, sim_user)*(user_item_rating[(sim_user, reco_item)]  - avg(sim_user)) for sim_user in D_])
            rui = r_ +  k * last # reco_user의 reco_item 에 대한 예상 rating
            reco_ratinglist.append(rui)

        _, reco_items =  zip(*sorted(zip(reco_ratinglist, reco_items), reverse=True)) # 예상 rating이 높은 순으로 정렬
        stdout.writelines(" ".join(map(str,reco_items[:num_item_rec_topk]))+'\n') # num_item_rec_topk개 만큼의 item 출력
        