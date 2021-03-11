import re

ss = ''

for _ in range(int(input())):
    ss += input() + '\n'

for _ in range(int(input())):
    wrd = input()
    print(len(re.findall(rf'\b{wrd}\b', ss)))
