D = open('in.in').read().strip()

lines = D.split("\n")

ans = 0

# part one

for line in lines:
	xs = list(map(int, line.split()))
	inc_or_dec = (xs==sorted(xs) or xs==sorted(xs, reverse=True))
	ok = True
	for i in range(len(xs) - 1):
		diff = abs(xs[i] - xs[i+1])
		if not 1 <= diff <= 3:
			ok = False
	if inc_or_dec and ok:
			ans += 1
print(ans)
			



