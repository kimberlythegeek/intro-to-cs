#Problem Set 1


####Variables####
choice = 1  # Program Selection




####Functions#####


#Minimum Monthly Payment Simulation
def minimum():
    balance = 0.0  # Current Balance

    while balance >= 0:

        total = 0.0

        balance = float(raw_input("\n\n---------------------------------\n\nWhat is the outstanding balance on your Credit Card? (Enter -1 to exit) "))
        if balance < 0:
            return
        annual_rate = float(raw_input("What is the Annual Interest Rate? "))
        mmp_rate = float(raw_input("What is your Minimum Monthly Payment Rate? "))

        for i in range (1,13):

            mmp = round(mmp_rate * balance,2)
            interest_paid = round(annual_rate / 12 * balance,2)
            principal_paid = mmp - interest_paid
            balance -= principal_paid
            total += mmp

            print "Month " + str(i)
            print "Minimum Monthly Payment: $" + str(mmp)
            print "Principal Paid: $" + str(principal_paid)
            print "Remaining Balance: $" + str(balance) + "\n"

        print "\nRESULT\n"
        print "Total amount paid this year: $" + str(total)
        print "Remaining Balance: $" + str(balance)


        total = 0.0


#Minimum Monthly Payment to pay off balance within 1 year
def oneyear():

    balance = 0.0

    while balance >= 0:

        balance = float(raw_input("\n\n---------------------------------\n\nWhat is the outstanding balance on your Credit Card? (Enter -1 to exit) "))
        if balance < 0:
            return
        annual_rate = float(raw_input("What is the Annual Interest Rate? "))
        monthly_rate = annual_rate / 12.0

        remaining = balance
        guess = 0.0
        epsilon = 10.0

        find_mmp(guess,remaining,balance,monthly_rate,epsilon)

        # while remaining > 0:
        #
        #     remaining = balance
        #     guess += epsilon
        #
        #     for i in range(1, 13):
        #         if remaining < 0.01:
        #             break
        #
        #         months = i
        #         print "\nMonth " + str(months)
        #         interest = round(monthly_rate * remaining, 2)
        #         remaining += interest
        #         remaining -= guess
        #         print "Payment amount: $" + str(guess)
        #         print "Remaining balance: $" + str(remaining)
        #
        # else:
        #     print "---------------------------------\nRESULT\n"
        #     print "Minimum Monthly Payment: $" + str(guess)
        #     print "Number of Months Needed: " + str(months)
        #     print "Remaining Balance: $" + str(remaining)







#Bisection Searching
def bisection():

    balance = 0.0

    while balance >= 0:

        balance = float(raw_input("\n\n---------------------------------\n\nWhat is the outstanding balance on your Credit Card? (Enter -1 to exit) "))
        annual_rate = float(raw_input("What is the Annual Interest Rate? "))

        monthly_rate = annual_rate/12.0
        remaining = balance
        lower = balance / 12
        upper = (balance * (1 + monthly_rate)**12)/12
        mmp_found = False

        while not mmp_found:

            guess = (lower + upper) / 2.0
            print "New Guess: $" + str(guess)
            remaining = balance

            for i in range (1,13):
                if remaining < 0.01:
                    break

                print "\n\nMonth: " + str(i)
                interest = round(monthly_rate * remaining, 2)
                print "Interest: $" + str(interest)
                remaining += interest
                print "Remaining + Interest: $" + str(round(remaining,2))
                remaining -= guess
                print "Remaining - Payment: $" + str(round(remaining,2))
                months = i



            print "---------------------------------\nPayment amount: $" + str(round(guess,2))
            print "Remaining balance: $" + str(round(remaining, 2)) + "\n---------------------------------\n"

            if upper - lower < 0.005:
                guess = round(guess + 0.004999, 2)




                print "---------------------------------\nRESULT\n"
                print "Minimum Monthly Payment: $" + str(round(guess,2))
                print "Number of Months Needed: " + str(round(months,2))
                print "Remaining Balance: $" + str(round(remaining, 2))
                mmp_found = True

            #Guess too low
            if remaining > 0:
                lower = guess

            #Guess too high
            elif remaining < -0.01:
                upper = guess


def find_mmp(guess, remaining, balance, monthly_rate, epsilon):

    while remaining > 0:

        remaining = balance
        guess += epsilon

        for i in range(1, 13):
            if remaining < 0.01:
                break

            months = i
            print "\nMonth " + str(months)
            interest = round(monthly_rate * remaining, 2)
            remaining += interest
            remaining -= guess
            print "Payment amount: $" + str(guess)
            print "Remaining balance: $" + str(remaining)

    else:
        print "---------------------------------\nRESULT\n"
        print "Minimum Monthly Payment: $" + str(guess)
        print "Number of Months Needed: " + str(months)
        print "Remaining Balance: $" + str(remaining)






# Program Selection #
switch = {
    1: minimum,
    2: oneyear,
    3: bisection,
}

# Program Begins #
while choice != 0:

    choice = int(raw_input(
        "\n\n---------------------------------\n\nWhat payment plan would you like to simulate?\n\t1: Minimum Monthly Payment\n\t2: Pay off debt within one year\n\t3: Bisection searching\n\t0: Exit Program\n>>"))
    if choice == 0:
        print "\n\n---------------------------------\n    >>>> Exiting Program <<<<\n---------------------------------"
        break
    switch[choice]()


