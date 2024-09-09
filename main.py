#Find sum of no 4 ==== 1+2+3+4=10

def fun1(n):
    return n*(n+1)/2

print(fun1(4))

def fun2(n):
    sum=0
    for i in range(1,n+1):
        sum+=i

    return sum
print(fun2(4)) 


        

