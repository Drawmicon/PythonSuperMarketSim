c2 = True
c3 = True
c4 = True
c5 = True
c6 = True
c7 = True
c8 = True
c9 = True
c10 = True
c11 = False
c12 = True


cashier1 = [1,2,3,4,5]
cashier2 = [2,4,6,8,10]
cashier3 = [3,6,9,12,15]
cashier4 = [4,8,12,16,20]
cashier5 = [5,10,15,20,25,]
cashier6 = [6,12,18,24,30]
cashier7 = [7,14,21,28,35]
cashier8 = [8,16,24,32,40]
cashier9 = [9,18,27,36,45]
cashier10 = [10,20,30,40,50]
cashier11 = [11,22,33,44,55]
cashier12 = [12,24,36,48,60]

for a in range(61):

    print("\na: ",a)
    if len(cashier1) > 0 and cashier1[0] == a:
        del cashier1[0]

    if len(cashier2) > 0 and cashier2[0] == a:
        del cashier2[0]

    if len(cashier3) > 0 and cashier3[0] == a:
        del cashier3[0]

    if len(cashier4) > 0 and cashier4[0] == a:
        del cashier4[0]

    if len(cashier5) > 0 and cashier5[0] == a:
        del cashier5[0]

    if len(cashier6) > 0 and cashier6[0] == a:
        del cashier6[0]

    if len(cashier7) > 0 and cashier7[0] == a:
        del cashier7[0]

    if len(cashier8) > 0 and cashier8[0] == a:
        del cashier8[0]

    if len(cashier9) > 0 and cashier9[0] == a:
        del cashier9[0]

    if len(cashier10) > 0 and cashier10[0] == a:
        del cashier10[0]

    if len(cashier11) > 0 and cashier11[0] == a:
        del cashier11[0]

    if len(cashier12) > 0 and cashier12[0] == a:
        del cashier12[0]


    print("1: ", cashier1)
    print("2: ", cashier2)
    print("3: ", cashier3)
    print("4: ", cashier4)
    print("5: ", cashier5)
    print("6: ", cashier6)
    print("7: ", cashier7)
    print("8: ", cashier8)
    print("9: ", cashier9)
    print("10: ", cashier10)
    print("11: ", cashier11)
    print("12: ", cashier12)


'''
allcust = len(cashier1) + len(cashier2) + len(cashier3) + len(cashier4) + len(cashier5) + len(cashier6) + len(cashier7) + len(cashier8) + len(cashier9) + len(cashier10) + len(cashier11) + len(cashier12)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ UNDER CONSTRUCTION
#n12=0
#max occupancy == 120
#if the total customers is less than 101 and customers are at register 12, close register 12, place rest of customers in other registers
if allcust < 110 and len(cashier12) > 0:
    #v12 = v12r
    #while customers still exist at register 12
    while len(cashier12) != 0:
        #if register is not full, add customer here
        if len(cashier11) != 10 and len(cashier12) != 0:
            cashier11.append(cashier12[0])
            #increment to next spot in array
            #n12 = n12 + 1
            #decrement number of items in array
            #v12 = v12 -1
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


print("1: ", cashier1)
print("2: ", cashier2)
print("3: ", cashier3)
print("4: ", cashier4)
print("5: ", cashier5)
print("6: ", cashier6)
print("7: ", cashier7)
print("8: ", cashier8)
print("9: ", cashier9)
print("10: ", cashier10)
print("11: ", cashier11)
print("12: ", cashier12)


sum1 = 0
for g in range (len(cashier1)):
    sum1 = sum1 + cashier1[g]
if sum1 > 30:
    print("Open Register 2. ")
    c2 = True
sum2 = 0
for g in range(len(cashier2)):
    sum2 = sum2 + cashier2[g]
if sum2 > 30:
    print("Open Register 3. ")
    c2 = True
sum3 = 0
for g in range(len(cashier3)):
    sum3 = sum3 + cashier3[g]
if sum3 > 30:
    print("Open Register 4. ")
    c2 = True
sum4 = 0
for g in range(len(cashier4)):
    sum4 = sum4 + cashier4[g]
if sum4 > 30:
    print("Open Register 5. ")
    c2 = True
sum5 = 0
for g in range(len(cashier5)):
    sum5 = sum5 + cashier5[g]
if sum5 > 30:
    print("Open Register 6. ")
    c2 = True
sum6 = 0
for g in range(len(cashier6)):
    sum6 = sum6 + cashier6[g]
if sum6 > 30:
    print("Open Register 7. ")
    c2 = True
sum7 = 0
for g in range(len(cashier7)):
    sum7 = sum7 + cashier7[g]
if sum7 > 30:
    print("Open Register 8. ")
    c2 = True
sum8 = 0
for g in range(len(cashier8)):
    sum8 = sum8 + cashier8[g]
if sum8 > 30:
    print("Open Register 9. ")
    c2 = True
sum9 = 0
for g in range(len(cashier9)):
    sum9 = sum9 + cashier9[g]
if sum9 > 30:
    print("Open Register 10. ")
    c2 = True
sum10 = 0
for g in range(len(cashier10)):
    sum10 = sum10 + cashier10[g]
if sum10 > 30:
    print("Open Register 11. ")
    c11 = True
sum11 = 0
for g in range(len(cashier11)):
    sum11 = sum11 + cashier11[g]
if sum11 > 30:
    print("Open Register 12. ")
    c12 = True





#total2vvr = [0,2,4,8,16,32,64]
#total3vr = [0,1,2,3,4,5,6]
total2vvr = [33, 36, 47, 60, 64, 71, 72, 83, 85, 95, 98, 104, 105, 114, 120, 122, 137, 137, 148, 153, 166, 168, 175, 178, 183, 186, 205, 206, 208, 220, 223, 228, 233, 235, 239, 239, 243, 250, 252, 256, 261, 283, 292, 293, 294, 308, 310, 323, 324, 336, 337, 347, 348, 351, 355, 359, 369, 380, 381, 393, 399, 400, 409, 426, 431, 432, 432, 442, 443, 456, 459, 459, 464, 465, 480, 487, 487, 488, 499, 510, 515, 524, 534, 539, 540, 541, 542, 557, 562, 563, 566, 574, 577, 586, 595, 602, 607, 620, 623, 631, 633, 646, 664, 666, 681, 683, 686, 689, 693, 696, 701, 709, 710, 715, 726, 730, 735, 735, 744, 748, 749, 764, 769, 772, 782, 790, 795, 797, 799, 819, 824, 824, 826, 833, 835, 838, 842, 851, 854, 854, 856, 863, 883, 889, 895, 897, 904]
total3vr =  [37, 1, 14, 14, 42, 3, 2, 25, 28, 48, 25, 40, 23, 21, 2, 21, 20, 21, 14, 3, 40, 19, 45, 2, 14, 13, 42, 38, 33, 19, 26, 21, 23, 2, 45, 31, 6, 26, 30, 20, 4, 18, 37, 17, 4, 29, 25, 32, 39, 4, 23, 9, 10, 39, 44, 4, 15, 6, 29, 20, 14, 12, 11, 6, 37, 24, 14, 3, 16, 28, 23, 25, 13, 19, 25, 7, 33, 6, 9, 6, 39, 17, 13, 27, 6, 41, 50, 15, 50, 32, 20, 42, 12, 24, 12, 33, 3, 38, 31, 7, 8, 23, 17, 19, 44, 43, 20, 21, 47, 4, 27, 17, 3, 8, 29, 48, 17, 17, 17, 10, 15, 40, 44, 36, 14, 47, 33, 8, 20, 2, 29, 40, 4, 27, 24, 20, 23, 4, 31, 22, 4, 21, 10, 28, 3, 48, 37, 15]


kt = False
i = 0

for a in range (1000):


    if len(total2vvr) > 0:
        if total2vvr[0] == a or total2vvr[0] == (a - 1):
            print("a: ", a)
            #print("Time When Arrived At Register: ", total2vvr[0])
            # make list of smallest lines
            # to find smallest length of cashier line, go through list of numbers until the length of one of the lines is reached
            # find smallest line length
            print("Total2vvr: ", total2vvr)
            print("Total3vr: ", total3vr)
            while kt == False:
                print("kt: ", kt, ", i: ", i)
                # if the line length is the current number for i (smallest to largest),  and the length is less than max (10), and the line is open, append data to line
                if len(cashier1) == i and len(cashier1) < 10 and kt == False:
                    cashier1.append(total3vr[0])
                    kt = True
                    if len(cashier1) >= 10:
                        c2 = True
                if len(cashier2) == i and c2 == True and len(cashier2) < 10 and kt == False:
                    cashier2.append(total3vr[0])
                    kt = True
                    if len(cashier2) >= 10:
                        c3 = True
                if len(cashier3) == i and c3 == True and len(cashier3) < 10 and kt == False:
                    cashier3.append(total3vr[0])
                    kt = True
                    if len(cashier3) >= 10:
                        c4 = True
                if len(cashier4) == i and c4 == True and len(cashier4) < 10 and kt == False:
                    cashier4.append(total3vr[0])
                    kt = True
                    if len(cashier4) >= 10:
                        c5 = True
                if len(cashier5) == i and c5 == True and len(cashier5) < 10 and kt == False:
                    cashier5.append(total3vr[0])
                    kt = True
                    if len(cashier5) >= 10:
                        c6 = True
                if len(cashier6) == i and c6 == True and len(cashier6) < 10 and kt == False:
                    cashier6.append(total3vr[0])
                    kt = True
                    if len(cashier6) >= 10:
                        c7 = True
                if len(cashier7) == i and c7 == True and len(cashier7) < 10 and kt == False:
                    cashier7.append(total3vr[0])
                    kt = True
                    if len(cashier7) >= 10:
                        c8 = True
                if len(cashier8) == i and c8 == True and len(cashier8) < 10 and kt == False:
                    cashier8.append(total3vr[0])
                    kt = True
                    if len(cashier8) >= 10:
                        c9 = True
                if len(cashier9) == i and c9 == True and len(cashier9) < 10 and kt == False:
                    cashier9.append(total3vr[0])
                    kt = True
                    if len(cashier9) >= 10:
                        c10 = True
                if len(cashier10) == i and c10 == True and len(cashier10) < 10 and kt == False:
                    cashier10.append(total3vr[0])
                    kt = True
                    if len(cashier10) >= 10:
                        c11 = True
                if len(cashier11) == i and c11 == True and len(cashier11) < 10 and kt == False:
                    cashier11.append(total3vr[0])
                    kt = True
                    if len(cashier11) >= 10:
                        c12 = True
                if len(cashier12) == i and c12 == True and kt == False:  # and len(cashier12) < 10:
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

print("Total2vvr: ", total2vvr)
print("Total3vr: ", total3vr)
'''