  
n=int(input("enter the size: "))
for row in range(n):
        for col in range(n):
            if row==col or row==n-1 or row+col==n-1:
                print("*",end=" ")
            else:
                print("",end="")
        print()
        
        
        
    #ATM
n=int(input("enter the number:"))
assert n>0, "n need positive"
data=int(input("welcome to atm:"))
account_number = int(input("enter account number:"))
pin= int(input("enter pin:"))
check_balance = int(input("1.check balance:"))
deposite = int(input("2.deposite:"))

print("welcome to atm")
print("1.check balance:",account_number)
print("2.deposite:",pin)
print("3.check_balance:",check_balance)
print("4.deposite:",deposite)       
        
        
        
        