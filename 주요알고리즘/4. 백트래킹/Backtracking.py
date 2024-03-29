'''
# 백트래킹: 완전 탐색을 재귀적으로 수행할 때, 가지치기를 활용하여 시간복잡도를 줄이는 것을 백트래킹(back tracking)이라고 한다.

# 백트래킹의 구현 방법

1. 재귀인지 확인한다 => 트리가 만들어진다!
2. 상태전이, 종료조건, 재귀조건을 구현한다.

def rec(상태, 초기값):
    로직
    if 종료조건:
    if 재귀호출: # 가지치기

'''

# 순열
import itertools

arr = ['A', 'B', 'C']
result = itertools.permutations(arr, 2) # 반복 가능한 객체, r = 뽑는 개수
print(list(result))
# [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]

# 중복 순열
from itertools import product

arr = ['A', 'B', 'C']
result = product(arr, arr, [1, 2]) # 반복 가능한 객체, 반복 가능한 객체, ..
print(list(result))
# [('A', 'A', 1), ('A', 'A', 2), ('A', 'B', 1), ('A', 'B', 2), ('A', 'C', 1), ('A', 'C', 2), ('B', 'A', 1), ('B', 'A', 2), ('B', 'B', 1), ('B', 'B', 2), ('B', 'C', 1), ('B', 'C', 2), ('C', 'A', 1), ('C', 'A', 2), ('C', 'B', 1), ('C', 'B', 2), ('C', 'C', 1), ('C', 'C', 2)]

from itertools import product

result = product([1,2,3], repeat=2) # 반복 가능한 객체, repeat=n (n번 반복)
print(list(result))
# [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]

# 조합
import itertools

arr = ['A', 'B', 'C']
result = itertools.combinations(arr, 2) # 반복 가능한 객체, r = 뽑는 개수
print(list(result))
# [('A', 'B'), ('A', 'C'), ('B', 'C')]

# 중복 조합
from itertools import combinations_with_replacement

arr = ['A', 'B', 'C', 'D']
result = combinations_with_replacement(arr, 2) # 반복 가능한 객체, r = 뽑는 개수
print(list(result))
# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'B'), ('B', 'C'), ('B', 'D'), ('C', 'C'), ('C', 'D'), ('D', 'D')]