# investment app
# user adds name
# user adds amount
# application returns 50% profits on capital
# user enters amount to withdraw
# user gets insufficient funds if amount inputed is haigher than account balance
# user get credited if inputed amount for withdrawal is lesser than account balance
# application gets 7% service charge from account balance

profit_percentage = 50
vat_percentage = 7
def investment():
    investor_name = input("Enter name:")
    print(investor_name , "Welcome to cohort4 Investment App")
    investor_wallet = int(input("Amount to invest:N"))
    interest = investor_wallet * profit_percentage / 100
    wallet_balance = investor_wallet + interest 
    print("Dear Investor" , investor_name , "Your Wallet has been credited with the sum of:N" , wallet_balance, "50% interest on your capital")
    withdrawal_amount = int(input("Enter Your withdrawal Amount:N"))
    if withdrawal_amount >= wallet_balance:
        print(investor_name,"You have an insufficient Funds to perform this transaction")
    else:
        final_wallet_balance = wallet_balance - withdrawal_amount
        vat_reduction = final_wallet_balance * vat_percentage/100
        final_balance = final_wallet_balance - vat_reduction
        print(investor_name ,"Your withdrawal was successful and your account has been debited with:N", withdrawal_amount, "and a 7% service charge,vat_reduction "has been deducted and" ,"your final balance is:" ,'N',final_balance)

investment()
