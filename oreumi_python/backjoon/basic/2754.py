# https://www.acmicpc.net/problem/2754

credit = input()
ans = 0

if credit[0] == 'A' :
    ans += 4
elif credit[0] == 'B' :
    ans += 3
elif credit[0] == 'C' :
    ans += 2
else :
    ans += 1
    
try :
    if credit[1] == '+' :
        ans += 0.3
    elif credit[1] == '0' :
        ans += 0.0
    else :
        ans -= 0.3
except :
    ans = 0.0


print(ans)
