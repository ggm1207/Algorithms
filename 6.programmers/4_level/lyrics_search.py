""" 가사 검색
입출력 예
words	                                                queries                                         result
["frodo", "front", "frost", "frozen", "frame", "kakao"]	["fro??", "????o", "fr???", "fro???", "pro?"]	[3, 2, 4, 1, 0]
"""
import sys
from collections import defaultdict

# 트라이 자료구조 -> 내가 생각했던...
class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.data_num = 0
        self.children = {}

class Trie(object):
    def __init__(self):
        self.head = Node(None)
        self.counts = [0]

    def insert(self, string):
        curr_node = self.head
        
        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            curr_node.data_num += 1
            curr_node = curr_node.children[char]
        curr_node.data = True

    def search(self, string):
        curr_node = self.head
        self.counts = [0]
        for char in string:
            if char == '?':
                return curr_node.data_num

            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return 0

        if curr_node.data:
            return 1
        return 0

def solution(words, queries):
    grouped_words_by_num_front = dict()
    grouped_words_by_num_back = dict()
    query_keyword = defaultdict(int)
    for word in words:
        grouped_words_by_num_front.setdefault(len(word), Trie()).insert(word)
        grouped_words_by_num_back.setdefault(len(word), Trie()).insert(word[::-1])

    query_counts = []
    for query in queries:
        if query_keyword[query] != 0:
            query_counts.append(query_keyword[query])
            continue

        if query[0] == '?':
            counts = grouped_words_by_num_back.setdefault(len(query), Trie()).search(query[::-1])
            query_counts.append(counts)
        else:
            counts = grouped_words_by_num_front.setdefault(len(query), Trie()).search(query)
            query_counts.append(counts)
            
        query_keyword[query] = counts
    
    return query_counts

# 1개 빼고 시간초과 나온 풀이..
def prev_solution(words, queries):
    grouped_words_by_num = defaultdict(list)
    query_keyword = defaultdict(int)
    for word in words:
        grouped_words_by_num[len(word)].append(word)

    query_counts = []
    for query in queries:
        if query_keyword[query] != 0:
            query_counts.append(query_keyword[query])
            continue

        search_list = grouped_words_by_num[len(query)]
        if not search_list:
            query_counts.append(0)
            query_keyword[query] = 0
            continue

        if query[0] == "?" and query[-1] == "?":
            query_counts.append(len(search_list))
            query_keyword[query] = len(search_list)
            continue

        count = 0

        flag = query[0] == '?'
        del_num = query.count('?')
        
        for word in search_list:
            if flag: # ?가 앞에
                if word[del_num:] == query[del_num:]:
                    count += 1
                    continue
            else:
                if word[:-del_num] == query[:-del_num]:
                    count += 1
                    continue

        query_keyword[query] = count
        query_counts.append(count)
        
    return query_counts

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?", "fros?", "?rost", "?????", "??????"]
# queries = ["fr???"]
print(solution(words, queries))
print(prev_solution(words, queries))