a, b, x = map(int, input().split())
res = 0

if a*10**9 + b*10 <= x: res = 10**9

left, right = 1, 10**9-1
while left<=right:
		mid = (left+right)//2
		p = a*mid + b*len(str(mid))
		
		if p<=x and mid > res:
			res = mid
			left += 2
		else: right = mid - 1
		
print(res)