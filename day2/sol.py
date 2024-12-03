D = open('in.in').read().strip()

lines = D.split("\n")

ans = 0

#helper function

def isSafe(level):
	inc_or_dec = (level==sorted(level) or level==sorted(level, reverse=True))
	ok = True
	for i in range(len(level) - 1):
		diff = abs(level[i] - level[i+1])
		if not 1 <= diff <= 3:
			ok = False
	if inc_or_dec and ok:
			return True

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


#part two
ans = 0
for line in lines:
	xs = list(map(int, line.split()))
	for i in range(len(xs)):
		n = xs.pop(i)
		if isSafe(xs):
			ans += 1
			break
		xs.insert(i, n)



