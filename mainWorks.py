#====================================
#             Made for              #
#       Computer Science 314        #
#           Assignment 1            #
#                                   #
#         By Dan Richards           #
#                                   #
#         Special Thanks:           #
#              Coffee               #
#              Python               #
#            CompSci 101            #
#            More Coffee            #
#====================================
from __future__ import print_function
from ast import literal_eval as make_tuple

#This variable is a dictionary which converts nibbles -> binary
QAM16 = {(-3,3): '0000',(-3,1):'0001', (-3,-1):'0011', (-3,-3):'0010', (-1,3):'0100', (-1,1): '0101', (-1,-1):'0111', (-1,-3): '0110', (1,3):'1100', (1,1):'1101', (1,-1):'1111', (1,-3):'1110', (3,3):'1000', (3,1):'1001', (3,-1):'1011', (3,-3):'1010'}        

def main():
    print("I am computer")
    textFileLinesArray = openText("nibble.txt")
    print(convertToAscii(textFileLinesArray))
 
def convertToAscii(array):
    string = ""
    for i in range(0, len(array) - 1, 2):
	item1 = makePretty(array[i])
	item2 = makePretty(array[i+1])
	print(str(array[i]) + " decodes as "+ item1)
	print(str(array[i+1]) +" decodes as " + item2 + " - together,"+  item1 + item2 + ' gives "' , end='')
	if unichr(int(item1 + item2,2)) == " ":
            print("[]\"")
            string += " "
        else:
            print(unichr(int(item1 + item2,2)) + '"')
            string += unichr(int(item1 + item2,2))
	print("")
    return string
    
def makePretty(tuple):
    #This basically rounds to the most appopriate point. 
    # My love of processor branches is obvious here. 
	x = 0
	if tuple[0] > 2:
		x = 3
	if tuple[0] < 2 and tuple[0] > 0:
		x = 1
	if tuple[0] < 0 and tuple[0] > -2:
		x = -1
	if tuple[0] < -2:
		x = -3

	y = 0
	if tuple[1] > 2:
		y = 3
	if tuple[1] < 2 and tuple[1] > 0:
		y = 1
	if tuple[1] < 0 and tuple[1] > -2:
		y = -1
	if tuple[1] < -2:
		y = -3


	result = QAM16[(x,y)]

	return result
    
def openText(fileName):
    f = open(fileName,"r")
    lines =  f.readlines()
    newArray  = [] 
    for item in lines:
        index = item.find("(")   
        newArray.append(make_tuple(item[index:].strip()))
    return newArray

main()

