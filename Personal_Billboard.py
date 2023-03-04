#5.2
#Imports everything from the microbit module
from microbit import *

#5.3
#assigns the integer 0 to the variable choice.
choice = 0

#5.9
#Creates a list named my_list that contains the items "Ahoy", Image.HAPPY, Image.SAD, Image.HEART, Image.ASLEEP, Image.SURPRISED.
#LEARNING : The list can contain mixed data types and allows for faster access using the index corresponding to a list item.
my_list = [
    "Ahoy",
    Image.HAPPY, 
    Image.SAD, 
    Image.HEART, 
    Image.ASLEEP,
    Image.SURPRISED
]

#5.9
#Assigns the integer 0 to the variable FIRST_CHOICE.
FIRST_CHOICE = 0

#5.9
#Takes the length of my_list and subtracts 1 from it.
#Then assigns this value to the variable LAST_CHOICE.
LAST_CHOICE = len(my_list) - 1

#5.2
#Loops the indented code block infinitely.
while True:
    
    #5.8
    #It takes an item of the list at the index corresponding to the value of the variable "choice".
    #The final value is assigned to the variable my_image.
    #LEARNING : Retrieving a specific item from a list using the index.
    my_image = my_list[choice]
    
    #5.12
    #checks if the variable my_image is of type string.
    #If my_image is a string type, then it will execute the indented code block.
    #LEARNING : the type() function returns the data type of the parameter passed.
    #LEARNING : This conditional statement is critical because the scroll expects only string data type. 
    if type(my_image) == str:
        
        #5.12
        #scrolls the contents of the variable my_image across the LED array.
        display.scroll(my_image)
    
    #5.12
    #If the conditional statement above is not satisfied, then it will execute the indented code block.
    else:
        
        #5.12
        #shows the contents of the variable my_image on the LED array.
        display.show(my_image)
    
    #5.3
    #Checks if Button B was pressed.
    #If pressed, the function returns the boolean value True.
    #If True, then the if statement's indented code block will execute.
    if button_b.was_pressed():
        
        #5.3
        #Adds the integer value of 1 to the initial value of the variable choice.
        #Then assigns this new summed up integer value to the variable choice.
        choice = choice + 1
        
        #5.9
        #Compares the value of the variable choice to the value of the variable LAST_CHOICE.
        #If the value of choice is greater than the value of LAST_CHOICE, the indented code block will execute.
        if choice > LAST_CHOICE:
            
            #5.9
            #Assigns the value of the variable FIRST_CHOICE to the variable choice.
            choice = FIRST_CHOICE
        
    
    #5.4
    #Checks if Button A was pressed.
    #If Button A has been pressed, the function returns the boolean value True.
    #If True, then the if statement's indented code block will execute.
    if button_a.was_pressed():
        
        #5.4
        #Subtracts the integer value of 1 from the initial value of the variable choice.
        #Then assigns this new subtracted integer value to the variable choice.
        choice = choice - 1
        
        #5.9
        #Compares the value of the variable choice to the value of the variable FIRST_CHOICE.
        #If the value of choice is greater than the value of LAST_CHOICE, the indented code block will execute.
        if choice < FIRST_CHOICE:
            
            #5.9
            #Assigns the value of the variable FIRST_CHOICE to the variable choice.
            choice = LAST_CHOICE
