n = int(input())
lst = [input().split() for i in range(n)]
result = [lst[i][0] for i in range(len(lst)) if 'win' in str(lst[i])]

# for i in range(len(lst)):
#     if 'win' in str(lst[i]):
#         result.append(lst[i][0])

print(result)
print(len(result))
