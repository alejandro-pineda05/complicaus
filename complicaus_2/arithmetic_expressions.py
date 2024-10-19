# Source: HackerRank
# URL: https://www.hackerrank.com/contests/projecteuler/challenges/euler093/problem
# Solution by Pablo Reina Jimenez

from itertools import permutations
from fractions import Fraction


def apply_operation(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/' and b != 0:
        return a / b
    return None


def generate_all_expressions(nums):
    if len(nums) == 1:
        return {nums[0]}

    results = set()
    for i in range(1, len(nums)):
        left_results = generate_all_expressions(nums[:i])
        right_results = generate_all_expressions(nums[i:])

        for left in left_results:
            for right in right_results:
                for op in ['+', '-', '*', '/']:
                    result = apply_operation(left, right, op)
                    if result is not None and result > 0:
                        results.add(result)
    return results


def find_largest_n(digits):
    achievable_numbers = set()

    for perm in permutations(digits):
        nums = [Fraction(n) for n in perm]
        results = generate_all_expressions(nums)
        for res in results:
            if res.denominator == 1:
                achievable_numbers.add(res.numerator)

    n = 1
    while n in achievable_numbers:
        n += 1

    return n - 1


m = int(input())
S = list(map(int, input().split()))

result = find_largest_n(S)
print(result)
