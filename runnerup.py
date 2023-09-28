'''
Print the runner-up score.
Input:
5
2 3 6 6 5
'''

n = int(input())
arr = map(int, input().split())
lst = list(set(arr))
lst.sort(reverse = True)
print(lst[1])
