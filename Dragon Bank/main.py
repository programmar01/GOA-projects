welcome = input("Welcome to one of the best bank in the world. do you want login or register?: ")


#registeer
if welcome == "register":

    name = input("enter your name: ")
    email = input("Enter your email address: ")
    id = input("enter your id: ")
    phone = input("Enter your phone number: ")

    if len(phone) != 9:
        print("invalid phone number. Try again")
        input("enter phone number again: ")

    cvc = input("enter your cvc: ")

    if len(cvc) != 3:
        print("invalid cvc. Try again")
        input("enter cvc again: ")
    
    password = input("enter your password: ")

    if len(password) < 10:
        print("password must be at least 10 characters")
        input("enter your password: ")
        confrim = input("Confrim your password: ")

    if confrim != password:
        print("you entered wrong password")
        input("enter password again: ")

    print("------------end------------")
    print("you succesfully registered !!! Welcome to Goa Bank <3")
    print("""                                                                                                                                       

        """)


#login

if welcome == "login":
    name1 = input("enter your name: ")
    email1 = input("enter your email: ")
    password1 = input("enter your password______forgot? Y/N: ")
    if password1 == "Y" or password1 == "y":
        resetemail = input("enter your email: ")
        resetcode = input("enter your one time code: ")
        newpassword = input("enter your new password: ")
        confrimPassword = input("confrim new password: ")

        if confrimPassword != newpassword:
            print("you entered wrong password")
            input("enter password again: ")
        else:
            print("you succesfully changed your password")
            print("---------------------------")
            print("you succesfully logged in !!! Welcome to Goa Bank <3")
    else:
        input("enter your password: ")
        print("you succesfully logged in !!! Welcome to Goa Bank <3")

#deposit

deposit = int(input("how much $ you want to deposit?: "))

if deposit == 0:
    print("you can't deposit 0$")
    input("how much $ you want to deposit?: ")

print("now on your bank account, you have " + str(deposit) + " $")
print("---------------------------")



#depos., with., tran.,

question1 = input("do you want to deposit again, withdraw or transfer ?: ")
if question1 == "deposit":
    newdeposit = int(input("how much $ you want to deposit"))
    deposit = deposit + newdeposit

print("now on your bank account, you have " + str(deposit) + " $")
print("""                                                                                                                                       

        """)
print("---------------------------")

#withdraw

if question1 == "withdraw":
    withdraw = int(input("how much $ you want to withdraw?: "))
    if withdraw > deposit:
        print("you can't withdraw more than you have")
        again = int(input("how much $ you want to withdraw?: "))

    print("now on your bank account, you have " + str(deposit - withdraw) + " $")
    print("---------------------------")




#transfer

if question1 == "transfer":
    transfer = input("do you want to transfer? (yes or no): ")
    
    if transfer == "yes":
        user_name = input("who you transfer to?: ")
        user_email = input("number of the person: ")
        transfer_to = int(input("how much he/she have?: "))
        user_id = input("id of the user: ")
        transfer_user = int(input("how much you want to transfer?: "))
        if transfer_user > deposit:
            print("you can't transfer more than you have")
            transfer_user = int(input("how much $ you want to transfer?: "))

        print("transfer succesfully  ")
        print("now you have " + str(deposit - transfer_user) + " $")
        print("now second acc have " + str(transfer_to + transfer_user) + " $")



#loguot
print("---------------------------")
print("""                                                                                                                                       

        """)

log_out = input("do you want to log out: ")
if log_out == "yes":
    print("---------------------------")
    print("you succesfully logged out")
    print("---------------------------")
    print("thank you for using Goa Bank")
    print("---------------------------")
else :
    print("---------------------------")
    print("thank you for using Goa Bank")
    print("---------------------------")






