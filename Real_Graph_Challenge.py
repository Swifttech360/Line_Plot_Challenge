

BackEnd_TopBoarder = ("", "", "", "", "", "")
BackEnd_Line1 = ("", 1, 2, 3, 4, "")
BackEnd_Line2 = ("", 5, 6, 7, 8, "")
BackEnd_Line3 = ("", 9, 10, 11, 12, "")
BackEnd_Line4 = ("", 13, 14, 15, 16, "")
BackEnd_BottomBoarder = ("", "", "", "", "", "")
backEndLineList = (BackEnd_TopBoarder, BackEnd_Line1, BackEnd_Line2, BackEnd_Line3, BackEnd_Line4,
                   BackEnd_BottomBoarder)
def devmode():
    print(f"{BackEnd_Line1}\n{BackEnd_Line2}\n {BackEnd_Line3}\n {BackEnd_Line4}")
    exit()
while True:
    topBoarder = ["", "", "", "", "", ""]
    line1 = ["", 0, 0, 0, 0, ""]
    line2 = ["", 0, 0, 0, 0, ""]
    line3 = ["", 0, 0, 0, 0, ""]
    line4 = ["", 0, 0, 0, 0, ""]
    bottomBoarder = ["", "", "", "", "", ""]
    lineList = [topBoarder, line1, line2, line3, line4, bottomBoarder]
    coordCheckList = []
    isConnected = True
    backEndConnected = False
    #possibly Junk Code Above
    [prevDupicate, conDuplicate] = [False, False]

    def display_graph():
        stringPrintList = ""
        for current in range(6):
            for cCurrent in range(6):
                if lineList[int(current) - 1][int(cCurrent) - 1] != "":
                    stringPrintList += (str(lineList[int(current) - 1][int(cCurrent) - 1])) + "  "
            stringPrintList += "\n"
        print(stringPrintList)

    display_graph()

    print('Enter two numbers (1 - 4) separated by a space to add a point to the graph (i.e,"x y")')
    while True:
        insQ = input("Where would you like to insert marks?:\n")
        if insQ in ("exit", "devmode"):
            devmode()


        #print(selection)
        if insQ in ("break", "next"):
            break
        selection = insQ.split()
        try:
            checker = int(selection[0]) + int(selection[1])
        except ValueError:
            print("Those aren't two integers, dummy")
            continue

        if int(selection[0] or selection[1]) > 4 or int(selection[0] or selection[1]) < 1:
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
        try:
            checker = int(prevConQuestion[0]) + int(prevConQuestion[1])
        except ValueError:
            print("Those aren't two points, dummy")
            StrPrevConQuestion = ""
            prevConQuestion = ''
            continue
        loopNum += 1
        if backEndLineList[int(prevConQuestion[1])][int(prevConQuestion[0])] not in coordCheckList:
            coordCheckList.append(backEndLineList[int(prevConQuestion[1])][int(prevConQuestion[0])])
        else:
            prevDupicate = True
        print(coordCheckList)

    while True:

        StrConQuestion = input(f"enter point #{loopNum}: ")
        if StrConQuestion in ("break", "next"):
            break
        conQuestion = StrConQuestion.split()
        try:
            checker = int(conQuestion[0]) + int(conQuestion[1])
        except ValueError:
            print("Those aren't two points, dummy")
            continue
        loopNum += 1

        if backEndLineList[int(conQuestion[1])][int(conQuestion[0])] not in coordCheckList:
            coordCheckList.append(backEndLineList[int(conQuestion[1])][int(conQuestion[0])])
        else:
            conDupicate = True
        #coordCheckList.append(backEndLineList[int(conQuestion[1])][int(conQuestion[0])])
        display_graph()
        print(coordCheckList)
        lineCheck1 = False
        lineCheck2 = False

        # ____________________________________________prevConQuestion Back End Test_____________________________________
        for i, current in enumerate (coordCheckList):
            x = int(backEndLineList[int(prevConQuestion[1])][int(prevConQuestion[0])])
            #Duplicate Check
            if (prevDupicate == False) or (x != backEndLineList[int(conQuestion[1])][int(conQuestion[0])]):
             #right check
             if (x + 1) not in coordCheckList and x not in (4, 8, 12, 16):
              #upRight check
              if (x - 3) not in coordCheckList and x not in (1,2,3,4,8,12,16):
               #Up Check
               if (x - 4) not in coordCheckList and x > 4:
                #upLeft Check
                if (x - 5) not in coordCheckList and x not in (1, 2, 3, 4, 5, 9, 13):
                 #Left Check
                 if (x - 1) not in coordCheckList and x not in (1, 5, 9, 13):
                  #downLeft Check
                  if (x + 3) not in coordCheckList and x not in (1, 5, 9, 13, 14, 15, 16):
                    #Down Check
                   if (x + 4) not in coordCheckList and x not in (13, 14, 15, 16):
                    #downRight Check
                    if (x + 5) not in coordCheckList and x  not in (4, 8, 12, 13, 14, 15, 16):
                     pass
            else:
                print('setting lineCheck1 to True')
                lineCheck1 = True
                break
        if not lineCheck1:
            print(f"This line is broken because prevConQuestion check #{loopNum - 1} isn't next to any points you've "
                  f"checked in the past")
            isConnected = False
        else: print("prevConCheck Passed!")
        prevDupicate = False
                   #Idea: implement a checknum variable that counts how many times not one flag returned false.
    # If the number if times that happens is the same as coordCheckList's length, isconnected gets set to false
#________________________________________________ConQuestion Back End Test_____________________________________________
        for i, current in enumerate (coordCheckList):
            x = int(backEndLineList[int(conQuestion[1])][int(conQuestion[0])])
            #Self check
            if conDuplicate == False:
             #right check
             if (x + 1) not in coordCheckList and x not in (4, 8, 12, 16):
              #upRight check
              if (x - 3) not in coordCheckList and x not in (1,2,3,4,8,12,16):
               #Up Check
               if (x - 4) not in coordCheckList and x > 4:
                #upLeft Check
                if (x - 5) not in coordCheckList and x not in (1, 2, 3, 4, 5, 9, 13):
                 #Left Check
                 if (x - 1) not in coordCheckList and x not in (1, 5, 9, 13):
                  #downLeft Check
                  if (x + 3) not in coordCheckList and x not in (1, 5, 9, 13, 14, 15, 16):
                    #Down Check
                   if (x + 4) not in coordCheckList and x not in (13, 14, 15, 16):
                    #downRight Check
                    if (x + 5) not in coordCheckList and x  not in (4, 8, 12, 13, 14, 15, 16):
                     pass
            else:
                lineCheck2 = True
                break
        if not lineCheck2:
            print(f"This line is broken because conQuestion check #{loopNum} isn't next to any points you've "
                  f"checked in the past")
            isConnected = False
        else: print("ConQuestion Check Passed!")
        conDuplicate = False





                 #print("Checks would continue")
            #else: print("checks would not continue")




            #if backEndLineList[int(prevConQuestion[1])][int(prevConQuestion[0])] != current:

        # for some reason, the loop below will always return false, saying that the current coord does not equal
        # itself
        #for (i, coord) in enumerate(coordCheckList):

         #     print(backEndLineList[int(coord[1])][int(coord[0])])
#backEndLineList[int(prevConQuestion[1])][int(prevConQuestion[0])] !=



            # else: pass
        #if backEndConnected:
           # print('yipeee')


        #else:
         #   print('160 degree connection test failed')



        # for some reason, the loop below will always return false, saying that the currend coord does not equal
        # itself











#________________________________________________PREV_CON_QUESTION_CHECKS______________________________________________#
          #downRight check
        # noinspection PyUnboundLocalVariable
        if lineList[int(prevConQuestion[1])][int(prevConQuestion[0])] != (lineList[int(prevConQuestion[1]) + 1][int(
           prevConQuestion[0]) + 1]):
            #right Check
          if lineList[int(prevConQuestion[1])][int(prevConQuestion[0])] != lineList[int(prevConQuestion[1])][
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
                  if lineList[int(prevConQuestion[1])][int(prevConQuestion[0])] != lineList[int(prevConQuestion[1])][
                     int(prevConQuestion[0]) - 1]:
                      #downLeft Check
                    if lineList[int(prevConQuestion[1])][int(prevConQuestion[0])] != lineList[int(prevConQuestion[1])
                       + 1][int(prevConQuestion[0]) - 1]:
                        #Down Check
                      if lineList[int(prevConQuestion[1])][int(prevConQuestion[0])] != lineList[int(prevConQuestion[1])\
                         + 1][int(prevConQuestion[0])]:
                          #self check
                        if lineList[int(prevConQuestion[1])][int(prevConQuestion[0])] != lineList[int(conQuestion[1]
                           )][int(conQuestion[0])]:
                         isConnected = False
                         print("These points are not connected because no points of the same value touch "
                               "prevConQuestion")
#___________________________________________________CON_QUESTION_CHECKS________________________________________________#
         #downRight check
        if lineList[int(conQuestion[1])][int(conQuestion[0])] != (lineList[int(conQuestion[1]) + 1][int(
           conQuestion[0]) + 1]):
            #right Check
          if lineList[int(conQuestion[1])][int(conQuestion[0])] != lineList[int(conQuestion[1])][
             int(conQuestion[0]) + 1]:
              #upRight Check
            if lineList[int(conQuestion[1])][int(conQuestion[0])] != lineList[int(conQuestion[1]) - 1][
               int(conQuestion[0]) + 1]:
                #Up Check
              if lineList[int(conQuestion[1])][int(conQuestion[0])] != lineList[int(conQuestion[1])- 1]\
                 [int(conQuestion[0])]:
                  #upLeft Check
                if lineList[int(conQuestion[1])][int(conQuestion[0])] != lineList[int(conQuestion[1]) - 1]\
                   [int(conQuestion[0]) - 1]:
                    #Left Check
                  if lineList[int(conQuestion[1])][int(conQuestion[0])] != lineList[int(conQuestion[1])][
                     int(conQuestion[0]) - 1]:
                      #downLeft Check
                    if lineList[int(conQuestion[1])][int(conQuestion[0])] != lineList[int(conQuestion[1])
                       + 1][int(conQuestion[0]) - 1]:
                        #Down Check
                      if lineList[int(conQuestion[1])][int(conQuestion[0])] != lineList[int(conQuestion[1])\
                          + 1][int(conQuestion[0])]:
                        if lineList[int(conQuestion[1])][int(conQuestion[0])] != lineList[int(prevConQuestion[1])][int
                            (prevConQuestion[0])]:
                         isConnected = False
                         print("These points are not connected because no points of the same value touch conQuestion")

        if lineList[int(conQuestion[1])][int(conQuestion[0])] != lineList[int(prevConQuestion[1])][int(
        prevConQuestion[0])]:
            print("These points are not connected because they are not the same value")
            isConnected = False





        if isConnected:
            print("True so far")
        else: print("Points no longer connected")

        StrPrevConQuestion = input(f"enter point #{loopNum}")
        if StrPrevConQuestion in ("break", "next"):
            break
        prevConQuestion = StrPrevConQuestion.split()
        try:
            checker = int(prevConQuestion[0]) + int(prevConQuestion[1])
        except ValueError:
            print("Those aren't two points, dummy")
            loopNum -= 1
            continue
        loopNum += 1
        if backEndLineList[int(prevConQuestion[1])][int(prevConQuestion[0])] not in coordCheckList:
            coordCheckList.append(backEndLineList[int(prevConQuestion[1])][int(prevConQuestion[0])])
        else:
            prevDupicate = True



    if isConnected:
        print("True")
    else:
        print("False")
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
