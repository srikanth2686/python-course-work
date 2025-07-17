fact=0
n=int(input("enter the num:"))
for i in range(2,(n//2)+1):
    if n%i==0:
        fact+=1
        if fact==0:
            print(f"{n} is prime number\nfactors count is {fact}")
        else:
            print(f"{n} is not prime number\nfactors count is {fact}")