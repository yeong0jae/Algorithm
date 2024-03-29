# 14888 연산자 끼워넣기

from itertools import permutations

n = int(input())
a = list(map(int, input().split()))
add, subtract, multiply, divide = map(int, input().split())

operators = ['+'] * add + ['-'] * subtract + ['*'] * multiply + ['/'] * divide

max_result = float('-inf')
min_result = float('inf')

# permutations(operators) 는 operators의 모든 순열을 구한다.
# 인자는 iterable 객체를 받는다. 리스트, 튜플, 문자열 가능
# 만약 인자가 (1, 1, 2, 3) 이라면 1, 1은 다른 것으로 취급되어 중복되는 순열을 반환함
# <itertools.permutations at 0x10872e390> 이런 식으로 iterator 객체를 반환한다

for perm in set(permutations(operators)): # set()으로 중복 제거
    # list일 경우 n=10이면 10!에다가 10을 곱해야 하므로 시간 초과

    result = a[0] # 계산 결과 초기화

    for i in range(1, n): # 순열마다 연산 수행
        if perm[i - 1] == '+':
            result += a[i]
        elif perm[i - 1] == '-':
            result -= a[i]
        elif perm[i - 1] == '*':
            result *= a[i]
        elif perm[i - 1] == '/' and a[i] != 0:
            result = int(result / a[i])

    max_result = max(max_result, result) # 최대 갱신
    min_result = min(min_result, result) # 최소 갱신

print(max_result)
print(min_result)


# 재귀함수를 이용한 풀이
n = int(input())
a = list(map(int, input().split()))
add, subtract, multiply, divide = map(int, input().split())

max_result = float('-inf')
min_result = float('inf')

def calculate(index, result, add, subtract, multiply, divide):
    global max_result, min_result # 전역변수로 선언하여 함수 호출 간에 값을 공유(유지)할 수 있음

    if index == n:
        max_result = max(max_result, result)
        min_result = min(min_result, result)
        return

    if add > 0:
        calculate(index + 1, result + a[index], add - 1, subtract, multiply, divide)
    if subtract > 0:
        calculate(index + 1, result - a[index], add, subtract - 1, multiply, divide)
    if multiply > 0:
        calculate(index + 1, result * a[index], add, subtract, multiply - 1, divide)
    if divide > 0 and a[index] != 0:
        calculate(index + 1, int(result / a[index]), add, subtract, multiply, divide - 1)


calculate(1, a[0], add, subtract, multiply, divide)
print(max_result)
print(min_result)
