table =  { ')': '(', ']':'[', '}':'{' }

for _ in range(int(input())):
    stack = []
    for x in input():
        if stack and table.get(x) == stack[-1]:
            stack.pop()
        else:
            stack.append(x)
    print("NO" if stack else "YES")
