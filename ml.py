n = int(input())
x = 0
for _ in range(n):
    s = input()
    if "++" in s:
        x +=1
    else:
        x -=1
print(x)


n = int(input())
while n != 0:
    digit = n % 10
    d = 9 - digit
    break
result = n + d
print(result)
