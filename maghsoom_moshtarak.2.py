n = int(input("enter your first number please :"))
def maghsoom(n):
    result = []
    for i in range(1,n+1):
        if n % i == 0 :
            result.append(i)
    result=set(result)
    return result 

m = int(input("enter your second number please :"))
def maghsoom2(m):
    result2 = []
    for p in range(1,m+1):
        if m % p == 0 :
            result2.append(p)
    result2=set(result2)            
    return result2
print(maghsoom(n))
print(maghsoom2(m))
print(set.intersection(maghsoom(n), maghsoom2(m)))
