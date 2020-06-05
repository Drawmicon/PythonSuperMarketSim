import random

'''

'''

#prints out time in 12 hour format
def timer():
    hours = 6
    i = 0
    timex = a
    while timex >= 60:
        timex = timex - 60
        i = i + 1
    hours = hours + i
    minutes = timex
    if i > 6:
        hours1 = hours - 12
        print(hours1, ":", str(minutes).zfill(2), " ")
    else:
        print(hours, ":", str(minutes).zfill(2), " ")

    matrix = random.randint(1, 800)
    if matrix == 154 and allcust > 0:
        print("\n\"Hey, what if we are all living in some simulation?\"\n\"What on earth do you expect us to do about that possibility?\" \n\"Just making conversation, sheesh.\" \n")


# prints out time in 12 hour format
def time12():
    hours = 6
    i = 0
    time1 = time
    while time1 >= 60:
        time1 = time1 - 60
        i = i + 1
    hours = hours + i
    minutes = time1
    if i > 6:
        hours1 = hours - 12
        print(hours1, ":", str(minutes).zfill(2), " ")
    else:
        print(hours, ":", str(minutes).zfill(2), " ")


#Per Day Loop
for i in range(1):
    #Starting Time
    time = 0
    print("Store Opens: ",end='')
    time12()

    #number of customers per day
    x = 0
    done = False

    # cashier arrays will store time needed to purchase items at register
    cashier1 = []
    cashier2 = []
    cashier3 = []
    cashier4 = []
    cashier5 = []
    cashier6 = []
    cashier7 = []
    cashier8 = []
    cashier9 = []
    cashier10 = []
    cashier11 = []
    cashier12 = []
    # arrays that holds all customer data for every customer
    #Customer number
    total1 = []
    #Customer time when go to a register
    total2 = []
    #Customer amount of time needed at register
    total3 = []
    #***********************************************************
    while time < 900 and done == False:

        #one more customer
        x = x + 1
        #random arrival time from 1 minutes to 15 minutes after previous person
        arrival = random.randint(1, 10)
        #print("Arrival: ", arrival)
        #time passes
        time = arrival + time
        #print("Time: ",time)

        #one day of shopping from 6:00 am to 6:00 pm
        print ("Customer ", x, " arrives at ", end='')
        time12()
        #*****************************************************************
        #random amount of time spent shopping
        shoppingTime = random.randint(1, 30)
        #Amount of items bought, influenced by shoppingTime
        k = random.randint(9,19)
        k = k/10
        regTime = shoppingTime*k
        int(regTime)
        #print("Items: ", int(regTime))

        #random stall variable
        forgot = random.randint(1, 50)
        stall = False
        if forgot == 37:
            stall = True
        #total amount of time until enter register line
        if regTime > 0:
            gotoReg = time + shoppingTime
            if stall == True:
                forgotten = random.randint(1, 20)
                gotoReg = gotoReg + forgotten
            #add customer number and amount of time needed
            #x = customer number, gotoReg = time when register is reached
            #regTime = time needed at register
            total1.append(x)
            total2.append(gotoReg)
            total3.append(int(regTime))




        # if the day is nearly over, allow no more customers
        if time > 840:
            done = True

    #All Customer Data
    for i in range(len(total1)):
        print("Customer: ",total1[i], " Done Shopping At: ", total2[i], " Time Needed At Register: ", total3[i])

    #Sort all customers in order of arrival to register time

    total2v = total2
    total2vv = []
    total3v = []
    total1v = []
    while len(total3v)!= (len(total2v)):
        hal = total2v[0]
        ibm = 0
        ll = 0
        gzk = 0
        for j in range(len(total2v)):
            #ibm = total1[i]
            #find smallest time until cash register reached
            if total2v[j] < hal:
                hal = total2v[j]
                ibm = total3[j]
                ll = j
                gzk = total1[j]
        total2v[ll] = 9999
        total2vv.append(hal)
        total3v.append(ibm)
        total1v.append(gzk)

    print (total1v)
    print(total2vv)
    #for i in range(len(total3v)):
    print("Customer times in order: ", total3v)


    print("\n")
    print("\n")
    print("\n")

#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
    #*************************************************************************
    #all customers organized by the time they reached the registers, data values represent amount of time needed at registers

    #loadTime = 0
    #boolean values to check if register is open

    c1 = True
    c2 = False
    c3 = False
    c4 = False
    c5 = False
    c6 = False
    c7 = False
    c8 = False
    c9 = False
    c10 = False
    c11 = False
    c12 = False

    total2vvr = total2vv
    total3vr = total3v
    # ////////////////////////////////////////////////////////////////////////////////////////

    #Process Part 2


    #t2vvCounter = 0
    #counter to iterate through arrays of customer data
    kt = False
    i = 0

    #New loop with customers going to the registers while cycling through time, 900 minutes
    for a in range(1080):
        print("\n")
        #prints out time in 12 hour format
        print("Current Time: ", end='')
        timer()

        kt = False
        i = 0

        if len(total2vvr) > 0:
            if total2vvr[0] <= a:
                #print("a: ", aj)
                # print("Time When Arrived At Register: ", total2vvr[0])
                # make list of smallest lines
                # to find smallest length of cashier line, go through list of numbers until the length of one of the lines is reached
                # find smallest line length
                print("Total2vvr: ", total2vvr)
                print("Total3vr: ", total3vr)
                while kt == False:
                    print("kt: ", kt, ", i: ", i)
                    # if the line length is the current number for i (increases by one; i grows from smallest to largest),
                    # and the length is less than max (10), and the line is open, append data to line
                    if len(cashier1) == i and len(cashier1) < 10 and kt == False:
                        cashier1.append(total3vr[0])
                        kt = True
                        if len(cashier1) >= 10:
                            c2 = True
                    if len(cashier2) == i and len(cashier2) < 10 and kt == False:
                        cashier2.append(total3vr[0])
                        kt = True
                        if len(cashier2) >= 10:
                            c3 = True
                    if len(cashier3) == i and len(cashier3) < 10 and kt == False:
                        cashier3.append(total3vr[0])
                        kt = True
                        if len(cashier3) >= 10:
                            c4 = True
                    if len(cashier4) == i and len(cashier4) < 10 and kt == False:
                        cashier4.append(total3vr[0])
                        kt = True
                        if len(cashier4) >= 10:
                            c5 = True
                    if len(cashier5) == i and len(cashier5) < 10 and kt == False:
                        cashier5.append(total3vr[0])
                        kt = True
                        if len(cashier5) >= 10:
                            c6 = True
                    if len(cashier6) == i and len(cashier6) < 10 and kt == False:
                        cashier6.append(total3vr[0])
                        kt = True
                        if len(cashier6) >= 10:
                            c7 = True
                    if len(cashier7) == i and len(cashier7) < 10 and kt == False:
                        cashier7.append(total3vr[0])
                        kt = True
                        if len(cashier7) >= 10:
                            c8 = True
                    if len(cashier8) == i and len(cashier8) < 10 and kt == False:
                        cashier8.append(total3vr[0])
                        kt = True
                        if len(cashier8) >= 10:
                            c9 = True
                    if len(cashier9) == i and len(cashier9) < 10 and kt == False:
                        cashier9.append(total3vr[0])
                        kt = True
                        if len(cashier9) >= 10:
                            c10 = True
                    if len(cashier10) == i and len(cashier10) < 10 and kt == False:
                        cashier10.append(total3vr[0])
                        kt = True
                        if len(cashier10) >= 10:
                            c11 = True
                    if len(cashier11) == i and len(cashier11) < 10 and kt == False:
                        cashier11.append(total3vr[0])
                        kt = True
                        if len(cashier11) >= 10:
                            c12 = True
                    if len(cashier12) == i and kt == False:  # and len(cashier12) < 10:
                        cashier12.append(total3vr[0])
                        kt = True
                    # increment list index if no line is chosen
                    if kt == False:
                        i = i + 1
                if kt == True:
                    del total2vvr[0]
                    del total3vr[0]
                    kt = False
                    i = 0


        print ("Total vvr: ", total2vvr)
        print("Total3vr: ", total3vr)

        allcust = 0

        # Print out cashier lines if they in use aka they have a length of more than zero
        if len(cashier1) != 0:
            print("Cashier Line 1: ", cashier1)
        if len(cashier2) != 0:
            print("Cashier Line 2: ", cashier2)
        if len(cashier3) != 0:
            print("Cashier Line 3: ", cashier3)
        if len(cashier4) != 0:
            print("Cashier Line 4: ", cashier4)
        if len(cashier5) != 0:
            print("Cashier Line 5: ", cashier5)
        if len(cashier6) != 0:
            print("Cashier Line 6: ", cashier6)
        if len(cashier7) != 0:
            print("Cashier Line 7: ", cashier7)
        if len(cashier8) != 0:
            print("Cashier Line 8: ", cashier8)
        if len(cashier9) != 0:
            print("Cashier Line 9: ", cashier9)
        if len(cashier10) != 0:
            print("Cashier Line 10: ", cashier10)
        if len(cashier11) != 0:
            print("Cashier Line 11: ", cashier11)
        if len(cashier12) != 0:
            print("Cashier Line 12: ", cashier12)

        #Customer 1 of each line is now processing...
        #subtract 1 from the time needed at register for the first customer of each line,
        #  after every minute passes, the amount of time needed at the register for customer 1 is reduced by 1 minute
        if len(cashier1) > 0 and cashier1[0] != 0:
            xof = cashier1[0]
            xof = xof - 1
            cashier1[0] = xof
        if len(cashier2) > 0 and cashier2[0] != 0:
            xof = cashier2[0]
            xof = xof - 1
            cashier2[0] = xof
        if len(cashier3) > 0 and cashier3[0] != 0:
            xof = cashier3[0]
            xof = xof - 1
            cashier3[0] = xof
        if len(cashier4) > 0 and cashier4[0] != 0:
            xof = cashier4[0]
            xof = xof - 1
            cashier4[0] = xof
        if len(cashier5) > 0 and cashier5[0] != 0:
            xof = cashier5[0]
            xof = xof - 1
            cashier5[0] = xof
        if len(cashier6) > 0 and cashier6[0] != 0:
            xof = cashier6[0]
            xof = xof - 1
            cashier6[0] = xof
        if len(cashier7) > 0 and cashier7[0] != 0:
            xof = cashier7[0]
            xof = xof - 1
            cashier7[0] = xof
        if len(cashier8) > 0 and cashier8[0] != 0:
            xof = cashier8[0]
            xof = xof - 1
            cashier8[0] = xof
        if len(cashier9) > 0 and cashier9[0] != 0:
            xof = cashier9[0]
            xof = xof - 1
            cashier9[0] = xof
        if len(cashier10) > 0 and cashier10[0] != 0:
            xof = cashier10[0]
            xof = xof - 1
            cashier10[0] = xof
        if len(cashier11) > 0 and cashier11[0] != 0:
            xof = cashier11[0]
            xof = xof - 1
            cashier11[0] = xof
        if len(cashier12) > 0 and cashier12[0] != 0:
            xof = cashier12[0]
            xof = xof - 1
            cashier12[0] = xof

        #after decreasing the time lengths of the first customer in every lines by 1 after every minute, when it gets to zero, it will remove itself from the list
        #if the remaining time is for a customer is already zero (less than 60 seconds), remove it from the customer from line
        if len(cashier1) > 0 and cashier1[0] == 0:
            del cashier1[0]

        if len(cashier2) > 0 and cashier2[0] == 0:
            del cashier2[0]

        if len(cashier3) > 0 and cashier3[0] == 0:
            del cashier3[0]

        if len(cashier4) > 0 and cashier4[0] == 0:
            del cashier4[0]

        if len(cashier5) > 0 and cashier5[0] == 0:
            del cashier5[0]

        if len(cashier6) > 0 and cashier6[0] == 0:
            del cashier6[0]

        if len(cashier7) > 0 and cashier7[0] == 0:
            del cashier7[0]

        if len(cashier8) > 0 and cashier8[0] == 0:
            del cashier8[0]

        if len(cashier9) > 0 and cashier9[0] == 0:
            del cashier9[0]

        if len(cashier10) > 0 and cashier10[0] == 0:
            del cashier10[0]

        if len(cashier11) > 0 and cashier11[0] == 0:
            del cashier11[0]

        if len(cashier12) > 0 and cashier12[0] == 0:
            del cashier12[0]
        
        #if the total amount of customers is less then amount of registers needed, close registers/ sum of lengths of arrays
        allcust = len(cashier1) + len(cashier2) + len(cashier3) + len(cashier4) + len(cashier5) + len(cashier6) + len(cashier7) + len(cashier8) + len(cashier9) + len(cashier10) + len(cashier11) + len(cashier12)
        
        # ////////////////////////////////////////////////////////////////////////////////////////
        # ////////////////////////////////////////////////////////////////////////////////////////
        # ////////////////////////////////////////////////////////////////////////////////////////



        #if Line Length is greater than x time, create new register line
        #if wait time is 60 minutes or greater, open new register line
        sum1 = 0
        for g in range (len(cashier1)):
            sum1 = sum1 + cashier1[g]
        if sum1 > 60:
            print("Open Register 2. ")
            c2 = True
            #cashier2.append(cashier1[len(cashier1)-1])
            #del cashier1[len(cashier1)-1]
        sum2 = 0
        for g in range(len(cashier2)):
            sum2 = sum2 + cashier2[g]
        if sum2 > 60:
            print("Open Register 3. ")
            c3 = True

        sum3 = 0
        for g in range(len(cashier3)):
            sum3 = sum3 + cashier3[g]
        if sum3 > 60:
            print("Open Register 4. ")
            c4 = True
        sum4 = 0
        for g in range(len(cashier4)):
            sum4 = sum4 + cashier4[g]
        if sum4 > 60:
            print("Open Register 5. ")
            c5 = True
        sum5 = 0
        for g in range(len(cashier5)):
            sum5 = sum5 + cashier5[g]
        if sum5 > 60:
            print("Open Register 6. ")
            c6 = True
        sum6 = 0
        for g in range(len(cashier6)):
            sum6 = sum6 + cashier6[g]
        if sum6 > 60:
            print("Open Register 7. ")
            c7 = True
        sum7 = 0
        for g in range(len(cashier7)):
            sum7 = sum7 + cashier7[g]
        if sum7 > 60:
            print("Open Register 8. ")
            c8 = True
        sum8 = 0
        for g in range(len(cashier8)):
            sum8 = sum8 + cashier8[g]
        if sum8 > 60:
            print("Open Register 9. ")
            c9 = True
        sum9 = 0
        for g in range(len(cashier9)):
            sum9 = sum9 + cashier9[g]
        if sum9 > 60:
            print("Open Register 10. ")
            c10 = True
        sum10 = 0
        for g in range(len(cashier10)):
            sum10 = sum10 + cashier10[g]
        if sum10 > 60:
            print("Open Register 11. ")
            c11 = True
        sum11 = 0
        for g in range(len(cashier11)):
            sum11 = sum11 + cashier11[g]
        if sum11 > 60:
            print("Open Register 12. ")
            c12 = True
        #




        #all customer data for time needed at register is in array total3v
        #for every value in array total2vv, if the time when entered into register line is equal to current time, related time needed at register is appended

        #*************************************************************************************
        #current time == time when entered line
        #when amount of time needed at register is equal to current time

        
        
        #if previous register is full, open new register
        if len(cashier1) >= 10:
            print("Cashier Line 1 is Full")
            #register 2 is now open, default false
            c2 = True
        if len(cashier2) >= 10:
            print("Cashier Line 2 is Full")
            c3 = True
        if len(cashier3) >= 10:
            print("Cashier Line 3 is Full")
            c4 = True
        if len(cashier4) >= 10:
            print("Cashier Line 4 is Full")
            c5 = True
        if len(cashier5) >= 10:
            print("Cashier Line 5 is Full")
            c6 = True
        if len(cashier6) >= 10:
            print("Cashier Line 6 is Full")
            c7 = True
        if len(cashier7) >= 10:
            print("Cashier Line 7 is Full")
            c8 = True
        if len(cashier8) >= 10:
            print("Cashier Line 8 is Full")
            c9 = True
        if len(cashier9) >= 10:
            print("Cashier Line 9 is Full")
            c10 = True
        if len(cashier10) >= 10:
            print("Cashier Line 10 is Full")
            c11 = True
        if len(cashier11) >= 10:
            print("Cashier Line 11 is Full")
            c12 = True
        if len(cashier12) >= 10:
            print("All Cashier Lines Are Full")
        
        # **************************************************************
        
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ UNDER CONSTRUCTION



        #**************************************************************************************





        #max occupancy == 120
        #While some register lanes may not be open, it is a reorganization that reduces total amount of register needed
        #if the total customers is less than 101 and customers are at register 12, close register 12, place rest of customers in other registers
        if allcust < 100 and len(cashier12) > 0 and sum11 < 60:
            #while customers still exist at register 12
            while len(cashier12) != 0:
                #if register is not full, add customer here
                if len(cashier11) != 10 and len(cashier12) != 0:
                    cashier11.append(cashier12[0])
                    #increment to next spot in array
                    #decrement number of items in array
                    del cashier12[0]
                if len(cashier10) != 10 and len(cashier12) != 0:
                    cashier10.append(cashier12[0])
                    del cashier12[0]
                if len(cashier9) != 10 and len(cashier12) != 0:
                    cashier9.append(cashier12[0])
                    del cashier12[0]
                if len(cashier8) != 10 and len(cashier12) != 0:
                    cashier8.append(cashier12[0])
                    del cashier12[0]
                if len(cashier7) != 10 and len(cashier12) != 0:
                    cashier7.append(cashier12[0])
                    del cashier12[0]
                if len(cashier6) != 10 and len(cashier12) != 0:
                    cashier6.append(cashier12[0])
                    del cashier12[0]
                if len(cashier5) != 10 and len(cashier12) != 0:
                    cashier5.append(cashier12[0])
                    del cashier12[0]
                if len(cashier4) != 10 and len(cashier12) != 0:
                    cashier4.append(cashier12[0])
                    del cashier12[0]
                if len(cashier3) != 10 and len(cashier12) != 0:
                    cashier3.append(cashier12[0])
                    del cashier12[0]
                if len(cashier2) != 10 and len(cashier12) != 0:
                    cashier2.append(cashier12[0])
                    del cashier12[0]
                if len(cashier1) != 10 and len(cashier12) != 0:
                    cashier1.append(cashier12[0])
                    del cashier12[0]

        if allcust < 80 and len(cashier11) > 0 and sum10 < 60:
            while len(cashier11) > 0:
                if len(cashier10) != 10 and len(cashier11) != 0:
                    cashier10.append(cashier11[0])
                    del cashier11[0]
                if len(cashier9) != 10 and len(cashier11) != 0:
                    cashier9.append(cashier11[0])
                    del cashier11[0]
                if len(cashier8) != 10 and len(cashier11) != 0:
                    cashier8.append(cashier11[0])
                    del cashier11[0]
                if len(cashier7) != 10 and len(cashier11) != 0:
                    cashier7.append(cashier11[0])
                    del cashier11[0]
                if len(cashier6) != 10 and len(cashier11) != 0:
                    cashier6.append(cashier11[0])
                    del cashier11[0]
                if len(cashier5) != 10 and len(cashier11) != 0:
                    cashier5.append(cashier11[0])
                    del cashier11[0]
                if len(cashier4) != 10 and len(cashier11) != 0:
                    cashier4.append(cashier11[0])
                    del cashier11[0]
                if len(cashier3) != 10 and len(cashier11) != 0:
                    cashier3.append(cashier11[0])
                    del cashier11[0]
                if len(cashier2) != 10 and len(cashier11) != 0:
                    cashier2.append(cashier11[0])
                    del cashier11[0]
                if len(cashier1) != 10 and len(cashier11) != 0:
                    cashier1.append(cashier11[0])
                    del cashier11[0]
#*********************************************
        if allcust < 60 and len(cashier10) > 0 and sum9 < 60:
            while len(cashier10) > 0 and len(cashier10) != 0:
                if len(cashier9) != 10:
                    cashier9.append(cashier10[0])
                    del cashier10[0]
                if len(cashier8) != 10 and len(cashier10) != 0:
                    cashier8.append(cashier10[0])
                    del cashier10[0]
                if len(cashier7) != 10 and len(cashier10) != 0:
                    cashier7.append(cashier10[0])
                    del cashier10[0]
                if len(cashier6) != 10 and len(cashier10) != 0:
                    cashier6.append(cashier10[0])
                    del cashier10[0]
                if len(cashier5) != 10 and len(cashier10) != 0:
                    cashier5.append(cashier10[0])
                    del cashier10[0]
                if len(cashier4) != 10 and len(cashier10) != 0:
                    cashier4.append(cashier10[0])
                    del cashier10[0]
                if len(cashier3) != 10 and len(cashier10) != 0:
                    cashier3.append(cashier10[0])
                    del cashier10[0]
                if len(cashier2) != 10 and len(cashier10) != 0:
                    cashier2.append(cashier10[0])
                    del cashier10[0]
                if len(cashier1) != 10 and len(cashier10) != 0:
                    cashier1.append(cashier10[0])
                    del cashier10[0]

        if allcust < 50 and len(cashier9) > 0 and sum8 < 60:
            while len(cashier9) > 0:
                if len(cashier8) != 10 and len(cashier9) != 0:
                    cashier8.append(cashier9[0])
                    del cashier9[0]
                if len(cashier7) != 10 and len(cashier9) != 0:
                    cashier7.append(cashier9[0])
                    del cashier9[0]
                if len(cashier6) != 10 and len(cashier9) != 0:
                    cashier6.append(cashier9[0])
                    del cashier9[0]
                if len(cashier5) != 10 and len(cashier9) != 0:
                    cashier5.append(cashier9[0])
                    del cashier9[0]
                if len(cashier4) != 10 and len(cashier9) != 0:
                    cashier4.append(cashier9[0])
                    del cashier9[0]
                if len(cashier3) != 10 and len(cashier9) != 0:
                    cashier3.append(cashier9[0])
                    del cashier9[0]
                if len(cashier2) != 10 and len(cashier9) != 0:
                    cashier2.append(cashier9[0])
                    del cashier9[0]
                if len(cashier1) != 10 and len(cashier9) != 0:
                    cashier1.append(cashier9[0])
                    del cashier9[0]


        if allcust < 40 and len(cashier8) > 0 and sum7 < 60:
            while len(cashier8) > 0:
                if len(cashier7) != 10 and len(cashier8) != 0:
                    cashier7.append(cashier8[0])
                    del cashier8[0]
                if len(cashier6) != 10 and len(cashier8) != 0:
                    cashier6.append(cashier8[0])
                    del cashier8[0]
                if len(cashier5) != 10 and len(cashier8) != 0:
                    cashier5.append(cashier8[0])
                    del cashier8[0]
                if len(cashier4) != 10 and len(cashier8) != 0:
                    cashier4.append(cashier8[0])
                    del cashier8[0]
                if len(cashier3) != 10 and len(cashier8) != 0:
                    cashier3.append(cashier8[0])
                    del cashier8[0]
                if len(cashier2) != 10 and len(cashier8) != 0:
                    cashier2.append(cashier8[0])
                    del cashier8[0]
                if len(cashier1) != 10 and len(cashier8) != 0:
                    cashier1.append(cashier8[0])
                    del cashier8[0]

        if allcust < 20 and len(cashier7) > 0 and sum6 < 60:
            while len(cashier7) > 0:
                if len(cashier6) != 10 and len(cashier7) != 0:
                    cashier6.append(cashier7[0])
                    del cashier7[0]
                if len(cashier5) != 10 and len(cashier7) != 0:
                    cashier5.append(cashier7[0])
                    del cashier7[0]
                if len(cashier4) != 10 and len(cashier7) != 0:
                    cashier4.append(cashier7[0])
                    del cashier7[0]
                if len(cashier3) != 10 and len(cashier7) != 0:
                    cashier3.append(cashier7[0])
                    del cashier7[0]
                if len(cashier2) != 10 and len(cashier7) != 0:
                    cashier2.append(cashier7[0])
                    del cashier7[0]
                if len(cashier1) != 10 and len(cashier7) != 0:
                    cashier1.append(cashier7[0])
                    del cashier7[0]

        if allcust < 10 and len(cashier6) > 0 and sum5 < 60:
            while len(cashier6) > 0:

                if len(cashier5) != 10 and len(cashier6) != 0:
                    cashier5.append(cashier6[0])
                    del cashier6[0]

                if len(cashier4) != 10 and len(cashier6) != 0:
                    cashier4.append(cashier6[0])
                    del cashier6[0]

                if len(cashier3) != 10 and len(cashier6) != 0:
                    cashier3.append(cashier6[0])
                    del cashier6[0]

                if len(cashier2) != 10 and len(cashier6) != 0:
                    cashier2.append(cashier6[0])
                    del cashier6[0]

                if len(cashier1) != 10 and len(cashier6) != 0:
                    cashier1.append(cashier6[0])
                    del cashier6[0]
        '''
        if allcust < 40 and len(cashier5) > 0 and sum4 < 60:
            while len(cashier5) > 0:
                if len(cashier4) != 10 and len(cashier5) != 0:
                    cashier4.append(cashier5[0])
                    del cashier5[0]

                if len(cashier3) != 10 and len(cashier5) != 0:
                    cashier3.append(cashier5[0])
                    del cashier5[0]

                if len(cashier2) != 10 and len(cashier5) != 0:
                    cashier2.append(cashier5[0])
                    del cashier5[0]

                if len(cashier1) != 10 and len(cashier5) != 0:
                    cashier1.append(cashier5[0])
                    del cashier5[0]

        if allcust < 30 and len(cashier4) > 0 and sum3 < 60:
            while len(cashier4) > 0:
                if len(cashier3) != 10 and len(cashier4) != 0:
                    cashier3.append(cashier4[0])
                    del cashier4[0]
                if len(cashier2) != 10 and len(cashier4) != 0:
                    cashier2.append(cashier4[0])
                    del cashier4[0]
                if len(cashier1) != 10 and len(cashier4) != 0:
                    cashier1.append(cashier4[0])
                    del cashier4[0]

        if allcust < 20 and len(cashier3) > 0 and sum2 < 60:
            while len(cashier3) > 0:
                if len(cashier1) != 10 and len(cashier3) != 0:
                    cashier1.append(cashier3[0])
                    del cashier3[0]
                if len(cashier2) != 10 and len(cashier3) != 0:
                    cashier2.append(cashier3[0])
                    del cashier3[0]

        if allcust < 11 and sum1 < 60:
            cashier1.extend(cashier2)
            del cashier2[:]
            cashier1.extend(cashier3)
            del cashier3[:]
            cashier1.extend(cashier4)
            del cashier4[:]
            cashier1.extend(cashier5)
            del cashier5[:]
            cashier1.extend(cashier6)
            del cashier6[:]
            cashier1.extend(cashier7)
            del cashier7[:]
            cashier1.extend(cashier8)
            del cashier8[:]
            cashier1.extend(cashier9)
            del cashier9[:]
            cashier1.extend(cashier10)
            del cashier10[:]
            cashier1.extend(cashier11)
            del cashier11[:]
            cashier1.extend(cashier12)
            del cashier12[:]
        '''
        #********************************************************************************


        #****************************************************
        #If the line is empty, close it
        if len(cashier2) == 0:
            c2 = False
        if len(cashier3) == 0:
            c3 = False
        if len(cashier4) == 0:
            c4 = False
        if len(cashier5) == 0:
            c5 = False
        if len(cashier6) == 0:
            c6 = False
        if len(cashier7) == 0:
            c7 = False
        if len(cashier8) == 0:
            c8 = False
        if len(cashier9) == 0:
            c9 = False
        if len(cashier10) == 0:
            c10 = False
        if len(cashier11) == 0:
            c11 = False
        if len(cashier12) == 0:
            c12 = False
