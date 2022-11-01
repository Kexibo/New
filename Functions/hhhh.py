def foo(x):
    all = x
    revers=0
    while x>0:
        d=x%10
        revers*=10
        revers+=d
        x=x//10
    return revers==all
x=int(input())
print(foo(x))