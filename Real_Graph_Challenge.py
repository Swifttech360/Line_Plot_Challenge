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
        coordCheckList.append(prevConQuestion)

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
        coordCheckList.append(conQuestion)
        display_graph()
        # for some reason, the loop below will always return false, saying that the current coord does not equal
        # itself
        for (i, coord) in enumerate(coordCheckList):

             #if backEndLineList[int(prevConQuestion[1])][int(prevConQuestion[0])] != backEndLineList[int(
                   # coord[1])][int(coord[0])]:
         if coord not in pre
             #downRight Check
              #if backEndLineList[int(prevConQuestion[1]) + 1][int(prevConQuestion[0]) + 1] != backEndLineList[int(
                    #coord[1])][int(coord[0])]:
               #right check
               #if backEndLineList[int(prevConQuestion[1])][int(prevConQuestion[0]) + 1] != backEndLineList\
                 # [int(coord[1])][int(coord[0])]:
                #upRight Check
                #if backEndLineList[int(prevConQuestion[1]) - 1][int(prevConQuestion[0]) + 1] != backEndLineList\
                    #[int(coord[1])][int(coord[0])]:
                  #Up Check
                  #if backEndLineList[int(prevConQuestion[1]) - 1][int(prevConQuestion[0])] !=backEndLineList\
                    #[int(coord[1])][int(coord[0])]:
                    #print(f"{coord} isn't sonnected to {prevConQuestion}")
                   # backEndConnected = False


            # else: pass
        #if backEndConnected:
           # print('yipeee')


        else:
            print('160 degree connection test failed')



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
                        isConnected = False
                        print("These points are not connected because no points of the same value touch prevConQuestion")
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
        coordCheckList.append(prevConQuestion)
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
