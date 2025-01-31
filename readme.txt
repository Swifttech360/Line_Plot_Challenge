Program: Line Plot Challenge
AUTHOR: Miles Butler
Date: 1/26/2025

##Overview/Instructions:
This repository acts as a demonstration of my ability to utilize Python and GitHub to develop programs. To start the
program, open the 'Line_Plot_Challenge.py' file in any python IDE (I.E., IDLE, PyCharm, Visual Studio, etc.)
before hitting the run button.

This program has two stages. First, the program allows the user to plot points on a 4x4 graph by typing two integers
(1-4) separated by a space; the first integer should be the column you want to insert a point in, and the second one
should be the row. These points can also be removed by entering the same coordinate again.
The user can then enter "next" or "break" to begin the second stage of the program.

In the second stage, the user can begin entering graph points in the same format to check if they
form a line of connected points of the same value (1 or 0) based on the graph they made previously.
After the user checks their first point, if any subsequent input checks the location of a point that isn't the same
value as the first checked point (which will either be a 1 or 0 based on the first stage), the program will notify the
user that their checked points no longer form a connected line of equal points (as well as the reason why).
The same thing will happen if any check input (excluding the first one) checks a point that isn't next to any
previously checked points. Otherwise, the program will print "All checked points form an unbroken line so far."
At any time after the first check, the user can once again enter "next" or "break" to see if their list of checked
points form a connected line of points or not. The user will then be asked if they want to run the program again via a
y/n input question.

