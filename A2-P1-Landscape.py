#Program 1 – Landscape Calculator
#A landscaping company needs a program that computes the price of landscaping for a new housing development. 

#Student #:    W0499622
#Student Name: Jack Leonard 

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    #TAKE INPUTS: house number, property depth(ft), property width(ft), type of grass, number of trees
    #CALCULATE landscaping cost; base labour is 1000$, each tree is 100$, cost of grasss is by square foot by grass type, fescue:0.05$, bentgrass:0.02$, campus:0.01$
    #check IF square footage is over 5000, if so extra 500$
    #PRINT total cost for landscaping | Total cost for house X is: $Y

    houseNum = input("Enter Your House Number: ") #input to get house number
    depth = int(input("Enter property depth (FT): "))   #input for depth
    width = int(input("Enter property width (FT): "))   #input for width
    grassType = input("Enter Grass Type (Fescue, Bentgrass, Campus)")   #input for grass type
    treesNum = int(input("Enter the number of trees: "))    #input for the amount of trees

    if (grassType.lower() == "fescue"):   #If statements to determine our grass price
        grassPrice = 0.05
    elif (grassType.lower() == "bentgrass"):
        grassPrice = 0.02
    elif (grassType.lower() == "campus"):   #^^^^^^^^^^^^^^
        grassPrice = 0.01

    cost = 1000 + (treesNum * 100) + ((width * depth) * grassPrice) #Calculates our total cost before potentially adding the extra 500$

    if width * depth > 5000:
        cost += 500
    
    print("Total cost for house {0} is: ${1:.2f}".format(houseNum, cost))   #Print statement formatted for outputting house number with total price
    # YOUR CODE ENDS HERE

main()