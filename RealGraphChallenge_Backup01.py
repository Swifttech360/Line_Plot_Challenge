#backup version (01/23/25)
def display_graph():
    stringPrintList = ""
    for currentRow in range(6):
        for currentColumn in range(6):
            if lineList[int(currentRow) - 1][int(currentColumn) - 1] != "":
                stringPrintList += (str(lineList[int(currentRow) - 1][int(currentColumn) - 1])) + "  "
        stringPrintList += "\n"
    print(stringPrintList)
    

def Input_History_Test():
    global isConnected
    global checkCondition
    global prevDupicate
    global conDuplicate
    global loopNum
#____________________________________________PrevConQuestion Input History Test ________________________________________
    x = int(backEndLineList[int(prevConQuestion[1])][int(prevConQuestion[0])])
    #Duplicate Check
    if (prevDupicate == False) and prevConQuestion != conQuestion:
        #or (x != backEndLineList[int(conQuestion[1])][int(conQuestion[0])])
     #right check
     if (x + 1) not in coordCheckList or x in (4, 8, 12, 16):
      #upRight check
      if (x - 3) not in coordCheckList or x in (1,2,3,4,8,12,16):
       #Up Check
       if (x - 4) not in coordCheckList or x <= 4:
        #upLeft Check
        if (x - 5) not in coordCheckList or x in (1, 2, 3, 4, 5, 9, 13):
         #Left Check
         if (x - 1) not in coordCheckList or x in (1, 5, 9, 13):
          #downLeft Check
          if (x + 3) not in coordCheckList or x in (1, 5, 9, 13, 14, 15, 16):
            #Down Check
           if (x + 4) not in coordCheckList or x in (13, 14, 15, 16):
            #downRight Check
            if (x + 5) not in coordCheckList or x  in (4, 8, 12, 13, 14, 15, 16):
             checkCondition = False
#            else: print("prevCon9")
#           else: print("prevCon8")
#          else: print("prevCon7")
#         else: print("prevCon6")
#        else: print("prevCon5")
#       else: print("prevCon4")
#      else: print("prevCon3")
#     else: print("prevCon2")
#    else: print("prevCon1")
#uncomment comments above to be able to see which flag got triggered each run
    if checkCondition == False:
        print(f"This line is broken because line check #{loopNum - 2} isn't next to any points you've "
              f"checked in the past")
        isConnected = False
#    else: print("prevConCheck Passed!")
    prevDupicate = False
    checkCondition = True
#______________________________________________ConQuestion Input History Test __________________________________________
    x = int(backEndLineList[int(conQuestion[1])][int(conQuestion[0])])
    #Self check
    if conDuplicate == False and prevConQuestion != conQuestion:
     #right check
     if (x + 1) not in coordCheckList or x in (4, 8, 12, 16):
      #upRight check
      if (x - 3) not in coordCheckList or x in (1,2,3,4,8,12,16):
       #Up Check
       if (x - 4) not in coordCheckList or x <= 4:
        #upLeft Check
        if (x - 5) not in coordCheckList or x in (1, 2, 3, 4, 5, 9, 13):
         #Left Check
         if (x - 1) not in coordCheckList or x in (1, 5, 9, 13):
          #downLeft Check
          if (x + 3) not in coordCheckList or x in (1, 5, 9, 13, 14, 15, 16):
            #Down Check
           if (x + 4) not in coordCheckList or x in (13, 14, 15, 16):
            #downRight Check
            if (x + 5) not in coordCheckList or x in (4, 8, 12, 13, 14, 15, 16):
             checkCondition = False
	
#	        else: print("Con9")
#	       else: print("Con8")
#	      else: print("Con7")
#	     else: print("Con6")
#	    else: print("Con5")
#	   else: print("Con4")
#	  else: print("Con3")
#	 else: print("Con2")
#	else: print("Con1")
#uncomment comments above to be able to see which flag got triggered each run

    if checkCondition == False:
	    print(f"This line is broken because line check #{loopNum - 1} isn't next to any points you've "
	          f"checked in the past")
	    isConnected = False
    #else: print("conCheck Passed!")
    conDuplicate = False
    checkCondition = True

def Equal_Value_Checks():
    global lineList
    global prevConQuestion
    global conQuestion
    global isConnected
#____________________________________________PREV_CON_QUESTION EQUAL VALUE_CHECKS______________________________________#
    if lineList[int(prevConQuestion[1])][int(prevConQuestion[0])] != (lineList[int(prevConQuestion[1]) + 1][int(\
           prevConQuestion[0]) + 1]):
            #right Check
          if lineList[int(prevConQuestion[1])][int(prevConQuestion[0])] != lineList[int(prevConQuestion[1])][\
             int(prevConQuestion[0]) + 1]:
              #upRight Check
            if lineList[int(prevConQuestion[1])][int(prevConQuestion[0])] != lineList[int(prevConQuestion[1]) - 1][
               int(prevConQuestion[0]) + 1]:
                #Up Check
              if lineList[int(prevConQuestion[1])][int(prevConQuestion[0])] != lineList[int(prevConQuestion[1])- 1]\
                [int(prevConQuestion[0])]:
                  #upLeft Check
                if lineList[int(prevConQuestion[1])][int(prevConQuestion[0])] != lineList[int(prevConQuestion[1]) - 1]\
                   [int(prevConQuestion[0]) - 1]:
                    #Left Check
                  if lineList[int(prevConQuestion[1])][int(prevConQuestion[0])] != lineList[int(prevConQuestion[1])][\
                     int(prevConQuestion[0]) - 1]:
                      #downLeft Check
                    if lineList[int(prevConQuestion[1])][int(prevConQuestion[0])] != lineList[int(prevConQuestion[1])\
                       + 1][int(prevConQuestion[0]) - 1]:
                        #Down Check
                      if lineList[int(prevConQuestion[1])][int(prevConQuestion[0])] != lineList[int(prevConQuestion[1])\
                         + 1][int(prevConQuestion[0])]:
                          #self check
                        if lineList[int(prevConQuestion[1])][int(prevConQuestion[0])] != lineList[int(conQuestion[1]\
                           )][int(conQuestion[0])]:
                         isConnected = False
                         print("This line is broken because no points of the same value touch this point")
#_____________________________________________CON_QUESTION EQUAL VALUE CHECKS__________________________________________#
    #downRight check
    if lineList[int(conQuestion[1])][int(conQuestion[0])] != (lineList[int(conQuestion[1]) + 1][int(\
       conQuestion[0]) + 1]):
        #right Check
      if lineList[int(conQuestion[1])][int(conQuestion[0])] != lineList[int(conQuestion[1])][\
         int(conQuestion[0]) + 1]:
          #upRight Check
        if lineList[int(conQuestion[1])][int(conQuestion[0])] != lineList[int(conQuestion[1]) - 1][\
           int(conQuestion[0]) + 1]:
            #Up Check
          if lineList[int(conQuestion[1])][int(conQuestion[0])] != lineList[int(conQuestion[1])- 1]\
             [int(conQuestion[0])]:
              #upLeft Check
            if lineList[int(conQuestion[1])][int(conQuestion[0])] != lineList[int(conQuestion[1]) - 1]\
               [int(conQuestion[0]) - 1]:
                #Left Check
              if lineList[int(conQuestion[1])][int(conQuestion[0])] != lineList[int(conQuestion[1])][\
                 int(conQuestion[0]) - 1]:
                  #downLeft Check
                if lineList[int(conQuestion[1])][int(conQuestion[0])] != lineList[int(conQuestion[1])\
                   + 1][int(conQuestion[0]) - 1]:
                    #Down Check
                  if lineList[int(conQuestion[1])][int(conQuestion[0])] != lineList[int(conQuestion[1])\
                      + 1][int(conQuestion[0])]:
                    if lineList[int(conQuestion[1])][int(conQuestion[0])] != lineList[int(prevConQuestion[1])][int\
                        (prevConQuestion[0])]:
                     isConnected = False
                     print("This line is broken connected because no points of the same value touch this point")

    if lineList[int(conQuestion[1])][int(conQuestion[0])] != lineList[int(prevConQuestion[1])][int(
    prevConQuestion[0])]:
        print("This line is broken because this point is not the same value as your previous one")
        isConnected = False
    if (lineList[int(prevConQuestion[1])][int(prevConQuestion[0])] and
            lineList[int(conQuestion[1])][int(conQuestion[0])]) != lineValue:
        print("This line is broken because not all points are the same value (1 or 0)")
        isConnected = False
        




BackEnd_TopBoarder = ("", "", "", "", "", "")
BackEnd_Line1 = ("", 1, 2, 3, 4, "")
BackEnd_Line2 = ("", 5, 6, 7, 8, "")
BackEnd_Line3 = ("", 9, 10, 11, 12, "")
BackEnd_Line4 = ("", 13, 14, 15, 16, "")
BackEnd_BottomBoarder = ("", "", "", "", "", "")
backEndLineList = (BackEnd_TopBoarder, BackEnd_Line1, BackEnd_Line2, BackEnd_Line3, BackEnd_Line4,
                   BackEnd_BottomBoarder)

while True:
    
    topBoarder = ["", "", "", "", "", ""]
    line1 =       ["", 0, 0, 0, 0, ""]
    line2 =       ["", 0, 0, 0, 0, ""]
    line3 =       ["", 0, 0, 0, 0, ""]
    line4 =       ["", 0, 0, 0, 0, ""]
    bottomBoarder = ["", "", "", "", "", ""]
    lineList = [topBoarder, line1, line2, line3, line4, bottomBoarder]
    coordCheckList = []
    isConnected = True
    [prevDupicate, conDuplicate] = [False, False]
    checkCondition = True
    checkHistoryList = []
    lineValue = ''
    
    

    print("\n"
        f"(1,1) is here\n"
          f"  ↓\n"
          f"  0  0  0  0\n"
          f"  0  0  0  0\n"
          f"  0  0  0  0\n"
          f"  0  0  0  0\n"
          f"           ↑\n"
          f"         (4,4) is here\n\n")

    print('Enter two numbers (1 - 4) separated by a space to add a point to the graph (i.e,"x y")')
    while True:
        insQ = input("Where would you like to insert marks?:\n")
        
        if insQ in ("break", "next", ""):
            break
        selection = insQ.split()
        try:
            checker = int(selection[0]) + int(selection[1])
        except Exception:
            print("Those aren't two integers, dummy")
            continue



        if int(selection[0]) > 4 or int(selection[1]) > 4 or int(selection[0]) < 1 or int(selection[1]) < 1:
            print("Numbers are out of range")
            continue
        #enter the solution here
        if lineList[int(selection[1])][int(selection[0])] == 0:
            lineList[int(selection[1])][int(selection[0])] = 1
            display_graph()

        elif lineList[int(selection[1])][int(selection[0])] == 1:
            lineList[int(selection[1])][int(selection[0])] = 0
            display_graph()



    loopNum = 1

    while loopNum < 2:

        StrPrevConQuestion = input(f"enter point #{loopNum}: ")
        if StrPrevConQuestion in ("break", "next"):
            print("please enter at least two points first")
            continue
        
        prevConQuestion = StrPrevConQuestion.split()
        if len(prevConQuestion) != 2:
            print('Invalid input\n'
                  'Be sure to enter two numbers seperated by a spece\n')
            continue
        try:
            checker = int(prevConQuestion[0]) + int(prevConQuestion[1])
        except ValueError:
            print("Invalid input, please try again")
            StrPrevConQuestion = ""
            prevConQuestion = ''
            continue
        if int(prevConQuestion[0]) < 1 or int(prevConQuestion[0]) > 4\
             or int(prevConQuestion[1]) < 1 or int(prevConQuestion[1]) > 4:
            print("One or more numbers are out of range\n"
                  "please make sure all numbers are within range 1-4")
            continue
        loopNum += 1
        if backEndLineList[int(prevConQuestion[1])][int(prevConQuestion[0])] not in coordCheckList:
            coordCheckList.append(backEndLineList[int(prevConQuestion[1])][int(prevConQuestion[0])])
        else:
            prevDupicate = True
        lineValue = lineList[int(prevConQuestion[1])][int(prevConQuestion[0])]
            #print('prevDupicate = True')
            #print(coordCheckList)

    while True:

        StrConQuestion = input(f"enter point #{loopNum}: ")
        if StrConQuestion in ("break", "next"):
            break
        conQuestion = StrConQuestion.split()
        if len(conQuestion) != 2:
            print('Invalid input\n'
                  'Be sure to enter two numbers seperated by a spece\n')
        try:
            checker = int(conQuestion[0]) + int(conQuestion[1])
        except ValueError:
            print("Invalid input, please try again")
            continue
        if int(conQuestion[0]) < 1 or int(conQuestion[0]) > 4 or int(conQuestion[1]) < 1 or int(conQuestion[1]) > 4:
            print("One or more numbers are out of range\n"
                  "please make sure all numbers are within range 1-4")
            continue
        loopNum += 1

        if backEndLineList[int(conQuestion[1])][int(conQuestion[0])] not in coordCheckList:
            coordCheckList.append(backEndLineList[int(conQuestion[1])][int(conQuestion[0])])
        else:
            conDupicate = True
            
        display_graph()
        
        #print(coordCheckList)

        lineCheck1 = False
        lineCheck2 = False

        Input_History_Test()
        
        Equal_Value_Checks()





        if isConnected:
            print("True so far")
        else: print("Points no longer connected")

        StrPrevConQuestion = input(f"enter point #{loopNum}")
        if StrPrevConQuestion in ("break", "next"):
            break
        prevConQuestion = StrPrevConQuestion.split()
        if len(prevConQuestion) != 2:
            print('Invalid input\n'
                  'Be sure to enter two numbers seperated by a spece\n')
        try:
            checker = int(prevConQuestion[0]) + int(prevConQuestion[1])
        except ValueError:
            print("Invalid input, please try again")
            loopNum -= 1
            continue
        if int(prevConQuestion[0]) < 1 or int(prevConQuestion[0]) > 4\
             or int(prevConQuestion[1]) < 1 or int(prevConQuestion[1]) > 4:
            print("One or more numbers are out of range\n"
                  "please make sure all numbers are within range 1-4")
            continue
        loopNum += 1
        if backEndLineList[int(prevConQuestion[1])][int(prevConQuestion[0])] not in coordCheckList:
            coordCheckList.append(backEndLineList[int(prevConQuestion[1])][int(prevConQuestion[0])])
        else:
            prevDupicate = True
        Equal_Value_Checks()
        Input_History_Test()
        
        if isConnected:
            print("True so far")
        else: print("Points no longer connected")

    if isConnected:
        print("All checked points connected")
    else:
        print("Checked points not connected")
    again = input("again? y/n").upper()
    if again == "N":
        break
    

#test graph:
#topBoarder = ["", "", "", "", "", ""]
#line1 = ["", 91, 92, 93, 94, ""]
#line2 = ["", 95, 96, 97, 98, ""]
#line3 = ["", 99, 10, 11, 12, ""]
#line4 = ["", 13, 14, 15, 16, ""]
#bottomBoarder = ["", "", "", "", "", ""]



#downRight check
#jhvouhf[hwfhiweh[wh[whf[ifghjkl;




#topBoarder = ["", "", "", "", "", ""]
#line1 = ["", 1, 2, 3, 4, ""]
#line2 = ["", 5, 6, 7, 8, ""]
#line3 = ["", 9, 10, 11, 12, ""]
#line4 = ["", 13, 14, 15, 16, ""]
#bottomBoarder = ["", "", "", "", "", ""]

    #IDLE Test
