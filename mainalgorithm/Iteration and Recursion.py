# 반복과 재귀: loop가 필요한 알고리즘을 설계할 때, 반복문(iteration)과 재귀(recursion) 중 하나를 선택할 수 있다.

# 반복문의 기본 동작 과정
'''
1. 초깃값이 존재해야 한다.
2. 종료 조건(= 반복 조건)을 설정하여 반복하는데, for은 횟수 조건(range), while은 상황 조건(if-break)이다.
'''

''' 팩토리얼 반복 구현

result = 1
for i in range(1, n + 1):
  result *= i

print(result)
'''


# 재귀 함수의 기본 동작 과정
'''
1. 재귀 함수를 정의한다. (매개변수 설정. 없을 수도 있음)
2. 종료 조건(= 재귀 조건)을 설정하여 반복하는데, 조건을 만족할 때 재귀 호출되거나, 함수 종료가 되어야 하고 만족하지 못할 때는 그 반대의 동작이 일어나야 한다.

+ 재귀 호출은 스택에서 push로 해석할 수 있고, 종료 호출은 스택에서 pop으로 해석할 수 있다.
따라서 스택 자료구조를 활용해야 하는 상당수의 알고리즘은 재귀 함수를 이용해서 간편하게 구현될 수 있다. ex) DFS
'''

''' 팩토리얼 재귀 구현

def factorial_recursive(n):
  if n <= 1:
    return 1
  return n * factorial_recursive(n - 1)
'''


''' 완전 탐색의 재귀적 구현 recursive bruteforce

arr = []

def rec(depth): # 깊이를 매개변수로 받기
  if depth == 3: # 종료 조건
    for i in range(3):
      print(arr[i], end = ' ')
    print()
    return
  
  for i in range(6): # 완전 탐색
    arr[depth] = i
    rec(depth + 1) # 재귀 호출

rec(0)

'''
