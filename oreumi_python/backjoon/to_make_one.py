n = 2

dp = [0]*(n+1)

print(dp)
count = 0

dp[0] = n

for i in range(1,len(dp)-1) :
    if dp[i] % 3 == 0:
        count += 1
        pass
    elif dp % 2 == 0:
        pass
    else:
        pass

