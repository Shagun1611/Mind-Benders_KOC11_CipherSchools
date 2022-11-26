
print("enter your name : ")
name=input()

print("Enter 1 for displaying name and cash Available")
print("Enter 2 for withdrawing cash")
print("Enter 3 for depositing cash")
print("Enter any other number to exit")

print("Enter the operation you want to perform: ")
x=int(input())
y=0
balance=20000
while(x>=1 and x<=3):
    if (x == 1):
        print("hello Mr ", name)
        print("Avaible Balance is :",balance)
    elif (x == 2):
        print("Enter the amount you want to withdraw : ")
        withdraw = int(input())
        if(balance>withdraw):
            balance = balance - withdraw
            print("Remaining Balance : ", balance)
            if (balance < 5000):
                print("LOW BALANCE")
        else:
            print("not suffucient balance in your account")

    elif (x == 3):
        print("Enter the amount you want to deposit:")
        deposit = int(input())
        balance = balance + deposit
        print("Remaining balnce : ", balance)
        if (balance < 5000):
            print("LOW BALANCE")


    print("Enter the operation you want to perform: ")
    x = int(input())

print("Thank You For Choosing Our Services")