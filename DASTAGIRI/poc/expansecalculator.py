##Read the salary from the user
##
##keep asking the user until unless user enters 'q'
##Enter the expenditure name: 
##Enter the amount for <expenditure name>:
##Eg:
##Enter the expenditure name: rent
##Enter the amount for rent: 1000
##
##Validations:
##------------
##if the expenditure name entered twice the previous amount should be added to the current amount
##
##if the amount is greater than the balance print 'Insufficient funds'
##
## 
##finally print the salary and expenditures and balance in a table format
##
##salary                                                         :                               10000/-
##---------------------------------------------------------------------------
##rent                                                           :                                 1000/-
##movie                                                        :                                   500/-
##----------------------------------------------------------------------------
##total                                                         :                                  1500/-
##balance                                                     :                                   8500/-




dic={}        
savings=0
actual_savings=0
transactions=0

salary=int(input("Enter the salary: "))
savings=savings+salary
actual_savings=actual_savings+salary

while True:
    exp=input('Enter the expenditure name: ')
    if exp=='q':
        break
    else:
        price=int(input("Enter the amount for {}: ".format(exp)))
        if price > savings:
            print('Insufficient funds')
        else:                
            savings=savings-price
            transactions=transactions+price
            if exp in dic.keys():
                dic[exp]=dic[exp]+price
            else:
                dic[exp]=price
            
print("salary \t\t\t\t:",salary,end="/-")
print()
print("-"*40)
for k,v in dic.items():
    print(k,'\t\t\t\t:',v,end="/-")
    print()
print("-"*40)
print("total\t\t\t\t:",transactions,end="/-")
print()
balance=actual_savings-transactions
print("balance\t\t\t\t:",balance,end="/-")

##Output:
##Enter the salary: 15000
##Enter the expenditure name: rent
##Enter the amount for rent: 5000
##Enter the expenditure name: shop
##Enter the amount for shop: 3000
##Enter the expenditure name: travel
##Enter the amount for travel: 90000
##Insufficient funds
##Enter the expenditure name: travel
##Enter the amount for travel: 900
##Enter the expenditure name: q
##salary 			: 15000/-
##--------------------------------------
##rent 				: 5000/-
##shop 				: 3000/-
##travel 			: 900/-
##--------------------------------------
##total				: 8900/-
##balance			: 6100/-
