nums = [int(num) for num in list(input())]
nums.sort(key=lambda x: x % 3)
print(nums)


dragons = ['Rudy', 'Targent', 'Aggie']
dragons.sort()
dragons = sorted(dragons, key=len)
dragons.reverse()
dragons