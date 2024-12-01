from collections import defaultdict

D = open('in.in').read().strip()

lines = D.split("\n")

#----------#
# part one
#----------#


left = []
right = []

numbers = defaultdict(int)

for line in lines:
	l, r = line.split()
	l, r = int(l), int(r)
	left.append(l)
	right.append(r)

left.sort()
right.sort()

distances = []
for i in range(len(left)):
	distances.append(abs(right[i] - left[i]))

print(sum(distances))
	
#----------#
# part two
#----------#

repeating = []

for left_n in left:
	for right_n in right:
		if right_n == left_n:
			numbers[right_n] += 1

for v, k in zip(numbers.values(), numbers.keys()):
	repeating.append(k * v)
	
print(sum(repeating))



