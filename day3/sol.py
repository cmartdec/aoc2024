data = open("in.in").read().strip()

import re

#xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))

pattern1 = r"mul\((\d+),(\d+)\)"
pattern2 = r"don't()"
pattern3 = r"do()"


matches = re.findall(pattern, data)

results = [int(a) * int(b) for a, b in matches]

total = sum(results)

print(total)






