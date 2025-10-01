print('a b c F')
for a in range(2):
    for b in range(2):
        for c in range(2):
            f = (not ((not a) or b)) or (not ((not b) or c)) or (not a) or c
            print(a, b, c, int(f))

