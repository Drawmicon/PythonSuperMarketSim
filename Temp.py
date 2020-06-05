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
    if matrix == 154:
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
        #random arrival time from 0 minutes to 15 minutes after previous person
        arrival = random.randint(0, 10)
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
        if time > 890:
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

    #////////////////////////////////////////////////////////////////////////////////////////
    #////////////////////////////////////////////////////////////////////////////////////////
    '''
    cashier1.append(5)
    cashier1.append(4)
    cashier2.append(3)
    cashier2.append(2)
    cashier3.append(1)
    cashier3.append(0)
    '''
    #////////////////////////////////////////////////////////////////////////////////////////
    #t2vvCounter = 0
    #counter to iterate through arrays of customer data
    loadTime = 0
    #New loop with customers going to the registers while cycling through time, 900 minutes
    for a in range(1001):
        #print("a: ", a)
        print("\n")
        #prints out time in 12 hour format
        print("Current Time: ", end='')
        timer()
        #Print out cashier lines if they are available, if c values are true
        if len(cashier1) != 0:
            print("Cashier Line 1: ", cashier1)
        if c2 == True:
            print("Cashier Line 2: ", cashier2)
        if c3 == True:
            print("Cashier Line 3: ", cashier3)
        if c4 == True:
            print("Cashier Line 4: ", cashier4)
        if c5 == True:
            print("Cashier Line 5: ", cashier5)
        if c6 == True:
            print("Cashier Line 6: ", cashier6)
        if c7 == True:
            print("Cashier Line 7: ", cashier7)
        if c8 == True:
            print("Cashier Line 8: ", cashier8)
        if c9 == True:
            print("Cashier Line 9: ", cashier9)
        if c10 == True:
            print("Cashier Line 10: ", cashier10)
        if c11 == True:
            print("Cashier Line 11: ", cashier11)
        if c12 == True:
            print("Cashier Line 12: ", cashier12)

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



        #print(cashier1)
        #print(cashier2)
        #print(cashier3)

        #********************************************************************************
        #if the length of the cashier is smallest out of availible arrays, go there
        #

        print("1: ", cashier1)
        print("2: ", cashier2)
        print("3: ", cashier3)
        print("4: ", cashier4)
        print("5: ", cashier5)
        print("6: ", cashier6)
        print("7: ", cashier7)
        print("8: ", cashier8)
        print("9: ", cashier9)
        print("10: " ,cashier10)
        print("11: ", cashier11)
        print("12: " ,cashier12)

#/*/*//**/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*//**//*/*/*
        #loadTime = 0
        if total2vv[loadTime] == a:
            print("total2vv: ", total2vv[loadTime], " a:", a)
            #make list of smallest lines
            #to find smallest length of cashier line, go through list of numbers until the length of one of the lines is reached

            if len(cashier1) < 10:
                cashier1.append(total3v[loadTime])
                loadTime = loadTime + 1
            else:
                if len(cashier2) < 10:
                    cashier2.append(total3v[loadTime])
                    loadTime = loadTime + 1
                else:
                    if len(cashier3) < 10:
                        cashier3.append(total3v[loadTime])
                        loadTime = loadTime + 1
                    else:
                        if len(cashier4) < 10:
                            cashier4.append(total3v[loadTime])
                            loadTime = loadTime + 1
                        else:
                            if len(cashier5) < 10:
                                cashier5.append(total3v[loadTime])
                                loadTime = loadTime + 1
                            else:
                                if len(cashier6) < 10:
                                    cashier6.append(total3v[loadTime])
                                    loadTime = loadTime + 1
                                else:
                                    if len(cashier7) < 10:
                                        cashier7.append(total3v[loadTime])
                                        loadTime = loadTime + 1
                                    else:
                                        if len(cashier8) < 10:
                                            cashier8.append(total3v[loadTime])
                                            loadTime = loadTime + 1
                                        else:
                                            if len(cashier9) < 10:
                                                cashier9.append(total3v[loadTime])
                                                loadTime = loadTime + 1
                                            else:
                                                if len(cashier10) < 10:
                                                    cashier10.append(total3v[loadTime])
                                                    loadTime = loadTime + 1
                                                else:
                                                    if len(cashier11) < 10:
                                                        cashier11.append(total3v[loadTime])
                                                        loadTime = loadTime + 1
                                                    else:
                                                        if len(cashier12) < 10:
                                                            cashier12.append(total3v[loadTime])
                                                            loadTime = loadTime + 1

        # **************************************************************
        # if the total amount of customers is less then amount of registers needed, close registers/ sum of lengths of arrays
        allcust = len(cashier1) + len(cashier2) + len(cashier3) + len(cashier4) + len(cashier5) + len(
            cashier6) + len(cashier7) + len(cashier8) + len(cashier9) + len(cashier10) + len(cashier11) + len(
            cashier12)
        # print("Sum: ", allcust)

        # n12=0
        # max occupancy == 120
        # if the total customers is less than 101 and customers are at register 12, close register 12, place rest of customers in other registers
        if allcust < 110 and len(cashier12) > 0:
            # v12 = v12r
            # while customers still exist at register 12
            while len(cashier12) != 0:
                # if register is not full, add customer here
                if len(cashier11) != 10:
                    cashier11.append(cashier12[0])
                    # increment to next spot in array
                    # n12 = n12 + 1
                    # decrement number of items in array
                    # v12 = v12 -1
                    del cashier12[0]

                if len(cashier10) != 10:
                    cashier10.append(cashier12[0])
                    del cashier12[0]
                if len(cashier9) != 10:
                    cashier9.append(cashier12[0])
                    del cashier12[0]
                if len(cashier8) != 10:
                    cashier8.append(cashier12[0])
                    del cashier12[0]
                if len(cashier7) != 10:
                    cashier7.append(cashier12[0])
                    del cashier12[0]
                if len(cashier6) != 10:
                    cashier6.append(cashier12[0])
                    del cashier12[0]
                if len(cashier5) != 10:
                    cashier5.append(cashier12[0])
                    del cashier12[0]
                if len(cashier4) != 10:
                    cashier4.append(cashier12[0])
                    del cashier12[0]
                if len(cashier3) != 10:
                    cashier3.append(cashier12[0])
                    del cashier12[0]
                if len(cashier2) != 10:
                    cashier2.append(cashier12[0])
                    del cashier12[0]
                if len(cashier1) != 10:
                    cashier1.append(cashier12[0])
                    del cashier12[0]

        if allcust < 100 and len(cashier11) > 0:
            while len(cashier11) > 0:
                if len(cashier10) != 10:
                    cashier10.append(cashier11[0])
                    del cashier11[0]
                if len(cashier9) != 10:
                    cashier9.append(cashier11[0])
                    del cashier11[0]
                if len(cashier8) != 10:
                    cashier8.append(cashier11[0])
                    del cashier11[0]
                if len(cashier7) != 10:
                    cashier7.append(cashier11[0])
                    del cashier11[0]
                if len(cashier6) != 10:
                    cashier6.append(cashier11[0])
                    del cashier11[0]
                if len(cashier5) != 10:
                    cashier5.append(cashier11[0])
                    del cashier11[0]
                if len(cashier4) != 10:
                    cashier4.append(cashier11[0])
                    del cashier11[0]
                if len(cashier3) != 10:
                    cashier3.append(cashier11[0])
                    del cashier11[0]
                if len(cashier2) != 10:
                    cashier2.append(cashier11[0])
                    del cashier11[0]
                if len(cashier1) != 10:
                    cashier1.append(cashier11[0])
                    del cashier11[0]
                    # *********************************************
        if allcust < 90 and len(cashier10) > 0:
            while len(cashier10) > 0:
                if len(cashier10) != 10:
                    cashier10.append(cashier10[0])
                    del cashier10[0]
                if len(cashier9) != 10:
                    cashier9.append(cashier10[0])
                    del cashier10[0]
                if len(cashier8) != 10:
                    cashier8.append(cashier10[0])
                    del cashier10[0]
                if len(cashier7) != 10:
                    cashier7.append(cashier10[0])
                    del cashier10[0]
                if len(cashier6) != 10:
                    cashier6.append(cashier10[0])
                    del cashier10[0]
                if len(cashier5) != 10:
                    cashier5.append(cashier10[0])
                    del cashier10[0]
                if len(cashier4) != 10:
                    cashier4.append(cashier10[0])
                    del cashier10[0]
                if len(cashier3) != 10:
                    cashier3.append(cashier10[0])
                    del cashier10[0]
                if len(cashier2) != 10:
                    cashier2.append(cashier10[0])
                    del cashier10[0]
                if len(cashier1) != 10:
                    cashier1.append(cashier10[0])
                    del cashier10[0]

        if allcust < 80 and len(cashier9) > 0:
            while len(cashier9) > 0:
                if len(cashier10) != 10:
                    cashier10.append(cashier9[0])
                    del cashier9[0]
                if len(cashier9) != 10:
                    cashier9.append(cashier9[0])
                    del cashier9[0]
                if len(cashier8) != 10:
                    cashier8.append(cashier9[0])
                    del cashier9[0]
                if len(cashier7) != 10:
                    cashier7.append(cashier9[0])
                    del cashier9[0]
                if len(cashier6) != 10:
                    cashier6.append(cashier9[0])
                    del cashier9[0]
                if len(cashier5) != 10:
                    cashier5.append(cashier9[0])
                    del cashier9[0]
                if len(cashier4) != 10:
                    cashier4.append(cashier9[0])
                    del cashier9[0]
                if len(cashier3) != 10:
                    cashier3.append(cashier9[0])
                    del cashier9[0]
                if len(cashier2) != 10:
                    cashier2.append(cashier9[0])
                    del cashier9[0]
                if len(cashier1) != 10:
                    cashier1.append(cashier9[0])
                    del cashier9[0]

        if allcust < 70 and len(cashier8) > 0:
            while len(cashier8) > 0:
                if len(cashier10) != 10:
                    cashier10.append(cashier8[0])
                    del cashier8[0]
                if len(cashier9) != 10:
                    cashier9.append(cashier8[0])
                    del cashier8[0]
                if len(cashier8) != 10:
                    cashier8.append(cashier8[0])
                    del cashier8[0]
                if len(cashier7) != 10:
                    cashier7.append(cashier8[0])
                    del cashier8[0]
                if len(cashier6) != 10:
                    cashier6.append(cashier8[0])
                    del cashier8[0]
                if len(cashier5) != 10:
                    cashier5.append(cashier8[0])
                    del cashier8[0]
                if len(cashier4) != 10:
                    cashier4.append(cashier8[0])
                    del cashier8[0]
                if len(cashier3) != 10:
                    cashier3.append(cashier8[0])
                    del cashier8[0]
                if len(cashier2) != 10:
                    cashier2.append(cashier8[0])
                    del cashier8[0]
                if len(cashier1) != 10:
                    cashier1.append(cashier8[0])
                    del cashier8[0]

        if allcust < 60 and len(cashier7) > 0:
            while len(cashier7) > 0:
                if len(cashier10) != 10:
                    cashier10.append(cashier7[0])
                    del cashier7[0]
                if len(cashier9) != 10:
                    cashier9.append(cashier7[0])
                    del cashier7[0]
                if len(cashier8) != 10:
                    cashier8.append(cashier7[0])
                    del cashier7[0]
                if len(cashier7) != 10:
                    cashier7.append(cashier7[0])
                    del cashier7[0]
                if len(cashier6) != 10:
                    cashier6.append(cashier7[0])
                    del cashier7[0]
                if len(cashier5) != 10:
                    cashier5.append(cashier7[0])
                    del cashier7[0]
                if len(cashier4) != 10:
                    cashier4.append(cashier7[0])
                    del cashier7[0]
                if len(cashier3) != 10:
                    cashier3.append(cashier7[0])
                    del cashier7[0]
                if len(cashier2) != 10:
                    cashier2.append(cashier7[0])
                    del cashier7[0]
                if len(cashier1) != 10:
                    cashier1.append(cashier7[0])
                    del cashier7[0]

        if allcust < 50 and len(cashier6) > 0:
            while len(cashier6) > 0:

                if len(cashier4) != 10:
                    cashier5.append(cashier6[0])
                    del cashier6[0]

                if len(cashier4) != 10:
                    cashier4.append(cashier6[0])
                    del cashier6[0]

                if len(cashier3) != 10:
                    cashier3.append(cashier6[0])
                    del cashier6[0]

                if len(cashier2) != 10:
                    cashier2.append(cashier6[0])
                    del cashier6[0]

                if len(cashier1) != 10:
                    cashier1.append(cashier6[0])
                    del cashier6[0]

        if allcust < 40 and len(cashier5) > 0:
            while len(cashier5) > 0:
                if len(cashier4) != 10:
                    cashier4.append(cashier5[0])
                    del cashier5[0]

                if len(cashier3) != 10:
                    cashier3.append(cashier5[0])
                    del cashier5[0]

                if len(cashier2) != 10:
                    cashier2.append(cashier5[0])
                    del cashier5[0]

                if len(cashier1) != 10:
                    cashier1.append(cashier5[0])
                    del cashier5[0]

        if allcust < 30 and len(cashier4) > 0:
            while len(cashier4) > 0:
                if len(cashier3) != 10:
                    cashier3.append(cashier4[0])
                    del cashier4[0]
                if len(cashier2) != 10:
                    cashier2.append(cashier4[0])
                    del cashier4[0]
                if len(cashier1) != 10:
                    cashier1.append(cashier4[0])
                    del cashier4[0]

        # print(cashier1)
        # print(cashier2)
        # print(cashier3)

        if allcust < 20 and len(cashier3) > 0:
            while len(cashier3) > 0:
                if len(cashier1) != 10:
                    cashier1.append(cashier3[0])
                    del cashier3[0]
                if len(cashier2) != 10:
                    cashier2.append(cashier3[0])
                    del cashier3[0]

        # print(cashier1)
        # print(cashier2)
        # print(cashier3)

        if allcust < 10:
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
            if len(cashier1) < 10 and checkers == False:
                cashier1.append(total3v[loadTime])
                checkers = True
                loadTime = loadTime + 1
            if len(cashier2) < 10 and checkers == False:
                cashier2.append(total3v[loadTime])
                checkers = True
                loadTime = loadTime + 1
            if len(cashier3) < 10 and checkers == False:
                cashier3.append(total3v[loadTime])
                checkers = True
                loadTime = loadTime + 1
            if len(cashier4) < 10 and checkers == False:
                cashier4.append(total3v[loadTime])
                checkers = True
                loadTime = loadTime + 1
            if len(cashier5) < 10 and checkers == False:
                cashier5.append(total3v[loadTime])
                checkers = True
                loadTime = loadTime + 1
            if len(cashier6) < 10 and checkers == False:
                cashier6.append(total3v[loadTime])
                checkers = True
                loadTime = loadTime + 1
            if len(cashier7) < 10 and checkers == False:
                cashier7.append(total3v[loadTime])
                checkers = True
                loadTime = loadTime + 1
            if len(cashier8) < 10 and checkers == False:
                cashier8.append(total3v[loadTime])
                checkers = True
                loadTime = loadTime + 1
            if len(cashier9) < 10 and checkers == False:
                cashier9.append(total3v[loadTime])
                checkers = True
                loadTime = loadTime + 1
            if len(cashier10) < 10 and checkers == False:
                cashier10.append(total3v[loadTime])
                checkers = True
                loadTime = loadTime + 1
            if len(cashier11) < 10 and checkers == False:
                cashier11.append(total3v[loadTime])
                checkers = True
                loadTime = loadTime + 1
            if len(cashier12) < 10 and checkers == False:
                cashier12.append(total3v[loadTime])
                loadTime = loadTime + 1
   
            h = 1 #find smallest line that is not equal to zero
            print("H: ", h)
            for h in range(900):

                if len(cashier1) == h and len(cashier1) < 10 and checkers == False:
                    cashier1.append(total3v[loadTime])
                    h = 900
                    checkers = True
                    loadTime = loadTime + 1
                if len(cashier2) == h and c2 == True and len(cashier2) < 10 and checkers == False:
                    cashier2.append(total3v[loadTime])
                    h = 900
                    checkers = True
                    loadTime = loadTime + 1
                if len(cashier3) == h and c3 == True and len(cashier3) < 10 and checkers == False:
                    cashier3.append(total3v[loadTime])
                    h = 900
                    checkers = True
                    loadTime = loadTime + 1
                if len(cashier4) == h and c4 == True and len(cashier4) < 10 and checkers == False:
                    cashier4.append(total3v[loadTime])
                    h = 900
                    checkers = True
                    loadTime = loadTime + 1
                if len(cashier5) == h and c5 == True and len(cashier5) < 10 and checkers == False:
                    cashier5.append(total3v[loadTime])
                    h = 900
                    checkers = True
                    loadTime = loadTime + 1
                if len(cashier6) == h and c6 == True and len(cashier6) < 10 and checkers == False:
                    cashier6.append(total3v[loadTime])
                    h = 900
                    checkers = True
                    loadTime = loadTime + 1
                if len(cashier7) == h and c7 == True and len(cashier7) < 10 and checkers == False:
                    cashier7.append(total3v[loadTime])
                    h = 900
                    checkers = True
                    loadTime = loadTime + 1
                if cashier8 == h and c8 == True and len(cashier8) < 10 and checkers == False:
                    cashier8.append(total3v[loadTime])
                    h = 900
                    checkers = True
                    loadTime = loadTime + 1
                if len(cashier9) == h and c9 == True and len(cashier9) < 10 and checkers == False:
                    cashier9.append(total3v[loadTime])
                    h = 900
                    checkers = True
                if len(cashier10) == h and c10 == True and len(cashier10) < 10 and checkers == False:
                    cashier10.append(total3v[loadTime])
                    h = 900
                    checkers = True
                    loadTime = loadTime + 1
                if len(cashier12) == h and c11 == True and len(cashier11) < 10 and checkers == False:
                    cashier11.append(total3v[loadTime])
                    h = 900
                    checkers = True
                    loadTime = loadTime + 1
                if len(cashier12) == h and c12 == True and len(cashier12) < 10 and checkers == False:
                    cashier12.append(total3v[loadTime])
                    h = 900
                    checkers = True
                    loadTime = loadTime + 1
    '''

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

        #**************************************************************************************
        #if time in cashier line is equal to current time, remove
    for r in range (len(cashier1)):
        if cashier1[r] == a:
            del cashier1[r]
    for rr in range (len(cashier2)):
        if cashier2[rr] == a:
            del cashier2[rr]
    for rrr in range (len(cashier3)):
        if cashier3[rrr] == a:
            del cashier3[rrr]
    for r4 in range (len(cashier4)):
        if cashier4[r4] == a:
            del cashier4[r4]
    for r5 in range (len(cashier5)):
        if cashier5[r5] == a:
            del cashier5[r5]
    for r6 in range (len(cashier6)):
        if cashier6[r6] == a:
            del cashier6[r6]
    for r7 in range (len(cashier7)):
        if cashier7[r7] == a:
            del cashier7[r7]
    for r8 in range (len(cashier8)):
        if cashier8[r8] == a:
            del cashier8[r8]
    for r9 in range (len(cashier9)):
        if cashier9[r9] == a:
            del cashier9[r9]
    for r10 in range (len(cashier10)):
        if cashier10[r10] == a:
            del cashier10[r10]
    for r11 in range (len(cashier11)):
        if cashier11[r11] == a:
            del cashier11[r11]
    for r12 in range (len(cashier12)):
        if cashier12[r12] == a:
            del cashier12[r12]
    
