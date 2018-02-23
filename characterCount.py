import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
counts = {}

for aChar in message:
    counts.setdefault(aChar, 0)
    counts[aChar] += 1

#print(counts)
pprint.pprint(counts)