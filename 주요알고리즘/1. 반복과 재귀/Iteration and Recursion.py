'''
반복과 재귀: loop가 필요한 알고리즘을 설계할 때, 반복문(iteration)과 재귀(recursion) 중 하나를 선택할 수 있다.
더 구현이 간단한 것을 선택하면 된다.

반복문의 구현 방법
1. 초깃값을 정할 수 있어야 한다.
2. 반복 조건(= 종료 조건)을 설정하여 반복하는데, for은 횟수 조건(range), while은 상황 조건(if-break)이다.

팩토리얼 반복 구현
'''
n = 100
result = 1
for i in range(1, n + 1):
  result *= i

print(result)

'''
재귀 함수의 구현 방법

1. 트리가 만들어진다!(문제가 여러 개의 부분 문제로 쪼개지는지 확인한다) => 가능성 높음
2. 상태전이와 종료 조건, 재귀 조건을 구현한다.

def rec(상태, 초기값):
    if 종료조건:
    + 재귀조건:

팩토리얼 재귀 구현
'''
def factorial_recursive(n):
  if n <= 1:
    return 1
  return n * factorial_recursive(n - 1)


