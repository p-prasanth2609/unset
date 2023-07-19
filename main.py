a=int(input())
b=int(input())
c=1<<b
if a&c:
    a=a^c
print(a)
